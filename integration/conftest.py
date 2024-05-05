MARKER = """\
integration: Mark integration tests
unit: Mark unit tests
high: High Prioriry
medium: Medium Prioriry
low: Low Prioriry
"""

def pytest_configure(config):
    map(lambda line: config.addinivalue_line('markers', line), MARKER.split("\n"))
