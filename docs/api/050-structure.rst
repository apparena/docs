API - Data structure
====================

App-Arena.com apps launched in the world wide web are designed to be highly customizable. Through a system of interconnected configuration sets,
we make sure that every customer is able to make his app look and feel like a unique and individually crafted application.

In order to create new apps it is crucial to know the mechanics working in the background.

At the foundation of every application is a project. Projects serve as the central entry point for a collection of version varieties, which
occur over the course of a development. Every version contains the information an application needs to operate, from configuration entries which define fundamental
application functionality to information entries framing it in its web context. Translations are found there as well as the languages in which the project
is available.

The distinctive versions of a project hold the entirety of customization options your customer has at his disposal to individualize his web appearance. It may contain
functionality and content which can selectively be activated to shape the application your customer wants to use in his or her individual context.

To clarify this concept, imagine a contest project. It contains the logic necessary to let users pick a single item of their preference out of a greater heap of related items.
These items can be anything from a picture or a video to a song. The core of the voting system stays the same, no matter what is being voted for. The difference between
the contest modes is achieved through configuration sets, which 'shape' the project to the customers needs.
On our platform, we call these configuration sets 'templates'. Templates can contain as little as a single configuration but may as well be used to configure, style and translate
an entire application. However, the real power of the templates derives from the possibility to chain them together and thus, let you create vast amounts of apps of individual
behaviour with minimal effort.
We could create a template which 'shapes' the contest-project to a video contest by altering the configuration accordingly. In the next step, we create three templates
which alter the Headline to 'Band-Contest', 'Beauty-Contest' and 'Funniest-Video-Contest' as well as setting the logos adequately. These templates now get chained to the template we
created in the first place by declaring them as children of it. This results in three different apps with individual look and feel while the core logic behind them stays the same.

Image 1 visualizes the relation between 'apps', 'templates' and 'projects'.

.. image:: images/App_Customization.jpg
    :alt: Image 1

As seen in Image 1, all versions point to their root project. Templates however can point to a project version as well as to a another template. The difference is determined by
the parentId: If the parentId points to itself, or in other words, if the parentId equals the templateId, the template points to the project version declared in it. If it is the case that
templateId and parentId differ, the template points to its parent template.
Templates may only contain settings that are already present in the project version. They are therefore only capable of overwriting existing settings and do not create configurations on their
own. Besides other crucial information, the app itself holds a set of configurations as well, making it a mixture between a template and additional customization options. The app is mostly
the customers domain where he can give the application his final personal touch.

Projects, templates and app settings are hierarchically structured. This means that settings in the app overwrite occurrences of the same setting from templates and the project. Likewise
template settings overwrite those of the parent template and project. Image 2 shows this behaviour.

.. image:: images/AppTemplateProjectRelation.jpg
    :alt: Image 2

The image shows how the different types of settings:

    - info:         Works as a key => value storage for general application information like e.g. domain name, facebook ID, app validity in days, ...
    - config:       Is used to configure the application itself like e.g. font, logo uri, images, html and css code, ... The different types of config values are categorized. See the different types of config values and their characteristics `here <../api/060-config.html>`_.
    - translation:  Stores the translation strings used for multi language support.
    - language:     Sets the available/activated languages.

The language support works in the following way:

The project version determines the languages available.

