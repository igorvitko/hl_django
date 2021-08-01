from django.core.management.base import BaseCommand
from faker import Faker

from hello.models import Question as Poll


class Command(BaseCommand):
    help = 'Adding questions in polls'

    def add_arguments(self, parser):
        parser.add_argument('-q', '--quantity', type=int, default=10, help="enter needs quantity of questions")

    def handle(self, *args, **options):
        fake = Faker('ru-RU')

        self.stdout.write('Start inserting questions')
        for _ in range(options['quantity']):
            poll = Poll()

            poll.question_text = fake.sentence(nb_words=4, variable_nb_words=True).replace(".", "?")
            poll.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully inserted {options['quantity']} polls"))
