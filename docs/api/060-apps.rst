==================
API - App requests
==================

    .. Hint:: While this documentation uses dummy names like config_1, info_1, etc., you are free to choose the ID of the values yourself as long as they contain only letters from a-z, numbers 0-9 and the underscore

/apps
-----

The app component consists of the following fields:

    **app fields**

    appId
        .. include:: /partials/uniqueId.rst
    templateId
        ``integer``     the template this app points to
    companyId
        ``integer``     id of the owning company
    lang
        .. include:: /partials/lang.rst
    name
        .. include:: /partials/name.rst
    activated
        .. include:: /partials/activated.rst
    expiryDate
        ``string``      the date until the app is running or ``integer`` the number of days the app is running

    **common fields**

    .. include:: /partials/common_all.rst

GET /apps
~~~~~~~~~

    Receive a collection of apps owned by your company.

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
              "N": {
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

|   *Query parameters*
|       fields
|       exclude

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
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

POST /apps
~~~~~~~~~~

    Creates a new app

|   *Query parameters*
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
        .. include:: /partials/name.rst
    templateId
        .. include:: /partials/templateId.rst
    lang
        .. include:: /partials/lang.rst

    **Optional data**

    companyId
        .. include:: /partials/post_companyId.rst
    expiryDate
        ``Integer``
            Sets the number of days the app is valid, 0 sets the app valid for 50 years.
        ``String``
            Sets a date for app expiration, needs to be in the format 'Y-m-d H:i:s' with Y=year, m=month, d=day, H=hour, i=minute, s=second
    activated
        .. include:: /partials/activated.rst

Copy an existing app
~~~~~~~~~~~~~~~~~~~~

If you want to modify an existing template but keep the original, you can copy it by sending a POST request with the field "copyFrom" : "template" and the templateId

.. http:response:: POST /apps

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"      : 1
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "appId": 2,
            "templateId": 1,
            "companyId": 1,
            "lang": "de_DE",
            "name": "App name [copy]",
            "activated": true,
            "expiryDate": "2016-10-03 13:16:52"
          }
        }

    **Required data**

    copyFrom
        ``string``  specifies the app which is to be copied

    **Optional data**

    templateId
        ``integer`` sets the template the new app is pointing to
    companyId
        ``integer`` sets a different company than your own as owner of the newly created app
    expiryDate
        ``string``  sets the expiration date of the app
        ``integer`` sets the expiration date in days. A value of 30 means that the app will expire in 30 days from the day of execution
    lang
        ``string``  sets the default language of the new app. This language must be present in the root project
    name
        ``string``  defines the name of the new app. If not specified, the name of the original app with an additional "[copy]" string is used
    activated
        ``bool``    sets the activation status of the new app

PUT /apps/:appId
~~~~~~~~~~~~~~~~

    Alters an app entry specified by :appId

|   *Query parameters*
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

    **modifiable parameters**

    templateId
        .. include:: /partials/templateId.rst
    name
        .. include:: /partials/name.rst
    activated
        .. include:: /partials/activated.rst
    expiryDate
        ``Integer``
            Sets the number of days the app is valid, 0 sets the app valid for 50 years.
        ``String``
            Sets a date for app expiration, needs to be in the format 'Y-m-d H:i:s' with Y=year, m=month, d=day, H=hour, i=minute, s=second

DELETE /apps/:appId
~~~~~~~~~~~~~~~~~~~

    Deletes an app from the database specified by :appId

    .. Warning:: This deletes all contained settings and translations as well!

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "app '1' deleted."
        }

/apps/:appId/configs
--------------------

The app config component consists of the following fields:

    **app config fields**

    appId/templateId/projectId
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

GET /apps/:appId/configs
~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of config values of an app specified by :appId

|   *Query parameters*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my.app-arena.com/api/v2/apps/1/configs"
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
              "name": "config value 1",
              "revision": 0,
              "value": "some_value",
              "meta": {
                "meta_key": {
                  "meta_inner": "meta_inner_value"
                }
              },
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
            }
          }
        }

PUT /apps/:appId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alter a config value for an app specified by :appId and :configId

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
        .. include:: /partials/put_value.rst
    name
        .. include:: /partials/name.rst
    description
        .. include:: /partials/description.rst
    meta
        .. include:: /partials/meta.rst

DELETE /apps/:appId/configs/:configId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a config value of an app from the database specified by :appId and :configId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Config 'config_1' deleted."
        }

/apps/:appId/infos
------------------

The app info component consists of the following fields:

    **app info fields**

    appId/templateId/projectId
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

GET /apps/:appId/infos
~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of info values of an app specified by :appId

|   *Query parameters*
|       fields
|       exclude
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my.app-arena.com/api/v2/apps/1/infos"
            }
          },
          "_embedded": {
            "data": {
              "info_1": {
                "infoId": "info_1",
                "lang": "de_DE",
                "revision": 0,
                "value": "some_value",
                "meta": {"meta_key":{"meta_inner":"meta_inner_value"}},
                "description": "This is an example of an app info value.",
                "appId": 1,
                "_links": {
                  "app": {
                    "href": "http://my.app-arena.com/api/v2/apps/1"
                  },
                  "info": {
                    "href": "http://my.app-arena.com/api/v2/apps/1/infos/info_1"
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

GET /apps/:appId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive the information of an info entity of an app specified by :appId and :infoId

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

PUT /apps/:appId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alter a info value for an app specified by :appId and :infoId

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
            "infoId": "info_1",
            "lang": "de_DE",
            "revision": 1,
            "value": "new value",
            "meta": {"type":"string"}
          }
        }

    **modifiable parameters**

    value
        .. include:: /partials/put_value.rst
    meta
        .. include:: /partials/meta.rst

DELETE /apps/:appId/infos/:infoId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a info value of an app from the database specified by :appId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Info 'info_1' in app '1' deleted."
        }

/apps/:appId/languages
----------------------

The app language component consists of the following fields:

    **app language fields**

    appId/projectId
        .. include:: /partials/uniqueId.rst
    lang
        .. include:: /partials/lang.rst

    **common fields**

    .. include:: /partials/common_all.rst

.. Note:: Activated languages always belong to the app while the available languages derive from the corresponding project.

GET /apps/:appId/languages
~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about the available and activated languages specified by :appId

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "activated": {
            "de_DE": {
              "lang": "de_DE",
              "appId": 1
            }
          },
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

POST /apps/:appId/languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Activate a language in an app specified by :appId and :lang

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
            "appId": 1,
            "lang": "en_US",
          }
        }

    **required data**

    lang
        .. include:: /partials/lang.rst

/apps/:appId/translations
-------------------------

The app translation component consists of the following fields:

    **app translation fields**

    translationId
        .. include:: /partials/identifier.rst
    lang
        .. include:: /partials/lang.rst
    appId
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

GET /apps/:appId/translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive translations of an app specified by :appId

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
              "href": "http://my.app-arena.com/api/v2/apps/1/translations"
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

PUT /apps/:appId/translations/:translationId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Change a translation for an app specified by :appId and :infoId

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
            "appId": 1,
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

DELETE /apps/:appId/translations/:translationId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a translation of an app specified by :appId and :infoId

|   *Query parameters*
|       lang

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Translation 'translation_1' deleted."
        }

.. _code: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

.. _meta: ../api/050-config.html#meta-data-behaviour