SDK - SmartLink
===============

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