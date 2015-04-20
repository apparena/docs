API - Getting started
=====================

.. note:: Test all available requests in our API-Explorer_.

.. _API-Explorer: http://v2.app-arena.com/apigility/swagger/API-v1

API key
-------

To request restricted information from the API, you need to add an API key to your request header::

    GET /api/v1/models HTTP/1.1
    Host: v2.app-arena.com
    Authorization: Basic YOURAPIKEY

If you do not have access to the developer section yet, please drop us an email to s.buckpesch at app-arena.com
with your contact data and will we get in touch with you and sent you an API key.

API Endpoint
------------

All API URLs listed in this documentation are relative to ``https://v2.app-arena.com/api/v1/``.

HTTP Verbs
----------

.. _instance_object:

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

We respond using HTTP Status Codes so that you can see immediately if you request was successful or an error occured.
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
| DELETE     |    204 (No content)          |
+------------+------------------------------+
