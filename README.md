PdJ Sphinx Theme
================

This theme is a theme for sphinx documentation based on the
read the docs theme.

It supports light and dark modes first using ``prefers-color-scheme`` with an option
to change the mode. If changed the decision will be remembered.

To install it, use pip:

```
$ pip install sphinx_pdj_theme
```

To enable it in your project documentation, set the following in
your conf.py file.

```python
import sphinx_pdj_theme
html_theme = 'sphinx_pdj_theme'
htm_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
```

Logo and favicon
-----------------

To change the logo and the favicon use the following options:

```python
html_logo = 'path/to/logo.svg'
html_favicon = 'path/to/favicon.ico'
```

To set the logo's width and height use the ``logo_width`` and `logo_height`
theme options


```python
html_theme_options = {
    'logo_width': '200px',
    'logo_height': '150px',
}
```

Other options
-------------

To hide the search bar set the `search` option to `hide`

```python
html_theme_options = {
	'search': 'hide'
}
```

To hide the name of the project above the search bar set the `home_link` option
to `hide`

```python
html_theme_options = {
	'home_link': 'hide'
}
```

To include a navigation to the homepage in the sidebar, set the `home_menu_item` option
to `show`

```python
html_theme_options = {
	'home_menu_item': 'show'
}
```

By default the label of the navigation item will be the project name. To change it
set the `home_menu_item_label` option:

```python
html_theme_options = {
	'home_menu_item': 'show',
	'home_menu_item_label': 'Home',
}




Screenshots
-----------
![defaulf](https://raw.githubusercontent.com/jucacrispim/sphinx_pdj_theme/master/default.jpg)
![darker](https://raw.githubusercontent.com/jucacrispim/sphinx_pdj_theme/master/darker.jpg)
