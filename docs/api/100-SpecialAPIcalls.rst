API - Copy calls
================

Copy an existing project
~~~~~~~~~~~~~~~~~~~~~~~~

.. http:response:: POST /projects

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"  : 1,
            "version"   : "1.0.0"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "projectId": 2,
            "companyId": 1,
            "name": "dummy project [copy]",
            "description": null
          }
        }

    **Required data**

    copyFrom
        ``string``  specifies the project which is to be copied
    version
        ``string``
            "all"                   copies all existing versions of the project
            "latest"                copies the most recent version of the project
            "X.Y.Z"                 copies the specified version of the project
            ["A.B.C","X.Y.Z",...]   copies all the declared versions of the project

    **Optional data**

    companyId
        ``integer`` defines a different company than your own as owner of the newly created template
    name
        ``string``  defines the name of the new project. If not specified, the name of the original project with an additional "[copy]" string is used
    description
        ``string``  describe the newly created project

Copy an existing version
~~~~~~~~~~~~~~~~~~~~~~~~

Copies a version inside a project specified by :projectId

.. http:response:: POST /projects/:projectId/versions

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"  : "1.0.0"
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "projectId": 1,
            "variant": "1.0.1",
            "companyId": 1,
            "name": "dummy version of project 1 [copy]",
            "lang": "de_DE",
            "public": false
          }
        }

    **Required data**

    copyFrom
        ``string``  specifies the version which is to be copied

    **Optional data**

    name
        ``string``  defines the name of the new version. If not specified, the name of the original version with an additional "[copy]" string is used
    lang
        ``string``  sets the default language of the new version
    variant
        ``string``  sets the version variant number ("A.B.C") of the new version. If not submitted, the last digit is increased by one
    public
        ``bool``    sets the public status of the new version

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
        ``string``  must be "app"
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
        ``string``  if a projectId is submitted, you can specify the version here
    lang
        ``string``  sets the default language of the new template. This language must be present in the root project.
    name
        ``string``  defines the name of the new template. If not specified, the name of the app with an additional "[copy]" string is used
    public
        ``bool``    sets the public status of the new template


Copy an existing template
~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to modify an existing template but keep the original, you can copy it by sending a POST request with the field "copyFrom" : "template" and the templateId

.. http:response:: POST /templates

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"      : "template",
            "templateId"    :   1
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
            "name": "Template Name [copy]",
            "public": false
          }
        }

    **Required data**

    copyFrom
        ``string``  must be "template"
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
        ``string``  if a projectId is submitted, you can specify the version here
    lang
        ``string``  sets the default language of the new template. This language must be present in the root project.
    name
        ``string``  defines the name of the new template. If not specified, the name of the original template with an additional "[copy]" string is used
    public
        ``bool``    sets the public status of the new template

Copy an existing app
~~~~~~~~~~~~~~~~~~~~

If you want to modify an existing template but keep the original, you can copy it by sending a POST request with the field "copyFrom" : "template" and the templateId

.. http:response:: POST /apps

.. http:response:: Example request body

    .. sourcecode:: js

        {
            "copyFrom"      : 1
        }

.. http:response:: Example response body

    .. sourcecode:: js

        {
          "status": 201,
          "data": {
            "appId": 2,
            "templateId": 1,
            "companyId": 1,
            "lang": "de_DE",
            "name": "App name [copy]",
            "activated": true,
            "expiryDate": "2016-10-03 13:16:52"
          }
        }

    **Required data**

    copyFrom
        ``string``  specifies the app which is to be copied

    **Optional data**

    templateId
        ``integer`` sets the template the new app is pointing to
    companyId
        ``integer`` sets a different company than your own as owner of the newly created app
    expiryDate
        ``string``  sets the expiration date of the app
        ``integer`` sets the expiration date in days. A value of 30 means that the app will expire in 30 days from the day of execution
    lang
        ``string``  sets the default language of the new app. This language must be present in the root project
    name
        ``string``  defines the name of the new app. If not specified, the name of the original app with an additional "[copy]" string is used
    activated
        ``bool``    sets the activation status of the new app