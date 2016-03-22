API - Authorization
===================

You have two options to authenticate against our API:
1) API Key
2) Json Web Token

Both methods can be used be sending an "Authorization" header.

API Key authentication
----------------------
::

    POST /api/v2/apps HTTP/1.1
    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: **YOURAPIKEY**


The example request will return a list of all apps of the company, the api key is assigned to.

Json Web Token (JWT)
--------------------

The token will automatically expire after 2 hours. It is meant for the use in browser for example for your Ajax
requests. To obtain a token send one of the following requests.

Generate user token
~~~~~~~~~~~~~~~~~~~

A user token can act in behalf of a user through the API. The token has the same access rights as the user account
the user is generated from.

.. http:method:: POST /api/v2/auth/token

Header::

    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: **YOURAPIKEY**


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "email":"s.buckpesch@iconsultants.eu",
            "password":"1234"
        }

Generate api key token
~~~~~~~~~~~~~~~~~~~~~~

An Api key token can be used independent from a user. The key advantage of an API key token is its limited access.
You can define all access rights for api keys in the App-Manager Backend Developer Section. ::

    POST /api/v2/auth/token HTTP/1.1
    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: YOURAPIKEY


    {
        "apikey":"123456"
    }

