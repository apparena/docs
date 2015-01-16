# App-Arena API Documentation #

## API Endpoint ##

All API URLs listed in this documentation are relative to https://v2.app-arena.com/api/1/.

## RESTful ##

The App-Arena API is a RESTful API. All requests can be made using one of the following HTTP verbs:


| HTTP verb | Usage                                         | Resource type      |
|-----------|-----------------------------------------------|--------------------|
| GET       | Request a single entity or a whole collection | entity, collection |
| POST      | Creates a new entity in a collection          | collection         |
| PUT       | Updates an entity                             | entity             |
| DELETE    | Deletes an entity                             | entity             |


All methods are accessed via: https://v2.app-arena.com/api/1/SOME-METHOD


## Passing Request Data ##

Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters. The documentation for each API call will contain more detail on the parameters accepted by the call. As an alternative, you can also use HTTP POST parameters, just like submitting an HTML FORM, but JSON objects are recommended.

## Output Formats ##

