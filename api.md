# App-Arena API Documentation #

## API Endpoint ##

All API URLs listed in this documentation are relative to https://mandrillapp.com/api/1.0/. For example, the /users/ping API call is reachable at https://mandrillapp.com/api/1.0/users/ping.json.

## RESTful ##

The App-Arena API is a RESTful API. All requests can be made using one of the following HTTP verbs:

* **GET**       - Read information
* **PUT**      - Update an entity
* **POST**      - Creates a new entity in a collection
* **DELETE**    - Deletes an antity

All methods are accessed via: https://v2.app-arena.com/api/1/SOME-METHOD


## Passing Request Data ##

Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters. The documentation for each API call will contain more detail on the parameters accepted by the call. As an alternative, you can also use HTTP POST parameters, just like submitting an HTML FORM, but JSON objects are recommended.

## Output Formats ##

