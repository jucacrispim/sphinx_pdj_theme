PdJ Sphinx Theme
================

This theme is a dark theme for sphinx documentation based on the
read the docs theme.

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

You can also have a darker appearence by setting the following in your conf.py
file.

```python
import sphinx_pdj_theme
html_theme = 'sphinx_pdj_theme'
htm_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

# sets the darker appearence
html_theme_options = {
    'style': 'darker'
}

```

Screenshots
-----------
![defaulf](https://raw.githubusercontent.com/jucacrispim/sphinx_pdj_theme/master/default.jpg)
![darker](https://raw.githubusercontent.com/jucacrispim/sphinx_pdj_theme/master/darker.jpg)
