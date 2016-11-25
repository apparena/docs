.. include:: /partials/helpers/html.rst

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

All API URLs listed in this documentation are relative to ``https://my.app-arena.com/api/v2/``.

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

Additionally, the requests can be manipulated by query parameters. The first query must be preceded by a '?' while the following queries
have to be separated by a '&' character.

Example:

http://route.to.api/collection/entity?query1=xxx&query2=yyy&query3=...

.. Note:: You can find the available queries for each call in their respective section.

Available query options:

+------------+--------------------------+-------------------------------------------------------+
| Query      | Valid for                | Description                                           |
+============+==========================+=======================================================+
| lang       | GET,PUT,DELETE           | points the request to the desired language            |
+------------+--------------------------+-------------------------------------------------------+
| fields     | GET                      | receive only desired fields in the response, |br|     |
|            |                          | list fields comma separated |br|                      |
|            |                          | example: fields=appId,expiryDate,name                 |
+------------+--------------------------+-------------------------------------------------------+
| exclude    | GET                      | exclude fields from the response                      |
+------------+--------------------------+-------------------------------------------------------+
| type       | GET                      | receive only media items of type image, audio or      |
|            |                          | video                                                 |
+------------+--------------------------+-------------------------------------------------------+
| orderasc   | GET                      | order the response items ascending |br|               |
|            |                          | example: orderasc=appId                               |
+------------+--------------------------+-------------------------------------------------------+
| orderdesc  | GET                      | order the response items descending                   |
+------------+--------------------------+-------------------------------------------------------+
| page       | GET                      | sets the page of paginated results                    |
+------------+--------------------------+-------------------------------------------------------+
| items      | GET                      | sets the amount of items of paginated results         |
+------------+--------------------------+-------------------------------------------------------+
| version    | GET, POST, PUT, DELETE   |                                                       |
+------------+--------------------------+-------------------------------------------------------+
| filter     | GET                      | filter the results, explanation in the                |
|            |                          | `Filter section`_ below.                              |
+------------+--------------------------+-------------------------------------------------------+
| rel        | GET                      | receive additional related information in a single    |
|            |                          | request, |br| explanation in the `Relation section`_  |
|            |                          | below                                                 |
+------------+--------------------------+-------------------------------------------------------+

.. _Filter section: #the-filter-query-parameter
.. _Relation section: #the-relation-query-parameter

.. Note:: Only collection requests on 'Apps', 'Templates', 'Projects', 'Versions', 'Companies' and 'Customers' have default pagination values. Elsewhere, when a query parameter is not defined, no action is performed.

The Filter Query Parameter
--------------------------

Requests can be refined with a filter query to shape the output exactly to what you want to receive. In combination with the
pagination query parameters, the filter function make a great search tool for the data you want to display.

.. Note:: The filter is applicable for all GET requests of collections and can be combined freely with the other available query parameter options.

The filter distinguishes between the different field types and allows only certain operator types for each type. You can find the types of the fields in the respective section of the calls.
The field types in use are:

    ``bool``
        operators: [eq], [neq]
    ``integer``
        operators: [eq], [neq],[gt], [gte], [lt], [lte]
    ``text`` |br|
    ``string``
        operators: [eq], [neq], [match], [not]
    ``datetime``
        in the format Y-m-D (Year-Month-Day) |br|
        operators: [eq], [neq], [gt], [gte], [lt], [lte]

.. Note:: The filter is generally case insensitive.

A field of an entity can be targeted for filtering with one of the following operators:

    [eq] equals :
        receive a collection of entities where the target field value equals the submitted value
        applicable for all field types, in case of type ``datetime`` the filter returns all entities that match the day regardless of the time of the day
    [neq] equals not :
        receive a collection of entities where the target field value does not equal the submitted value
        applicable for all field types, in case of type ``datetime`` the filter returns all entities that do not match the day regardless of the time of the day
    [match] matches :
        receive a collection of entities where the target field value matches the submitted value partially |br|
        e.g. : the match value 'test' for the target field 'name' returns all entities where the 'name' field contains the string 'test' independent of the location of the occurrence in the string like 'testApp', 'Apptest' or 'appTESTapp' |br|
        applicable only for the field types 'string'
    [not] matches not:
        receive a collection of entities where the target field value does not contain the submitted value
        applicable only for the field types 'string'
    [gt] greater than :
        receive a collection of entities where the target field value is greater than the submitted value
        applicable for field types 'integer' and 'datetime'
    [gte] greater than or equal:
        receive the same as [gt] inclusive the submitted value
        applicable for field types 'integer' and 'datetime'
    [lt] lower than :
        receive a collection of entities where the target field value is lower than the submitted value
        applicable for field types 'integer' and 'datetime'
    [lte] lower than or equal:
        receive the same as [gt] inclusive the submitted value
        applicable for field types 'integer' and 'datetime'

Syntax:
~~~~~~~

.. http:response:: GET /{collection}?filter.{target}[{operator}]={value}


    {collection}
        The {collection} is the route to the target collection, if we wanted to receive apps it would be just 'apps', for the config entities of that app it would be 'apps/:appId/configs'.
    filter.
        The 'filter.' keyword at the beginning of the query parameter is mandatory, indicating the filter intention to the API.
    {target}
        The {target} defines the field which is to be filtered. Find the available fields in the corresponding section of the call.
    {operator}
        In the brackets follows the {operator} which is defining the mode of the filter (see operators list above).
    {value}
        The {value} is mandatory and needs to follow a '=' character. Just put here the plain value without any " or ', no matter integer or string.

Examples:
~~~~~~~~~

1.) If we wanted to get apps which are not yet expired and will not expire today, the request would look like this (on the 25th of november in 2016, the date this was written):

.. http:response:: GET /apps?filter.expiryDate[gt]=2016-11-25


2.) If we wanted to get all the config entities of app '1' where the 'type' field is 'input' the request would be

.. http:response:: GET /apps/1/configs?filter[eq]=input


Combine these request with pagination, order- and field filters to make precise and lightweight requests!

The Relation Query Parameter
----------------------------

As you can see in Chapter `Data Structure <040-structure.html>`_, there are quite a few connections between different entities. Every App is owned by a company,
connected to a Template while having multiple configs, translations, infos, etc... . Sometimes the information stored in these connected resources is needed
because they contain vital information for element description and presentation. To gather these details, multiple API calls are necessary. To avoid excessive
requesting, the relation query parameter got introduced.

With this request enhancement it is possible to gather any connected information in a single request for an entity. When fetching a collection this underlies a restriction.

General Usage
~~~~~~~~~~~~~

The syntax for this enhancement is quite simple: just add the query parameter 'rel' to the request with a comma separated list of desired relations as its value.

.. http:response:: GET /{entity/collection}?rel={relation1},{relation2}, ...

    {entity/collection}
        Request a single entity or a collection of entities. Valid targets are: |br|
        'apps', 'templates', 'projects', 'projects/:projectId/versions', 'companies' and 'customers'
    rel=
        Mandatory keyword to indicate the relation intention to the API.
    {relationX}
        The relation identifier. You can find the valid relations in the corresponding section of the call.

.. Note:: While you can combine this query parameter as usual with the other query modifiers, the field filter influences only the base entities while the relations will always
be outputted completely. They will however never contain sensitive information like passwords when fetching user relations.

Entity Relations
~~~~~~~~~~~~~~~~

There are no restrictions when fetching an entity. Add as much relations to the request as you want, the response format will look somewhat like this:

    .. sourcecode:: js

        {
            "_embedded": {
                "data": {
                    "entityProperty1": "value1",
                    "entityProperty2": "value2",
                        .
                        .
                        .
                    "relation1": {                                                        //relation entity
                        "relationProperty1": "relValue1",
                        "relationProperty2": "relValue2",
                            .
                            .
                            .
                    },
                    "relation2": {                                                        //relation collection
                        "relationIdentifier1": {
                            "relationProperty1": "relValue1",
                            "relationProperty2": "relValue2",
                                .
                                .
                                .
                        },
                        "relationIdentifier2": {
                                .
                                .
                                .
                        },
                    },
                    "relation3": {
                        .
                        .
                        .
                    },
                    .
                    .
                    .
                }
            }
        }

You will find the relation data under its identifier key (already used in the request) in the "_embedded" -> "data" object. Relation entities
data is in the first level of the relation object while relation collections data is in objects with their identifier as keys.

.. Warning:: The relation query parameter directly modifies the query to the database. Therefore you only receive properties directly connected to the base entity,
no inheritance of entities from the App/Template/Version chain as you know it from the regular calls on those collections/entities takes place! Relation calls are not intended
to substitute the regular calls, but rather to complete requests in order to save time and reduce server load.

Collection Relations
~~~~~~~~~~~~~~~~~~~~

When fetching a collection the relation query parameter underlies the restriction that no relation collections may be fetched. A relation collection
can easily consist of tens to hundreds of entities which have to be fetched for tens to hundreds of base entities. The result can cause memory issues as well as
heavy workload on the server, which is to be avoided. For this reason only relation entities are allowed with the exception of some small collections
which are expected to be small enough to avoid these issues. You can find the allowed relations for each call in the corresponding section.

The response format of a collection request with relations looks something like this (exemplified by a request to 'apps'):

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
                "relation1": {                                                        //relation entity
                    "relationProperty1": "relValue1",
                    "relationProperty2": "relValue2",
                        .
                        .
                        .
                },
                "relation2": {                                                        //relation collection
                    "relationIdentifier1": {
                        "relationProperty1": "relValue1",
                        "relationProperty2": "relValue2",
                            .
                            .
                            .
                    },
                    "relationIdentifier2": {
                            .
                            .
                            .
                    },
                },
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

.. Note:: Relation entities/collection do not contain links in the `HAL-format <#response-formats>`_ style

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

The JSON output depends on the type of request and the data submitted. GET Requests will mostly output data in the HAL-format_,
a format which provides links to the mentioned resources for easy resource browsing.
As some of the requests are intended for listing items to the user, these requests will additionally output the data paginated.
It comes in chunks of adjustable size for convenient item displaying. PUT and POST requests however output
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

|   Pagination information is added and can be modified by the following queries:
|   - items : defines the number of objects to be sent per page
|   - page  : defines the current page

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