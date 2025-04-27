# Jinja template: {{cookiecutter.project_slug}}/tests/test_app.py
import pytest
from {{ cookiecutter.package_name }}.app import {{ cookiecutter.app_class_name }}

def test_app_instantiation():
    """Test if the main application class can be instantiated."""
    app = {{ cookiecutter.app_class_name }}()
    assert app.name == "{{ cookiecutter.project_name }}"

def test_list_tools():
    """Test if list_tools returns the expected 'run' method."""
    app = {{ cookiecutter.app_class_name }}()
    tools = app.list_tools()
    assert len(tools) >= 1
    for tool in tools:
        assert tool.__doc__ is not None
