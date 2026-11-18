# -*- coding: utf-8 -*-

import os
import re

from pygments.lexers.c_cpp import CLexer
from pygments.token import Comment, Name


class PDJCLexer(CLexer):
    def get_tokens_unprocessed(self, text, **kwargs):
        for offset, token, value in super().get_tokens_unprocessed(text, **kwargs):
            if token is Comment.Preproc:
                match = re.match(r'^(#?[ \t]*(define|ifndef|ifdef)[ \t]+)', value)
                if match:
                    yield offset, token, match[0]
                    end = match.end()
                    if match[2] == 'define':
                        name = re.match(r'[a-zA-Z_]\w*', value[end:])
                        if name:
                            yield offset + end, Name.Constant, name[0]
                            end += name.end()
                    if end < len(value):
                        yield offset + end, Name, value[end:]
                    continue
            yield offset, token, value


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return cur_dir

def get_locale_path():
    return  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')


def setup(app):
    app.add_lexer('c', PDJCLexer)
    app.add_message_catalog('sphinx', get_locale_path())
    app.add_html_theme('sphinx_pdj_theme', get_html_theme_path())
