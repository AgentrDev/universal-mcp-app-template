from unittest.mock import MagicMock

import pytest

from {{ cookiecutter.project_slug }}.app import {{ cookiecutter.app_class_name }}

@pytest.fixture
def app_instance():
    """Provides a {{ cookiecutter.app_class_name }} instance for tests."""
    mock_integration = MagicMock()
    mock_integration.get_credentials.return_value = {"access_token": "dummy_access_token"}

    return {{ cookiecutter.app_class_name }}(integration=mock_integration)

def test_{{ cookiecutter.project_slug }}_app_initialization(app_instance):
    """
    Test that the {{ cookiecutter.app_class_name }} instance is initialized correctly with a name.
    """
    assert hasattr(app_instance, 'name'), "Application instance should have a 'name' attribute."
    assert isinstance(app_instance.name, str), "Application name should be a string."
    assert app_instance.name.strip() != "", "Application name should not be empty."
    assert app_instance.name == "{{ cookiecutter.app_name }}", "{{ cookiecutter.app_class_name }} instance has unexpected name."


def test_{{ cookiecutter.project_slug }}_tool_docstrings_format(app_instance):
    """
    Test that each tool method in {{ cookiecutter.app_class_name }} has a well-formatted docstring,
    including summary, Args, Returns, and Tags sections.
    Checks for Raises section optionally.
    """
    tools = app_instance.list_tools()
    assert isinstance(tools, list), "list_tools() should return a list."
    assert len(tools) > 0, "list_tools() should return at least one tool."

    for tool in tools:
        tool_name = getattr(tool, '__name__', 'Unknown Tool')
        docstring = tool.__doc__
        assert docstring is not None, f"Tool '{tool_name}' is missing a docstring."
        assert isinstance(docstring, str), f"Docstring for '{tool_name}' should be a string."

        lines = docstring.strip().split('\n')
        assert len(lines) > 0, f"Docstring for '{tool_name}' is empty after stripping whitespace."

        # Check for summary line (first non-empty line)
        summary_line = lines[0].strip()
        assert summary_line != "", f"Docstring for '{tool_name}' is missing a summary line."

        # Check for specific sections (case-insensitive and strip whitespace)
        docstring_lower = docstring.lower()
        assert "args:" in docstring_lower, f"Docstring for '{tool_name}' is missing 'Args:' section."
        assert "returns:" in docstring_lower, f"Docstring for '{tool_name}' is missing 'Returns:' section."
        assert "raises:" in docstring_lower, f"Docstring for '{tool_name}' is missing 'Raises:' section."
        assert "tags:" in docstring_lower, f"Docstring for '{tool_name}' is missing 'Tags:' section."


def test_{{ cookiecutter.project_slug }}_tools_are_callable(app_instance):
    """
    Test that each tool method returned by list_tools in {{ cookiecutter.app_class_name }} is callable.
    """
    tools = app_instance.list_tools()
    assert isinstance(tools, list), "list_tools() should return a list."

    for tool in tools:
        tool_name = getattr(tool, '__name__', 'Unknown Tool')
        assert callable(tool), f"Tool '{tool_name}' is not callable."