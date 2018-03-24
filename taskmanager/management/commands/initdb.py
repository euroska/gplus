from django.core.management.base import BaseCommand, CommandError
from ...models import User


class Command(BaseCommand):
    help = 'Init base user'

    def handle(self, *args, **options):
        admin, create = User.objects.get_or_create(username='admin')
        test, create = User.objects.get_or_create(username='test')

        admin.is_superadmin = True
        admin.setPassword('admin')
        admin.save()

        test.is_superadmin = False
        test.setPassword('test')
        test.save()

        self.stdout.write(self.style.SUCCESS('Successfully inicialize users'))
