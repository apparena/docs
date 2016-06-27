API - Getting started
=====================

API key
-------

To request restricted information from the API, you need to add an API key or a JSON Web Token (`JWT`_) to your request header. Read more
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

Request data is passed to the API by Posting JSON objects to the API endpoints with the appropriate parameters.
The documentation for each API call will contain more detail on the parameters accepted by the call.

Additionally, the requests can be manipulated by queries. The first query must be preceded by a '?' while the following queries
have to be separated by a '&'.

Example:

http://route.to.api/collection/entity?query1=xxx&query2=yyy&query3=...

Available query options:

+------------+--------------------------+-------------------------------------------------------+
| Query      |    Valid for             |   Description                                         |
+============+==========================+=======================================================+
| lang       |    GET,PUT,DELETE        |   points the request to the desired language          |
+------------+--------------------------+-------------------------------------------------------+
| fields     |    GET                   |                                            |
+------------+--------------------------+-------------------------------------------------------+
| PUT        |    Entity                |   Updates an entity                                   |
+------------+--------------------------+-------------------------------------------------------+
| DELETE     |    Entity                |   Deletes an entity                                   |
+------------+--------------------------+-------------------------------------------------------+

The queries

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
a format which provides links to the mentioned resources for easy resource browsing.
As some of the requests are intended for listing items to the user, these requests will additionally output the data paginated.
The data comes in chunks of an adjustable size for convenient item representation. PUT and POST requests however output
besides a status code the created/updated information without any links to the resources, as this information serves for
verification and further processing.
DELETE requests will always output a status and a message.

.. _HAL-format: https://en.wikipedia.org/wiki/Hypertext_Application_Language

Response examples
-----------------

.. http:method:: GET request HAL format


    The relevant data can be found in "_embedded" -> "data" and the status code is only submitted via HTTP. The keys of the
    contained objects are named after their characterizing item for easy processing and representation. This example shows
    the output of the 'App' 9999 entity GET request.

.. http:response:: Example request body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "9999": {
                "appId":        9999,
                "name":         "Example App",
                "lang":         "en_US",
                "activated":    false,
                "expiryDate":   "2099-01-01 00:00:00",
                "companyId":    1,
                "templateId":   888,
                "_links": {
                  "app": {
                    "href":     "https://my.app-arena.com/api/v2/apps/9999"
                  },
                  "language": {
                    "href":     "https://my.app-arena.com/api/v2/apps/9999/languages/en_US"
                  },
                  "company": {
                    "href":     "https://my.app-arena.com/api/v2/companies/1"
                  },
                  "template": {
                    "href":     "https://my.app-arena.com/api/v2/templates/888"
                  }
                }
              }
            }
          }
        }

.. http:method:: GET request HAL format paginated

    Pagination information is added and can be modified by the following queries:
    items : defines the number of objects to be sent per page
    page  : defines the current page

.. http:response:: Example request body

    .. sourcecode:: js

        {
          "_links": {
            "next": {
              "href":   "https://my.app-arena.com/api/v2/apps?items=5&page=3"
            },
            "previous": {
              "href":   "https://my.app-arena.com/api/v2/apps?items=5&page=1"
            },
            "self": {
              "href":   "https://my.app-arena.com/api/v2/apps?items=5&page=2"
            }
          },
          "_embedded": {
            "data": {
              "100": {
                "appId":        100,
                "name":         "example App",
                "lang":         "en_US",
                "activated":    true,
                "expiryDate":   "2017-08-04 00:00:00",
                "companyId":    1,
                "templateId":   10,
                "_links": {
                  "app": {
                    "href":     "https://my.app-arena.com/api/v2/apps/100"
                  },
                  "language": {
                    "href":     "https://my.app-arena.com/api/v2/apps/100/languages/en_US"
                  },
                  "company": {
                    "href":     "https://my.app-arena.com/api/v2/companies/1"
                  },
                  "template": {
                    "href":     "https://my.app-arena.com/api/v2/templates/10"
                  }
                }
              },
              "101": {
                "appId": 101,
                    .
                    .
                    .
                }
              },
              "102": {
                "appId": 102,
                    .
                    .
                    .
                }
              },
              .
              .
              .
            }
          },
          "total_items": 10511,
          "page_size": 5,
          "page_count": 2103,
          "page_number": 2
        }

.. http:method:: POST or PUT request

    The output of these types of requests contains the HTTP status and the created/updated information of the entity in the object "data".

.. http:response:: Example request body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "appId":        11559,
            "templateId":   888,
            "companyId":    1,
            "lang":         "en_US",
            "name":         "example App",
            "activated":    false,
            "expiryDate":   "2016-08-23 12:24:12"
          }
        }

.. http:method:: DELETE request

    The output of a delete request contains the status and a message.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "status":   200,
            "message":  "App '9999' deleted."
        }