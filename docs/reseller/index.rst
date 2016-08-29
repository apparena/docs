Reseller guide
==============

As a reseller you can create your own Whitelabel Web-App-Store running under your own domain. To setup a store and to
integrate the store into your processes there is some information, which makes it easier for you to integrate.
Read about it on this page.


Let customer's create free demos
--------------------------------

That's an easy one. Just link to `https://www.yourstoredomain.com/app/create?templateId=123&templateName=App-Name`

+--------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter    | type              | description                                                                                                                                                         |
+==============+===================+=====================================================================================================================================================================+
| templateId   | (required) int    | ID of the template you want the customer to crete an app of                                                                                                         |
+--------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| templateName | (optional) string | Name of the template you want to be displayed in the header of the app creation screen. If you leave this field emplty, then the default template name will be used |
+--------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

When a customer clicks on that link, then he will be asked to register or login. After that he will be redirected to
the app creation page.