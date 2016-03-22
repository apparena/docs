API - App requests
==================

.. Tip:: You can test all requests in our API-Explorer_.

.. _API-Explorer: http://www.app-arena.com

GET /apps
---------

.. _apps:

.. http:method:: GET /api/v2/apps

Receive a collection of the apps of your company showing basic information.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_embedded": {
                "data": {
                    "1": {
                        "appId":            1,
                        "companyId":        1,
                        "name":             "Example App",
                        "lang":             "en_US",
                        "activated":        true,
                        "expiryDate":       "2015-08-16 00:00:00",
                        "deletedAt":        null,
                        "createdFromIp":    "0.0.0.0",
                        "updatedFromIp":    "0.0.0.0",
                        "createdBy":        "j.doe",
                        "updatedBy":        "j.doe",
                        "created":          "2016-01-17 11:20:56",
                        "updated":          "2016-02-17 11:20:56"
                    }
                }
            }
        }

