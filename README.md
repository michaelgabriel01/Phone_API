work_at_olist
=============

Work_at_Olist challenge project

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Description
-----------

My solution for the OLIST challenge found at (https://github.com/olist/work-at-olist/blob/master/README.md). This application receives call detail records and calculates monthly bills for a given telephone number.

I'm gonna implement three (3) separated APIs To solve the problem and package them together
===========================================================================================

CallApi
=======

This API is capable of displaying the 'Receive telephone call detail records'. Such as Call Start Record information, which include: record type, record timestamp, call identifier, origin phone number, destination phone number.

BillApi
=======

This API can get the 'Get telephone bill information'. For example, the call destination, call start date, call start time, call duration (hour, minute and seconds), and call price.

PriceApi
========

This API can show the 'Pricing rules'. Like fixed charges, tarifs time, standard charge, discount charge, Reduced tariff time call, Standing charge, Call charge/minute, and Call charge/month

Settings
--------

Installation
-----------
First clone the project.
Then, go ahead and use the following commands   # Must come back Michael to finish here
```console
cd work-at-olist/
virtualenv env -p python3
source env/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
python manage.py migrate
python manage.py loaddata fixture_tax.json
```

Test
----
python manage.py test apps


Environment
===========

|   |    |
|---|---|
|  Computer |   Sony Vaio CORE i5|
|  O.S| Ubuntu 18.04lts  |
|  Editor | SublimeText  |
|  Django version| 2.0.6  |
|  Python version | 3.6.5  |
|  djangorestframework version | 3.8.2 |

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html




