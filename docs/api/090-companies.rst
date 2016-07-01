API - Company/Customer requests
===============================

.. Note:: /customers and /companies request are similar (exceptions are highlighted) and are therefore presented combined here

/companies & /customers
-----------------------

GET /companies & GET /customers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a list of your customers

.. Note:: The GET /companies request is reserved to store owners

|   *Available queries*
|       page
|       items
|       fields
|       exclude
|       orderasc/orderdesc

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "next": {
              "href": "http://my.app-arena.com/api/v2/customers?page=2"
            },
            "self": {
              "href": "http://my.app-arena.com/api/v2/customers"
            }
          },
          "_embedded": {
            "data": {
              "1": {
                "companyId": 1,
                "subdomain": "fictional",
                "name": "Fictional Corp.",
                "address1": "Brainstormroad 333",
                "address2": null,
                "zip": "12345",
                "city": "Cloud City",
                "country": "DE",
                "logo": "www.fictional.com/logo.png",
                "color1": "#478AB8",
                "color2": "#2D343D",
                "parentId": 1,
                "storeId": 1,
                "_links": {
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  }
                }
              },
              "2": {
                "companyId": 2,
                            .
                            .
                            .
              },
                .
                .
                .
              "N": {
                            .
                            .
                            .
              }
            }
          },
          "total_items": 100,
          "page_size": 20,
          "page_count": 5,
          "page_number": 1
        }

GET /customers/:companyId & GET /companies/:companyId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about one of your customers specified by :companyId

.. Note:: From a database point of view there is no difference between a company and a customer. That is why there is used :companyId instead of :customerId in customer requests!

|   *Available queries*
|       fields
|       exclude
|       orderasc/orderdesc

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "1": {
                "companyId": 1,
                "subdomain": "fictional",
                "name": "Fictional Corp.",
                "address1": "Brainstormroad 333",
                "address2": null,
                "zip": "12345",
                "city": "Cloud City",
                "country": "DE",
                "logo": "www.fictional.com/logo.png",
                "color1": "#478AB8",
                "color2": "#2D343D",
                "parentId": 1,
                "storeId": 1,
                "_links": {
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  }
                }
              }
            }
          }
        }

POST /companies & POST /customers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Creates a company or customer

    .. Note:: This request creates a new company with your own companyId as parentId which makes it a customer of your company. To create a company/customer for a different owner than yourself use POST /companies/:companyId/customers.

|   *Available queries*
|       none

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"      : "new customer"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "companyId": 2,
            "storeId": 1,
            "subdomain": null,
            "parentId": 1,
            "name": "new customer",
            "address1": null,
            "address2": null,
            "zip": null,
            "city": null,
            "country": "DE",
            "logo": null,
            "color1": "#478AB8",
            "color2": "#2D343D"
          }
        }

    **Required data**

    name
        (string) The name of the company/customer

    **Optional data**

    subdomain
        (string) Sets the individual subdomain of the company
    address1 & address2
        (string) Sets address information of the company
    zip
        (string) Sets the zip code
    city
        (string)
    country
        (string) Sets the country of the company with a two letter code e.g.: Germany -> DE, Autria -> AT etc.
    logo
        (string) Sets the uri of the company logo
    color1 & color2
        (string) Set the company's default colors as Hex values

PUT /companies/:companyId & PUT /customer/:companyId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alters a company entry specified by :companyId

|   *Available queries*
|       none

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":         "new company name",
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "companyId": 1,
            "storeId": 1,
            "subdomain": null,
            "parentId": 1,
            "name": "new company name",
            "address1": null,
            "address2": null,
            "zip": null,
            "city": null,
            "country": "DE",
            "logo": null,
            "color1": "#478AB8",
            "color2": "#2D343D"
          }
        }

    **Changeable fields**

    name
        (string)
    subdomain
        (string)
    address1 & address 2
        (string)
    zip
        (string)
    city
        (string)
    country
        (string)
    logo
        (string)
    color1 & color2
        (string)

DELETE /companies/:companyId & DELETE /customers/:companyId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes an company from the database specified by :companyId

    .. Warning:: This deletes every project, template or app this company owns!

|   *Available queries*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Company '1' deleted."
        }

/companies/:companyId/users & /customers/:companyId/users
---------------------------------------------------------

GET /companies/:companyId/users & GET /customers/:companyId/users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a list of the users of a company specified by :companyId

.. Note:: The GET /companies request is reserved to store owners

|   *Available queries*
|       page
|       items
|       fields
|       exclude
|       orderasc/orderdesc

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_links": {
            "self": {
              "href": "http://my.app-arena.com/api/v2/companies/1/users"
            }
          },
          "_embedded": {
            "data": {
              "1": {
                "userId": 1,
                "username": "john_doe",
                "email": "john@doe.com",
                "gender": "male",
                "firstName": "John",
                "lastName": "Doe",
                "telephone": +555 12345678,
                "displayname": "John Doe",
                "avatar": null,
                "lang": "de_DE",
                "companyId": 1,
                "_links": {
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  }
                }
              },
              "2": {
                "userId": 2,
                        .
                        .
                        .
              },
                .
                .
                .
              "N": {
                        .
                        .
                        .
              }
            }
          },
          "total_items": 10,
          "page_size": 5,
          "page_count": 2,
          "page_number": 1
        }

GET /companies/:companyId/users/:userId & GET /customers/:companyId/users/:userId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive information about a user of a company specified by :companyId and :userId

.. Note:: The GET /companies request is reserved to store owners

|   *Available queries*
|       fields
|       exclude
|       orderasc/orderdesc

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "_embedded": {
            "data": {
              "1": {
                "userId": 1,
                "username": "john_doe",
                "email": "john@doe.com",
                "gender": "male",
                "firstName": "John",
                "lastName": "Doe",
                "telephone": +555 12345678,
                "displayname": "Sebastian Buckpesch",
                "avatar": null,
                "lang": "de_DE",
                "companyId": 1,
                "_links": {
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  }
                }
              }
            }
          }
        }

POST /companies/:companyId/users & POST /customers/:companyId/users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Creates a user

|   *Available queries*
|       none

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "firstname"     : "Jane",
            "lastname"      : "Doe",
            "email"         : "Jane@doe.com",
            "password"      : "quite_secret_pw",
            "username"      : "Jane_Doe",
            "roles"         : "Administrator",
            "gender"        : "female"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "userId": 2,
            "companyId": 1,
            "email": "Jane@doe.com",
            "username": "Jane_Doe",
            "gender": female,
            "firstname": "Jane",
            "lastname": "Doe",
            "displayname": Jane_Doe,
            "telephone": null,
            "avatar": null,
            "lang": "de_DE",
            "roles": "Administrator"
          }
        }

    **Required data**

    firstname
        (string)
    lastname
        (string)
    email
        (string)
    username
        (string)


    **Optional data**

    subdomain
        (string) Sets the individual subdomain of the company
    address1 & address2
        (string) Sets address information of the company
    zip
        (string) Sets the zip code
    city
        (string)
    country
        (string) Sets the country of the company with a two letter code e.g.: Germany -> DE, Autria -> AT etc.
    logo
        (string) Sets the uri of the company logo
    color1 & color2
        (string) Set the company's default colors as Hex values