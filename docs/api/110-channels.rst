API - Channel requests
======================

.. Note:: Channels are types of publishing an App/Template/Project

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




