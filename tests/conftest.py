"""
This module configures pytest for the calculator project.

It adds a custom command-line option (--num_records) to generate dynamic test data
using the Faker library. The test data consists of random numbers and operations
(add, subtract, multiply, divide) for automated testing.

"""

import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    """
    Add a custom pytest command-line option.

    This function allows the user to specify the number of test records to generate
    using the `--num_records` argument when running pytest.

    Args:
        parser (pytest.Parser): The pytest parser to add custom options.
    """
    parser.addoption(
        "--num_records",
        action="store",
        default=10,
        type=int,
        help="Number of test cases to generate"
    )

@pytest.fixture(scope="session")
def test_data(request):
    """
    Generate dynamic test data for pytest using Faker.

    This fixture generates a list of test cases based on the user-specified
    number of records from the `--num_records` option.

    Args:
        request (pytest.FixtureRequest): The request object to access test options.

    Returns:
        list: A list of tuples containing (a, b, operation, expected_result).
    """
    num_records = request.config.getoption("--num_records")
    test_cases = []
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
        expected_result = None  # Expected result logic to be implemented
        test_cases.append((a, b, operation, expected_result))

    return test_cases
