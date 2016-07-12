API - Config data
=================

Config values have a mandatory field 'type' which determines what kind of data is stored. When creating a config value in
a project (-version) or updating (overwriting) it in a template or app, the 'value' field gets validated based on the contents of
the 'type' field. This table shows the data types and what to keep in mind using them.

+---------------+-----------------------------------+-------------------------------------------+
| Config-Type   | Valid input                       | Description                               |
+===============+===================================+===========================================+
| checkbox      | - ``mixed`` boolean values:       | * Simple Checkbox which can be checked or |
|               | - 1, 0, "1", "0", true, false     | * unchecked                               |
|               |                                   |                                           |
+---------------+-----------------------------------+-------------------------------------------+
| color         | - ``string`` Hex value:           | - Sets a color in Hex format              |
|               | - #FFFFFF - #000000               |                                           |
+---------------+-----------------------------------+-------------------------------------------+
| css           | - ``string`` CSS contents         | - CSS content optionally with variables   |
|               |                                   | - (config values)                         |
+---------------+-----------------------------------+-------------------------------------------+
| date          | - ``string`` Date in UNIX format: | - Y = Year, m = Month, d = Day, H = Hour, |
|               | - "Y-m-d H:i:s"                   | - i = Minute, s = Second                  |
+---------------+-----------------------------------+-------------------------------------------+
| HTML          |                                   |                                           |
|               |                                   |                                           |
+---------------+-----------------------------------+-------------------------------------------+
| image         | - ``string`` URI to an image      | - Points to the location of an image      |
|               | - e.g.: www.example.com/logo.jpg  |                                           |
+---------------+-----------------------------------+-------------------------------------------+
| input         | - ``string`` any string           | - Can be any string the user inputs e.g.  |
|               |                                   | - a custom name                           |
+---------------+-----------------------------------+-------------------------------------------+
| select        | - ``string`` any value contained  | - Allows the user to select one item out  |
|               | - in the 'options' field in the   | - of a list. The list is defined in the   |
|               | - meta data                       | - meta-field 'options' of the config value|
|               |                                   | - (see explanation below).                |
+---------------+-----------------------------------+-------------------------------------------+
| multiselect   | - ``string`` multiple values      | - Similar to 'select' but the user can    |
|               | - contained in the 'options'      | - select multiple items                   |
|               | - field in the meta data          |                                           |
+---------------+-----------------------------------+-------------------------------------------+

