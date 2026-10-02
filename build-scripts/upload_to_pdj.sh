#!/bin/bash

cd dist

fname=`ls | grep tar`
project_name=sphinx_pdj_theme

curl -F file=@$fname -F prefix=$project_name https://pypi.poraodojuca.dev/u/ -H "Authorization: Key $PYPI_AUTH_KEY"
