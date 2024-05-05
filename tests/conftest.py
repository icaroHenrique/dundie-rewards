import pytest
MARKER = """\
integration: Mark integration tests
unit: Mark unit tests
high: High Prioriry
medium: Medium Prioriry
low: Low Prioriry
"""

def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line('markers', line)


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield
