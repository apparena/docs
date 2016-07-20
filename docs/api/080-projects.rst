API - Project requests
======================

    .. Hint:: While this documentation uses dummy names like config_1, info_1, etc., you are free to choose the ID of the values yourself as long as they contain only alphanumerics and the underscore

The version concept
-------------------

As you can see in image 1 of the structure_ chapter, all versions point to a root project. This was introduced in order to
give every application a home instead of letting them coexist on the same level, which can lead to long unordered lists when displaying.
With this approach, the list of existing projects is slimmed down drastically while keeping everything nicely accessible.

In order to work on a specific version, the project routes are used while the version can be selected through the query parameter 'version'.

    .. http:response:: GET /projects/1/configs?version=2.1.0 will return all config entries of the version '2.1.0' of project '1'

If no version query parameter is defined, the API automatically determines the highest version and performs the requested action on it.

The format of the version-number is based on `semantic versioning<http://semver.org/>`_. It is stored in a string and consists of three integers in the format
'Ma.Mi.P', where Ma stands for 'MAJOR', Mi for 'MINOR' and P for 'PATCH'.

Recommended usage is that you increment the:

    - MAJOR version when you make incompatible changes,
    - MINOR version when you add functionality in a backwards-compatible manner, and
    - PATCH version when you make backwards-compatible bug fixes.

.. _structure: ../api/040-structure.html#an-example

/projects
---------

The project component consists of the following fields:

    **project fields**

    projectId
        .. include:: /partials/uniqueId.rst
    companyId
        .. include:: /partials/companyId.rst
    name
        .. include:: /partials/name.rst
    description
        .. include:: /partials/description.rst

    **common fields**

    .. include:: /partials/common_all.rst

GET /projects
~~~~~~~~~~~~~

    Receive a collection of projects owned by your company.

|   *Query parameters*
|       page
|       items
|       fields
|       exclude
|       orderasc/orderdesc

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "next": {
              "href": "http://my.app-arena.com/api/v2/projects?page=2"
            },
            "self": {
              "href": "http://my.app-arena.com/api/v2/projects"
            }
          },
          "_embedded": {
            "data": {
              "1": {
                "projectId": 1,
                "name": "Project_1",
                "description": "This is a project description",
                "companyId": 1,
                "_links": {
                  "project": {
                    "href": "http://my.app-arena.com/api/v2/projects/1"
                  },
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  }
                }
              },
              "2": {
                "projectId": 2,
                        .
                        .
                        .
              },
                .
                .
                .
              "N":{
                        .
                        .
                        .
              }
            }
          },
          "total_items": 100,
          "page_size": 20,
          "page_count": 5,
          "page_number": 1
        }

GET /projects/:projectId
~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about a project entity specified by :projectId

|   *Query parameters*
|       fields
|       exclude

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "1": {
                "projectId": 1,
                "name": "Project_1 name",
                "description": "This is s project description",
                "companyId": 1,
                "_links": {
                  "project": {
                    "href": "http://my.app-arena.com/api/v2/projects/1"
                  },
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  }
                }
              }
            }
          }
        }

POST /projects
~~~~~~~~~~~~~~

    Creates a new project

    .. Note:: When creating a new project, a version '1.0' and the specified language will be created as well.

|   *Query parameters*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"      : "new project",
            "lang"      : "de_DE"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "projectId": 2,
            "companyId": 1,
            "name": "new project",
            "description": null,
            "version": {
              "projectId": 1,
              "version": "1.1.0"
              "projectId": 2,
              "companyId": 1,
              "name": "autogenerated initial version of project 'new project'.",
              "lang": "de_DE",
              "variant": 1,
              "public": false,
              "language": {
                "projectId": 1,
                "version": "1.1.0"
                "lang": "de_DE",
              }
            }
          }
        }

    .. Tip:: You can change the name of the initial version with a PUT request to /projects/:projectId/versions/1.0

    **Required data**

    name
        .. include:: /partials/name.rst
    lang
        .. include:: /partials/lang.rst

        sets the default language of the initial project version and makes the language available to all connected templates/apps

    **Optional data**

    companyId
        .. include:: /partials/companyId.rst
    description
        .. include:: /partials/description.rst

PUT /projects/:projectId
~~~~~~~~~~~~~~~~~~~~~~~~

    Alters an project entry specified by :projectId

|   *Query parameters*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":         "new project name",
            "description":  "This is a new project description"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "projectId": 2,
            "companyId": 1,
            "name": "new project name",
            "description": "This is a new project description"
          }
        }

    **modifiable parameters**

    name
        .. include:: /partials/name.rst
    companyId
        .. include:: /partials/companyId.rst
    description
        .. include:: /partials/description.rst

DELETE /projects/:projectId
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes an project from the database specified by :projectId

    .. Warning:: This deletes all versions including all contained settings and translations as well!

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Project '2' deleted."
        }

/projects/:projectId/versions
-----------------------------

The version component consists of the following fields:

    **version fields**

    projectId
        .. include:: /partials/uniqueId.rst
    companyId
        .. include:: /partials/companyId.rst
    lang
        .. include:: /partials/lang.rst
    name
        .. include:: /partials/name.rst
    variant
        ``string`` the version number (is called 'variant' only in the version itself, all other components call this field 'version')
    public
        .. include:: /partials/public.rst

    **common fields**

    .. include:: /partials/common_all.rst

GET /projects/:projectId/versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about the versions of a project specified by :project_id

|   *Query parameters*
|       page
|       items
|       fields
|       exclude
|       orderasc/orderdesc

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my.app-arena.com/api/v2/projects/1/versions"
            },
            "next": {
              "href": "http://my.app-arena.com/api/v2/projects/1/versions?page=2"
            },
          },
          "_embedded": {
            "data": {
              "1.0.0": {
                "projectId": 1,
                "name": "project version 1.0.0",
                "variant": "1.0.0",
                "public": false,
                "lang": "de_DE",
                "companyId": 1,
                "projectId": 1,
                "_links": {
                  "version": {
                    "href": "http://my.app-arena.com/api/v2/projects/1/versions/1.0"
                  },
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  },
                  "project": {
                    "href": "http://my.app-arena.com/api/v2/projects/1"
                  }
                }
              },
              "1.1.0": {
                "projectId": 2,
                "version": "1.1.0",
                        .
                        .
                        .
              },
                .
                .
                .
              "M.m.P": {
                        .
                        .
                        .
              }
            }
          },
          "total_items": 10,
          "page_size": 5,
          "page_count": 1,
          "page_number": 1
        }

GET /projects/:projectId/versions/:version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about a project version specified by :projectId and :version

    .. Note:: Use the version number as :version e.g.: GET /projects/1/versions/1.1.0

|   *Query parameters*
|       fields
|       exclude

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "1.1.0": {
                "name": "project version 1.1.0",
                "variant": "1.1.0",
                "public": false,
                "lang": "de_DE",
                "companyId": 1,
                "projectId": 1,
                "_links": {
                  "version": {
                    "href": "http://my.app-arena.com/api/v2/projects/1/versions/1.1"
                  },
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  },
                  "project": {
                    "href": "http://my.app-arena.com/api/v2/projects/1"
                  }
                }
              }
            }
          }
        }

POST /projects/:projectId/versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Create a new version for a project, specified by :projectId

    .. Note:: The default language specified in the request body will be created automatically and is included in the response under the 'language' sub-object!

|   *Query parameters*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"      : "new project version",
            "lang"      : "de_DE"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "projectId": 1,
            "companyId": 1,
            "name": "new project version",
            "lang": "de_DE",
            "variant": "1.2.0",
            "public": false,
            "language": {
              "projectId": 3,
              "version": "1.2.0"
              "lang": "de_DE",
            }
          }
        }

    **Required data**

    name
        .. include:: /partials/name.rst
    lang
        .. include:: /partials/lang.rst

    **Optional data**

    variant
        ``string`` the version number (is called 'variant' only in the version itself, all other components call this field 'version')
    public
        .. include:: /partials/public.rst

PUT /projects/:projectId/versions/:version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alters the properties of a version, specified by :projectId and :version

|   *Query parameters*
|       none

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"      : "new version name"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "projectId": 1,
            "companyId": 1,
            "name": "new version name",
            "lang": "de_DE",
            "variant": "1.2.0",
            "public": false
          }
        }

    **modifiable parameters**

    name
        .. include:: /partials/name.rst
    public
        .. include:: /partials/public.rst

DELETE /projects/:projectId/versions/:version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a version of an project from the database specified by :projectId and :version

    .. Warning:: This deletes all containing settings and translations of the version as well!

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Version '111' deleted."
        }

/projects/:projectId/configs
----------------------------

    The project config component consists of the following fields:

    **project config fields**

    projectId
        .. include:: /partials/uniqueId.rst
    version
        ``string`` the version number, format: "Ma.Mi.P" Ma=Major, Mi=Minor, P=Patch e.g.: "2.0.3"
    configId
        .. include:: /partials/identifier.rst
    lang
        .. include:: /partials/lang.rst
    type
        .. include:: /partials/type.rst
    name
        .. include:: /partials/name.rst
    value
        .. include:: /partials/value.rst
    description
        .. include:: /partials/description.rst
    meta
        .. include:: /partials/meta.rst

    **common fields**

    .. include:: /partials/common_revision.rst

    .. Note:: For all of the following requests, the query 'version' can be used to select a specific project-version. If it is left blank the operation will automatically use the most recent version

GET /projects/:projectId/configs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of config values of an project specified by :projectId

|   *Query parameters*
|       fields
|       exclude
|       lang
|       version

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my.app-arena.com/api/v2/projects/1/configs"
            }
          },
          "_embedded": {
            "data": {
              "config_1": {
                "configId": "config_1",
                "lang": "de_DE",
                "revision": 0,
                "type": "input",
                "name": "project config_1 name",
                "value": "some_value",
                "meta": {"meta_key":{"meta_inner":"meta_inner_value"}},
                "description": "This is a config value description",
                "projectId": 1,
                "version": "1.1.0"
                "_links": {
                  "version": {
                    "href": "http://my.app-arena.com/api/v2/projects/1/versions/1.0"
                  }
                }
              },
              "config_2": {
                "configId": "config_2",
                        .
                        .
                        .
              },
                .
                .
                .
              "config_N": {
                        .
                        .
                        .
              }
            }
          }
        }

GET /projects/:projectId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive the information of a config value entity of a project specified by :templateId and :configId

|   *Query parameters*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "config_1": {
                "configId": "bla",
                "lang": "de_DE",
                "revision": 0,
                "type": "input",
                "name": "bla",
                "value": "lala",
                "meta": null,
                "description": null,
                "projectId": 1,
                "version": "1.1.0"
                "_links": {
                  "version": {
                    "href": "http://my.app-arena.com/api/v2/projects/111/versions/384"
                  }
                }
              }
            }
          }
        }

POST /projects/:projectId/configs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Creates a new config value

|   *Query parameters*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"      : "new config",
            "configId"  : "text_content",
            "type"      : "input"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "projectId": 1,
            "version": "1.1.0"
            "configId": "text_content",
            "lang": "de_DE",
            "type": "input",
            "name": "new config",
            "value": null,
            "description": null,
            "meta": null,
            "revision": 0
          }
        }

    **Required data**

    name
        .. include:: /partials/name.rst
    configId
        .. include:: /partials/identifier.rst
    type
        .. include:: /partials/type.rst

    **Optional data**

    value
        .. include:: /partials/put_value.rst
    description
        .. include:: /partials/description.rst
    meta
        .. include:: /partials/meta.rst
    lang
        .. include:: /partials/lang.rst


PUT /projects/:projectId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alters the properties of a project config entry specified by :projectId and :configId

|   *Query parameters*
|       lang
|       version

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":         "new config name",
            "meta_example": "meta_content",
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "projectId": 1,
            "version": "1.1.0"
            "configId": "config_1",
            "lang": "de_DE",
            "type": "input",
            "name": "new config name",
            "value": "some_value",
            "description": null,
            "meta": "{\"meta_example\":\"meta_content\"}",
            "revision": 2
          }
        }

    **modifiable parameters**

    description
        .. include:: /partials/description.rst
    name
        .. include:: /partials/name.rst
    value
        .. include:: /partials/value.rst
    meta
        .. include:: /partials/meta.rst

DELETE /projects/:projectId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a config entry of an project from the database specified by :projectId and :configId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Config 'config_1' in project '1' deleted."
        }

/projects/:projectId/infos
--------------------------

The project info component consists of the following fields:

    **project info fields**

    projectId
        .. include:: /partials/uniqueId.rst
    version
        ``string`` the version number, format: "Ma.Mi.P" Ma=Major, Mi=Minor, P=Patch e.g.: "2.0.3"
    info_id
        .. include:: /partials/identifier.rst
    lang
        .. include:: /partials/lang.rst
    value
        .. include:: /partials/value.rst
    meta
        .. include:: /partials/meta.rst

    **common fields**

    .. include:: /partials/common_revision.rst

GET /projects/:projectId/infos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive the collection of info values of a project specified by :projectId

|   *Query parameters*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my.app-arena.com/api/v2/projects/1/infos"
            }
          },
          "_embedded": {
            "data": {
              "info_1": {
                "infoId": "info_1",
                "lang": "de_DE",
                "revision": 1,
                "value": "some_value",
                "projectId": 1,
                "version": "1.1.0"
                "meta": null,
                "_links": {
                  "version": {
                    "href": "http://my.app-arena.com/api/v2/projects/1/versions/1.0"
                  }
                }
              },
              "info_2": {
                "infoId": "info_2",
                        .
                        .
                        .
              },
                .
                .
                .
              "info_N": {
                        .
                        .
                        .
              }
            }
          }
        }

GET /projects/:projectId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive the information of an info entity of an project specified by :projectId and :infoId

|   *Query parameters*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "info_1": {
                "infoId": "info_1",
                "lang": "de_DE",
                "revision": 1,
                "value": "some_value",
                "projectId": 1,
                "version": "1.1.0"
                "meta": {"type": "string"},
                "_links": {
                  "version": {
                    "href": "http://my.app-arena.com/api/v2/projects/1/versions/1.0"
                  }
                }
              }
            }
          }
        }

POST /projects/:projectId/infos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Creates a new info entry

|   *Query parameters*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"      : "new info name",
            "infoId"    : "new info",
            "lang"      : "de_DE",
            "metakey"   : "metavalue"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "projectId": 1,
            "version": "1.1.0"
            "infoId": "new info",
            "lang": "de_DE",
            "value": null,
            "meta": {"metakey": "metavalue"},
            "revision": 0
          }
        }

    **Required data**

    infoId
        .. include:: /partials/identifier.rst

    **Optional data**

    value
        .. include:: /partials/put_value.rst
    meta
        .. include:: /partials/meta.rst
    lang
        .. include:: /partials/lang.rst

PUT /projects/:projectId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alter a info value for an project specified by :projectId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "value":   "new value"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "projectId": 1,
            "version": "1.1.0"
            "infoId": "info_1",
            "lang": "de_DE",
            "value": "new value",
            "meta": "{\"type\":\"string\"}",
            "revision": 2
          }
        }

    **modifiable parameters**

    value
        .. include:: /partials/put_value.rst
    meta
        .. include:: /partials/meta.rst

DELETE /projects/:projectId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a info value of an project from the database specified by :projectId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Info 'info_1' in project '1' deleted."
        }

/projects/:projectId/languages
------------------------------

The project language component consists of the following fields:

    **project language fields**

    projectId
        .. include:: /partials/uniqeId.rst
    version
        ``string`` the version number, format: "Ma.Mi.P" Ma=Major, Mi=Minor, P=Patch e.g.: "2.0.3"
    lang
        .. include:: /partials/lang.rst

    **common fields**

    .. include:: /partials/common_all.rst

GET /projects/:projectId/languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about the available languages specified by :projectId

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "available": {
            "de_DE": {
              "lang": "de_DE",
              "projectId": 1,
              "version": "1.1.0"
            }
          }
        }

POST /projects/:projectId/languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Activate a language in an project specified by :projectId and :lang

|   *Query parameters*
|       none

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "lang"  : "en_US"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "projectId": 1,
            "version": "1.1.0"
            "lang": "en_US"
          }
        }

    **required data**

    lang
        .. include:: /partials/lang.rst

/projects/:projectId/translations
---------------------------------

The template translation component consists of the following fields:

    **template translation fields**

    translationId
        .. include:: /partials/identifier.rst
    version
        ``string`` the version number, format: "Ma.Mi.P" Ma=Major, Mi=Minor, P=Patch e.g.: "2.0.3"
    lang
        .. include:: /partials/lang.rst
    projectId
        .. include:: /partials/uniqueId.rst
    translated
        .. include:: /partials/translated.rst
    translation
        .. include:: /partials/translation.rst
    pluralized
        .. include:: /partials/pluralized.rst
    translationPluralized
        .. include:: /partials/translationPluralized.rst

    **common fields**

    .. include:: /partials/common_revision.rst

GET /projects/:projectId/translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive translations of a project specified by :projectId

|   *Query parameters*
|       lang
|       fields
|       exclude
|       orderasc/orderdesc

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my-app-arena.com/api/v2/projects/1/translations"
            }
          },
          "_embedded": {
            "data": {
              "translation_1": {
                "translationId": "translation_1",
                "lang": "de_DE",
                "revision": 0,
                "translation": "This is a translated text",
                "translated": true,
                "translationPluralized": null,
                "pluralized": false,
                "projectId": 1,
                "version": "1.1.0"
                "_links": {
                  "version": {
                    "href": "http://my-app-arena.com/api/v2/projects/1/versions/1.0"
                  }
                }
              },
              "translation_2": {
                "translationId": "translation_2",
                            .
                            .
                            .
              },
                .
                .
                .
              "translation_N": {
                            .
                            .
                            .
              }
            }
          }
        }

PUT /projects/:projectId/translations/:translationId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Change a translation for a project specified by :projectId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "translation":  "new translation"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "translationId": "translation_1",
            "lang": "de_DE",
            "projectId": 1,
            "version": "1.1.0"
            "translated": true,
            "translation": "new translation",
            "translationPluralized": null,
            "pluralized": false,
            "revision": 1
          }
        }

    **modifiable parameters**

    translation
        .. include:: /partials/translation.rst
    translated
        .. include:: /partials/translated.rst
    translationPluralized
        .. include:: /partials/translationPluralized.rst
    pluralized
        .. include:: /partials/pluralized.rst

DELETE /projects/:projectId/translations/:translationId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a translation of a project specified by :projectId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Translation 'translation_1' in project '1' deleted."
        }

.. _code: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2