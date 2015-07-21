SDK - PHP
=========

Getting started
---------------

You can find our `PHP SDK on github_`.



If you do not have access to the developer section yet, please drop us an email to s.buckpesch at app-arena.com
with your contact data and will we get in touch with you and sent you an API key.

Installation
------------

    ::

    composer require app-arena/php-sdk dev-master


Usage
-----

    ::

    $app_manager = new \AppManager\AppManager(
        array(
            'cache_dir' => ROOT_PATH . "/var/cache"
        )
    );
    $instance    = $app_manager->getInstance();
    $config      = $instance->getConfigs();
    $translation = $instance->getTranslations();
    $info        = $instance->getInfo();

