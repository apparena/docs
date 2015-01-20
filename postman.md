# Working with POSTman

Postman is an easy to use Google Chrome extension, which enables you to send HTTP-Request to a server. As we are running all our API tests using [POSTman](https://getpostman.com), we prepared a collection of requests for you, so that you have **examples of all available requests** of the App-Manager API.

## 1. Import the environment

1. Download one of our environment files
    - [POSTman Production environment](https://app-manager.s3.amazonaws.com/api/tutorials/App-Manager-Production.postman_environment)
    - [POSTman Stage environment](https://app-manager.s3.amazonaws.com/api/tutorials/App-Manager-Stage.postman_environment)

1. Import the environment-file
![Manage environments](https://app-manager.s3.amazonaws.com/api/tutorials/POSTman-add-environment-1.png)
![Import environment file](https://app-manager.s3.amazonaws.com/api/tutorials/POSTman-add-environment-2.png)

## 2. Import the collection

Click the import button on the top right cornor and import one of our collection urls

- Complete API Request list: https://www.getpostman.com/collections/1c02a557a932d3f7aa64

![Import collection](https://app-manager.s3.amazonaws.com/api/tutorials/POSTman-import-collection-1.png)

## 3. Send your first request

So select the currently imported environment in the top-navigation, select one of the imported requests and hit the SEND-Button.

![Send a HTTP Request using Postman](https://app-manager.s3.amazonaws.com/api/tutorials/POSTman-send-request-1.png)

## 4. Add your API key

As you might noticed, you do not have permissions to send all of the requests in the collection. To submit even restricted requests you need to add an [API key](api_key).