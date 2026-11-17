from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

from faker import Faker

fake_uz = Faker('uz_UZ')
fake_ru = Faker('ru_RU')
fake_en = Faker()

User = get_user_model()




class Command(BaseCommand):

    help = "Create users with random data"

    def add_arguments(self, parser):

        parser.add_argument(
            "--count",
            type=int,
            default=10,
            help="Number of users to create"
        )

    def handle(self, *args, **options):

        count = options["count"]
        
        
        for i in range(count):
            username = fake_en.user_name()
            email = fake_en.email()
            bio = fake_en.text()
            bio_en = fake_en.text()
            
            biog_en = fake_en.text()
            biog_ru = fake_ru.text()
            biog_uz = fake_uz.text()
            User.objects.create_user(
                username=username,
                email=email,
                password="defaultpassword",
                bio_en = biog_en,
                bio_ru = biog_ru,
                bio_uz = biog_uz,
                bio = biog_en
                
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created user: {username}")
            )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {count} users")
        )