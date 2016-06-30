API - Template requests
=======================

.. Tip:: You can test all requests in our API-Explorer_.

.. _API-Explorer: http://www.app-arena.com

/templates
----------

GET /templates
~~~~~~~~~~~~~~

    Receive a collection of templates owned by your company.

|   *Available queries*
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

|   *Available queries*
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

|   *Available queries*
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
        Name of the company
    templateId
        The template ID this app is connected to
    lang
        A language code_. Syntax: de_DE for Germany, de_AT for Austrian german

    **Optional data**

    companyId
        ID of the owning company, if not specified, app will be owned by the company used for authorization
    expiryDate
        Integer
            Sets the number of days the app is valid, 0 sets the app valid for 50 years.
        String
            Sets a date for app expiration, needs to be in the format 'Y-m-d H:i:s' with Y=year, m=month, d=day, H=hour, i=minute, s=second
    activated
        Sets the activation status of the app

.. _code: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

PUT /templates/:templateId
~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alters an template entry specified by :templateId

|   *Available queries*
|       force

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

    **Changeable fields**

    parentId
        integer
    versionId
        integer
    companyId
        integer
    name
        string
    public
        bool

DELETE /templates/:templateId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes an template from the database specified by :templateId

|   *Available queries*
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

|   *Available queries*
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

|   *Available queries*
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