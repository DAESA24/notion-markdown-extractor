"""Project directory detection for auto-organization."""

from pathlib import Path
from typing import Optional


class ProjectDetector:
    """Determines when to use auto-directory organization."""

    def __init__(self, cwd: Optional[Path] = None):
        """
        Initialize with current working directory.

        Args:
            cwd: Current working directory (defaults to Path.cwd())
        """
        self.cwd = cwd or Path.cwd()

    def should_use_auto_directory(self, explicit_output: bool) -> bool:
        """
        Determine if auto-directory feature should activate.

        Auto-directory saves extracted pages to user-context/notion-pages/
        in the current working directory.

        Args:
            explicit_output: True if user provided --output flag

        Returns:
            True to use auto-directory, False to use explicit path
        """
        return not explicit_output
