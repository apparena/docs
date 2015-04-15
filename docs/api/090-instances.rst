API - Instances calls
=====================

.. Tip:: Test all of those requests in our API-Explorer_.

.. _API-Explorer: https://v2.app-arena.com/apigility/swagger/API-v1#!/instance

/instances
----------

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


    :data bool active: Is this instance active or not (can it be used by the client)
    :data string base_url: Public URI to access the instance
    :data string description: Description for the instance
    :data string expiration_date: Until which date the instance can be used. Format: YYYY-MM-DD
    :data string fb_app_id: Facebook App ID used for this instance,
    :data string fb_app_namespace: Facebook App namespace used for this instance
    :data string fb_page_id: Facebook Fanpage ID the instance is installed on
    :data string fb_page_name: Facebook Fanpage Name the instance is installed on
    :data string fb_page_url: Facebook Fanpage Url the instance is installed on
    :data int id: ID of the instance
    :data string lang_tag: language of for new instances
    :data int m_id: ID of the app model of the instance
    :data string name: Name of the instance
    :data int template_id: ID of the template of this instance
    :data int timestamp: Creation/Update time on the server


.. http:method:: PUT /api/v1/instances/{i_id}

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name": "This is my new instance name. It's changed!",
            "expiration_date": "2015-12-24"
        }

For parameter documentation see :ref:`instance_object`


.. http:response:: Example response body

    .. sourcecode:: js

        {
            "active": 1,
            "base_url": "https:\/\/adventskranz.onlineapp.co\/",
            "description": "The description of my new instance.",
            "expiration_date": "2015-12-24",
            "fb_app_id": "725444547534506",
            "fb_app_namespace": "advents-kranz",
            "fb_page_id": "",
            "fb_page_name": "",
            "fb_page_url": "https:\/\/www.facebook.com\/",
            "id": 9759,
            "lang_tag": "en_US",
            "m_id": 299,
            "name": "This is my new instance name. It's changed!",
            "template_id": 780,
            "timestamp": 1427960768,
            "_links": {
            "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9759"
                }
            }
        }

    For parameter documentation see :ref:`instance_object`

.. http:method:: DELETE /api/v1/instances/{i_id}

       :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single instance.


/instances/{i_id}/configs
-------------------------

.. http:method:: GET /api/v1/instances/{i_id}/configs


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/configs?page=1"
                },
                "first": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/configs"
                },
                "last": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/configs?page=11"
                },
                "next": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/configs?page=2"
                }
            },
            "_embedded": {
                "data": [
                    {
                        "description": "Show debug information for this instance?",
                        "id": "admin_debug_mode",
                        "lang_tag": "de_DE",
                        "name": "[Show debug information]",
                        "template_id": 0,
                        "type": "checkbox",
                        "value": 0,
                        "_links": {
                            "self": {
                                "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/configs\/admin_debug_mode"
                            }
                        }
                    },
                }
            }
        }


/instances/{i_id}/configs/{config_id}
-------------------------------------

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":               "Updated Name of Checkbox",
            "value":              false,
            "description":        "Updated description of my checkbox",
            "data_caption_off":   "Updated Custom Off",
            "data_caption_on":    "Updated Custom On",
            "data_label":         "Updated Optional label"
        }

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(color)

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":       "Updated Name of Color",
            "value":      "#EEEEEE",
            "description":"Updated The description of my color"
        }

    :data string name: (Optional)
    :data string value: (Optional)
    :data string description: (Optional) Description for the instance

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(css)

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":           "Updated Name of my CSS config",
            "value":          "body { text-align:center; text-color:red; } h1.h1, h2, h3 { font-size: 30px; }",
            "description":    "Updated The description of my config value.",
            "data_compiler":  "css"
        }

    :data string name: (Optional)
    :data string value: (Optional)
    :data string description: (Optional) Description for the instance
    :data object data_compiler: (Optional)

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(date) DEPRECATED

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":       "Updated Name of my date",
            "value":      "1911-02-22",
            "description":"Updated Enter a valid date"
        }

    :data string name: (Optional)
    :data string value: (Optional)
    :data string description: (Optional) Description for the instance

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(image)

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":           "Updated Name of my image config value",
            "value":          "https://app-manager.s3.amazonaws.com/apps/models/3/0/4/0/de_DE/AppArena_Logo_aufblau_1426686667_0.png",
            "description":    "Updated The description of my config value.",
            "data_alt":       "Updated Service Flatrate promotion image",
            "data_title":     "Updated Save 25% in may on our service flatrate",
            "data_max_height":2000,
            "data_max_width": 2000,
            "data_min_height":200,
            "data_min_width" :200,
            "data_height":    600,
            "data_width":     1000,
            "data_format":    ["jpg"],
            "data_nullable":  true
        }

    :data string name: (Optional)
    :data string value: (Optional)
    :data string description: (Optional) Description for the instance
    :data object meta_data: (Optional)

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(multiselect)

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":"Updated Name of my config value",
            "description":"Updated The description of my config value.",
            "source":[
                {
                    "value": "updated_value_id_1",
                    "text": "Updated Text for value 1"
                },
                {
                    "value": "value_id_2",
                    "text": "Updated Text for value 2"
                },
                {
                    "value": "updated_value_id_3",
                    "text": "Updated Text for value 3"
                }
            ],
            "value":[ "page" ]
        }

    :data string name: (Optional)
    :data array value: (Optional)
    :data string description: (Optional) Description for the instance
    :data array source: (Optional)

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(select)

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":"Updated Name of my config value",
            "description":"The description of my config value.",
            "source":[
                {
                    "value": "ubuntu",
                    "text": "New Ubuntu text"
                },
                {
                    "value": "updated_value_id_2",
                    "text": "Updated Text for value 2"
                },
                {
                    "value": "value_id_3",
                    "text": "Updated Text for value 3"
                }
            ],
            "value":"ubuntu"
        }

    :data string name: (Optional)
    :data string value: (Optional)
    :data string description: (Optional) Description for the instance
    :data array source: (Optional)

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(text)

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":"Updated Name of my config value",
            "value":"updated@email.com",
            "description":"Updated Enter a valid Email (max. 22 lowercase characters or numbers, no whitespaces, @).",
            "data_type":"email",
            "data_placeholder":"Updated Enter email here",
            "data_pattern":"[a-zA-Z0-9@]{22}"
        }

    :data string name: (Optional)
    :data string value: (Optional)
    :data string description: (Optional) Description for the instance
    :data object meta_data: (Optional)

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(textarea)

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":       "Updated Name of my config value",
            "value":      "<h1>Updated This is my default HTML content</h1>",
            "description":"Updated The description of my config value.",
            "data_editor":"code"
        }

    :data string name: (Optional)
    :data string value: (Optional)
    :data string description: (Optional) Description for the instance
    :data object meta_data: (Optional)


/instances/{i_id}/languages
---------------------------

.. http:method:: GET /api/v1/instances/{i_id}/languages


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/languages?page=1"
                },
                "first": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/languages"
                },
                "last": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/languages?page=1"
                }
            },
            "_embedded": {
                "data": [
                    {
                        "lang_id": 409,
                        "name": "German (Germany)",
                        "is_activated": 1,
                        "lang_tag": "de_DE"
                    },
                    {
                        "lang_id": 410,
                        "name": "English (United States)",
                        "is_activated": 0,
                        "lang_tag": "en_US"
                    },
                    {
                        "lang_id": 413,
                        "name": "French (France)",
                        "is_activated": 0,
                        "lang_tag": "fr_FR"
                    },
                    {
                        "lang_id": 488,
                        "name": "German (Austria)",
                        "is_activated": 0,
                        "lang_tag": "de_AT"
                    },
                    {
                        "lang_id": 490,
                        "name": "Italian (Italy)",
                        "is_activated": 0,
                        "lang_tag": "it_IT"
                    },
                    {
                        "lang_id": 524,
                        "name": "Spanish (Spain)",
                        "is_activated": 0,
                        "lang_tag": "es_ES"
                    }
                ]
            },
            "page_count": 1,
            "page_size": 25,
            "total_items": 6
        }
/instances/{i_id}/languages/{lang_tag}
--------------------------------------

.. http:method:: PUT /api/v1/instances/{i_id}/configs/{config_id}(textarea)

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "is_activated":0
        }




/instances/{i_id}/languages/{lang_tag}/translations
---------------------------------------------------

.. http:method:: GET /api/v1/instances/{i_id}/languages/{lang_tag}/translations

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/languages\/en_US\/translations?page=1"
                },
                "first": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/languages\/en_US\/translations"
                },
                "last": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/languages\/en_US\/translations?page=19"
                },
                "next": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9847\/languages\/en_US\/translations?page=2"
                }
            },
            "_embedded": {
            "data": [
                {  ... },
                {
                    "translation_id": "vote",
                    "value": "Abstimmen"
                },
                {
                    "translation_id": "please_enter_custom_field",
                    "value": "Bitte geben Sie einen Wert für %s an."
                },
                {
                    "translation_id": "select_video",
                    "value": "Video auswählen"
                },
                {  ... },
            }
        }


