API - Models calls
==================

.. Tip:: Test all of those requests in our API-Explorer_.

.. _API-Explorer: https://v2.app-arena.com/apigility/swagger/API-v1#!/model

/models
-------

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


/models/:model_id/configs
-------------------------

.. note:: ``data_*`` parameters are different for each config type. The following table will list all parameters
          for all config types.

+---------------+-----------------------------------+---------------------------------------------------------+
| Config-Type   | Attribute                         | Description                                             |
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
