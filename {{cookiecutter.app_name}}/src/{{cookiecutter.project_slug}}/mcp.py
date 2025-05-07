{% if cookiecutter.integration_type == "none" %}
from universal_mcp.servers import SingleMCPServer

from {{ cookiecutter.project_slug }}.app import {{ cookiecutter.app_class_name }}

app_instance = {{ cookiecutter.app_class_name }}()

mcp = SingleMCPServer(
    app_instance=app_instance
)

if __name__ == "__main__":
    print(f"Starting {mcp.name}...")
    mcp.run()

{% elif cookiecutter.integration_type == "api_key" %}
from universal_mcp.servers import SingleMCPServer
from universal_mcp.integrations import ApiKeyIntegration
from universal_mcp.stores import EnvironmentStore

from {{ cookiecutter.project_slug }}.app import {{ cookiecutter.app_class_name }}

env_store = EnvironmentStore()
integration_instance = ApiKeyIntegration(name="{{ cookiecutter.app_name.upper() }}_API_KEY", store=env_store)
app_instance = {{ cookiecutter.app_class_name }}(integration=integration_instance)

mcp = SingleMCPServer(
    app_instance=app_instance,
)

if __name__ == "__main__":
    mcp.run()

{% elif cookiecutter.integration_type == "agentr" %}
from universal_mcp.servers import SingleMCPServer
from universal_mcp.integrations import AgentRIntegration
from universal_mcp.stores import EnvironmentStore

from {{ cookiecutter.project_slug }}.app import {{ cookiecutter.app_class_name }}

env_store = EnvironmentStore()
integration_instance = AgentRIntegration(name="{{ cookiecutter.app_name.lower() }}", store=env_store)
app_instance = {{ cookiecutter.app_class_name }}(integration=integration_instance)

mcp = SingleMCPServer(
    app_instance=app_instance,
)

if __name__ == "__main__":
    mcp.run()

{% else %}
# If integration_type is invalid
raise ValueError("Invalid integration_type: {{ cookiecutter.integration_type }}")

{% endif %}
