API - App requests
==================

.. Tip:: You can test all requests in our API-Explorer_.

.. _API-Explorer: http://www.app-arena.com

/apps
-----

.. _apps:

GET /apps
~~~~~~~~~

    Receive a collection of apps owned by your company.

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
              "href": "https://my.app-arena.com/api/v2/apps?page=2"
            },
            "self": {
              "href": "https://my.app-arena.com/api/v2/apps"
            }
          },
          "_embedded": {
            "data": {
              "1": {
                "appId": 1,
                "name": "Example app",
                "lang": "en_US",
                "activated": true,
                "expiryDate": "2016-11-30 00:00:00",
                "companyId": 1,
                "templateId": 888,
                "_links": {
                  "app": {
                    "href": "https://my.app-arena.com/api/v2/apps/1"
                  },
                  "appLanguage": {
                    "href": "https://my.app-arena.com/api/v2/apps/1/languages/en_US"
                  },
                  "company": {
                    "href": "https://my.app-arena.com/api/v2/companies/1"
                  },
                  "template": {
                    "href": "https://my.app-arena.com/api/v2/templates/888"
                  }
                }
              },
              "2": {
                "appId": 2,
                "name": "Example app 2",
                 .
                 .
                 .
              },
              "3": {
                 .
                 .
                 .
              },
                 .
                 .
                 .
              "20": {
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


GET /apps/:appId
~~~~~~~~~~~~~~~~

    Receive information about an app entity specified by :appId

    *Available queries*
|       fields
|       exclude

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "1": {
                "appId": 1,
                "name": "Example app",
                "lang": "de_DE",
                "activated": false,
                "expiryDate": "2099-01-01 00:00:00",
                "companyId": 1,
                "templateId": 888,
                "_links": {
                  "app": {
                    "href": "https://my.app-arena.com/api/v2/apps/1"
                  },
                  "appLanguage": {
                    "href": "https://my.app-arena.com/api/v2/apps/1/languages/de_DE"
                  },
                  "company": {
                    "href": "https://my.app-arena.com/api/v2/companies/1"
                  },
                  "template": {
                    "href": "https://my.app-arena.com/api/v2/templates/888"
                  }
                }
              }
            }
          }
        }

POST /apps
~~~~~~~~~~

    Creates a new app

    *Available queries*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "templateId"    :   888,
            "name"          :   "created example app",
            "expiryDate"    :   60,
            "lang"          :   "de_DE"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "appId": 1,
            "templateId": 888,
            "companyId": 1,
            "lang": "de_DE",
            "name": "created example app",
            "activated": false,
            "expiryDate": "2016-08-26 10:39:00"
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

PUT /apps/:appId
~~~~~~~~~~~~~~~~

    Alters an app entry specified by :appId

    *Available queries*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "activated"    :   true,
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "appId": 1,
            "templateId": 888,
            "companyId": 1,
            "lang": "de_DE",
            "name": "created Example app",
            "activated": true,
            "expiryDate": "2016-08-26 10:39:00"
          }
        }

    **Changeable fields**

    templateId
        integer
    name
        string
    activated
        bool
    expiryDate
        integer
            app validity in days
        string
            date in format 'Y-m-d H:i:s' with Y=year, m=month, d=day, H=hour, i=minute, s=second

DELETE /apps/:appId
~~~~~~~~~~~~~~~~~~~

    Deletes an app from the database specified by :appId

    *Available queries*
        none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "app '1' deleted."
        }

/apps/:appId/configs
--------------------

GET /apps/:appId/configs
~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of config values of an app specified by :appId

    *Available queries*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://manager.local/api/v2/apps/1/configs"
            }
          },
          "_embedded": {
            "data": {
              "config_1": {
                "configId": "config_1",
                "lang": "de_DE",
                "name": "config value 1",
                "revision": 0,
                "value": "some_value",
                "meta": {"meta_key":{"meta_inner":"meta_inner_value"}},
                "type": "input",
                "description": "This is an example of a app config value.",
                "appId": 1,
                "_links": {
                  "app": {
                    "href": "http://my.app-arena.com/api/v2/apps/1"
                  },
                  "config": {
                    "href": "http://my.app-arena.com/api/v2/apps/1/configs/config_1"
                  }
                }
              },
              "config_2": {
                "configId": "config_2",
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

GET /apps/:appId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive the information of a config value entity of an app specified by :appId and :configId

    *Available queries*
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
                "name": "config value 1",
                "revision": 0,
                "value": "some_value",
                "meta": {"meta_key":{"meta_inner":"meta_inner_value"}},
                "type": "input",
                "description": "This is an example of a app config value.",
                "appId": 1,
                "_links": {
                  "app": {
                    "href": "http://manager.local/api/v2/apps/1"
                  },
                  "config": {
                    "href": "http://my.app-arena.com/api/v2/apps/1/configs/config_1"
                  }
                }
              }
            }
          }
        }

PUT /apps/:appId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alter a config value for an app specified by :appId and :configId

    *Available queries*
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

    **Changeable fields**

    value
        see `config <../api/060-config.html>`_ for characteristic behavior
    name
        string
    description
        string
    meta
        see `config <../api/060-config.html>`_ meta section for information about the meta data of config values

DELETE /apps/:appId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a config value of an app from the database specified by :appId and :configId

    *Available queries*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Config 'config_1' deleted."
        }

/apps/:appId/infos
------------------

GET /apps/:appId/infos
~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of info values of an app specified by :appId

    *Available queries*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://manager.local/api/v2/apps/1/infos"
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
                "description": "This is an example of an app info value.",
                "appId": 1,
                "_links": {
                  "app": {
                    "href": "http://my.app-arena.com/api/v2/apps/1"
                  },
                  "info": {
                    "href": "http://my.app-arena.com/api/v2/apps/1/configs/config_1"
                  }
                }
              },
              "config_2": {
                "configId": "config_2",
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

GET /apps/:appId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive the information of an info entity of an app specified by :appId and :infoId

    *Available queries*
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

PUT /apps/:appId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alter a info value for an app specified by :appId and :infoId

    *Available queries*
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
            "infoId": "info_1",
            "lang": "de_DE",
            "revision": 1,
            "value": "new value",
            "meta": {"type":"string"}
          }
        }

DELETE /apps/:appId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a info value of an app from the database specified by :appId and :infoId

    *Available queries*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Config 'info_1' deleted."
        }

GET /apps/:appId/languages
~~~~~~~~~~~~~~~~~~~~~~~~~~

