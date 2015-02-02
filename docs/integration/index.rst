Integration guide
=================

.. note:: Before you can integrate App-Arena to your systems backend, you have to generate an
          `API key <../api/apikey.html>`_.
          Once you got it, you can start requesting our `API <../api/index.html>`_.

To make it easy here are some examples for an integration. All requests are available in a `POSTman <../postman.html>`_.

Scenario 1: Create a new customer
---------------------------------

Each user is part of a company. So before creating a user you need to create
a company or assign the user to an existing company by submitting the **company_id** in your POST request.

Create a new customer (company)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Send a POST request to create a new company. Do not forget to add your `API Key <../api/apikey.html>`_ to the request,
as it is not possible to send POST requests without authentication.

**Header** ::

    POST /api/v1/companies HTTP/1.1
    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: Basic c2J1Y2twZXNjaDphcGlrZXk=

**Parameters** ::

    {
      "name"		:"Big star cooperation",
      "subdomain"	:"big_star_corp"
    }

**Example response** ::

    {
        "id":           17,
        "name":         "New App-Arena customer 1421685371",
        "parent_id":    1,
        "subdomain":    "company_subdomain",
        "timestamp":    1421685366,
        "_links": {
            "self": {
                "href": "http:\/\/v2.app-arena.com\/api\/v1\/companies\/17"
            }
        }
    }

A new *company_id* (in the example response the company_id is 17) has been generated...
You should have it in mind for the following request...

Create a new user for this customer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So now you've got a new company set up. So now it's time to create the first user for this company.
Send a POST request including your [API key](api_key) to create a user.

.. note:: If you are using our `POSTman collection <../postman.html#import-the-collection>`_ you can just send
          the next request to create a user without replacing the ``:company_id`` in the request,
          as the ``POST /companies`` request adds a company_id environment variable in its `POSTman tests`_.

.. _POSTman tests: https://www.getpostman.com/docs/jetpacks_writing_tests


**Header** ::

    POST /api/v1/companies/17/users HTTP/1.1
    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: Basic c2J1Y2twZXNjaDphcGlrZXk=

**Parameters** ::

    {
        "username":  "dhasselhoff",
        "email":     "david@hasselhoff.com",
        "name":      "David Hasselhoff",
        "password":  "iSetGermanyFree!",
        "roles":     [ "user", "admin" ],
        "lang_tag":  "en_US"
    }

**Example response** ::

    TODO


Szenario 2: Create a new instance for a customer
------------------------------------------------

Ok, so an empty account is boring... Give your customer some apps they are impressed of. :-)
Let's create a ``photo contest demo`` (template_id 728)

**Header** ::

    POST /api/v1/instances HTTP/1.1
    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: Basic c2J1Y2twZXNjaDphcGlrZXk=

**Parameters** ::

    {
        "template_id": 728,
        "name":"My customers new photo contest demo",
        "description": "The description of my new instance.",
        "lang_tag":"en_US"
    }

An example response would look like this:

**Example response** ::

You're done :-) - Tell your customer about it!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Great! Now let's send your customer all necessary information, so that he can start using and configuring his app: ::

    Dear David,

    we've setup a new photo-contest demo app for you. You can access your app here:

    App-Url: https://www.fotowettbewerb.co/?i_id=1234

    If you want to change the content of your app just visit the configuration wizard interface and login using your access data:

    Wizard-Url: https://manager.app-arena.com/instances/....
    Username:   dhasselhoff
    Password:   iSetGermanyFree!

    Thanks a lot,
    Your App-Support Team
