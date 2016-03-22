API - App requests
==================

.. Tip:: You can test all requests in our API-Explorer_.

.. _API-Explorer: http://www.app-arena.com

GET /apps
---------

.. _apps:

.. http:method:: GET /api/v2/apps

Receive a collection of the apps of your company, showing basic information.

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


.. http:method:: GET /api/v2/apps/:app_id

Receive detailed information about the requested app. Additionally to the basic properties of the app key "Appinfo"
holds specific app information , key "AppLanguage" contains available languages and their translation status.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_embedded": {
                "data": {
                    "App": {
                        "appId":            1,
                        "name":             "Example App",
                        "lang":             "de_DE",
                        "activated":        true,
                        "expiryDate":       "2099-01-01 00:00:00"
                        "templateId":       22,
                        "companyId":        1
                    },
                    "AppInfo": {
                        "Example info": {
                            "infoId":       "Example info",
                            "lang":         "de_DE",
                            "revision":     0,
                            "value":        "Some information",
                            "meta":         null,
                            "appId":        1
                        }
                    },
                    "AppLanguage": {
                        "en_US": {
                            "name":         "english",
                            "lang":         "en_US",
                            "activated":    true,
                            "translated":   1,
                            "appId":        1
                        }
                    }
                }
            }
        }