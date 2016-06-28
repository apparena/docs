API - Data structure
====================

App-Arena.com apps launched in the world wide web are designed to be highly customizable. Through a system of interconnected configuration sets,
we make sure that every customer is able to make his app look and feel like a unique and individually crafted application.

In order to create new apps it is crucial to know the mechanics which work in the background.

At the foundation of every application is a project. Projects serve as the central entry point for a collection of version varieties, which
occur over the course of a development. Every version contains everything the application needs to operate, from configuration entries which define fundamental
application functionality over information entries framing it in its web context. Translations are found there as well as the languages in which the project
is available.

The distinctive versions of a project hold the entirety of customization options your customer has at his disposal to individualize his web appearance. It may contain
functionality and content which can selectively be activated to shape the application your customer wants to use in his or her individual context.

To clarify this concept, imagine a contest project. It contains the logic necessary to let users pick a single item of their preference out of a pile of related items.
These items can be anything from a picture or a video to a song. The core of the voting system stays the same, no matter what is being voted for. The difference between
the voting modes is achieved through configuration sets, which 'shape' the project to the customers needs.
On our platform, we call these configuration sets 'templates'. Templates can contain as little as a single configuration but may be used as well to configure, style and translate
an entire application. However, the real power of the templates derives from the possibility to chain them together and thus, let you create vast amounts of apps of individual
behaviour with minimal effort. We could create a template which 'shapes' the contest-project to a video contest by altering the configuration accordingly. Now we create three templates
which alter the Headline to 'Band-Contest', 'Beauty-Contest' and 'Funniest-Video-Contest' as well as setting the logos adequately.

Figure 1 visualizes the relations between 'apps', 'templates' and 'projects'.

.. image:: docs/img/App-Customization.jpg
    :height: 600
       :width: 800
           :scale: 50
                :alt: Figure 1: App customization

language    -> project language makes the possible languages
             creating a language in a template or app activates it

configs     -> represents the set of config values available
            -> same for infos

struktur apps, templates, projects,