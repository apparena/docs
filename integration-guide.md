# App-Arena Integration Guide #

Before you can integrate App-Arena to your systems backend, you have to generate an API key. Once you got it, you can start requesting our [API](api).

To make it easy here are some examples for an integration. All requests are available in a [POSTman collection](postman).

## Szenario 1: Create a new customer
Each user is part of a company. So before creating a user you need to create a company or assign the user to an existing company by submitting the **company_id** in your POST request.

### Create a new customer (company)
Send a POST request to create a new company. Do not forget to add your [API key](api_key) to the request, as it is not possible to send POST requests without authentication.
    
    POST /api/v1/companies HTTP/1.1
    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: Basic c2J1Y2twZXNjaDphcGlrZXk=

    {
      "name"		:"New company name",
      "subdomain"	:"company_subdomain"
    }

An example response would look like this:

    {
        "id": 17,
        "name": "New App-Arena customer 1421685371",
        "parent_id": 1,
        "subdomain": "company_subdomain",
        "timestamp": 1421685366,
        "_links": {
            "self": {
                "href": "http:\/\/v2.app-arena.com\/api\/v1\/companies\/17"
            }
        }
    }

A new *company_id* (in the example response the company_id is 17) has been generated... You should have it in mind for the following request...

### Create a new user for this customer

So now you got a new company set up. So now it's time to create the first user for this company. Send a POST request including your [API key](api_key) to create a user. 

**Note:** If you are using our [POSTman collection](postman) you can just send the next request to create a user without replacing the `:company_id` in the request, as the `POST /companies` request adds a company_id environment variable in its <a href="https://www.getpostman.com/docs/jetpacks_writing_tests" target="_blank">POSTman test</a>.
    
    POST /api/v1/companies/17/ HTTP/1.1
    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: Basic c2J1Y2twZXNjaDphcGlrZXk=

    {
      "name"		:"New company name",
      "subdomain"	:"company_subdomain",
      "role"        : ["user", "admin"]
    }

An example response would look like this:

    TODO

### Create a new instance for this customer

Ok, so an empty account is boring... Give your customer some apps they are impressed of. :-) To create

