API - Special API calls
=======================

Creating a template from an app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes it might be handy to convert an app into a template. In this case a new template is created and all config, info,
translation and language entries are copied into it.

In order to execute this, make a regular POST request onto /templates, but instead of submitting the required information for creating
a template, just send a field "copyFrom" : "app" and the appId of the app you want to convert.

To keep the response JSON small, only the basic template information is returned. Use a GET request on templates/:templateId/infos, .../configs,
.../translations or .../languages to retrieve its contents.

.. http:response:: POST /templates

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"  : "app",
            "appId"     :   1
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "templateId": 2,
            "version": "1.0.0",
            "projectId": 1,
            "parentId": 2,
            "companyId": 1,
            "lang": "en_US",
            "name": "App Name [copy]",
            "public": false
          }
        }

    **Required data**

    copyFrom
        ``string`` must be "app"
    appId
        ``integer`` specifies the app the template will be copied from

    **Optional data**

    companyId
        ``integer`` defines a different company than your own as owner of the newly created template
    parentId
        ``integer`` defines the template, the newly created template should point to. If left out, the template to which the app pointed will be used, if set to '0', the template points to the project.
    projectId
        ``integer`` defines the project the newly created template points to. If the parentId is not equal to the templateId, the template points to the parent template, meaning that this will have no effect if a parent template is defined.
    version
        ``string`` if a projectId is submitted, you can specify the version here
    lang
        ``string`` sets the default language of the new template. This language must be present in the root project.
    name
        ``string`` defines the name of the new template. If not specified, the name of the app with an additional "[copy]" string is used
    public
        ``bool`` sets the public status of the new template


Copy an existing template
~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to modify an existing template but keep the original, you can copy it by sending a POST request with the field "copyFrom" : "template" and the templateId

.. http:response:: POST /templates

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"  : "app",
            "templateId"     :   1
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "templateId": 2,
            "version": "1.0.0",
            "projectId": 1,
            "parentId": 2,
            "companyId": 1,
            "lang": "en_US",
            "name": "App Name [copy]",
            "public": false
          }
        }

    **Required data**

    copyFrom
        ``string`` must be "template"
    templateId
        ``integer`` specifies the pattern template

    **Optional data**

    companyId
        ``integer`` defines a different company than your own as owner of the newly created template
    parentId
        ``integer`` defines the template, the newly created template should point to. If left out, the template to which the app pointed will be used, if set to '0', the template points to the project.
    projectId
        ``integer`` defines the project the newly created template points to. If the parentId is not equal to the templateId, the template points to the parent template, meaning that this will have no effect if a parent template is defined.
    version
        ``string`` if a projectId is submitted, you can specify the version here
    lang
        ``string`` sets the default language of the new template. This language must be present in the root project.
    name
        ``string`` defines the name of the new template. If not specified, the name of the app with an additional "[copy]" string is used
    public
        ``bool`` sets the public status of the new template