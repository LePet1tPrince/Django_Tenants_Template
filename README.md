# Django_Tenants_Template
This is a generic Django project that uses django-tenants to create isolated schemas with authentication. This will be used as the base of any SAAS product where the tenants don't interact with each other.

## Testing and Linting
This project contains a github testing and linting workflow that is triggered on every push and pull request.

## Getting Started


## Common commands
```docker-compose run --rm app sh -c "python manage.py test"``` - run tests
```docker-compose run --rm app sh -c "flake8"``` - run linting
```docker-compose run --rm app sh -c "python manage.py create_public_tenant"``` - Created the public tenant. Necessary to do the first time you spin up the project.