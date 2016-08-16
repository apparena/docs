API - Special API calls
=======================

Creating a template from an app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes it might be handy to convert an app into a template. In this case a new template is created and all config, info,
translation and language entries are copied into it. The template that the app was pointing to is being inserted as the parent template.

In order to execute this, make a regular POST request onto /templates, but instead of submitting the required information for creating
a template, just send the appId of the app you want to convert.

To keep the response JSON small, only the basic template information is returned. Use a GET/PUT request on templates/:templateId/infos, .../configs,
.../translations or .../languages to retrieve/change its contents.

.. Note:: Submit only the appId. Additional information leads to denial of the request.

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "appID"    :   1
        }

    .. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "templateId": 1,
            "version": "1.0.0",
            "projectId": 1,
            "parentId": 2,
            "companyId": 1,
            "lang": "en_US",
            "name": "App Name [copy]",
            "public": false
          }
        }

.. Note:: The newly created template will be created as non-public. To change it into a publically available template, use a PUT request.