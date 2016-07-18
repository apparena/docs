API - Authorization
===================

You have two options to authenticate against our API:
1) API Key
2) Json Web Token

Both methods can be used be by sending an "Authorization" header.

API Key usage
-------------

The example request will return a list of all apps of the company, the api key is assigned to.

.. http:method:: POST /api/v2/apps

.. http:response:: Request header

    .. sourcecode:: js

        Host: v2.app-arena.com
        Content-Type: application/json
        Authorization: **YOURAPIKEY**


Json Web Token (JWT)
--------------------

The token will automatically expire after 2 hours. It is meant for the use in browser for example for your Ajax
requests.

The example request will return a list of all apps of the company, the token is assigned to.

.. http:method:: POST /api/v2/apps

.. http:response:: Request header

    .. sourcecode:: js

        Host: v2.app-arena.com
        Content-Type: application/json
        Authorization: Bearer **JWT-TOKEN**


Generate user token
~~~~~~~~~~~~~~~~~~~

A user token can act in behalf of a user through the API. The token has the same access rights as the user account
the user is generated from.

.. http:method:: POST /api/v2/auth/token

.. http:response:: Request header

    .. sourcecode:: js

        Host: v2.app-arena.com
        Content-Type: application/json

.. http:response:: Request body

    .. sourcecode:: js

        {
            "email":"s.buckpesch@iconsultants.eu",
            "password":"1234"
        }

    :data string email: Email address of the user you want to generate a token for
    :data string password: Clear text password of the user you want to generate a token for

Generate api key token
~~~~~~~~~~~~~~~~~~~~~~

An Api key token can be used independent from a user. The key advantage of an API key token is its limited access.
You can define all access rights for api keys in the App-Manager Backend Developer Section.

.. http:method:: POST /api/v2/auth/token

.. http:response:: Request header

    .. sourcecode:: js

        Host: v2.app-arena.com
        Content-Type: application/json

.. http:response:: Request body

    .. sourcecode:: js

        {
            "apikey":"123456"
        }

    :data string apikey: Apikey you want to generate a token for


