API - Models calls
==================

.. Tip:: Test all of those requests in our API-Explorer_.

.. _API-Explorer: https://v2.app-arena.com/apigility/swagger/API-v1#!/model

/models
-------

.. http:method:: POST /api/v1/models

.. http:response:: Create a new model

    .. sourcecode:: js

        {
            "name":           "My shiny new app",
            "description":    "Using this app you will superpower your skills.",
            "base_url":       "https://www.url-to-your-app.com/appsubfolder/"
        }

    :data string name: (Required) Name of the model.
        :data string description: (Optional) Description of the model.
        :data string base_url: (Optional) Public Url path to your app


.. http:response:: Newly created model object

    .. sourcecode:: js

        {
            "app_domain": "",
            "base_url": "https:\/\/www.url-to-your-app.com\/appsubfolder\/",
            "created_at": "2015-03-24",
            "description": "Using this app you will superpower your skills.",
            "fb_app_id": "",
            "fb_app_namespace": "",
            "fb_app_secret": "",
            "fb_canvas_url": "",
            "id": 312,
            "lang_tag": "de_DE",
            "name": "My shiny new app",
            "secret": "fd0691803888c9171abfde4ec8d00747",
            "validity": "",
            "timestamp": 1427207187,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/312"
                }
            }
        }

.. http:method:: GET /api/v1/models

.. http:response:: Retrieve a list of models.

    .. sourcecode:: js

        {
           "_links":{ ... },
           "_embedded":{
              "data":[
                 {  ... },
                 {
                    "base_url":"https:\/\/dev.iconsultants.eu\/git\/Photopuzzle-App\/",
                    "description":"A Picture Puzzle Application in which the user have to find the right picture part in the full image.",
                    "id":42,
                    "lang_tag":"de_DE",
                    "name":"*BETA* Picture puzzle",
                    "_links":{
                       "self":{
                          "href":"https:\/\/v2.app-arena.com\/api\/v1\/models\/42"
                       }
                    }
                 },
                 {  ... },
              ]
           },
           "page_count":8,
           "page_size":25,
           "total_items":176
        }


/models/:model_id
-----------------

.. http:method:: GET /api/v1/models/{model_id}

   :arg model_id: ID of the model.

.. http:response:: Retrieve basic information of a single model.

   .. sourcecode:: js

        {
           "app_domain":"your-domain.com",
           "base_url":"https:\/\/www.your-domain.com\/myappsubfolder\/",
           "created_at":"2015-03-05",
           "description":"Get new super-powers using this cool web-app.",
           "fb_app_id":"1234567890123456",
           "fb_app_secret":"1234567890123456789012345612345678901234567890",
           "id":310,
           "lang_tag":"de_DE",
           "name":"My Super-Power App",
           "secret":"12345678901234567890123456",
           "validity":"90",
           "_links":{
              "self":{
                 "href":"https:\/\/v2.app-arena.com\/api\/v1\/models\/310"
              }
           }
        }


   :data string app_domain: Date of Build.
   :data string base_url: Error from Sphinx build process.
   :data string created_at: Build id.
   :data string description: Description for the model
   :data string fb_app_id: Facebook app id
   :data string fb_app_secret: Facebook App, used to install apps to the clients fanpages
   :data string id: ID of the model
   :data string lang_tag: Default language of for new instances
   :data string name: Name of the model
   :data string secret: Model secret, which is needed to generate a signature (e.g. Client-Browser HTTP requests to the API)
   :data int validity: How many days a new instance of this model will be available until it expires



.. http:method:: PUT /api/v1/models/{model_id}

    :arg model_id: ID of the model.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "name":"UPDATED New app model {{$timestamp}}",
            "description":"UPDATED This is my test description",
            "base_url":"https://UPDATED.url-to-my-app.com/myappsubfolder/",
            "lang_tag": "en_US"
        }


    :data string name: (Required) Name of the model
    :data string description: (Optional) Description of the model
    :data string base_url: (Optional) Url to the app
    :data enum lang_tag: (Optional) Default language for the model ("sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ",
                        "ar_JO", "ar_KW","ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SD", "ar_SY",
                        "ar_TN", "ar_AE", "ar_YE","be_BY", "bg_BG", "ca_ES", "zh_CN", "zh_HK", "zh_SG", "hr_HR",
                        "cs_CZ", "da_DK", "nl_BE", "nl_NL", "en_AU", "en_CA","en_IN", "en_IE", "en_MT", "en_NZ",
                        "en_PH", "en_SG", "en_ZA", "en_GB", "en_US", "et_EE", "fi_FI", "fr_BE","fr_CA", "fr_FR",
                        "fr_LU", "fr_CH", "de_AT", "de_DE", "de_LU", "de_CH", "el_CY", "el_GR", "iw_IL", "hi_IN",
                        "hu_HU","is_IS", "in_ID", "ga_IE", "it_IT", "it_CH", "ja_JP", "ja_JP", "ko_KR", "lv_LV",
                        "lt_LT", "mk_MK", "ms_MY", "mt_MT","no_NO", "no_NO", "pl_PL", "pt_BR", "pt_PT", "ro_RO",
                        "ru_RU", "sr_BA", "sr_ME", "sr_CS", "sr_RS", "sk_SK", "sl_SI","es_AR", "es_BO", "es_CL",
                        "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA",
                        "es_PY", "es_PE", "es_PR", "es_ES", "es_US", "es_UY", "es_VE", "sv_SE", "th_TH", "th_TH",
                        "tr_TR", "uk_UA", "vi_VN"



.. http:method:: DELETE /api/v1/models/{model_id}

Documentation will follow soon...


/models/:model_id/configs
-------------------------

.. note:: ``data_*`` parameters are different for each config type. The following table will list all parameters
          for all config types.

+---------------+-----------------------------------+---------------------------------------------------------+
| Config-Type   | Parameter                         | Description                                             |
+===============+===================================+=========================================================+
| checkbox      | - ``string`` data_caption_off     | - Caption for the 'Off'-value                           |
|               | - ``string`` data_caption_on      | - Caption for the 'On'-value                            |
|               | - ``string`` data_label           | - Label for the checkbox                                |
+---------------+-----------------------------------+---------------------------------------------------------+
| color         |                                   |                                                         |
+---------------+-----------------------------------+---------------------------------------------------------+
| css           | - ``enum`` data_compiler          | - [css | less] Compiler to process the value with       |
+---------------+-----------------------------------+---------------------------------------------------------+
| date          |                                   |                                                         |
+---------------+-----------------------------------+---------------------------------------------------------+
| image         | - ``string`` data_alt             | - HTML image alt attribute                              |
|               | - ``string`` data_title           | - HTML image title attribute                            |
|               | - ``int`` data_height             | - Forced image height (when set, image will be cropped) |
|               | - ``int`` data_min_height         | - Minimal allowed height value for this image           |
|               | - ``int`` data_max_height         | - Max. allowed height value for this image              |
|               | - ``int`` data_width              | - Forced image width (when set, image will be cropped)  |
|               | - ``int`` data_min_width          | - Minimal allowed width value for this image            |
|               | - ``int`` data_max_width          | - Max. allowed width value for this image               |
|               | - ``array`` data_format           | - [jpg | png | gif ] Array of accepted image formats    |
|               | - ``bool`` data_nullable          | - Image value can be NULL or not                        |
+---------------+-----------------------------------+---------------------------------------------------------+
| text          | - ``string`` data_type            | - HTML5 input data type                                 |
|               | - ``string`` data_placeholder     | - HTML5 placeholder attribute                           |
|               | - ``string`` data_pattern         | - RegExp for input validation. Defines an input mask    |
|               | - ``int`` data_min                | - Minimum value (validation for data_type "number")     |
|               | - ``int`` data_max                | - Maximum value (validation for data_type "number")     |
|               | - ``int`` data_min_length         | - Min. number of characters                             |
|               | - ``int`` data_max_length         | - Max. number of characters                             |
+---------------+-----------------------------------+---------------------------------------------------------+
| textarea      | - ``enum`` data_editor            | - [wysiwyg, code, none] Rendered frontend editor        |
|               | - ``bool`` data_code_view         | - Code view allowed in the frontend                     |
+---------------+-----------------------------------+---------------------------------------------------------+
| select        |                                   |                                                         |
+---------------+-----------------------------------+---------------------------------------------------------+
| multiselect   |                                   |                                                         |
+---------------+-----------------------------------+---------------------------------------------------------+


.. http:method:: GET /api/v1/models/{model_id}/configs

   :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

   .. sourcecode:: js

        {
           "app_domain":"your-domain.com",
           "base_url":"https:\/\/www.your-domain.com\/myappsubfolder\/",
           "created_at":"2015-03-05",
           "description":"Get new super-powers using this cool web-app.",
           "fb_app_id":"1234567890123456",
           "fb_app_secret":"1234567890123456789012345612345678901234567890",
           "id":310,
           "lang_tag":"de_DE",
           "name":"My Super-Power App",
           "secret":"12345678901234567890123456",
           "validity":"90",
           "_links":{
              "self":{
                 "href":"https:\/\/v2.app-arena.com\/api\/v1\/models\/310"
              }
           }
        }


   :data string app_domain: Date of Build.
   :data string base_url: Error from Sphinx build process.
   :data string created_at: Build id.
   :data string description: Description for the model
   :data string fb_app_id: Facebook app id
   :data string fb_app_secret: Facebook App, used to install apps to the clients fanpages
   :data string id: ID of the model
   :data string lang_tag: Default language of for new instances
   :data string name: Name of the model
   :data string secret: Model secret, which is needed to generate a signature (e.g. Client-Browser HTTP requests to the API)
   :data int validity: How many days a new instance of this model will be available until it expires



/models/{model_id}/configs/{config_id}
--------------------------------------

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(checkbox)


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

    :data string name: (Optional) Name of the config value
    :data bool value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data string data_caption_off: (Optional) Caption for the 'Off'-value
    :data string data_caption_on: (Optional) Caption for the 'On'-value
    :data string data_label: (Optional) Label for the checkbox

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(color)


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":               "Updated Name of color",
            "value":              #FFFFFF,
            "description":        "Updated description of my color",
        }

    :data string name: (Optional) Name of the config value
    :data bool value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(css)


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":"Updated Name of my CSS config",
            "value":"body { text-align:center; color:red; } h1.h1, h2, h3 { font-size: 30px; }",
            "description":"Updated The description of my config value.",
            "data_compiler":"css"
        }

    :data string name: (Optional) Name of the config value
    :data bool value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data object meta_data: (Optional) Meta data for the config field

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(data) DEPRECATED


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":               "Updated Name of my date",
            "value":              1911-02-22,
            "description":        "Updated Enter a valid date",
        }

    :data string name: (Optional) Name of the config value
    :data bool value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(image)


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":"Updated Name of my image config value",
            "value":null,
            "description":"Updated The description of my config value.",
            "data_alt": "Updated Service Flatrate promotion image",
            "data_title": "Updated Save 25% in may on our service flatrate",
            "data_max_height":2000,
            "data_max_width":2000,
            "data_min_height":200,
            "data_min_width":200,
            "data_height":600,
            "data_width":1000,
            "data_format":["jpg"],
            "data_nullable":true
        }

    :data string name: (Optional) Name of the config value
    :data string value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data object meta_data: (Optional) Meta data for the config field

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(text)


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

    :data string name: (Optional) Name of the config value
    :data string value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data object meta_data: (Optional) Meta data for the config field

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(textarea)


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":"Updated Name of my config value",
            "value":"<h1>Updated This is my default HTML content</h1>",
            "description":"Updated The description of my config value.",
            "data_editor":"code"
        }

    :data string name: (Optional) Name of the config value
    :data string value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data object meta_data: (Optional) Meta data for the config field

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(select)


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":"Updated Name of my config value",
            "description":"The description of my config value.",
            "source":[
                {
                    "value": "updated_value_id_1",
                    "text": "Updated Text for value 1"
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
            "value":"updated_value_id_1"
        }

    :data string name: (Optional) Name of the config value
    :data string value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data array source: (Optional) All available options of the select config value

.. http:method:: PUT /api/v1/models/{model_id}/configs/{config_id}(select)


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
            "value":[ "updated_value_id_3", "updated_value_id_1" ]
        }

    :data string name: (Optional) Name of the config value
    :data array value: (Optional) All values which should be selected by default
    :data string description: (Optional) Description for the config value
    :data array source: (Optional) All available options of the select config value



/models/{model_id}/languages
----------------------------

.. http:method:: POST /api/v1/models/{model_id}/languages


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "lang_tag":"fr_FR"
        }

    :data enum lang_tag: (Required) Language tag of the language to add to the model
    :data is_activated: (Optional) If the new language is activated immediately



/models/{model_id}/languages/{lang_tag}
---------------------------------------

.. http:method:: PUT /api/v1/models/{model_id}/languages/{lang_tag}


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "is_activated":1
        }

    :data boolean is_activated: (Required) If the new language is activated immediately

/models/{model_id}/languages/{lang_tag}/translations
----------------------------------------------------

.. http:method:: POST /api/v1/models/{model_id}/languages/{lang_tag}/translations


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "translation_id":"test_translation",
            "value":"Il mio test translations!"
        }

    :data string translation_id: (Required) Translation ID
    :data string value: (Required) Translation


/models/{model_id}/templates
----------------------------

Documentation will follow soon...