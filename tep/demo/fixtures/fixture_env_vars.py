from tep.dao import mysql_engine
from tep.fixture import *


@pytest.fixture(scope="session")
def env_vars(set_env_vars):
    # Environment and variables
    mapping = {
        "qa": {
            "domain": "https://qa.com",
            "mysql_engine": mysql_engine("127.0.0.1",  # host
                                         "2306",  # port
                                         "root",  # username
                                         "123456",  # password
                                         "test"),  # db_name
        },
        "release": {
            "domain": "https://release.com",
            "mysql_engine": mysql_engine("127.0.0.1",
                                         "2306",
                                         "root",
                                         "123456",
                                         "release"),
        }
        # Add your environment and variables
    }
    return set_env_vars(mapping)
