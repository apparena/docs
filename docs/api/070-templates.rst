API - Template requests
=======================

    .. Hint:: While this documentation uses dummy names like config_1, info_1, etc., you are free to choose the ID of the values yourself as long as they contain only letters from a-z, numbers 0-9 and the underscore

/templates
----------

GET /templates
~~~~~~~~~~~~~~

    Receive a collection of templates owned by your company.

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
              "href": "https://my.app-arena.com/api/v2/templates?page=2"
            },
            "self": {
              "href": "https://my.app-arena.com/api/v2/templates"
            }
          },
          "_embedded": {
            "data": {
              "1": {
                "templateId": 1,
                "name": "template_1",
                "lang": "de_DE",
                "parentId": 1,
                "versionId": 1,
                "companyId": 1,
                "public": true,
                "_links": {
                  "template": {
                    "href": "https://my.app-arena.com/api/v2/templates/1"
                  },
                  "language": {
                    "href": "https://my.app-arena.com/api/v2/templates/1/languages"
                  },
                  "parent": {
                    "href": "https://my.app-arena.com/api/v2/templates/1"
                  },
                  "version": {
                    "href": "https://my.app-arena.com/api/v2/projects/1/versions/1"
                  },
                  "company": {
                    "href": "https://my.app-arena.com/api/v2/companies/1"
                  }
                }
              },
              "2": {
                "templateId": 2,
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
          "total_items": 1000,
          "page_size": 20,
          "page_count": 50,
          "page_number": 1
        }

GET /templates/:templateId
~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about a template entity specified by :templateId

|   *Query parameters*
|       fields
|       exclude

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "1": {
                "templateId": 1,
                "name": "template_1",
                "lang": "de_DE",
                "parentId": 1,
                "versionId": 1,
                "companyId": 1,
                "public": true,
                "_links": {
                  "template": {
                    "href": "http://my.app-arena.com/api/v2/templates/1"
                  },
                  "language": {
                    "href": "http://my.app-arena.com/api/v2/templates/1/languages"
                  },
                  "parent": {
                    "href": "http://my.app-arena.com/api/v2/templates/1"
                  },
                  "version": {
                    "href": "http://my.app-arena.com/api/v2/projects/1/versions/1"
                  },
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  }
                }
              }
            }
          }
        }

POST /templates
~~~~~~~~~~~~~~~

    Creates a new template

|   *Query parameters*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "projectId"     : 1,
            "version"       : 1.2,
            "name"          : "new template"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "templateId": 1,
            "versionId": 1,
            "projectId": 1,
            "parentId": 1190,
            "companyId": 1,
            "lang": "de_DE",
            "name": "test template for collectionrunner 1467211852",
            "public": false
          }
        }

    **Required data**

    name
        (string) Name of the template
    projectId
        (integer) The project this template is connected to

    **Optional data**

    parentId
        (integer) The ID of the parent template
    version
        (float) The version of the specified project the template should point to, if not specified the most recent version is used
    companyId
        (integer) ID of the owning company, if not specified, app will be owned by the company used for authorization
    lang
        (string) The default language of the template, if left out, the default language of the project is used instead.
        Syntax: de_DE for Germany, de_AT for Austrian german, en_US for american english ...
    public
        (bool) Sets the public status of the template

.. _code: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

PUT /templates/:templateId
~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alters an template entry specified by :templateId

|   *Query parameters*
|       lang

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"          : "new template name"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "templateId": 1,
            "versionId": 1,
            "projectId": 1,
            "parentId": 1,
            "companyId": 1,
            "lang": "de_DE",
            "name": "new template name",
            "public": false
          }
        }

    **modifiable parameters**

    parentId
        (integer)
    versionId
        (integer)
    companyId
        (integer)
    name
        (string)
    public
        (bool)

DELETE /templates/:templateId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes an template from the database specified by :templateId

    .. Warning:: This deletes all containing settings and translations as well!

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Template '1' deleted."
        }

/templates/:templateId/configs
------------------------------

GET /templates/:templateId/configs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of config values of an template specified by :templateId

|   *Query parameters*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my.app-arena.com/api/v2/templates/1/configs"
            }
          },
          "_embedded": {
            "data": {
              "config_1": {
                "configId": "config_1",
                "lang": "de_DE",
                "revision": 0,
                "name": "template_config_name",
                "value": "some_value",
                "type": "input",
                "description": "This is an example of a template config value.",
                "templateId": 1,
                "meta": {"meta_key":{"meta_inner":"meta_inner_value"}},
                "_links": {
                  "template": {
                    "href": "http://my.app-arena.com/api/v2/templates/1"
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
              "config_N":{
              }
            }
          }
        }

GET /templates/:templateId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive the information of a config value entity of an template specified by :templateId and :configId

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
                "configId": "config_1",
                "lang": "de_DE",
                "name": "template_config_name",
                "revision": 0,
                "value": "some_value",
                "meta": {"meta_key":{"meta_inner":"meta_inner_value"}},
                "type": "input",
                "description": "This is an example of a template config value.",
                "appId": 1,
                "_links": {
                  "app": {
                    "href": "http://my.app-arena.com/api/v2/apps/1"
                  },
                  "config": {
                    "href": "http://my.app-arena.com/api/v2/apps/1/configs/config_1"
                  }
                }
              }
            }
          }
        }

PUT /templates/:templateId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alter a config value for an template specified by :templateId and :configId

|   *Query parameters*
|       lang

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "value"    :   "new value"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "appId": 1,
            "configId": "config_1",
            "lang": "de_DE",
            "type": "input",
            "name": "config value 1",
            "value": "new value",
            "description": "This is an example of a app config value.",
            "revision": 1,
            "meta": {"meta_key":{"meta_inner":"meta_inner_value"}}
          }
        }

    **modifiable parameters**

    value
        see `config <../api/060-config.html>`_ for characteristic behavior
    name
        (string)
    description
        (string)
    meta
        see `config <../api/060-config.html>`_ meta section for information about the meta data of config values

DELETE /templates/:templateId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a config value of an template from the database specified by :templateId and :configId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Config 'config_1' deleted."
        }

/templates/:templateId/infos
----------------------------

GET /templates/:templateId/infos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of info values of an template specified by :templateId

|   *Query parameters*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my.app-arena.com/api/v2/templates/1/infos"
            }
          },
          "_embedded": {
            "data": {
              "info_1": {
                "infoId": "info_1",
                "lang": "de_DE",
                "name": "info value 1",
                "revision": 0,
                "value": "some_value",
                "meta": {"meta_key":{"meta_inner":"meta_inner_value"}},
                "type": "input",
                "description": "This is an example of an template info value.",
                "templateId": 1,
                "_links": {
                  "app": {
                    "href": "http://my.app-arena.com/api/v2/templates/1"
                  },
                  "info": {
                    "href": "http://my.app-arena.com/api/v2/templates/1/configs/info_1"
                  }
                }
              },
              "info_2": {
                "infoId": "info_2",
                    .
                    .
                    .
                }
              },
                    .
                    .
                    .
              }
            }
          }
        }

GET /templates/:templateId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive the information of an info entity of an template specified by :templateId and :infoId

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
                "revision": 0,
                "value": "1234",
                "templateId": 888,
                "meta": {"type": "integer"},
                "_links": {
                  "info": {
                    "href": "http://my.app-arena.com/api/v2/apps/1/infos/info_1"
                  },
                  "template": {
                    "href": "http://my.app-arena.com/api/v2/templates/888"
                  }
                }
              }
            }
          }
        }

PUT /templates/:templateId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alter a info value for an template specified by :templateId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "value"    :   "new value"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "templateId": 1,
            "infoId": "info_1",
            "lang": "de_DE",
            "revision": 1,
            "value": "new value",
            "meta": {"type":"string"}
          }
        }

    **modifiable parameters**

    value
        (string)
    meta
        see `config <../api/060-config.html>`_ meta section for information about the PUT behaviour of meta data

DELETE /templates/:templateId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a info value of an template from the database specified by :templateId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Info 'info_1' in template '1' deleted."
        }

/templates/:templateId/languages
--------------------------------

GET /templates/:templateId/languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about the available and activated languages specified by :templateId

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "available": {
            "de_DE": {
              "lang": "de_DE",
              "versionId": 1
            },
            "en_US": {
              "lang": "en_US",
              "versionId": 1
            }
          }
        }

POST /templates/:templateId/languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Activate a language in an template specified by :templateId and :lang

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
            "templateId": 1,
            "lang": "en_US",
          }
        }

/templates/:templateId/translations
-----------------------------------

GET /templates/:templateId/translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive translations of an template specified by :templateId

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
              "href": "http://my.app-arena.com/api/v2/templates/1/translations"
            }
          },
          "_embedded": {
            "data": {
              "translation_1": {
                "translationId": "translation_1",
                "lang": "de_DE",
                "revision": 0,
                "translation": "translated_text",
                "translated": true,
                "translationPluralized": "translation_pluralized_text",
                "pluralized": true,
                "versionId": 1,
                "_links": {
                  "version": {
                    "href": "http://my.app-arena.com/api/v2/projects/1/versions/1"
                  }
                }
              },
              "translation_2": {
                "translationId": "translation_2",
                    .
                    .
                    .
              },
              "translation_3":{
                    .
                    .
                    .
              },
                .
                .
                .
              "translation_N":{
                    .
                    .
                    .
              }
            }
          }
        }

PUT /templates/:templateId/translations/:translationId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Change a translation for an template specified by :templateId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "translation": "new translation"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "translationId": "translation_1",
            "lang": "de_DE",
            "templateId": 1,
            "translation": "new translation",
            "translated": true,
            "translation_pluralized": "translation_pluralized_text",
            "pluralized": true,
            "revision": 1
          }
        }

    **modifiable parameters**

    translation
        (string)
    translated
        (bool)
    translationPluralized
        (string)
    pluralized
        (bool)

DELETE /templates/:templateId/translations/:translationId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a translation of an template specified by :templateId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Translation 'translation_1' in template '1' deleted."
        }