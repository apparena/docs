API - Companies calls
=====================

.. Tip:: Test all of those requests in our API-Explorer_.

.. _API-Explorer: https://v2.app-arena.com/apigility/swagger/API-v1#!/instance

/companies
----------

.. http:method:: POST /api/v1/companies


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"		:"New App-Arena customer. {{$timestamp}}",
            "subdomain"	        :"apparena_customer_{{$timestamp}}",
            "address1"	        :"My street 1",
            "address2"	        :"My street 2",
            "zip"		:"12345",
            "city"		:"My city",
            "country"		:"DE",
            "logo"		:"https://app-manager.s3.amazonaws.com/apps/models/3/0/4/0/de_DE/AppArena_Logo_aufweiss300x80_1413369016_0.png",
            "color1"		:"#478AB8",
            "color2"		:"#2D343D",
            "font"		:"helvetica-neue"
        }

    :data string name: (Required) Name of the company
    :data integer parent_id: (Optional) ID of the company whos customer the newly created company should be like
    :data string subdomain: (Required) Subdomain for all apps the company will create
    :data string address1: (Optional) Address field 1, e.g. Street 1
    :data string address2: (Optional) Address field 2, e.g. Street 2
    :data string zip: (Optional) Zip code
    :data string city: (Optional) City
    :data string country: (Optional) Two letter country code http://en.wikipedia.org/wiki/ISO3166-1alpha-2
    :data string logo: (Optional) Url to the company logo
    :data string color1: (Optional) Primary company color
    :data string color2: (Optional) Secondary company color
    :data string font: (Optional) Company font name

.. http:method:: GET /api/v1/companies


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/companies?page=1"
                },
                "first": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/companies"
                },
                "last": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/companies?page=1"
                }
        },
        "_embedded": {
            "data": [
                {
                    "id": 1,
                    "name": "iConsultants GmbH",
                    "subdomain": "app-arena",
                    "address1": "Kleingedankstr. 12",
                    "zip": "50677",
                    "city": "KÃ¶lle",
                    "country": "DE",
                    "logo": "https:\/\/app-manager.s3.amazonaws.com\/apps\/models\/3\/0\/4\/0\/de_DE\/AppArena_Logo_aufweiss300x80_1413369016_0.png",
                    "color1": "#478AB8",
                    "color2": "#2D343D",
                    "users": { },
                    "_links": {
                        "self": {
                            "href": "https:\/\/v2.app-arena.com\/api\/v1\/companies\/1"
                        }
                    }
                }
            ]
        }

/companies/{company_id}
-----------------------

.. http:method:: PUT /api/v1/companies/{company_id}


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"          :"Updated New Company Name _{{$timestamp}}",
            "subdomain"     :"updated_my_subdomain_{{$timestamp}}",
            "address1"	    :"Updated My street 1",
            "address2"	    :"Updated My street 2",
            "zip"	:"11112345",
            "city"	    :"Updated My city",
            "country"	    :"AT",
            "logo"	    :"https://app-manager.s3.amazonaws.com/apps/models/3/0/4/0/de_DE/AppArena_Logo_aufweiss300x80_1413369016_0.png",
            "color1"	    :"#111111",
            "color2"	    :"#222222",
            "font"	    :"verdana"
        }

    :data string name: (Required) Name of the company
    :data string subdomain: (Optional) Subdomain for all apps the company will create
    :data object address: (Optional) Company billing address
    :data object corporate_identity: (Optional) Corporate Identity configuration for faster app setup (values will be used as default settings, when creating apps)

.. http:method:: DELETE /api/v1/companies/{company_id}

       :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single instance.

/companies/{company_id}/customers
---------------------------------

.. http:method:: GET /api/v1/companies/{company_id}/customers


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/companies\/%7B%7Bcompany_id%7D%7D\/customers"
                }
            },
            "_embedded": {
                "data": [ ]
            },
            "page_count": 0,
            "page_size": 25,
            "total_items": 0
        }


/companies/{company_id}/instances
---------------------------------

.. http:method:: GET /api/v1/companies/{company_id}/instances


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/companies\/%7B%7Bcompany_id%7D%7D\/instances"
                }
            },
            "_embedded": {
                "data": [ ]
            },
            "page_count": 0,
            "page_size": 25,
            "total_items": 0
        }


/companies/{company_id}/templates
---------------------------------

Documentation will follow soon...


/companies/{company_id}/users
-----------------------------

.. http:method:: GET /api/v1/companies/{company_id}/users


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/companies\/%7B%7Bcompany_id%7D%7D\/users"
                }
            },
            "_embedded": {
                "data": [ ]
            },
            "page_count": 0,
            "page_size": 25,
            "total_items": 0
        }
