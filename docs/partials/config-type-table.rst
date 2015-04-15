.. note:: ``data_*`` parameters are different for each config type. The following table will list all parameters
          for all config types.

+---------------+-----------------------------------+---------------------------------------------------------+
| Config-Type   | Parameter                         | Description                                             |
+===============+===================================+=========================================================+
| checkbox      | - ``string`` data_caption_off     | - Caption for the 'Off'-value                           |
|               | - ``string`` data_caption_on      | - Caption for the 'On'-value                            |
|               | - ``string`` data_label           | - Label for the checkbox                                |
+---------------+-----------------------------------+---------------------------------------------------------+
| color         |                                   |                                                         |
+---------------+-----------------------------------+---------------------------------------------------------+
| css           | - ``enum`` data_compiler          | - [css | less] Compiler to process the value with       |
+---------------+-----------------------------------+---------------------------------------------------------+
| date          |                                   |                                                         |
+---------------+-----------------------------------+---------------------------------------------------------+
| image         | - ``string`` data_alt             | - HTML image alt attribute                              |
|               | - ``string`` data_title           | - HTML image title attribute                            |
|               | - ``int`` data_height             | - Forced image height (when set, image will be cropped) |
|               | - ``int`` data_min_height         | - Minimal allowed height value for this image           |
|               | - ``int`` data_max_height         | - Max. allowed height value for this image              |
|               | - ``int`` data_width              | - Forced image width (when set, image will be cropped)  |
|               | - ``int`` data_min_width          | - Minimal allowed width value for this image            |
|               | - ``int`` data_max_width          | - Max. allowed width value for this image               |
|               | - ``array`` data_format           | - [jpg | png | gif ] Array of accepted image formats    |
|               | - ``bool`` data_nullable          | - Image value can be NULL or not                        |
+---------------+-----------------------------------+---------------------------------------------------------+
| text          | - ``string`` data_type            | - HTML5 input data type                                 |
|               | - ``string`` data_placeholder     | - HTML5 placeholder attribute                           |
|               | - ``string`` data_pattern         | - RegExp for input validation. Defines an input mask    |
|               | - ``int`` data_min                | - Minimum value (validation for data_type "number")     |
|               | - ``int`` data_max                | - Maximum value (validation for data_type "number")     |
|               | - ``int`` data_min_length         | - Min. number of characters                             |
|               | - ``int`` data_max_length         | - Max. number of characters                             |
+---------------+-----------------------------------+---------------------------------------------------------+
| textarea      | - ``enum`` data_editor            | - [wysiwyg, code, none] Rendered frontend editor        |
|               | - ``bool`` data_code_view         | - Code view allowed in the frontend                     |
+---------------+-----------------------------------+---------------------------------------------------------+
| select        |                                   |                                                         |
+---------------+-----------------------------------+---------------------------------------------------------+
| multiselect   |                                   |                                                         |
+---------------+-----------------------------------+---------------------------------------------------------+
