SDK - SmartLink
===============

To setup a SmartLink, which is responsible for all your redirects, copy the ``smartlink.template.php`` file to your root
folder and rename it to ``smartlink.template.php``. As you can see in the file you can customize Meta-Data for sharing
by calling ``setMetaData(..)``. Additional Parameters which will be passed to your app as GET-Parameters can be add via
``addParams(..)`` or by just adding your parameters as GET parameter to the "Smart-Link"-Url you will get, when calling
``getUrl()``.


Device detection
~~~~~~~~~~~~~~~~

The users device will be detected, when the user is being redirected to your app target. So mobile and tablet devices
will never be redirected to a facebook page tab, as it is not possible for them to display them (No Support from Facebook).

Device simulation ($_GET['device'])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To simulate a different device type (mobile, tablet or desktop), just add a ``device``-GET Parameter to your URL. The
SmartLink will automatically use this device type then and respond with it. Allowed values are ``mobile``, ``tablet``
and ``desktop``.

    ::

        composer require app-arena/php-sdk
        // Your request will be `https://www.my-web-app.com/?i_id=1234&device=mobile` from a desktop device
        // Initialize the App-Manager
        $am = new \AppManager\AppManager(
           $m_id,
           array(
               "cache_dir" => ROOT_PATH . "/var/cache"
           )
        );
        echo $am->getDeviceType(); // Output: mobile
        $device = $am->getDevice();
        echo $device['type']; // Output: mobile


Website Embeds ($_GET['device'])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: Safari is blocking third-party cookies within iframes! You need to assure that users visiting your app
will be redirected via SmartLink to your application, so the SmartLink can set a cookie as first-party. Within
the iframe cookies from this domain will be allowed then. **DO NOT link directly to the page, your app is embedded in**.
Always link to the SmartLink redirecting to the page your app is embedded in.

If your app is being embedded in a website via iframe, you should add a GET-Parameter called ``website`` containing the URL
the app is embedded in to your smartlink.php Url. Your users will then be redirected the Website Url and not directly to
your app. Like this you can keep your traffic up on the website. :-)

Use the ``website``-GET Parameter for your iframe-Source is the easiest way to keep your visitors on the website. The
App-Manager SDK automatically detects ``website``-GET Parameters and set them to a cookie.


Easy parameter passthrough
~~~~~~~~~~~~~~~~~~~~~~~~~~

The SmartLink Technology makes it easy to pass parameters to your application no matter if the application is embedded
via iframe or into a Facebook Page-Tab.
All GET Parameters passed to your ``smartlink.php`` file will be written to a cookie (Cookie-key ``aa_1234_smartlink``, 1234
is the instance id of your application). When you initialize the app manager object in your application again, then all
parameters will be deleted from the cookie and written to the GET parameter again.

So you don't have to care about that... Pass GET parameters to your smartlink.php file and expect them in your app
target file. :-)

The Smart-Link technology manages redirects for app users depending on their device, language and environment settings.
The Smart-Link should be used for all sharing functionality in your app. It offers an easy way to generate sharing
links.

Here are some use-cases:


iframe Embeds
~~~~~~~~~~~~~

A user uses your app, which is embedded in a website via iframe. He invites a friend via Facebook Share Dialog.
The sharing dialog uses the SmartLink. The invited user will be redirected to the webseite your app is embedded in and
not directly to your App Url.


Facebook Fanpage Tabs
~~~~~~~~~~~~~~~~~~~~~

A user uses you app on a Facebook Fanpage Tab. He shares the App on his timeline using the Facebook Share Dialog.
A friend sees this post in his facebook native app (e.g. mobile iOS or Android App) and clicks on it. This user will
be redirected to the mobile version of the app, as Facebook Fanpage Tabs are not available for mobile devices.


Multilanguage Support
~~~~~~~~~~~~~~~~~~~~~

The default language for your app is english, but you offer more languages to your users. One user switches the language
to german. Then he invites a friend. The friend clicks on the invitation link and will see the app as well in german.