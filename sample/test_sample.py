from django.test import TestCase

from sample.views import sample


class SampleTestCase(TestCase):

    def test_sample(self):
        assert sample() == 1


def test_sample():
    assert sample() == 1
