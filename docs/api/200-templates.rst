API - Templates calls
=====================

.. Tip:: Test all of those requests in our API-Explorer_.

.. _API-Explorer: https://v2.app-arena.com/apigility/swagger/API-v1#!/instance

/templates
----------

.. http:method:: POST /api/v1/templates


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name"		:"My new template",
            "description"	:"Description of my new template",
            "parent_id"	:287,
            "parent_type"	:"model"
        }

:data string name: (Required) name of the instance
:data string description: (Optional) Description of the instance
:data integer parent_id: (Required) ID the entity to copy from
:data enum parent_type: (Optional) The entity the template should generated of


/templates/{template_id}
------------------------

.. http:method:: PUT /api/v1/templates/{template_id}


.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":"UPDATED My new template name {{$timestamp}}"
        }

:data string name: (Required) name of the instance


/templates/{template_id}/configs
--------------------------------

Documentation will follow soon...


/templates/{template_id}/configs/{config_id}
--------------------------------------------

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(checkbox)


.. http:response:: Example request body

    .. sourcecode:: js

            {
                "name":"Updated Name of Checkbox",
                "value":false,
                "description":"Updated description of my checkbox",
                "meta_data":{
                    "text":{
                        "off":"Updated Custom Off",
                        "on":"Updated Custom On",
                        "label":"Updated Optional label"
                    }
                 }
            }


:data string name: (Optional) name of the config value
:data bool value: (Optional) Value for the config element
:data string description: (Optional) Description for the config value
:data object meta_data: (Optional) Meta data for the config field

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(color)


.. http:response:: Example request body

    .. sourcecode:: js

            {
                "name":"Updated Name of Color",
                "value":"#FFFFFF",
                "description":"Updated The description of my color"
            }


:data string name: (Optional) name of the config value
:data string value: (Optional) Value for the config element
:data string description: (Optional) Description for the config value

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(css)


.. http:response:: Example request body

    .. sourcecode:: js

            {
                "name":"Updated Name of my CSS config",
                "value":"/* Updated */ body { text-align:center; } h1.h1, h2, h3 { font-size: 30px; }",
                "description":"Updated The description of my config value.",
                "meta_data":{
                    "compiler":"css"
                }
            }


:data string name: (Optional) name of the config value
:data string value: (Optional) Value for the config element
:data string description: (Optional) Description for the config value
:data object meta_data: (Optional) Meta data for the config field

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(date) DEPRECATED


.. http:response:: Example request body

    .. sourcecode:: js

            {
                "name":"Updated Name of my date",
                "value":"1911-02-22",
                "description":"Updated Enter a valid date"
            }


:data string name: (Optional) name of the config value
:data string value: (Optional) Value for the config element
:data string description: (Optional) Description for the config value

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(image)


.. http:response:: Example request body

    .. sourcecode:: js

            {
                "name":"Updated Name of my image config value",
                "value":null,
                "description":"Updated The description of my config value.",
                "meta_data":{
                    "alt": "Updated Service Flatrate promotion image",
                    "title": "Updated Save 25% in may on our service flatrate",
                    "size":{
                        "max_height":2000,
                        "max_width":2000,
                        "min_height":200,
                        "min_width":200,
                        "height":600,
                        "width":1000
                    },
                    "format":["jpg"],
                    "nullable":true
                }
            }


:data string name: (Optional) name of the config value
:data string value: (Optional) Value for the config element
:data string description: (Optional) Description for the config value
:data object meta_data: (Optional) Meta data for the config field


/templates/{template_id}/languages
----------------------------------

Documentation will follow soon...


/templates/{template_id}/languages/{lang_tag}
---------------------------------------------

Documentation will follow soon...


/templates/{template_id}/languages/{lang_tag}/translations
----------------------------------------------------------

Documentation will follow soon...


/templates/{template_id}/templates
----------------------------------

Documentation will follow soon...