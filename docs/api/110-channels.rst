API - Channel requests
======================

.. Note:: Channels are the types of publishing an App, but need to be registered for the company first



/apps/:appId/channels
---------------------

.. Note:: A Channel needs to be connected to an App in order to publish that App through it

POST /apps/:appId/channels
~~~~~~~~~~~~~~~~~~~~~~~~~~

Connects an App with an existing channel of your company

|   *Query parameters*
|       none

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "channelId": 1
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "app": {
              "appId": 111,
              "templateId": 111,
              "companyId": 1,
              "lang": "de_DE",
              "name": "my App's name",
              "activated": false,
              "expiryDate": "2016-11-08 00:00:00"
            },
            "channel": {
              "channelId": 1,
              "companyId": 1,
              "type": "domain",
              "name": "my domain channel",
              "value": "www.mydomain.com",
              "meta": {}
            }
          }
        }

    **Required data**

    channelId
        ``integer`` the channel you want to connect this app to

DELETE /apps/:appId/channels/:channelId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Removes a channel from an App

|   *Query parameters*
|       none

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "message": "Channel '10' of app '13784' removed"
        }