API - Channel requests
======================

.. Note:: Channels are the types of publishing an App, but need to be registered for the company first

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