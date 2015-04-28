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
            "template_id":    780,
            "name":           "New Instance {{$timestamp}}",
            "description":    "The description of my new instance.",
            "lang_tag":       "en_US"
        }



    :data string name: (Required) Name of the instance
    :data integer template_id: (Required) Template ID the instance should be created of
    :data int company_id:  (Optional) Company_id of the company the instance should be created for
    :data enum template_type: (Optional) The entity the instance should be generated of
    :data string description: (Optional) Description of the instance.
    :data enum lang_tag:  (Optional) ["sq_AL", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY",
                        "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SD", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "be_BY",
                        "bg_BG", "ca_ES","zh_CN", "zh_HK", "zh_SG", "hr_HR", "cs_CZ", "da_DK", "nl_BE", "nl_NL",
                        "en_AU", "en_CA", "en_IN", "en_IE","en_MT", "en_NZ", "en_PH", "en_SG", "en_ZA", "en_GB",
                        "en_US", "et_EE", "fi_FI", "fr_BE", "fr_CA", "fr_FR","fr_LU", "fr_CH", "de_AT", "de_DE",
                        "de_LU", "de_CH", "el_CY", "el_GR", "iw_IL", "hi_IN", "hu_HU", "is_IS","in_ID", "ga_IE",
                        "it_IT", "it_CH", "ja_JP", "ja_JP", "ko_KR", "lv_LV", "lt_LT", "mk_MK", "ms_MY", "mt_MT",
                        "no_NO", "no_NO", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sr_BA", "sr_ME", "sr_CS",
                        "sr_RS", "sk_SK","sl_SI", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC",
                        "es_SV", "es_GT", "es_HN", "es_MX","es_NI", "es_PA", "es_PY", "es_PE", "es_PR", "es_ES",
                        "es_US", "es_UY", "es_VE", "sv_SE", "th_TH", "th_TH","tr_TR", "uk_UA", "vi_VN"]



.. http:response:: Newly created instance object

    .. sourcecode:: js

        {
            "active": 1,
            "base_url": "https:\/\/adventskranz.onlineapp.co\/",
            "description": "The description of my new instance.",
            "expiration_date": "2015-04-27",
            "fb_app_id": "725444547534506",
            "fb_app_namespace": "advents-kranz",
            "fb_page_id": null,
            "fb_page_name": null,
            "fb_page_url": "",
            "id": 9865,
            "lang_tag": "en_US",
            "m_id": 299,
            "name": "New Instance 1429522046",
            "template_id": 780,
            "timestamp": 1429522082,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9865"
                }
            }
        }

`Link to the parameter documentation. <../api/090-instances.html#instance_object>`_




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

`Link to the parameter documentation. <../api/090-instances.html#instance_object>`_


/instances/:i_id
----------------

.. _instance_object:

.. http:method:: GET /api/v1/instances/:i_id

   :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single instance.

    .. sourcecode:: js

        {
            "active": 1,
            "base_url": "https:\/\/adventskranz.onlineapp.co\/",
            "description": "The description of my new instance.",
            "expiration_date": "2015-05-05",
            "fb_app_id": "725444547534506",
            "fb_app_namespace": "advents-kranz",
            "fb_page_id": null,
            "fb_page_name": null,
            "fb_page_url": "",
            "id": 9905,
            "lang_tag": "en_US",
            "m_id": 299,
            "name": "New Instance 1430202395",
            "template_id": 780,
            "timestamp": 1430202441,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9905"
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


.. http:method:: PUT /api/v1/instances/:i_id

       :arg i_id: ID of the instance.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name": "This is my new instance name. It's changed!",
            "expiration_date": "2015-12-24"
        }

`Link to the parameter documentation. <../api/090-instances.html#instance_object>`_


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

`Link to the parameter documentation. <../api/090-instances.html#instance_object>`_

.. http:method:: DELETE /api/v1/instances/:i_id

    :arg i_id: id of the instance.

`Successful DELETE requests will return HTTP-Status code 204. <../api/001-index.html#codes>`_



/instances/:i_id/configs
------------------------



.. http:method:: GET /api/v1/instances/:i_id/configs

    :arg i_id: id of the instance.

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
                    {  ... },
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
                    {  ... },
                }
            }
        }

.. warning:: The Documentation about the parameter_answer will follow soon!!!

/instances/:i_id/configs/:config_id
-----------------------------------

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(checkbox)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Zusätzliche Loginabfrage für Export und löschen der Userdaten, inklusive Log-Eintrag der angemeldeten Person. Funktioniert nur mit App-Internen Logins, nicht mit Social-Connects!",
            "id": "activate_admin_secure_login",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "name": "[Admin Sicherheitslogin aktivieren]",
            "template_id": 780,
            "type": "checkbox",
            "value": 0,
            "timestamp": 1429104304,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/activate_admin_secure_login"
                }
            }
        }

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(color)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Die Hintergrundfarbe betrifft alle Seiten der App, inklusive Footer. Empfehlung: Wählen Sie eine helle, neutrale Farbe (z.B. weiß). Weitere Infos siehe Grafikleitfaden.",
            "id": "app_color_1",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "name": "Hintergrundfarbe",
            "template_id": 780,
            "type": "color",
            "value": "#ffffff",
            "timestamp": 1429104762,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/app_color_1"
                }
            }
        }

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(css)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "compiler": "less",
            "description": "Diese CSS Konfiguration wird vom Entwickler erstellt und enthält die wichtigsten CSS Formatierungen der App.",
            "id": "css_app",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "name": "CSS der Applikation",
            "src": "https:\/\/www.app-arena.com\/uploads\/apps\/model\/299\/0\/de_DE\/css\/css_app.css",
            "template_id": 780,
            "type": "css",
            "value": "Here you find the complete styling of the application."
            "timestamp": 1429104816,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/css_app"
                }
            }
        }

.. warning:: The Documentation about the parameter_answer will follow soon!!!

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(date)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Nutzer können ab 0.01 Uhr des von Ihnen festgelegten Datums teilnehmen.",
            "id": "door_11_validity_period_start",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "name": "Startdatum für die Teilnahme",
            "template_id": 780,
            "type": "date",
            "value": "2014-12-11",
            "timestamp": 1429105031,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/door_11_validity_period_start"
                }
            }
        }

.. warning:: The Documentation about the parameter_answer will follow soon!!!

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(image)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Das Unternehmenslogo wird auf der Header-Grafik abgebildet. Alternativ können Sie das Logo in Ihre Grafiken integrieren und die automatische Ansicht des Logos in dem Punkt Header deaktivieren. Empfohlene Größe: 180 x 180 px. Weitere Infos siehe Grafikleitfaden.",
            "height": "",
            "id": "app_logo",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "name": "Unternehmenslogo",
            "size": "",
            "src": "https:\/\/app-manager.s3.amazonaws.com\/apps\/models\/2\/9\/9\/0\/de_DE\/01_01_logo_1411631048_0.png",
            "template_id": 780,
            "type": "image",
            "value": "https:\/\/app-manager.s3.amazonaws.com\/apps\/models\/2\/9\/9\/0\/de_DE\/01_01_logo_1411631048_0.png",
            "width": "",
            "timestamp": 1429105088,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/app_logo"
                }
            }
        }

.. warning:: The Documentation about the parameter_answer will follow soon!!!

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(multiselect)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Geben Sie hier an, welche Art von Inhalten Sie hinter dem Türchen anzeigen möchten. Die jeweiligen Inhalte legen Sie innerhalb der nächsten Schritte fest. Weitere Infos siehe Konfigurationsleitfaden.",
            "id": "door_1_pages_activated",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "name": "Inhalte des Türchens",
            "source": [
                {
                    "value": "none",
                    "text": "Keine Seite"
                },
                {
                    "value": "page",
                    "text": "Inhaltsseite"
                },
                {
                    "value": "quiz",
                    "text": "Quiz-Seite"
                }
            ],
            "template_id": 780,
            "type": "multiselect",
            "value": [
                "page",
                "quiz"
            ],
            "timestamp": 1429105338,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/door_1_pages_activated"
                }
            }
        }

.. warning:: The Documentation about the parameter_answer will follow soon!!!

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(select)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Wählen Sie eine der vordefinierten Schriftarten aus oder legen Sie per CSS eine eigene Schriftart fest. Weitere Infos siehe Grafikleitfaden.",
            "id": "app_font_body",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "name": "Schriftart für Textkörper",
            "source": [
                {  ... },
                {
                    "value": "arial",
                    "text": "Arial"
                },
                {
                    "value": "delius-Swash",
                    "text": "Delius Swash Caps"
                }
                {  ... },
            ],
            "template_id": 780,
            "type": "select",
            "value": "source-sans-pro",
            "timestamp": 1429105490,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/app_font_body"
                }
            }
        }

.. warning:: The Documentation about the parameter_answer will follow soon!!!

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(text)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "Die E-Mail-Adresse des Ansprechpartners wird nicht veröffentlicht oder an Dritte weitergegeben. Beispiel: maxmustermann@unternehmensname.com.",
            "format": "text",
            "id": "admin_mails",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "maxlength": "",
            "name": "E-Mail-Adresse des Ansprechpartners (nicht öffentlich sichtbar)",
            "placeholder": "",
            "template_id": 780,
            "type": "text",
            "value": "",
            "timestamp": 1429105669,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/admin_mails"
                }
            }
        }

.. warning:: The Documentation about the parameter_answer will follow soon!!!

.. http:method:: GET /api/v1/instances/:i_id/configs/:config_id(textarea)

    :arg model_id: ID of the config.
    :arg i_id: ID of the instance.

.. http:response:: Retrieve basic information of a single model.

    .. sourcecode:: js

        {
            "description": "<p>Erklärung, die ein Admin bestätigen muss, bevor er die Teilnehmer-Daten des Wettbewerbs exportieren darf.\ \ <\/p>",
            "id": "admin_export_terms",
            "instance_id": 9849,
            "lang_tag": "de_DE",
            "name": "[Erklärung zur Datenverwendung beim Export]",
            "template_id": 780,
            "type": "textarea",
            "value": "<h3>Erklärung zur vertraulichen Datenverwendung<\/h3>Hiermit bestätige ich, dass die durch diese Facebook Applikation erhobenen Daten ausschließlich zur Durchführung dieses Wettbewerbs verwendet werden. Zudem bestätige ich die Daten nach Ablauf der Werbeaktion zu löschen. Die iConsultants GmbH wird von jeglicher Haftung, die durch den Missbrauch der zur Verfügung gestellten Daten entsteht, befreit.",
            "timestamp": 1429105717,
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9849\/configs\/admin_export_terms"
                }
            }
        }

.. warning:: The Documentation about the parameter_answer will follow soon!!!


.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(checkbox)

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

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

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(color)

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":       "Updated Name of Color",
            "value":      "#EEEEEE",
            "description":"Updated The description of my color"
        }

    :data string name: (Optional) Name for the config value
    :data string value: (Optional) Default value for the config element
    :data string description: (Optional) Description for the instance

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(css)

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":           "Updated Name of my CSS config",
            "value":          "body { text-align:center; text-color:red; } h1.h1, h2, h3 { font-size: 30px; }",
            "description":    "Updated The description of my config value.",
            "data_compiler":  "css"
        }

    :data string name: (Optional) Name for the config value
    :data string value: (Optional) Default value for the config element
    :data string description: (Optional) Description for the instance

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(date) DEPRECATED

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":       "Updated Name of my date",
            "value":      "1911-02-22",
            "description":"Updated Enter a valid date"
        }

    :data string name: (Optional) Name for the config value
    :data string value: (Optional) value for the config element
    :data string description: (Optional) Description for the instance

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(image)

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

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

    :data string name: (Optional) Name for the config value
    :data string value: (Optional) value for the config element
    :data string description: (Optional) Description for the instance

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(multiselect)

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

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

    :data string name: (Optional) Name for the config value
    :data array value: (Optional) All values which should be selected by defaul
    :data string description: (Optional) Description for the instance
    :data array source: (Optional) All available options of the select config value

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(select)

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

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

    :data string name: (Optional) Name for the config value
    :data string value: (Optional) Default value for the config element
    :data string description: (Optional) Description for the instance
    :data array source: (Optional) All available options of the select config value

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(text)

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

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
    :data string value: (Optional) value for the config element
    :data string description: (Optional) Description for the config value
    :data integer min: (Optional) Minimum value (validation for type "number")
    :data integer max: (Optional) Maximum value (validation for type "number")
    :data integer max_lenght: (Optional) Maximum value (validation for type "text")
    :data integer min_lenght: (Optional) Minimum value (validation for type "text")
    :data string pattern: (Optional) Regular expression for input validation defines an input mask

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: PUT /api/v1/instances/:i_id/configs/:config_id(textarea)

       :arg i_id: ID of the instance.
       :arg model_id: ID of the config.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "name":       "Updated Name of my config value",
            "value":      "<h1>Updated This is my default HTML content</h1>",
            "description":"Updated The description of my config value.",
            "data_editor":"code"
        }

    :data string name: (Optional) Name of the config value
    :data string value: (Optional) Default value for the config element
    :data string description: (Optional) Description for the config value
    :data enum editor: (Optional) Which editor should be shown to the user?

`Table with data_ parameters and the description of them. <../api/130-models.html#table>`_

.. http:method:: DELETE /api/v1/instances/:i_id/configs/:config_id

`Successful DELETE requests will return HTTP-Status code 204. <../api/001-index.html#codes>`_







/instances/:i_id/languages
--------------------------

.. http:method:: GET /api/v1/instances/:i_id/languages


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

`Documentation for the language. <../api/090-instances.html#language>`_

/instances/:i_id/languages/:lang_tag
------------------------------------

.. _language:

.. http:method:: PUT /api/v1/instances/:i_id/languages/:lang_tag

       :arg i_id: ID of the instance.
       :arg lang_tag: ID of the language.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "is_activated":0
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
            "is_activated": 0,
            "lang_tag": "en_US",
            "timestamp": 1430141442,
            "id": "en_US",
            "_links": {
                "self": {
                    "href": "https:\/\/v2.app-arena.com\/api\/v1\/instances\/9903\/languages\/en_US"
                }
            }
        }

/instances/:i_id/languages/:lang_tag/translations
-------------------------------------------------

.. http:method:: GET /api/v1/instances/:i_id/languages/:lang_tag/translations

       :arg i_id: ID of the instance.
       :arg lang_tag: ID of the language.

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

`Documentation for the language. <../api/090-instances.html#language>`_

/instances/{i_id}/languages/:lang_tag/translation/:translation_id
-----------------------------------------------------------------


.. http:method:: PUT /api/v1/instances/{i_id}/languages/:lang_tag/translation/:translation_id

       :arg i_id: ID of the translation.
       :arg lang_tag: ID of the language.
       :arg translation_id: ID of the translation.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "value":"UPDATED Il mio test translation!"
        }

    :data string value: (Required) Translation

`Documentation for the language. <../api/090-instances.html#language>`_