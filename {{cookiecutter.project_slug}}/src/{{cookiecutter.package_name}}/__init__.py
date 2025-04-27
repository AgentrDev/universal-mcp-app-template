# Jinja template: {{cookiecutter.project_slug}}/src/{{cookiecutter.package_name}}/__init__.py
"""
{{ cookiecutter.project_name }}

A Universal MCP Application.
"""
__version__ = "{{ cookiecutter.version }}"

from .app import {{ cookiecutter.app_class_name }}

__all__ = ["{{ cookiecutter.app_class_name }}"]