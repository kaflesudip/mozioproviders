Installing and Testing Locally
==============================

1. Create a new virtualenv under Python 3.
2. Clone this repository into your local computer.
3. Activate the virtualenv.
4. Run `pip install -r requirements/local.txt`
5. Make sure that you have created a postgresql database for this project. You also need to install PostGIS extension. Please refer to [GeoDjango Documentation](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/install/) for more details.
6. Edit `env.example` file with you database credentials and save it as `.env`.
7. Migrate your database using `python manage.py migate`
8. Run all tests using `python manage.py test`

This project is created using [Django Cookiecutter](https://github.com/pydanny/cookiecutter-django) template. Refer to its documentation on more infomation on setting up environment, running locally and on production.