import pytest
from subprocess import check_output


@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """Test command load"""
    out = check_output(
        ["dundie", "load", "tests/assets/people.csv"]
    ).decode().split("\n")
    assert len(out) == 2
