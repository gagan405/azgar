# azgar

A simple flask based server to generate PDF/HTML from given templates and data.

## Setup

### Create virtualenv

* `pip install virtualenv`
* `virtualenv venv`
* `source venv/bin/activate`

More details here: https://docs.python-guide.org/dev/virtualenvs/

On MacOS, installation of Weasyprint might create troubles. The below could solve it.
More here: https://stackoverflow.com/questions/37437041/dlopen-failed-to-load-a-library-cairo-cairo-2

~~~
brew install cairo pango gdk-pixbuf libxml2 libxslt libffi

export DYLD_FALLBACK_LIBRARY_PATH=$DYLD_FALLBACK_LIBRARY_PATH:/usr/local/lib
~~~

## Setup on PyCharm

### Run Configurations

* Script path : `/path/to/virtualenv/bin/flask`
* Parameter : `run`
* Environment variables : `FLASK_APP=azgar;LANG=en_US.UTF-8`



