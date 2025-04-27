# Jinja template: {{cookiecutter.project_slug}}/src/{{cookiecutter.package_name}}/app.py
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class {{cookiecutter.app_class_name}}(APIApplication):
    """
    Base class for Universal MCP Applications.
    """
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="{{ cookiecutter.app_name }}", integration=integration, **kwargs)

    def run(self):
        """
        Example tool implementation.
        """
        print(f"Running the main task for {self.name}...")
        print("Hello from {{ cookiecutter.app_class_name }}!")
        return "Task completed successfully."

    def list_tools(self):
        """
        Lists the available tools (methods) for this application.
        """
        return [self.run]
