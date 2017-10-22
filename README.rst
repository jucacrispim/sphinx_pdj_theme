PdJ Sphinx Theme
================

This theme is a dark theme for sphinx documentation based on the
read the docs theme.

To install it, use pip:


.. code-block:: sh

  $ pip install sphinx_pdj_theme


To enable it in your project documentation, set the following in
your conf.py file.

.. code-block:: python

   import sphinx_pdj_theme
   html_theme = 'sphinx_pdj_theme'
   htm_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
