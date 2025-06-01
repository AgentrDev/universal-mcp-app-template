from unittest.mock import MagicMock

import pytest
from universal_mcp.utils.testing import (
    check_application_instance,
)

from {{ cookiecutter.project_slug }}.app import {{ cookiecutter.app_class_name }}

@pytest.fixture
def app_instance():
    mock_integration = MagicMock()
    mock_integration.get_credentials.return_value = {"access_token": "dummy_access_token"}
    return {{ cookiecutter.app_class_name }}(integration=mock_integration)

def test_application(app_instance):
    check_application_instance(app_instance, app_name="{{ cookiecutter.app_name }}")
