API - Template requests
=======================

    .. Hint:: While this documentation uses dummy names like config_1, info_1, etc., you are free to choose the ID of the values yourself as long as they contain only letters from a-z, numbers 0-9 and the underscore

    Every template points to a parent template or a project. When the parentId is not equal to the templateId, the parent template is used. Only if the parentId equals the templateId, the project is the next step in the chain.

/templates
----------

The template component consists of the following fields:

    **template fields**

    templateId
        .. include:: /partials/uniqueId.rst
    projectId
        .. include:: /partials/template_projectId.rst
    parentId
        .. include:: /partials/parentId.rst
    companyId
        .. include:: /partials/companyId.rst
    lang
        .. include:: /partials/lang.rst
    name
        .. include:: /partials/name.rst
    public
        .. include:: /partials/public.rst

    **common fields**

    .. include:: /partials/common_all.rst

    **relations**

    apps, company*, parentTemplate*, configs, translations, infos, versions*, languages*

    * can be fetched via collection request

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
                "projectId": 1,
                "version": "1.1.0"
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
              "templateId": 1,
              "name": "template_1",
              "lang": "de_DE",
              "parentId": 1,
              "projectId": 1,
              "version": "1.1.0",
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
            "projectId": 1,
            "version": "1.1.0"
            "parentId": 1190,
            "companyId": 1,
            "lang": "de_DE",
            "name": "test template for collectionrunner 1467211852",
            "public": false
          }
        }

    **Required data**

    name
        .. include:: /partials/name.rst
    projectId
        .. include:: /partials/uniqueId.rst

    **Optional data**

    parentId
        ``integer`` the template this template should be connected to, if left blank the newly created templateId is inserted
    version
        ``string`` The version of the specified project the template should point to, if not specified the most recent version is used
    companyId
        ``integer`` ID of the owning company, if not specified, app will be owned by the company used for authorization
    lang
        .. include:: /partials/lang.rst
    public
        .. include:: /partials/public.rst

Creating a template from an app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes it might be handy to convert an app into a template. In this case a new template is created and all config, info,
translation and language entries are copied into it.

In order to execute this, make a regular POST request onto /templates, but instead of submitting the required information for creating
a template, just send a field "copyFrom" : "app" and the appId of the app you want to convert.

To keep the response JSON small, only the basic template information is returned. Use a GET request on templates/:templateId/infos, .../configs,
.../translations or .../languages to retrieve its contents.

.. http:response:: POST /templates

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"  : "app",
            "appId"     :   1
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "templateId": 2,
            "version": "1.0.0",
            "projectId": 1,
            "parentId": 2,
            "companyId": 1,
            "lang": "en_US",
            "name": "App Name [copy]",
            "public": false
          }
        }

    **Required data**

    copyFrom
        ``string``  must be "app"
    appId
        ``integer`` specifies the app the template will be copied from

    **Optional data**

    companyId
        ``integer`` defines a different company than your own as owner of the newly created template
    parentId
        ``integer`` defines the template, the newly created template should point to. If left out, the template to which the app pointed will be used, if set to '0', the template points to the project.
    projectId
        ``integer`` defines the project the newly created template points to. If the parentId is not equal to the templateId, the template points to the parent template, meaning that this will have no effect if a parent template is defined.
    version
        ``string``  if a projectId is submitted, you can specify the version here
    lang
        ``string``  sets the default language of the new template. This language must be present in the root project.
    name
        ``string``  defines the name of the new template. If not specified, the name of the app with an additional "[copy]" string is used
    public
        ``bool``    sets the public status of the new template


Copy an existing template
~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to modify an existing template but keep the original, you can copy it by sending a POST request with the field "copyFrom" : "template" and the templateId

.. http:response:: POST /templates

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"      : "template",
            "templateId"    :   1
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "templateId": 2,
            "version": "1.0.0",
            "projectId": 1,
            "parentId": 2,
            "companyId": 1,
            "lang": "en_US",
            "name": "Template Name [copy]",
            "public": false
          }
        }

    **Required data**

    copyFrom
        ``string``  must be "template"
    templateId
        ``integer``|``string`` sets the template ID which is to be copied

    **Optional data**

    companyId
        ``integer`` defines a different company than your own as owner of the newly created template
    parentId
        ``integer`` defines the template, the newly created template should point to. If left out, the template to which the app pointed will be used, if set to '0', the template points to the project.
    projectId
        ``integer`` defines the project the newly created template points to. If the parentId is not equal to the templateId, the template points to the parent template, meaning that this will have no effect if a parent template is defined.
    version
        ``string``  if a projectId is submitted, you can specify the version here
    lang
        ``string``  sets the default language of the new template. This language must be present in the root project.
    name
        ``string``  defines the name of the new template. If not specified, the name of the original template with an additional "[copy]" string is used
    public
        ``bool``    sets the public status of the new template

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
            "projectId": 1,
            "version": "1.1.0"
            "parentId": 1,
            "companyId": 1,
            "lang": "de_DE",
            "name": "new template name",
            "public": false
          }
        }

    **modifiable parameters**

    parentId
        .. include:: /partials/parentId.rst
    projectId
        .. include:: /partials/template_projectId.rst
    version
        ``string`` The version of the specified project the template should point to, if not specified the most recent version is used (needs a projectId)
    companyId
        .. include:: /partials/companyId.rst
    name
        .. include:: /partials/name.rst
    public
        .. include:: /partials/public.rst

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

--------

/templates/:templateId/configs
------------------------------

The template config component consists of the following fields:

    **template config fields**

    templateId/projectId
        .. include:: /partials/uniqueId.rst
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
              "configId": "config_1",
              "lang": "de_DE",
              "name": "template_config_name",
              "revision": 0,
              "value": "some_value",
              "meta": {
                "meta_key": {
                  "meta_inner": "meta_inner_value"
                }
              },
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
        .. include:: /partials/value.rst
    name
        .. include:: /partials/name.rst
    description
        .. include:: /partials/description.rst
    meta
        .. include:: /partials/meta.rst

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

--------

/templates/:templateId/infos
----------------------------

The template info component consists of the following fields:

    **template info fields**

    templateId/projectId
        .. include:: /partials/uniqueId.rst
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
              "infoId": "info_1",
              "lang": "de_DE",
              "revision": 0,
              "value": "1234",
              "templateId": 888,
              "meta": {
                "type": "integer"
              },
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
        .. include:: /partials/value.rst
    meta
        .. include:: /partials/meta.rst

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

--------

/templates/:templateId/languages
--------------------------------

The template language component consists of the following fields:

    *template language fields*

    appId/projectId
        .. include:: /partials/uniqueId.rst
    lang
        .. include:: /partials/lang.rst

    **common fields**

    .. include:: /partials/common_all.rst


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
              "projectId": 1,
              "version": "1.1.0"
            },
            "en_US": {
              "lang": "en_US",
              "projectId": 1,
              "version": "1.1.0"
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

    **required data**

    lang
        .. include:: /partials/lang.rst

/templates/:templateId/translations
-----------------------------------

The template translation component consists of the following fields:

    **template translation fields**

    translationId
        .. include:: /partials/identifier.rst
    lang
        .. include:: /partials/lang.rst
    templateId
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
                "projectId": 1,
                "version": "1.1.0"
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
        .. include:: /partials/translation.rst
    translated
        .. include:: /partials/translated.rst
    translationPluralized
        .. include:: /partials/translationPluralized.rst
    pluralized
        .. include:: /partials/pluralized.rst

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

.. _code: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

.. _meta: ../api/050-config.html#meta-data-behaviour