{% comment "This comment section will be deleted in the generated project" %}

# [Magic Eye Robot][docs]



**Magic Eye Robot.**

## Features

* Ready Bootstrap-themed pages
* User Registration/Sign up
* Better Security 
* Logging/Debugging Helpers
* Works on Python 3 and Django 2 as Back-end
* Formatted with [Black](https://github.com/chakertriangle)


## Quick start:

1. `$ django-admin.py startproject --template=https://github.com/arocks/edge/archive/master.zip --extension=py,md,html,env my_proj`
2. `$ cd Magic_Eye`
3. `$ pip install -r requirements.txt `
4. `$ cd src`
5. `$ cp Magic_Eye/settings/local.sample.env Magic_Eye/settings/local.env`
6. `$ python manage.py migrate`

More information at: [http://django-edge.readthedocs.org/][docs] ✨ 🍰 ✨

[docs]: http://django-edge.readthedocs.org/


## Recommended Installation (with `pipenv`)
1. `$ pip install --user --upgrade pipenv` ([Install pipenv system-wide or locally](https://docs.pipenv.org/) but outside a virtualenv)
2. `$ mkdir my_proj` (choose a better name than `myDjangoPro3` for your project)

3. `$ pipenv install --dev`
4. `$ pipenv shell`
5. `$ cp src/myDjangoPro3/settings/local.sample.env src/my_proj/settings/local.env` (or rename this file)
6. `$ cd src`
7. `$ python manage.py migrate`
8. `$ python manage.py createsuperuser`
9. `$ python manage.py runserver`

Rest of this README will be copied to the generated project.

--------------------------------------------------------------------------------------------

{% endcomment %}

# {{ Magic Eye }}

{{ Magic Eye }} is a _short description_. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* App1 (which decide the allowed persons)
* App2 (which monitor all visitors)
* 

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv {{ project_name }}`
    2. `$ . {{ project_name }}/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
