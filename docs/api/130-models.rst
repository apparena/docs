API - Models calls
==================

.. Tip:: Test all of those requests in our API-Explorer_.

.. _API-Explorer: https://v2.app-arena.com/apigility/swagger/API-v1#!/model

/models
-------

.. _models:

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

`Documentation of the models. <../api/130-models.html#models>`_

/models/:model_id
-----------------

.. http:method:: GET /api/v1/models/:model_id

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



.. http:method:: PUT /api/v1/models/:model_id

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


.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "app_domain": "",
            "base_url": "https:\/\/UPDATED.url-to-my-app.com\/myappsubfolder\/",
            "created_at": "2015-04-27",
            "description": "UPDATED This is my test description",
            "fb_app_id": "",
            "fb_app_namespace": "",
            "fb_app_secret": "",
            "fb_canvas_url": "",
            "id": 317,
            "lang_tag": "en_US",
            "name": "New app model 1430141524",
            "secret": "da8a0ad63edbaced92b1d99f46c4cacf",
            "validity": "",
            "timestamp": 1430141572,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317"
                }
            }
        }




.. http:method:: DELETE /api/v1/models/:model_id

`Successful DELETE requests will return HTTP-Status code 204. <../api/001-index.html#codes>`_


/models/:model_id/configs
-------------------------

.. _table:

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

.. http:method:: POST /api/v1/models/:model_id/configs(checkbox)

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":  "config_checkbox_{{$timestamp}}",
            "type":       "checkbox",
            "name":       "Name of Checkbox",
            "value":      true,
            "description":"The description of my checkbox",
            "data_caption_off":"Custom Off",
            "data_caption_on":"Custom On",
            "data_label":"Optional label"
        }


    :data string config_id: (Required) Identifier for the new config value
    :data enum type: (Required) Type of the config element
    :data string name: (Required) Name for the config value
    :data bool value: (Required) Default value for the config element
    :data string description: (Optional) Description for the config value

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "The description of my checkbox",
            "id": "config_checkbox_1430141851",
            "lang_tag": "en_US",
            "meta_data": [ ],
            "name": "Name of Checkbox",
            "type": "checkbox",
            "value": 1,
            "timestamp": 1430141892,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_checkbox_1430141851"
                }
            }
        }


.. http:method:: POST /api/v1/models/:model_id/configs(color)

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":      "config_color_{{$timestamp}}",
            "type":           "color",
            "name":           "Name of Color",
            "value":          "#335566",
            "description":    "The description of my color"
        }


    :data string config_id: (Required) Identifier for the new config value
    :data enum type: (Required) Type of the config element
    :data string name: (Required) Name for the config value
    :data string value: (Required) Default value for the config element
    :data string description: (Optional) Description for the config value


.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "The description of my color",
            "id": "config_color_1430141894",
            "lang_tag": "en_US",
            "meta_data": [ ],
            "name": "Name of Color",
            "type": "color",
            "value": "#335566",
            "timestamp": 1430141935,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_color_1430141894"
                }
            }
        }


.. http:method:: POST /api/v1/models/:model_id/configs(css)

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":      "config_css_{{$timestamp}}",
            "type":           "css",
            "name":           "Name of my CSS config",
            "value":          "body { text-align:center; } h1.h1, h2, h3 { font-size: 30px; }",
            "description":    "The description of my config value.",
            "data_compiler":  "less"
        }


    :data string config_id: (Required) Identifier for the new config value
    :data enum type: (Required) Type of the config element
    :data string name: (Required) Name for the config value
    :data string value: (Required) Default value for the config element
    :data string description: (Optional) Description for the config value

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_


.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_css_1430142010",
            "lang_tag": "en_US",
            "meta_data": [ ],
            "name": "Name of my CSS config",
            "type": "css",
            "value": "body { text-align:center; } h1.h1, h2, h3 { font-size: 30px; }",
            "timestamp": 1430142051,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_css_1430142010"
                }
            }
        }


.. http:method:: POST /api/v1/models/:model_id/configs(date) DEPRECATED

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":      "config_date_{{$timestamp}}",
            "name":           "Updated Name of my date",
            "type":           "date",
            "value":          "2011-11-11",
            "description":    "Updated Enter a valid date"
        }


    :data string name: (Required) Name for the config value
    :data string value: (Required) Default value for the config element
    :data string description: (Optional) Description for the config value

.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "Updated Enter a valid date",
            "id": "config_date_1430142048",
            "lang_tag": "en_US",
            "meta_data": [ ],
            "name": "Updated Name of my date",
            "type": "date",
            "value": "2011-11-11",
            "timestamp": 1430142089,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_date_1430142048"
                }
            }
        }


.. http:method:: POST /api/v1/models/:model_id/configs(image)

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":          "config_image_{{$timestamp}}",
            "type":               "image",
            "name":               "Name of my image config value",
            "value":              "https://www.app-arena.com/media/wysiwyg/serviceflatrate.png",
            "description":        "The description of my config value.",
            "data_alt":           "Service Flatrate promotion image",
            "data_title":         "Save 25% in may on our service flatrate",
            "data_max_height":    1000,
            "data_max_width":     1000,
            "data_min_height":    100,
            "data_min_width":     100,
            "data_height":        300,
            "data_width":         500,
            "data_format":        ["jpg","png","gif"],
            "data_nullable":      false
        }


    :data string config_id: (Required) Identifier for the new config value
    :data enum type: (Required) Type of the config element
    :data string name: (Required) Name for the config value
    :data string value: (Required) Default value for the config element
    :data string description: (Optional) Description for the config value

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_image_1430142090",
            "lang_tag": "en_US",
            "meta_data": {
                "tag": '<img src="https:\/\/www.app-arena.com\/media\/wysiwyg\/serviceflatrate.png' \/>"
            },
            "name": "Name of my image config value",
            "type": "image",
            "value": "https:\/\/www.app-arena.com\/media\/wysiwyg\/serviceflatrate.png",
            "timestamp": 1430142131,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_image_1430142090"
                }
            }
        }


.. http:method:: POST /api/v1/models/:model_id/configs(text)

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":          "config_text_{{$timestamp}}",
            "type":               "text",
            "name":               "Name of my config value",
            "value":              "my_username",
            "description":        "Enter a valid Username (max. 12 lowercase characters or numbers, no whitespaces).",
            "data_type":          "text",
            "data_placeholder":   "Enter username here",
            "data_pattern":       "[a-z0-9]{12}"
        }


    :data string config_id: (Required) Identifier for the new config value
    :data enum type: (Required) Type of the config element
    :data string name: (Required) Name for the config value
    :data string value: (Required) Default value for the config element
    :data string description: (Optional) Description for the config value

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "Enter a valid Username (max. 12 lowercase characters or numbers, no whitespaces).",
            "id": "config_text_1430142145",
            "lang_tag": "en_US",
            "meta_data": [ ],
            "name": "Name of my config value",
            "type": "text",
            "value": "my_username",
            "timestamp": 1430142186,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_text_1430142145"
                }
            }
        }


.. http:method:: POST /api/v1/models/:model_id/configs(textarea)

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":"config_textarea_{{$timestamp}}",
            "type":"textarea",
            "name":"Name of my config value",
            "value":"<h1>This is my default HTML content</h1>",
            "description":"The description of my config value.",
            "data_editor":"wysiwyg",
            "data_code_view":false
        }


    :data string config_id: (Required) Identifier for the new config value
    :data enum type: (Required) Type of the config element
    :data string name: (Required) Name for the config value
    :data string value: (Required) Default value for the config element
    :data string description: (Optional) Description for the config value
    :data enum editor: (Optional) "wysiwyg", "code", "none" | Which editor should be shown to the user?
    :data bool code_view: (Optional) Is the code-view button available in the wysiwyg-editor?

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_textarea_1430142205",
            "lang_tag": "en_US",
            "meta_data": [ ],
            "name": "Name of my config value",
            "type": "textarea",
            "value": "<h1>This is my default HTML content<\/h1>",
            "timestamp": 1430142246,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_textarea_1430142205"
                }
            }
        }


.. http:method:: POST /api/v1/models/:model_id/configs(select)

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":"config_select_{{$timestamp}}",
            "type":"select",
            "name":"Name of my config value",
            "description":"The description of my config value.",
            "source":[
                {
                    "value": "value_id_1",
                    "text": "Text for value 1"
                },
                {
                    "value": "value_id_2",
                    "text": "Text for value 2"
                },
                {
                    "value": "value_id_3",
                    "text": "Text for value 3"
                }
            ],
            "value":"value_id_2"
        }


    :data string config_id: (Required) Identifier for the new config value
    :data enum type: (Required) Type of the config element
    :data string name: (Required) Name for the config value
    :data string value: (Required) Default value for the config element
    :data string description: (Optional) Description for the config value
    :data array source: (Required) All available options of the config element

.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_select_1430142251",
            "lang_tag": "en_US",
            "meta_data": [ ],
            "name": "Name of my config value",
            "source": [
                {
                    "value": "value_id_1",
                    "text": "Text for value 1"
                },
                {
                    "value": "value_id_2",
                    "text": "Text for value 2"
                },
                {
                    "value": "value_id_3",
                    "text": "Text for value 3"
                }
            ],
            "type": "select",
            "value": "value_id_2",
            "timestamp": 1430142293,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_select_1430142251"
                }
            }
        }


.. http:method:: POST /api/v1/models/:model_id/configs(multiselect)

    :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

    .. sourcecode:: js

        {
            "config_id":"config_multiselect_{{$timestamp}}",
            "type":"multiselect",
            "name":"Name of my config value",
            "description":"The description of my config value.",
            "source":[
                {
                    "value": "value_id_1",
                    "text": "Text for value 1"
                },
                {
                    "value": "value_id_2",
                    "text": "Text for value 2"
                },
                {
                    "value": "value_id_3",
                    "text": "Text for value 3"
                }
            ],
            "value":[ "value_id_2", "value_id_3" ]
        }


    :data string config_id: (Required) Identifier for the new config value
    :data enum type: (Required) Type of the config element
    :data string name: (Required) Name for the config value
    :data array value: (Optional) Default value for the config element
    :data string description: (Optional) Description for the config value
    :data array source: (Required) All available options of the config element

.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_multiselect_1430142358",
            "lang_tag": "en_US",
            "meta_data": [ ],
            "name": "Name of my config value",
            "source": [
                {
                    "value": "value_id_1",
                    "text": "Text for value 1"
                },
                {
                    "value": "value_id_2",
                    "text": "Text for value 2"
                },
                {
                    "value": "value_id_3",
                    "text": "Text for value 3"
                }
            ],
            "type": "multiselect",
            "value": [
                "value_id_2",
                "value_id_3"
            ],
            "timestamp": 1430142399,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/317\/configs\/config_multiselect_1430142358"
                }
            }
        }

.. _model:

.. http:method:: GET /api/v1/models/:model_id/configs

   :arg model_id: ID of the model.

.. http:response:: Retrieves a paginated list of config values of a model

   .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/318\/configs"
                }
            },
            "_embedded": {
                "data": [
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
                ]
            },
            "page_count": 0,
            "page_size": 25,
            "total_items": 0
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



/models/:model_id/configs/:config_id
------------------------------------

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(checkbox)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "The description of my checkbox",
            "id": "config_checkbox_1429099711",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Name of Checkbox",
            "type": "checkbox",
            "value": 1,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_checkbox_1429099711"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(color)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "The description of my color",
            "id": "config_color_1429099923",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Name of color",
            "type": "color",
            "value": 1,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_color_1429099923"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(css)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_css_1429099927",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Name of my CSS config",
            "type": "css",
            "value": "body { text-align:center; } h1.h1, h2, h3 { font-size: 30px; }",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_css_1429099927"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(date)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Updated Enter a valid date",
            "id": "config_date_1429099929",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Updated Name of my date",
            "type": "date",
            "value": "2011-11-11",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_date_1429099929"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(image)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_image_1429099933",
            "lang_tag": "de_DE",
            "meta_data": {
                "tag": "<img src='https:\/\/www.app-arena.com\/media\/wysiwyg\/serviceflatrate.png' \/>"
            },
            "name": "Name of my image config value",
            "type": "image",
            "value": "https:\/\/www.app-arena.com\/media\/wysiwyg\/serviceflatrate.png",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_image_1429099933"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(text)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Enter a valid Username (max. 12 lowercase characters or numbers, no whitespaces).",
            "id": "config_text_1429099936",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Name of my config value",
            "type": "text",
            "value": "my_username",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_text_1429099936"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(textarea)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_textarea_1429099939",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Name of my config value",
            "type": "textarea",
            "value": "<h1>This is my default HTML content<\/h1>",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_textarea_1429099939"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(select)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_select_1429099941",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Name of my config value",
            "source": [
                {
                    "value": "value_id_1",
                    "text": "Text for value 1"
                },
                {
                    "value": "value_id_2",
                    "text": "Text for value 2"
                },
                {
                    "value": "value_id_3",
                    "text": "Text for value 3"
                }
            ],
            "type": "select",
            "value": "value_id_2",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_select_1429099941"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: GET /api/v1/models/:model_id/configs/:config_id(multiselect)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "The description of my config value.",
            "id": "config_multiselect_1429099943",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Name of my config value",
            "source": [
                {
                    "value": "value_id_1",
                    "text": "Text for value 1"
                },
                {
                    "value": "value_id_2",
                    "text": "Text for value 2"
                },
                {
                    "value": "value_id_3",
                    "text": "Text for value 3"
                }
            ],
            "type": "multiselect",
            "value": [
                "value_id_2",
                "value_id_3"
            ],
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/configs\/config_multiselect_1429099943"
                }
            }
        }

`Documentation of the configs. <../api/130-models.html#model>`_

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(checkbox)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


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


.. http:response:: Example response body

    .. sourcecode:: js

        {
            "description": "The description of my checkbox",
            "id": "config_checkbox_1430221458",
            "lang_tag": "de_DE",
            "meta_data": [ ],
            "name": "Name of Checkbox",
            "type": "checkbox",
            "value": 1,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/319\/configs\/config_checkbox_1430221458"
                }
            }
        }

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(color)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":               "Updated Name of color",
            "value":              "#FFFFFF",
            "description":        "Updated description of my color"
        }

    :data string name: (Optional) Name of the config value
    :data bool value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(css)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


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

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(data) DEPRECATED

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


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

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(image)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


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

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(text)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


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

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(textarea)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


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

`Table with data_ parameters and the description of them. <../api/130-models.html#data>`_

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(select)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


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

.. http:method:: PUT /api/v1/models/:model_id/configs/:config_id(multiselect)

    :arg model_id: ID of the model.
    :arg config_id: ID of the config.


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

.. http:method:: DELETE /api/v1/models/:model_id/configs/:config_id

`Successful DELETE requests will return HTTP-Status code 204. <../api/001-index.html#codes>`_



/models/:model_id/languages
---------------------------

.. _mlanguage:

.. http:method:: POST /api/v1/models/:model_id/languages

    :arg model_id: ID of the model.


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "lang_tag":"fr_FR"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
            "is_activated": 0,
            "lang_tag": "fr_FR",
            "timestamp": 1430211490,
            "id": "fr_FR",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/318\/languages\/fr_FR"
                }
            }
        }

    :data enum lang_tag: (Required) Language tag of the language to add to the model
    :data is_activated: (Optional) If the new language is activated immediately

.. http:method:: GET /api/v1/models/:model_id/languages

    :arg model_id: ID of the model.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/languages?page=1"
                },
                "first": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/languages"
                },
                "last": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/languages?page=1"
                }
            },
            "_embedded": {
                "data": [
                    {
                        "lang_id": 528,
                        "name": "de",
                        "is_activated": 1,
                        "lang_tag": "de_DE"
                    }
                ]
            },
            "page_count": 1,
            "page_size": 25,
            "total_items": 1
        }

`Documentation of the languages of models. <../api/130-models.html#mlanguages>`_

/models/:model_id/languages/:lang_tag
-------------------------------------

.. http:method:: PUT /api/v1/models/:model_id/languages/:lang_tag

    :arg model_id: ID of the model.
    :arg lang_tag: ID of the language.


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "is_activated":1
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
            "is_activated": 1,
            "lang_tag": "fr_FR",
            "timestamp": 1430211734,
            "id": "fr_FR",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/318\/languages\/fr_FR"
                }
            }
        }

    :data boolean is_activated: (Required) If the new language is activated immediately

.. http:method:: DELETE /api/v1/models/:model_id/languages/:lang_tag

`Successful DELETE requests will return HTTP-Status code 204. <../api/001-index.html#codes>`_

/models/:model_id/languages/:lang_tag/translations
--------------------------------------------------

.. http:method:: POST /api/v1/models/:model_id/languages/:lang_tag/translations

    :arg model_id: ID of the model.
    :arg lang_tag: ID of the language.


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "translation_id":"test_translation",
            "value":"Il mio test translations!"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
            "id": "test_translation",
            "translation": "Il mio test translations!",
            "timestamp": 1430211997,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/318\/languages\/fr_FR\/translations\/test_translation"
                }
            }
        }


    :data string translation_id: (Required) Translation ID
    :data string value: (Required) Translation

.. http:method:: GET /api/v1/models/:model_id/languages/:lang_tag/translations

    :arg model_id: ID of the model.
    :arg lang_tag: ID of the language.

.. http:response:: Example request body.

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/316\/languages\/%7B%7Blang_tag%7D%7D\/translations"
                }
            },
            "_embedded": {
                "data": [ ]
            },
            "page_count": 0,
            "page_size": 25,
            "total_items": 0
        }

.. http:response:: Example response body.

    .. sourcecode:: js

        {
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/318\/languages\/fr_FR\/translations?page=1"
                },
                "first": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/318\/languages\/fr_FR\/translations"
                },
                "last": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/318\/languages\/fr_FR\/translations?page=1"
                }
            },
            "_embedded": {
                "data": [
                    {
                        "id": "test_translation",
                        "value": "Il mio test translations!",
                        "_links": {
                            "self": {
                                "href": "https:\/\/v2.app-arena.com\/api\/v1\/models\/318\/languages\/fr_FR\/translations\/test_translation"
                            }
                        }
                    }
                ]
            },
            "page_count": 1,
            "page_size": 25,
            "total_items": 1
        }


`Documentation of the languages of models. <../api/130-models.html#mlanguages>`_

/models/:model_id/languages/:lang_tag/translations/:translation_id
------------------------------------------------------------------


.. http:method:: PUT /models/:model_id/languages/:lang_tag/translations/:translation_id

       :arg i_id: ID of the translation.
       :arg lang_tag: ID of the language.
       :arg translation_id: ID of the translation.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "value":"UPDATED Il mio test translation!"
        }

    :data string value: (Required) Translation


.. http:method:: DELETE /models/:model_id/languages/:lang_tag

`Successful DELETE requests will return HTTP-Status code 204. <../api/001-index.html#codes>`_
