JS-SDK
=======

Getting started
---------------

You can find our `JS SDK on github`_.

.. _JS SDK on github: https://github.com/apparena/js-sdk

Installation
------------

1. Clone the repository
2. npm install
3. npm run build (production & develop)  | npm run build:prod (production) | npm run build:dev (develop)


Usage
-----



Methods
-------

+-------------------------------------------------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Method                                          | Description                                                         | Parameters                                                                                                            | Response                                                     |
+=================================================+=====================================================================+=======================================================================================================================+==============================================================+
| init(params)                                    | This will add parameters to the smartLink Url. These                | array $params Array of parameters                                                                                     |                                                              |
|                                                 | parameters will be available as GET-Parameters, when a              | which should be passed through                                                                                        |                                                              |
|                                                 | user* clicks on the smartLink. The parameters will be               |                                                                                                                       |                                                              |
|                                                 | available as GET parameters as well in the facebook                 |                                                                                                                       |                                                              |
|                                                 | page tab* or within an iframe                                       |                                                                                                                       |                                                              |
+-------------------------------------------------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+