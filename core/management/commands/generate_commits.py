import random
from datetime import timedelta

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Commit, Repository


class Command(BaseCommand):
    help = 'Generates random commits.'

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        if not user:
            raise CommandError('No user found.')

        now = timezone.now()
        previous_year = now - timedelta(weeks=52)

        # create a repository

        repo = Repository.objects.get_or_create(
            name='The Next Facebook',
            user=user,
        )[0]

        repo.created = previous_year
        repo.save()

        # generate commits from one year previous.
        # clear any existing first

        Commit.objects.filter(repository=repo).delete()

        delta = now - previous_year

        for n in range(delta.days):
            day = previous_year + timedelta(days=n)

            # with probability 0.5 skip making any commits
            if random.uniform(0, 1) > 0.5:
                continue

            # create random number of commits for this day
            num_commits = random.randint(1, 10)
            for _ in range(num_commits):
                Commit.objects.create(
                    user=user,
                    repository=repo,
                    created=day,
                    code='print("Hello world!")'
                )
