from django.core.management.base import BaseCommand
from ...models import Client, Domain

class Command(BaseCommand):
    help = 'Create a public tenant'

    def handle(self, *args, **kwargs):
        tenant = Client(schema_name='public',
                        name='Schemas Inc.',
                        paid_until='2016-12-05',
                        on_trial=False)
        tenant.save()

        domain = Domain()
        domain.domain = 'localhost'  # use 'localhost' for local development
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()

        self.stdout.write(self.style.SUCCESS('Successfully created public tenant'))