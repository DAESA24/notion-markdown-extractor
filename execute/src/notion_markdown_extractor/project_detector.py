"""Project directory detection for auto-organization."""

from pathlib import Path
from typing import Optional


class ProjectDetector:
    """Detects if running in a Software or Thought Project directory."""

    PROJECT_MARKERS = ["Software Projects", "Thought Projects"]

    def __init__(self, cwd: Optional[Path] = None):
        """
        Initialize with current working directory.

        Args:
            cwd: Current working directory (defaults to Path.cwd())
        """
        self.cwd = cwd or Path.cwd()

    def is_project_directory(self) -> bool:
        """
        Check if current directory is within a project structure.

        Checks if the current working directory path contains either
        "Software Projects" or "Thought Projects" as a parent directory.

        Returns:
            True if in Software Projects or Thought Projects, False otherwise
        """
        cwd_str = str(self.cwd.resolve())
        return any(marker in cwd_str for marker in self.PROJECT_MARKERS)

    def should_use_auto_directory(self, explicit_output: bool) -> bool:
        """
        Determine if auto-directory feature should activate.

        The auto-directory feature creates user-context/notion-pages/ and
        saves extracted Notion pages there automatically.

        Logic:
        1. If user provided explicit --output path, don't use auto (return False)
        2. If in a project directory, use auto (return True)
        3. As fallback, use auto everywhere (return True)

        Args:
            explicit_output: True if user provided --output flag

        Returns:
            True if should use auto-directory, False otherwise
        """
        # Always defer to explicit user choice
        if explicit_output:
            return False

        # Primary: Use auto-directory in project directories
        if self.is_project_directory():
            return True

        # Fallback: Use auto-directory everywhere
        return True
