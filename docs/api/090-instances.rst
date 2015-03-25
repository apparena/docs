API - Instances calls
=====================

.. Tip:: Test all of those requests in our API-Explorer_.

.. _API-Explorer: https://v2.app-arena.com/apigility/swagger/API-v1#!/instance

/instances
----------

.. http:method:: GET /api/v1/instances

.. http:response:: Retrieve a list of instances.

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https://v2-stage.app-arena.com/api/v1/instances?page=1"
                },
                "first": {
                    "href": "https://v2-stage.app-arena.com/api/v1/instances"
                },
                "last": {
                    "href": "https://v2-stage.app-arena.com/api/v1/instances?page=371"
                },
                "next": {
                    "href": "https://v2-stage.app-arena.com/api/v1/instances?page=2"
                }
            },
            "_embedded": {
                "data": [
                    {  ... },
                    {
                        "active": 1,
                        "base_url": "https://dev.iconsultants.eu/git/Photopuzzle-App/",
                        "description": "",
                        "id": 68,
                        "lang_tag": "en_US",
                        "m_id": 42,
                        "name": "Test Photopuzzle",
                        "template_id": 0,
                        "_links": {
                            "self": {
                                "href": "https://v2-stage.app-arena.com/api/v1/instances/68"
                            }
                        }
                    },
                    {  ... },
                ]
            },
            "page_count": 371,
            "page_size": 25,
            "total_items": 9270
        }

/instances/{i_id}
-----------------

Documentation will follow soon...


/instances/{i_id}/configs
-------------------------

Documentation will follow soon...


/instances/{i_id}/configs/{config_id}
-------------------------------------

Documentation will follow soon...


/instances/{i_id}/languages
---------------------------

Documentation will follow soon...


/instances/{i_id}/languages/{lang_tag}
--------------------------------------

Documentation will follow soon...


/instances/{i_id}/languages/{lang_tag}/translations
---------------------------------------------------

Documentation will follow soon...


/instances/{i_id}/templates
---------------------------

Documentation will follow soon...