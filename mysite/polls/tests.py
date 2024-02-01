import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_in_future(self):
        """
        was_published_recently() should return False for Questions posted in the future.

        """
        time = timezone.now() + datetime.timedelta(days=30)
        fq = Question(pub_date=time)
        self.assertIs(fq.was_published_recently(),False)
