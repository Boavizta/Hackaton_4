from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "boagent"
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "Boagent is a local API and monitoring agent to help you estimate the environmental impact of your machine, including software activity and hardware embodied impacts."
    TAGS_METADATA: list = [
        {"name": "info", "description": "Returns runtime configuration of Boagent."},
        {"name": "web", "description": "Web UI to explore Boagent metrics."},
        {
            "name": "csv",
            "description": "Internal route. Generates and returns a CSV-formatted dataset with metrics needed by the webUI",
        },
        {
            "name": "metrics",
            "description": "Returns metrics as a Prometheus HTTP exporter.",
        },
        {
            "name": "query",
            "description": "This is the main route. Returns metrics in JSON format.",
        },
    ]
    seconds_in_one_year: int = 31536000
    default_lifetime: float = os.getenv("DEFAULT_LIFETIME", 5.0)
    hardware_file_path: str = os.getenv("HARDWARE_FILE_PATH", "./hardware_data.json")
    power_file_path: str = os.getenv("POWER_FILE_PATH", "./power_data.json")
    hardware_cli: str = os.getenv("HARDWARE_CLI", "../hardware/hardware_cli.py")
    boaviztapi_endpoint: str = os.getenv("BOAVIZTAPI_ENDPOINT", "http://localhost:5000")
    db_path: str = os.getenv("BOAGENT_DB_PATH", "../../db/boagent.db")
    public_path: str = os.getenv("BOAGENT_PUBLIC_PATH", "../public")
    assets_path: str = os.getenv("BOAGENT_ASSETS_PATH", "../public/assets")
    carbon_aware_api_endpoint: str = os.getenv(
        "CARBON_AWARE_API_ENDPOINT", "https://carbon-aware-api.azurewebsites.net"
    )
    carbon_aware_api_token: str = os.getenv("CARBON_AWARE_API_TOKEN")
    azure_location: str = os.getenv("AZURE_LOCATION", "northeurope")

    class Config:
        env_file = ".env"


settings = Settings()
