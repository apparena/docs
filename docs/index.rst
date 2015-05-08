App-Arena Developer documentation
=================================

`App-Arena.com`_ provides an infrastructure to manage and scale web-apps.
Developers can publish and sell own web-apps through our sales channels.
Sales partners can integrate our Web-App-CMS in their third-party software solutions and sell all published
apps of the platform under their name and brand.

The code of this documentation is open source, and `available on github`_. We appreciate every contribution to make
this documentation better.

.. _App-Arena.com: http://www.app-arena.com/
.. _available on github: https://github.com/apparena/docs


The main documentation for the site is organized into a couple sections:

    * :ref:`tools`
    * :ref:`dev-docs`
    * :ref:`sdk`
    * :ref:`integrator-docs`

.. _tools:

Tools
~~~~~

    `API-Explorer`_ - Quick overview of all available requests and interactive testing

.. _API-Explorer: https://v2.app-arena.com/apigility/swagger/API-v1


.. _dev-docs:

App Developer
~~~~~~~~~~~~~

If you want to develop apps, then start with one of these topics:

.. toctree::
:maxdepth: 2

        api/001-index
        api/030-companies
        api/090-instances
        api/130-models
        // echo "api/200-templates";
        postman

.. _sdk:

SDK
~~~

Use one of our SDKs to get started quick and easy.

.. toctree::
    :maxdepth: 2

    sdk/php/001-index

.. _integrator-docs:

Integrator
~~~~~~~~~~

If you want to integrate the App-Manager to your system and you want to sell apps on your website,
please get started with one of the following topics:

.. toctree::
    :maxdepth: 2

    integration/index
