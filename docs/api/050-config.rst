API - Config data
=================

Config values have a mandatory field 'type' which determines what kind of data is stored. When creating a config value in
a project (-version) or updating (overwriting) it in a template or app, the 'value' field gets validated based on the contents of
the 'type' field. This table shows the data types and what to keep in mind using them.

+---------------+-----------------------------------+-------------------------------------------+
| Config-Type   | Valid input                       | Description                               |
+===============+===================================+===========================================+
| checkbox      | | ``mixed`` boolean values:       | | Simple Checkbox which can be checked or |
|               | | 1, 0, "1", "0", true, false     | | unchecked                               |
|               |                                   |                                           |
+---------------+-----------------------------------+-------------------------------------------+
| color         | | ``string`` Hex value:           | | Sets a color in Hex format              |
|               | | #FFFFFF - #000000               |                                           |
+---------------+-----------------------------------+-------------------------------------------+
| css           | | ``string`` CSS contents         | | CSS content optionally with variables   |
|               |                                   | | (config values), gets validated         |
+---------------+-----------------------------------+-------------------------------------------+
| date          | | ``string`` Date in format:      | | Y = Year, m = Month, d = Day, H = Hour, |
|               | | "Y-m-d H:i:s"                   | | i = Minute, s = Second                  |
+---------------+-----------------------------------+-------------------------------------------+
| HTML          | | ``string``                      | | HTML contents in a string               |
|               |                                   |                                           |
+---------------+-----------------------------------+-------------------------------------------+
| image         | | ``string`` URI to an image      | | Points to the location of an image      |
|               | | e.g.: www.example.com/logo.jpg  |                                           |
+---------------+-----------------------------------+-------------------------------------------+
| input         | | ``string`` any string           | | Can be any string the user inputs e.g.  |
|               |                                   | | a custom name                           |
+---------------+-----------------------------------+-------------------------------------------+
| select        | | ``string`` any value contained  | | Allows the user to select one item out  |
|               | | in the 'options' field in the   | | of a list. The list is defined in the   |
|               | | meta data                       | | meta-field 'options' of the config value|
|               |                                   | | (see explanation below).                |
+---------------+-----------------------------------+-------------------------------------------+
| multiselect   | | ``string`` multiple values      | | Similar to 'select' but the user can    |
|               | | contained in the 'options'      | | select multiple items                   |
|               | | field in the meta data          |                                           |
+---------------+-----------------------------------+-------------------------------------------+

Meta data behaviour
~~~~~~~~~~~~~~~~~~~

POST/PUT requests addressing non existing fields (e.g. changing a non existing field with a PUT request or a
typo in a JSON key when POSTing a new entity) usually lead to an error with the status code 400 (bad request).
This is not the case when PUTting a config or info entry, or more specific, when changing an entry containing the meta
data field: unrecognized fields are saved into the meta data array.

Add meta data
~~~~~~~~~~~~~

To clarify this concept, we go through the process in simple example.

Lets assume a config entry of an app/template/project with the configId 'test_config' and the type 'input' which means it
is a text field. The meta data field is initially empty. A GET request on that entry would yield something like:

.. sourcecode:: js

    {
      "_embedded": {
        "data": {
          "test_config": {
            "configId": "test_config",
            "lang": "de_DE",
            "name": "noname",
            "revision": 0,
            "value": "some_value",
            "meta": null,
            "type": "input",
            "description": "This is a test config entry.",
            "appId": 1,
            "_links": {
                    .
                    .
                    .
              }
            }
          }
        }
      }
    }

Now we want to give this entry some additional information in the meta data field, so we submit a PUT request. In this
example the config entry lives in an app with the appId '1', so the request url is

.. http:response:: PUT /apps/1/configs/test_config

.. sourcecode:: js

    {
        "author"    :   "John Doe",
        "content"   :   "this is an example"
    }

Because the app config entry doesn't have fields called 'author' and 'content' they will be created in the meta data.
A GET request on this config entry now yields

.. Warning:: In consequence, you cannot use meta-keys equal to existing fields of a config entry like: 'configId', 'lang', 'value', ...

.. sourcecode:: js

    {
      "_embedded": {
        "data": {
          "test_config": {
            "configId": "test_config",
            "lang": "de_DE",
            "name": "noname",
            "revision": 1,
            "value": "some_value",
            "meta": {
              "author": "John Doe",
              "content": "this is an example"
            },
            "type": "input",
            "description": null,
            "appId": 1,
            "_links": {
                    .
                    .
                    .
            }
          }
        }
      }
    }

Add meta objects
~~~~~~~~~~~~~~~~

As you can see, the meta field became an object with the newly created information on the top level. To create
sub-level objects, an object can be submitted. This way it is possible to create objects with unlimited depth.
An example of a sub-level object:

.. sourcecode:: js

    {
        "options": {"option1": "something", "option2": "something2"}
    }

After this request, a GET on the 'test_config' yields:

.. sourcecode:: js

    {
      "_embedded": {
        "data": {
          "test_config": {
            "configId": "test_config",
            "lang": "de_DE",
            "name": "noname",
            "revision": 1,
            "value": "some_value",
            "meta": {
              "author": "John Doe",
              "content": "this is an example",
              "options": {
                "option1": "something",
                "option2": "something2"
              }
            },
            "type": "input",
            "description": null,
            "appId": 1,
            "_links": {
                    .
                    .
                    .
              }
            }
          }
        }
      }
    }

While it is possible to create deep level structures, you can only address the top-level entries. Keeping the meta object
shallow is therefore recommended in order to avoid confusion and simplify the reading process.

Delete meta keys
~~~~~~~~~~~~~~~~

To delete entries, send a PUT request with an empty value.

.. sourcecode:: js

    {
        "options": null
    }

Now a GET request yields:

.. sourcecode:: js

    {
      "_embedded": {
        "data": {
          "test_config": {
            "configId": "test_config",
            "lang": "de_DE",
            "name": "noname",
            "revision": 1,
            "value": "some_value",
            "meta": {
              "author": "John Doe",
              "content": "this is an example"
            },
            "type": "input",
            "description": null,
            "appId": 1,
            "_links": {
                    .
                    .
                    .
              }
            }
          }
        }
      }
    }

Change meta data
~~~~~~~~~~~~~~~~

In order to change existing meta data entries use the same approach as adding data.

.. Warning:: Changing a meta key will overwrite the existing data in that key completely!