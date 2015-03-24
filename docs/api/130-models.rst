API: Models calls
=================

.. note:: Test these requests in our API-Explorer_.

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

/models/:id
-----------
.. http:method:: GET /api/v1/models/{id}

   :arg id: ID of the model.

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


/models/:id/configs
-------------------

.. note:: data_* parameters are different for each config type. The following table will list these parameters.


+------------+--------------------------+-------------------------------------------------------+
| Config-Type   |    Attribute             |   Description                                         |
+===============+==========================+=======================================================+
| GET        |    Entity, Collection    |   Request a single entity or a whole collection       |
+------------+--------------------------+-------------------------------------------------------+
| POST       |    Collection            |   Creates a new entity in a collection                |
+------------+--------------------------+-------------------------------------------------------+
| PUT        |    Entity                |   Updates an entity                                   |
+------------+--------------------------+-------------------------------------------------------+
| DELETE     |    Entity                |   Deletes an entity                                   |
+------------+--------------------------+-------------------------------------------------------+