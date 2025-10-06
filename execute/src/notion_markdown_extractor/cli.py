"""CLI interface for Notion Markdown Extractor."""

import click
import sys
from typing import Optional
from .config import Config
from .notion_client import NotionClient
from .block_converter import BlockConverter
from .storage import Storage
from .project_detector import ProjectDetector


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """
    Notion Markdown Extractor - Extract Notion pages to Markdown files.

    A CLI tool for extracting Notion pages and converting them to clean Markdown
    format with local image downloads.
    """
    pass


@cli.command()
@click.option(
    '--token',
    required=True,
    help='Notion integration token',
    prompt='Enter your Notion API token',
    hide_input=True
)
def configure(token: str):
    """
    Configure Notion API token for authentication.

    Saves the token to ~/.notion-md/config.yaml for reuse across commands.

    Example:
        notion-md configure --token secret_abc123xyz
    """
    try:
        config = Config()
        config.save_token(token)

        click.echo("[OK] Configuration saved successfully!")
        click.echo(f"Config file: {config.get_config_path()}")
        click.echo("\nYou can now use the 'extract' command to export Notion pages.")

    except Exception as e:
        click.echo(f"[ERROR] Error saving configuration: {e}", err=True)
        raise click.Abort()


@cli.command()
def status():
    """
    Check configuration and API connection status.

    Verifies that the API token is configured and tests connectivity to Notion.

    Example:
        notion-md status
    """
    try:
        config = Config()

        # Check if token exists
        token = config.load_token()

        if not token:
            click.echo("[ERROR] No API token configured")
            click.echo("\nRun 'notion-md configure --token YOUR_TOKEN' to set up authentication")
            raise click.Abort()

        click.echo("[OK] API token configured")
        click.echo(f"Config file: {config.get_config_path()}")

        # Test API connection
        click.echo("\nTesting API connection...")

        try:
            client = NotionClient(token)
            if client.test_connection():
                click.echo("[OK] API connection successful!")
            else:
                click.echo("[ERROR] API connection failed")
                raise click.Abort()

        except Exception as e:
            click.echo(f"[ERROR] API connection failed: {e}", err=True)
            raise click.Abort()

    except click.Abort:
        raise
    except Exception as e:
        click.echo(f"[ERROR] Error checking status: {e}", err=True)
        raise click.Abort()


@cli.command()
@click.argument('page_url')
@click.option(
    '--output',
    '-o',
    default=None,
    help='Output file path (defaults to page title in current directory)'
)
def extract(page_url: str, output: Optional[str]):
    """
    Extract a Notion page to Markdown format.

    Fetches the page content from Notion, converts it to Markdown, and downloads
    any images to a local ./images/ directory.

    Arguments:
        PAGE_URL: The URL of the Notion page to extract

    Examples:
        notion-md extract https://notion.so/My-Page-abc123

        notion-md extract https://notion.so/My-Page-abc123 --output ~/docs/my-page.md
    """
    try:
        # Load configuration
        config = Config()
        token = config.load_token()

        if not token:
            click.echo("[ERROR] No API token configured", err=True)
            click.echo("\nRun 'notion-md configure --token YOUR_TOKEN' first", err=True)
            raise click.Abort()

        # Initialize components
        click.echo("Initializing...")
        client = NotionClient(token)
        storage = Storage()
        converter = BlockConverter(storage=storage)

        # Extract page ID from URL
        click.echo("Parsing page URL...")
        try:
            page_id = client.extract_page_id(page_url)
        except ValueError as e:
            click.echo(f"[ERROR] Invalid Notion URL: {e}", err=True)
            raise click.Abort()

        # Fetch page metadata
        click.echo("Fetching page metadata...")
        try:
            page = client.get_page(page_id)
            page_title = client.get_page_title(page)
            click.echo(f"Page title: {page_title}")
        except Exception as e:
            click.echo(f"[ERROR] Failed to fetch page: {e}", err=True)
            raise click.Abort()

        # Determine output path with auto-directory support
        detector = ProjectDetector()

        if output:
            # User specified explicit output - use it
            output_path = output
            click.echo(f"Output file: {output_path}")
        elif detector.should_use_auto_directory(explicit_output=False):
            # Use auto-directory feature
            output_path = storage.get_auto_output_path(page_title)
            click.echo(f"Auto-organizing to: {output_path}")
        else:
            # Fallback to current behavior (shouldn't reach here with current logic)
            output_path = storage.get_output_path(page_title)
            click.echo(f"Output file: {output_path}")

        # Fetch page blocks
        click.echo("Fetching page content...")
        try:
            blocks = client.get_blocks(page_id, recursive=True)
            click.echo(f"[OK] Retrieved {len(blocks)} blocks")
        except Exception as e:
            click.echo(f"[ERROR] Failed to fetch blocks: {e}", err=True)
            raise click.Abort()

        # Convert to markdown
        click.echo("Converting to Markdown...")
        try:
            markdown_content = converter.convert_blocks_to_markdown(blocks, output_path, page_title)
        except Exception as e:
            click.echo(f"[ERROR] Conversion failed: {e}", err=True)
            raise click.Abort()

        # Save to file
        click.echo("Saving to file...")
        try:
            saved_path = storage.save_markdown(markdown_content, output_path)
            click.echo(f"[OK] Successfully saved to: {saved_path}")

            # Check if images directory was created
            images_dir = storage.create_image_directory(output_path)
            if images_dir.exists() and any(images_dir.iterdir()):
                image_count = len(list(images_dir.iterdir()))
                click.echo(f"Downloaded {image_count} image(s) to {images_dir}")

        except Exception as e:
            click.echo(f"[ERROR] Failed to save file: {e}", err=True)
            raise click.Abort()

        click.echo("\n[SUCCESS] Extraction complete!")

    except click.Abort:
        raise
    except Exception as e:
        click.echo(f"[ERROR] Unexpected error: {e}", err=True)
        raise click.Abort()


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
