API - Company/Customer requests
===============================

.. Note:: /customers and /companies request are similar (exceptions are highlighted) and are therefore presented combined here

/companies & /customers
-----------------------

GET /companies & GET /customers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a list of your customers

.. Note:: The GET /companies request is reserved to store owners

|   *Query parameters*
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

|   *Query parameters*
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

|   *Query parameters*
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

|   *Query parameters*
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

    **modifiable parameters**

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

|   *Query parameters*
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

|   *Query parameters*
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

|   *Query parameters*
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
                "displayname": "John_Doe",
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

|   *Query parameters*
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

    gender
        (string) Sets the gender of the user. Valid strings: "male" or "female"
    telephone
        (string)
    avatar
        (string) Sets the uri to an avatar picture
    lang
        (string) The default language of the version, if left blank, the default language of the project is used instead
        Syntax: de_DE for Germany, de_AT for Austrian german, en_US for american english ...
    roles
        (string) Sets the roles of the user. Every role consists of a set of rights. A user can have as much roles as desired.

        Syntax: "roles" : "Support" for a single role,

        "roles" : ["Support","Translator", ...] for multiple roles. See  `config <../api/060-config.html>`_  for available roles.

PUT /companies/:companyId/users/:userId & PUT /customer/:companyId/users/:userId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alters a user entry specified by :companyId and :userId

|   *Query parameters*
|       force

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "username"      : "new user name"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "data": {
            "userId": 2,
            "companyId": 1,
            "email": "Jane@doe.com",
            "username": "new user name",
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

    **modifiable parameters**

    email
        (string)
    username
        (string)
    gender
        (string)
    firstname
        (string)
    lastname
        (string)
    displayname
        (string)
    telephone
        (string)
    avatar
        (string)
    lang
        (string)
    roles
        (string)

DELETE /companies/:companyId/users/:userId & DELETE /customers/:companyId/users/:userId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes an user from the database specified by :companyId

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "User '1' deleted."
        }

/companies/:companyId/customers
-------------------------------

    .. Note:: The output of the following requests is similar to `GET /customers <../api/090-companies.html#companies-customers>`_. It is used to receive information about a customer of your customer companies.

GET /companies/:companyId/customers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. Note:: You can find the output format of this request `here <../api/090-companies.html#get-companies-get-customers>`_

GET /companies/:companyId/customers/:companyId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. Note:: You can find the output format of this request `here <../api/090-companies.html#get-customers-companyid-get-companies-companyid>`_

POST /companies/:companyId/customers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. Note:: You can find the output format of this request `here <../api/090-companies.html#post-companies-post-customers>`_

PUT /companies/:companyId/customers/:companyId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. Note:: You can find the output format of this request `here <../api/090-companies.html#put-companies-companyid-put-customer-companyid>`_

DELETE /companies/:companyId/customers/:companyId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. Note:: You can find the output format of this request `here <../api/090-companies.html#delete-companies-companyid-delete-customers-companyid>`_

/companies/:companyId/projects
------------------------------

    .. Note:: This request is similar to the `GET /projects <../api/080-projects.html#get-projects>`_ with the difference that it shows only projects owned by the specified company.

GET /companies/:companyId/projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of projects owned by a company specified by :companyId.

|   *Query parameters*
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
              "href": "http://my.app-arena.com/api/v2/projects?page=2"
            },
            "self": {
              "href": "http://my.app-arena.com/api/v2/projects"
            }
          },
          "_embedded": {
            "data": {
              "1": {
                "projectId": 1,
                "name": "Project_1",
                "description": "This is a project description",
                "companyId": 1,
                "_links": {
                  "project": {
                    "href": "http://my.app-arena.com/api/v2/projects/1"
                  },
                  "company": {
                    "href": "http://my.app-arena.com/api/v2/companies/1"
                  }
                }
              },
              "2": {
                "projectId": 2,
                        .
                        .
                        .
              },
                .
                .
                .
              "N":{
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

/companies/:companyId/templates
-------------------------------

    .. Note:: This request is similar to the `GET /templates <../api/080-projects.html#get-projects>`_ with the difference that it shows only templates owned by the specified company.

GET /companies/:companyId/templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of templates owned by your company.

|   *Query parameters*
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
              "href": "https://my.app-arena.com/api/v2/templates?page=2"
            },
            "self": {
              "href": "https://my.app-arena.com/api/v2/templates"
            }
          },
          "_embedded": {
            "data": {
              "1": {
                "templateId": 1,
                "name": "template_1",
                "lang": "de_DE",
                "parentId": 1,
                "versionId": 1,
                "companyId": 1,
                "public": true,
                "_links": {
                  "template": {
                    "href": "https://my.app-arena.com/api/v2/templates/1"
                  },
                  "language": {
                    "href": "https://my.app-arena.com/api/v2/templates/1/languages"
                  },
                  "parent": {
                    "href": "https://my.app-arena.com/api/v2/templates/1"
                  },
                  "version": {
                    "href": "https://my.app-arena.com/api/v2/projects/1/versions/1"
                  },
                  "company": {
                    "href": "https://my.app-arena.com/api/v2/companies/1"
                  }
                }
              },
              "2": {
                "templateId": 2,
                    .
                    .
                    .
              },
              .
              .
              .
              "N":{
                    .
                    .
                    .
              }
            }
          },
          "total_items": 1000,
          "page_size": 20,
          "page_count": 50,
          "page_number": 1
        }

/companies/:companyId/apps
--------------------------

    .. Note:: This request is similar to the `GET /apps <../api/060-apps.html#get-apps>`_ with the difference that it shows only apps owned by the specified company.

GET /companies/:companyId/apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive a collection of apps owned by a company specified by :companyId.

|   *Query parameters*
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
              "href": "https://my.app-arena.com/api/v2/apps?page=2"
            },
            "self": {
              "href": "https://my.app-arena.com/api/v2/apps"
            }
          },
          "_embedded": {
            "data": {
              "1": {
                "appId": 1,
                "name": "Example app",
                "lang": "en_US",
                "activated": true,
                "expiryDate": "2016-11-30 00:00:00",
                "companyId": 1,
                "templateId": 888,
                "_links": {
                  "app": {
                    "href": "https://my.app-arena.com/api/v2/apps/1"
                  },
                  "appLanguage": {
                    "href": "https://my.app-arena.com/api/v2/apps/1/languages/en_US"
                  },
                  "company": {
                    "href": "https://my.app-arena.com/api/v2/companies/1"
                  },
                  "template": {
                    "href": "https://my.app-arena.com/api/v2/templates/888"
                  }
                }
              },
              "2": {
                "appId": 2,
                "name": "Example app 2",
                        .
                        .
                        .
              },
              "3": {
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
          "total_items": 1000,
          "page_size": 20,
          "page_count": 50,
          "page_number": 1
        }

/companies/:companyId/channels
------------------------------

The company channels consist of the following fields:

    **channel fields**

    channelId
            .. include:: /partials/uniqueId.rst
type
            .. include:: /partials/channeltype.rst
value
            .. include:: /partials/value.rst
companyId
            .. include:: /partials/companyId.rst
meta
            .. include:: /partials/meta.rst
name
            .. include:: /partials/name.rst

GET /companies/:companyId/channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Receive an array of channels of the requested company

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        [
          {
            "channelId": 1,
            "type": "domain",
            "name": "my channel",
            "value": "www.mydomain.com",
            "companyId": 1,
            "created": "2016-11-03 11:39:33",
            "updated": "2016-11-03 11:39:33",
            "createdFromIp": "127.0.0.1",
            "updatedFromIp": "127.0.0.1",
            "createdBy": "apikey_1",
            "updatedBy": "apikey_1",
            "meta": {}
          }
        ]

POST /companies/:companyId/channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Creates a new Channel for the specified company

|   *Query parameters*
|       none

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "type": "domain",
            "value": "www.mydomain.com",
            "name": "my channel"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "channelId": 1,
          "companyId": 1,
          "type": "domain",
          "name": "my channel",
          "value": "www.mydomain.com"
        }

    **Required data**

    name
        .. include:: /partials/name.rst
    type
        .. include:: /partials/channeltype.rst
    value
        ``string`` stores channel information like a key, domain name, etc.

    **Optional data**

    meta
        .. include:: /partials/meta.rst

PUT /companies/:companyId/channels/:channelId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Alters the channel information of a specified company

|   *Query parameters*
|       none

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name": "new channel name"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "channelId": 1,
          "companyId": 1,
          "type": "domain",
          "name": "new channel name",
          "value": "www.mydomain.com",
          "meta": {}
        }

    **modifiable parameters**

    type
        ``string`` has to be one of "facebook", "domain" or "website"
    name
        ``string`` the channel name
    value
        ``string`` stores channel information like a key, domain name, etc.
    meta
        ``string`` stores meta data in JSON format

DELETE /companies/:companyId/channels/:channelId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deletes a channel specified by companyId and channelId

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 200,
          "message": "Channel '1' deleted."
        }