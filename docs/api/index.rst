Working with the API
====================

API Endpoint
------------

All API URLs listed in this documentation are relative to https://v2.app-arena.com/api/1/.

HTTP Verbs
----------

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

Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters. The documentation for each API call will contain more detail on the parameters accepted by the call.

Response Formats
----------------

We respond using HTTP Status Codes so that you can see immediately if you request was successful or an error occured. A complete list of HTTP response formats you can find here: [HTTP-Statuscodes](http://de.wikipedia.org/wiki/HTTP-Statuscode "Title")

For successful calls the `GET` and `PUT` methods will return HTTP-Status code **200 (OK)**, the `POST` request will return **201
(CREATED)** and the `DELETE` request will return **204 (NO CONTENT)**.