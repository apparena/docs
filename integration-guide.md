# App-Arena Integration Guide #

Before you can integrate App-Arena to your systems backend, you have to generate an API key. Once you got it, you can start requesting our [API](api).

To make it easy here are some examples for an integration. All requests are available in a [POSTman collection](postman).

## Szenario 1: Create a new customer
Each user is part of a company. So before creating a user you need to create a company or assign the user to an existing company by submitting the **company_id** in your POST request.

### Create a new company
Send a POST request to create a new company. Do not forget to add your [API key](api_key) to the request, as it is not possible to send POST requests without authentication.
    
    POST /api/v1/companies HTTP/1.1
    Host: v2.app-arena.com
    Content-Type: application/json
    Authorization: Basic c2J1Y2twZXNjaDphcGlrZXk=

    {
      "name"		:"New company name",
      "subdomain"	:"company_subdomain"
    }

### Create a new user


### Create a new instance using the companies initial API key

