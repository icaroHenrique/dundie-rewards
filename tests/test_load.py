import pytest

from dundie.core import load

from .constants import PEOPLE_FILE

EXPECTED_NAMES = ["Jim Halpert", "Dwight Schrute"]
EXPECTED_DEPTS = ["Sales"]
EXPECTED_ROLES = ["Salesman", "Manager"]
EMAIL_DOMAIN = "dundlermifflin.com"


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test loaded data conforms with loaded file"""
    result = load(PEOPLE_FILE)  # load people.csv as a list of csv lines
    assert len(result) == 2
