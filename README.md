# Django_Tenants_Template
This is a generic Django project that uses django-tenants to create isolated schemas with authentication. This will be used as the base of any SAAS product where the tenants don't interact with each other.

## Testing and Linting
This project contains a github testing and linting workflow that is triggered on every push and pull request.

## Getting Started


## Common commands
```docker-compose run --rm app sh -c "python manage.py test"``` - run tests

```docker-compose run --rm app sh -c "flake8"``` - run linting

```docker-compose run --rm app sh -c "python manage.py create_public_tenant"``` - Created the public tenant. Necessary to do the first time you spin up the project.

```docker-compose up --build``` - spin up the project and build it.

```docker volume rm django_tenants_template_dev-db-data``` - Reset the volume.

To reformat the project and full start over, run
```docker-compose down```
```docker volume rm django_tenants_template_dev-db-data```
Delete any migrations files in any apps (don't delete the migrations file itself of the __init__.py file)
```docker-compose build```
```docker-compose run --rm app sh -c "python manage.py create_public_tenant"```
```docker-compose up```
