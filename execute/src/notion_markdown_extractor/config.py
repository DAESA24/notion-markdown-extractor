"""Configuration management for Notion API token storage."""

import os
import yaml
from pathlib import Path
from typing import Optional


class Config:
    """Manages Notion API token configuration."""

    CONFIG_DIR = Path.home() / ".notion-md"
    CONFIG_FILE = CONFIG_DIR / "config.yaml"

    def __init__(self):
        """Initialize config manager."""
        self.config_dir = self.CONFIG_DIR
        self.config_file = self.CONFIG_FILE

    def save_token(self, token: str) -> None:
        """
        Save Notion API token to config file.

        Args:
            token: Notion integration token
        """
        # Create config directory if it doesn't exist
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # Prepare config data
        config_data = {
            "notion": {
                "api_token": token,
                "version": "2022-06-28"
            },
            "settings": {
                "default_output_dir": "./notion-exports",
                "filename_format": "kebab-case",
                "encoding": "utf-8"
            }
        }

        # Write config file with UTF-8 encoding
        with open(self.config_file, 'w', encoding='utf-8') as f:
            yaml.dump(config_data, f, default_flow_style=False)

        # Set restrictive permissions (owner read/write only)
        if os.name != 'nt':  # Unix-like systems
            os.chmod(self.config_file, 0o600)

    def load_token(self) -> Optional[str]:
        """
        Load Notion API token from config file or environment variable.

        Returns:
            API token if found, None otherwise
        """
        # First check environment variable
        env_token = os.getenv("NOTION_API_TOKEN")
        if env_token:
            return env_token

        # Then check config file
        if not self.config_file.exists():
            return None

        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config_data = yaml.safe_load(f)

            return config_data.get("notion", {}).get("api_token")
        except Exception:
            return None

    def token_exists(self) -> bool:
        """
        Check if a token is configured.

        Returns:
            True if token exists, False otherwise
        """
        return self.load_token() is not None

    def get_config_path(self) -> str:
        """
        Get the path to the config file.

        Returns:
            String path to config file
        """
        return str(self.config_file)
