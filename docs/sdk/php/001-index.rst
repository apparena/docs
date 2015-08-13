SDK - PHP
=========

Getting started
---------------

You can find our `PHP SDK on github_`.


Installation
------------

    ::

        composer require app-arena/php-sdk


Usage
-----

Use the Composer Autoloader to start using the App-Manager

    ::

        define("ROOT_PATH", realpath(dirname(__FILE__)) . "../../../../");
        require ROOT_PATH . '/vendor/autoload.php';

        $m_id = 123; // Set your app-arena Model ID here

        // Clear the cache before, requestion Instance in for each
        $am = new \AppManager\AppManager(
            $m_id,
            array(
                "cache_dir" => ROOT_PATH . "/var/cache"
            )
        );
        // Get all necessary instance information to start working
        $config = $am->getConfigs();
        $translation = $am->getTranslations();
        $info = $am->getInfos();


Now the connection is build up and you can start using you App-Instance. The App-Manager SDK automatically tries to get
your Instance ID (i_id) from GET-Parameters or from Cookies. So your Url should be something like this:

    ``http://www.domainofmyapp.com/mypage.php?i_id=1234``

Methods
-------

+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| Method                | Description                                                      | Parameters                                    | Response |
+=======================+==================================================================+===============================================+==========+
| addParams($params)    | This will add parameters to the smartLink Url. These             | array $params Array of parameters             |          |
|                       | parameters will be available as GET-Parameters, when a           | which should be passed through                |          |
|                       | user* clicks on the smartLink. The parameters will be            |                                               |          |
|                       | available as GET parameters as well in the facebook              |                                               |          |
|                       | page tab* or within an iframe                                    |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| cleanCache()          | Cleans the cache, so that a fresh API call will be done          |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getBaseUrl()          | Returns the BaseUrl your Sharing Url is generated with.          |                                               | string   |
|                       | By default it will use the currently used domain                 |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getBrowser()          | Returns user browser information                                 |                                               | array    |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getConfigs()          | Returns all Config Elements of the current instance as array     |                                               | array    |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getCssHelper()        | Returns CSS Helper object to compile and concatenate Less, CSS   |                                               | CSS      |
|                       | and Config-Type (CSS) values                                     |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getDevice()           | Returns user device information                                  |                                               | array    |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getDeviceType()       | Returns the device type of the current device                    |                                               | string   |
|                       | ``mobile``, ``tablet``, ``desktop``                              |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getEnvironment()      | Returns if the app currently running on a ``website``, ``facebook``  |                                           | string   |
|                       | or ``direct`` ``website`` means the app is embedded via iframe to    |                                           |          |
|                       | a website ``facebook`` means the app is embedded in a              |                                             |          |
|                       | facebook page tab ``direct`` means the app is being accessed       |                                             |          |
|                       | directly without iframe embed                                    |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getIId()              | Returns the currently used Instance ID                           |                                               | int      |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getInfos()            | Returns all basic information of the current instance            |                                               | array    |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getLang()             | Returns the currently used Language as Language                  |                                               | string   |
|                       | Code (e.g. de_DE, en_US, ...)                                    |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getMId()              | Returns the model ID of the currently selected instance          |                                               | int      |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getTranslations()     | Returns all translations of the current instance and language    |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getUrl()              | Returns the SmartLink Url for Sharing                            |                                               | string   |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getUrlLong()          | Returns the SmartLink Url without Url Shortener                  | bool $shorten Shorten URL using smartl.ink    | string   |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getInfos()            | Returns all basic information of the current instance            |                                               | array    |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| getLang()             | Returns the currently used Language as Language Code             |                                               | string   |
|                       | (e.g. de_DE, en_US, ...)                                         |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| renderSharePage       | Renders the complete HTML of the Share page including            | bool $debug - Show debug information          | string   |
| ($debug = false)      | all meta tags and redirection.                                   | on the page?                                  |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| setBaseUrl($base_url) | Sets a new base url for your sharing links (–>getUrl()).         | string $base_url New base url                 | void     |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| setLang($lang)        | Sets a new language for the current instance                     | string $lang 5 char Language Code, e.g. de_DE |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| setMeta($meta)        | Sets the meta data for SmartLink Share page. All key value       | array $meta (see description)                 | array    |
|                       | pairs will be generated as meta information into the head        |                                               |          |
|                       | of the share page. The array keys ``title``, ``desc``, ``image`` |                                               |          |
|                       | are the most important. The array values can be Strings or       |                                               |          |
|                       | config identifiers of the instance                               |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+
| setParams($params)    | This will reset all parameters of the smartLink Url. These       | array $params Array of parameters             |          |
|                       | parameters will be available as GET-Parameters, when a           | which should be passed through                |          |
|                       | user* clicks on the smartLink. The parameters will be            |                                               |          |
|                       | available as GET parameters as well in the facebook              |                                               |          |
|                       | page tab* or within an iframe                                    |                                               |          |
+-----------------------+------------------------------------------------------------------+-----------------------------------------------+----------+

