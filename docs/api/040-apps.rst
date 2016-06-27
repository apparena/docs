API - App requests
==================

.. Tip:: You can test all requests in our API-Explorer_.

.. _API-Explorer: http://www.app-arena.com

GET /apps
---------

.. _apps:

.. http:method:: GET /api/v2/apps

    Receive a collection of apps owned by your company.

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
                "name": "Example App",
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
                "name": "Example App 2",
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


.. http:method:: GET /api/v2/apps/:app_id

    Receive information about an app entity.

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "1": {
                "appId": 1,
                "name": "Example App",
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

.. http:method:: POST /api/v2/apps

    Creates a new App

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "templateId"    :   888,
            "name"          :   "created example App",
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
            "name": "created example App",
            "activated": false,
            "expiryDate": "2016-08-26 10:39:00"
          }
        }

    Required data:

    :data string name:          Name of the company
    :data integer templateId:   The Template ID this App is connected to
    :data string lang:          A language code_. Syntax: de_DE for Germany, de_AT for Austrian german

    Optional data:

    :optional integer companyId:            ID of the owning company
    :optional integer/string expiryDate:    Integer: Sets the number of days the App is valid, 0 sets the app valid for 50 years. String: Sets a date for app expiration, needs to be in the format 'Y-m-d H:i:s' with Y=year, m=month, d=day, H=hour, i=minute, s=second
    :optional boolean activated:            Sets the Status of the App

.. _code: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

.. http:method:: PUT /api/v2/apps/:app_id

    Alters an App entry

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
            "name": "created Example App",
            "activated": true,
            "expiryDate": "2016-08-26 10:39:00"
          }
        }

.. http:method:: DELETE /api/v2/apps/:app_id

    Deletes an App from the database

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "App '1' deleted."
        }