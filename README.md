# ensalada_de_frutas

empresa distribuidora de frutas

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy ensalada_de_frutas

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

Primer_Entrega\ensalada_de_frutas\empresa
- Ahí se encuentran los 3 modelos solicitados (models.py).
- También admin.py.
- views.py no fue utilizado finalmente.

Primer_Entrega\ensalada_de_frutas\empresa2
- views.py están las clases utilizadas para crear los formularios para cargar info en cada BD.
- views.py también está la clase searchView (para el formulario de búsqueda).

Primer_Entrega\ensalada_de_frutas\ensalada_de_frutas\templates\empresa2
- Está el template usado de base para todas lás páginas html y home que permite acceder a todos los formularios tanto de ingreso de info como de búsqueda.

Primer_Entrega\ensalada_de_frutas\ensalada_de_frutas\templates\forms
- Están los html de cada formulario de ingreso de info y de búsqueda.

Probar búsqueda con Lechuga, Naranja y Tomate Perita.

ADMIN => si querés acceder te armé un usuario que es Rafael y clave: coder123 (si no entra es Coder123).