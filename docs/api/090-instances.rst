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

    For parameter documentation see :ref:`instance_object`

.. http:method:: POST /api/v1/instances

.. http:response:: Create a new instance

    .. sourcecode:: js

        {
            "description": "Description of my Magento Instance",
            "name":"Instance from Magento SKU {{$timestamp}}",
            "template_id": "10-10-10101-1",
            "template_type": "magento"
        }

    :data int company_id:  (Optional) Company_id of the company the instance should be created for
    :data string description: (Optional) Description of the instance.
    :data enum lang_tag:  (Optional) ["sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY",
        "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SD", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "be_BY", "bg_BG", "ca_ES",
        "zh_CN", "zh_HK", "zh_SG", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_CA", "en_IN", "en_IE",
        "en_MT", "en_NZ", "en_PH", "en_SG", "en_ZA", "en_GB", "en_US", "et_EE", "fi_FI", "fr_BE", "fr_CA", "fr_FR",
        "fr_LU", "fr_CH", "de_AT", "de_DE", "de_LU", "de_CH", "el_CY", "el_GR", "iw_IL", "hi_IN", "hu_HU", "is_IS",
        "in_ID", "ga_IE", "it_IT", "it_CH", "ja_JP", "ja_JP", "ko_KR", "lv_LV", "lt_LT", "mk_MK", "ms_MY", "mt_MT",
        "no_NO", "no_NO", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sr_BA", "sr_ME", "sr_CS", "sr_RS", "sk_SK",
        "sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX",
        "es_NI", "es_PA", "es_PY", "es_PE", "es_PR", "es_ES", "es_US", "es_UY", "es_VE", "sv_SE", "th_TH", "th_TH",
        "tr_TR", "uk_UA", "vi_VN"] Default language for the instance
    :data string name: (Required) Name of the instance.
    :data int template_id: (Required) Template ID the instance should be created of
    :data enum template_type:  (Optional) [ "instance" | "template" ] The entity the instance should be generated of



.. http:response:: Newly created instance object

    .. sourcecode:: js

        {
            "active": 1,
            "base_url": "https:\/\/adventskranz.onlineapp.co\/",
            "description": "The description of my new instance.",
            "id": 9627,
            "lang_tag": "en_US",
            "m_id": 299,
            "name": "New Instance 1427295997",
            "template_id": 780,
            "timestamp": 1427296018,
            "_links": {
                "self": {
                    "href": "https:\/\/v2-stage.app-arena.com\/api\/v1\/instances\/9627"
                }
            }
        }

    For parameter documentation see :ref:`instance_object`


.. _instance_object:

/instances/{i_id}
-----------------

.. http:method:: GET /api/v1/instances/{i_id}

   :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single instance.

    .. sourcecode:: js

        {
            "active": 1,
            "base_url": "https:\/\/adventskranz.onlineapp.co\/",
            "description": "The description of my new instance.",
            "id": 9627,
            "lang_tag": "en_US",
            "m_id": 299,
            "name": "New Instance 1427295997",
            "template_id": 780,
            "timestamp": 1427296778,
            "_links": {
                "self": {
                    "href": "https:\/\/v2-stage.app-arena.com\/api\/v1\/instances\/9627"
                }
            }
        }



    :data bool active: TODO
    :data string base_url: TODO
    :data string description: Description for the instance
    :data int id: ID of the instance
    :data string lang_tag: language of for new instances
    :data int m_id: TODO
    :data string name: Name of the instance
    :data int template_id: TODO
    :data int timestamp: TODO


.. http:method:: PUT /api/v1/instances/{i_id}

       :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single instance.

    .. sourcecode:: js

        {
            "active": 1,
            "base_url": "https:\/\/adventskranz.onlineapp.co\/",
            "description": "The description of my new instance.",
            "id": 9627,
            "lang_tag": "en_US",
            "m_id": 299,
            "name": "This is my new instance name. It's changed!",
            "template_id": 780,
            "timestamp": 1427297181,
            "_links": {
                "self": {
                    "href": "https:\/\/v2-stage.app-arena.com\/api\/v1\/instances\/9627"
                }
            }
        }

    For parameter documentation see :ref:`instance_object`

.. http:method:: DELETE /api/v1/instances/{i_id}

       :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single instance.




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