"""File storage and image download management."""

import os
import re
import hashlib
import requests
from pathlib import Path
from typing import Optional
from PIL import Image
from io import BytesIO


class Storage:
    """Handles markdown file saving and image downloads."""

    def __init__(self):
        """Initialize storage manager."""
        pass

    def save_markdown(self, content: str, output_path: str) -> str:
        """
        Save markdown content to file with UTF-8 encoding.

        Args:
            content: Markdown content string
            output_path: Path to output file

        Returns:
            Absolute path to saved file

        Raises:
            IOError: If file cannot be written
        """
        output_file = Path(output_path)

        # Create parent directories if they don't exist
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Write file with UTF-8 encoding (critical for Windows)
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            raise IOError(f"Failed to write markdown file: {e}")

        return str(output_file.absolute())

    def sanitize_filename(self, title: str) -> str:
        """
        Convert page title to safe filename in kebab-case.

        Args:
            title: Page title string

        Returns:
            Sanitized filename (kebab-case)

        Examples:
            "My Page Title!" -> "my-page-title"
            "Hello   World" -> "hello-world"
            "Revenue Growth: Q4 2024" -> "revenue-growth-q4-2024"
        """
        # Convert to lowercase
        filename = title.lower()

        # Replace spaces and underscores with hyphens
        filename = re.sub(r'[\s_]+', '-', filename)

        # Remove any characters that aren't alphanumeric or hyphens
        filename = re.sub(r'[^a-z0-9\-]', '', filename)

        # Remove multiple consecutive hyphens
        filename = re.sub(r'-+', '-', filename)

        # Remove leading/trailing hyphens
        filename = filename.strip('-')

        # Ensure we have a valid filename
        if not filename:
            filename = "untitled"

        return filename

    def get_output_path(
        self,
        page_title: str,
        output_dir: Optional[str] = None,
        custom_filename: Optional[str] = None
    ) -> str:
        """
        Generate output path from page title and optional directory.

        Args:
            page_title: Page title to convert to filename
            output_dir: Optional output directory (defaults to current directory)
            custom_filename: Optional custom filename (overrides page_title)

        Returns:
            Full output path with .md extension
        """
        # Use custom filename or sanitize page title
        if custom_filename:
            base_name = custom_filename
            # Remove .md extension if present (we'll add it)
            if base_name.endswith('.md'):
                base_name = base_name[:-3]
        else:
            base_name = self.sanitize_filename(page_title)

        # Add .md extension
        filename = f"{base_name}.md"

        # Determine output directory
        if output_dir:
            output_path = Path(output_dir) / filename
        else:
            output_path = Path.cwd() / filename

        return str(output_path)

    def create_image_directory(self, output_path: str) -> Path:
        """
        Create images/ subdirectory relative to output markdown file.

        Args:
            output_path: Path to the markdown file

        Returns:
            Path to images directory
        """
        output_file = Path(output_path)
        images_dir = output_file.parent / "images"

        # Create directory if it doesn't exist
        images_dir.mkdir(parents=True, exist_ok=True)

        return images_dir

    def download_image(
        self,
        image_url: str,
        output_path: str,
        alt_text: str = ""
    ) -> Optional[str]:
        """
        Download image from URL and save to images/ subdirectory.

        Args:
            image_url: URL of the image to download
            output_path: Path to the markdown file (images saved relative to this)
            alt_text: Alt text for the image (used for filename if available)

        Returns:
            Relative path to downloaded image for markdown reference,
            or None if download failed

        Raises:
            Exception: If download or save fails
        """
        try:
            # Create images directory
            images_dir = self.create_image_directory(output_path)

            # Generate filename from alt text or URL hash
            if alt_text:
                base_name = self.sanitize_filename(alt_text)
            else:
                # Use hash of URL for unique filename
                url_hash = hashlib.md5(image_url.encode()).hexdigest()[:12]
                base_name = f"image-{url_hash}"

            # Download image
            response = requests.get(image_url, timeout=30)
            response.raise_for_status()

            # Verify it's an image and get extension
            try:
                img = Image.open(BytesIO(response.content))
                extension = img.format.lower()
                if extension == 'jpeg':
                    extension = 'jpg'
            except Exception:
                # Fallback: guess from URL
                extension = self._guess_extension(image_url)

            # Create full filename with extension
            filename = f"{base_name}.{extension}"
            image_path = images_dir / filename

            # Handle filename collisions
            counter = 1
            while image_path.exists():
                filename = f"{base_name}-{counter}.{extension}"
                image_path = images_dir / filename
                counter += 1

            # Save image
            with open(image_path, 'wb') as f:
                f.write(response.content)

            # Return relative path for markdown
            return f"./images/{filename}"

        except Exception as e:
            # Log error but don't crash - return None to indicate failure
            print(f"[WARNING] Failed to download image from {image_url}: {e}")
            return None

    def _guess_extension(self, url: str) -> str:
        """
        Guess image extension from URL.

        Args:
            url: Image URL

        Returns:
            File extension (png, jpg, gif, webp, etc.)
        """
        # Common image extensions
        for ext in ['png', 'jpg', 'jpeg', 'gif', 'webp', 'svg', 'bmp']:
            if ext in url.lower():
                return 'jpg' if ext == 'jpeg' else ext

        # Default to png
        return 'png'

    def ensure_directory(self, path: str) -> Path:
        """
        Ensure directory exists, creating if necessary.

        Args:
            path: Directory path

        Returns:
            Path object for the directory
        """
        dir_path = Path(path)
        dir_path.mkdir(parents=True, exist_ok=True)
        return dir_path
