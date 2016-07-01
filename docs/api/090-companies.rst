API - Company/Customer requests
===============================

.. Note:: With the exception of GET /companies, customers and companies request are similar and are therefore presented combined here

/companies & /customers
-----------------------

.. Note:: The GET companies request is reserved to store owners and is not listed here

GET /customers
~~~~~~~~~~~~~~

    Receive a list of your customers

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

.. Note:: From a database point of view there is no difference between a company and a customer. That is why there is used :companyId instead of :customerId!

