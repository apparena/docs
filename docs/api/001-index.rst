API - Getting started
=====================

API key
-------

To request restricted information from the API, you need to add an API key or `JWT`_ to your request header. Read more
about it in `Authorization <020-auth.html>`_

If you do not have access to the developer section yet, please drop us an email to s.buckpesch at app-arena.com
with your contact data and will we get in touch with you and sent you an API key.

.. _JWT: http://jwt.io/

API Endpoint
------------

All API URLs listed in this documentation are relative to ``https://v25.app-arena.com/api/v2/``.

HTTP Verbs
----------

.. _codes:

The App-Arena API is a RESTful API. All requests can be made using one of the following HTTP verbs

+------------+--------------------------+-------------------------------------------------------+
|            |    Valid for             |   Description                                         |
+============+==========================+=======================================================+
| GET        |    Entity, Collection    |   Request a single entity or a whole collection       |
+------------+--------------------------+-------------------------------------------------------+
| POST       |    Collection            |   Creates a new entity in a collection                |
+------------+--------------------------+-------------------------------------------------------+
| PUT        |    Entity                |   Updates an entity                                   |
+------------+--------------------------+-------------------------------------------------------+
| DELETE     |    Entity                |   Deletes an entity                                   |
+------------+--------------------------+-------------------------------------------------------+


Passing Request Data
--------------------

Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.
The documentation for each API call will contain more detail on the parameters accepted by the call.

Response Formats
----------------

The API responds using HTTP Status Codes so that you can see immediately if you request was successful or an error occurred.
A complete list of HTTP response formats you can find here: HTTP-Statuscodes_

.. _HTTP-Statuscodes: http://de.wikipedia.org/wiki/HTTP-Statuscode

+------------+------------------------------+
|            |    HTTP-Response on Success  |
+============+==============================+
| GET        |    200 (OK)                  |
+------------+------------------------------+
| POST       |    201 (Created)             |
+------------+------------------------------+
| PUT        |    200 (OK)                  |
+------------+------------------------------+
| DELETE     |    200 (OK)                  |
+------------+------------------------------+

The JSON output depends on the type of request and the data submitted. GET Requests will mostly output data in the HAL-format,
a format which provides links to the mentioned resources for easy resource browsing. As some of the requests are intended for listing
items to the user, these requests will output the data paginated. The data comes in chunks of an adjustable size for convenient
item browsing. PUT and POST requests however output besides a status code the created/updated information without any links to the resources,
as this information serves for verification and further processing. DELETE requests will always output a status and a message.

.. _HAL-format: https://en.wikipedia.org/wiki/Hypertext_Application_Language

Response examples
-----------------

.. http:method:: GET request HAL format

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "9273": {
                "appId": 9273,
                "name": "Onpage App-1421917963",
                "lang": "de_DE",
                "activated": false,
                "expiryDate": "2099-01-01 00:00:00",
                "companyId": 2,
                "templateId": 838,
                "_links": {
                  "app": {
                    "href": "https://v25-stage.app-arena.com/api/v2/apps/9273"
                  },
                  "appLanguage": {
                    "href": "https://v25-stage.app-arena.com/api/v2/apps//languages/de_DE"
                  },
                  "company": {
                    "href": "https://v25-stage.app-arena.com/api/v2/companies/2"
                  },
                  "template": {
                    "href": "https://v25-stage.app-arena.com/api/v2/templates/838"
                  }
                }
              }
            }
          }
        }