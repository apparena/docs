# App-Arena Integration Guide #

Before you can integrate App-Arena to your systems backend, you have to generate an API key. Once you got it, you can start requesting our [API](api).

To make it easy here are some default examples for an integration:

## Szenario 1: Create a new customer
Each user is part of a company. So before creating a user you need to create a company or assign the user to an existing company by submitting the **company_id** in your POST request.

### Create a new company
Send a POST request to create a new company
    
    POST /companies
    

### Create a new user


### Create a new instance using the companies initial API key

