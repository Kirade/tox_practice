from sample.views import sample


def test_sample():
    assert sample() == 1


def test_sample_fails():
    assert sample() == 2
