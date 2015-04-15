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
    :data string text_off: (Optional) Caption for the 'Off'-value
    :data string text_on: (Optional) Caption for the 'On'-value
    :data string text_label: (Optional) Caption for the label of the on/off switch

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
    :data enum compiler: (Optional) Which compiler should be used to generate CSS

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
    :data string data_alt: (Optional) Alternative tag for the image (used for blind people surfing the web)
    :data string data_title: (Optional) Title of the image (normally appears, when the user hovers with the mouse cursor over the image)
    :data object data_size: (Optional) JSON object containing optional image size restriction for the image
    :data integer data_max_height: (Optional) Maximal height of the image, that will be accepted
    :data integer data_max_width: (Optional) Maximal width of the image, that will be accepted
    :data integer data_min_height: (Optional) Minimum height of the image, that will be accepted
    :data integer data_min_width: (Optional) Minimum height of the image, that will be accepted
    :data integer data_height: (Optional) Exact height of the image, that will be accepted
    :data integer data_width: (Optional) Exact width of the image, that will be accepted
    :data array data_format: (Optional) Title of the image (normally appears, when the user hovers with the mouse cursor over the image)
    :data bool data_nullable: (Optional) Can the image url be empty

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(text)


.. http:response:: Example request body

    .. sourcecode:: js

            {
                "name":"Updated Name of my config value",
                "value":"updated@email.com",
                "description":"Updated Enter a valid Email (max. 22 lowercase characters or numbers, no whitespaces, @).",
                "meta_data":{
                    "type":"email",
                    "placeholder":"Updated Enter email here",
                    "pattern":"[a-zA-Z0-9@]{22}"
                }
            }


    :data string name: (Optional) name of the config value
    :data string value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data object meta_data: (Optional) Meta data for the config field
    :data enum data_type: (Optional) "text", "email", "number", "url", "tel", "date" | Data schema for the text field. Default is text
    :data string data_placeholder: (Optional) Input field placeholder
    :data integer data_min: (Optional) Minimum value (validation for type "number")
    :data integer data_max: (Optional) Maximum value (validation for type "number")
    :data integer data_max_lenght: (Optional) Maximum value (validation for type "text")
    :data integer data_min_lenght: (Optional) Minimum value (validation for type "text")
    :data string data_pattern: (Optional) Regular expression for input validation defines an input mask

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(textarea)


.. http:response:: Example request body

    .. sourcecode:: js

            {
                "name":"Updated Name of my config value",
                "value":"<h1>Updated This is my default HTML content</h1>",
                "description":"Updated The description of my config value.",
                "meta_data":{
                    "editor":"code"
                }
            }


    :data string name: (Optional) name of the config value
    :data string value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data object meta_data: (Optional) Meta data for the config field
    :data enum editor: (Optional) "wysiwyg", "code", "none" | Which editor should be shown to the user?
    :data bool code_view: (Optional) Is the code-view button available in the wysiwyg-editor?

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(select)


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


    :data string name: (Optional) name of the config value
    :data string value: (Optional) Value for the config element
    :data string description: (Optional) Description for the config value
    :data array source: (Optional) All available options of the select config value

.. http:method:: PUT /api/v1/templates/{template_id}/configs/{config_id}(multiselect)


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
                "value":[ "updated_value_id_3", "updated_value_id_1" ]
            }


    :data string name: (Optional) name of the config value
    :data array value: (Optional) all values which should be selected by default
    :data string description: (Optional) Description for the config value
    :data array source: (Optional) All available options of the select config value


/templates/{template_id}/languages
----------------------------------

Documentation will follow soon...


/templates/{template_id}/languages/{lang_tag}
---------------------------------------------

.. http:method:: PUT /api/v1/templates/{template_id}/languages/{lang_tag}


.. http:response:: Example request body

    .. sourcecode:: js

            {
                "is_activated":1
            }


    :data boolean is_activated: (Required) If the new language is activated immediately



/templates/{template_id}/languages/{lang_tag}/translations
----------------------------------------------------------

Documentation will follow soon...


/templates/{template_id}/templates
----------------------------------

Documentation will follow soon...