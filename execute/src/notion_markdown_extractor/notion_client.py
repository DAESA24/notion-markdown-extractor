"""Notion API client wrapper for fetching pages and blocks."""

from typing import List, Dict, Any, Optional
from notion_client import Client
from notion_client.errors import APIResponseError
import time


class NotionClient:
    """Wrapper for Notion API client with authentication and fetching logic."""

    def __init__(self, token: str):
        """
        Initialize Notion API client.

        Args:
            token: Notion integration token
        """
        self.client = Client(auth=token)
        self.token = token

    def get_page(self, page_id: str) -> Dict[str, Any]:
        """
        Fetch page metadata and properties.

        Args:
            page_id: Notion page ID

        Returns:
            Page object dictionary

        Raises:
            APIResponseError: If API request fails
        """
        try:
            return self.client.pages.retrieve(page_id=page_id)
        except APIResponseError as e:
            raise Exception(f"Failed to retrieve page: {e.message}")

    def get_blocks(self, block_id: str, recursive: bool = True) -> List[Dict[str, Any]]:
        """
        Fetch all blocks for a page or block, with optional recursive fetching.

        Args:
            block_id: Block or page ID to fetch children from
            recursive: If True, recursively fetch nested blocks

        Returns:
            List of block objects with children populated if recursive=True

        Raises:
            APIResponseError: If API request fails
        """
        all_blocks = []

        try:
            # Fetch first page of blocks
            has_more = True
            start_cursor = None

            while has_more:
                # Handle rate limiting with exponential backoff
                response = self._fetch_blocks_with_retry(block_id, start_cursor)

                blocks = response.get("results", [])

                # If recursive, fetch children for blocks that have them
                if recursive:
                    for block in blocks:
                        if block.get("has_children", False):
                            # Recursively fetch children
                            children = self.get_blocks(block["id"], recursive=True)
                            block["children"] = children

                all_blocks.extend(blocks)

                # Handle pagination
                has_more = response.get("has_more", False)
                start_cursor = response.get("next_cursor")

            return all_blocks

        except APIResponseError as e:
            raise Exception(f"Failed to retrieve blocks: {e.message}")

    def _fetch_blocks_with_retry(
        self,
        block_id: str,
        start_cursor: Optional[str] = None,
        max_retries: int = 3
    ) -> Dict[str, Any]:
        """
        Fetch blocks with exponential backoff retry logic.

        Args:
            block_id: Block or page ID
            start_cursor: Pagination cursor
            max_retries: Maximum number of retry attempts

        Returns:
            API response dictionary

        Raises:
            APIResponseError: If all retries fail
        """
        for attempt in range(max_retries):
            try:
                params = {"block_id": block_id}
                if start_cursor:
                    params["start_cursor"] = start_cursor

                return self.client.blocks.children.list(**params)

            except APIResponseError as e:
                # Handle rate limiting (429) with exponential backoff
                if e.status == 429 and attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                    time.sleep(wait_time)
                    continue

                # Re-raise for other errors or final attempt
                raise

        # This should never be reached due to raise in loop
        raise Exception("Max retries exceeded")

    def test_connection(self) -> bool:
        """
        Test if the API token is valid and connection works.

        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Try to list users (requires minimal permissions)
            self.client.users.me()
            return True
        except Exception:
            return False

    def extract_page_id(self, url: str) -> str:
        """
        Extract page ID from Notion URL.

        Args:
            url: Notion page URL (e.g., https://notion.so/Page-Title-abc123def456)

        Returns:
            Cleaned page ID (32-character hex string)

        Raises:
            ValueError: If URL format is invalid
        """
        # Notion URLs format: https://www.notion.so/{workspace}/{title}-{id}
        # or: https://notion.so/{title}-{id}
        # ID is last 32 characters (without hyphens) in the URL path

        try:
            # Remove query parameters and trailing slashes
            url = url.split('?')[0].rstrip('/')

            # Get last part of URL path
            url_parts = url.split('/')
            last_part = url_parts[-1]

            # ID is typically after last hyphen
            # Format: Page-Title-abc123def456 or just abc123def456
            if '-' in last_part:
                potential_id = last_part.split('-')[-1]
            else:
                potential_id = last_part

            # Remove any remaining hyphens
            page_id = potential_id.replace('-', '')

            # Validate ID format (32 hex characters)
            if len(page_id) == 32 and all(c in '0123456789abcdefABCDEF' for c in page_id):
                return page_id

            # Try alternative: ID might be the full last segment
            if len(last_part.replace('-', '')) == 32:
                return last_part.replace('-', '')

            raise ValueError(f"Could not extract valid page ID from URL: {url}")

        except Exception as e:
            raise ValueError(f"Invalid Notion URL format: {e}")

    def get_page_title(self, page: Dict[str, Any]) -> str:
        """
        Extract page title from page object.

        Args:
            page: Page object from Notion API

        Returns:
            Page title as string
        """
        try:
            # Try to get title from properties
            properties = page.get("properties", {})

            # Look for title property (could be "title", "Title", or "Name")
            for prop_name, prop_value in properties.items():
                if prop_value.get("type") == "title":
                    title_parts = prop_value.get("title", [])
                    if title_parts:
                        return "".join([part.get("plain_text", "") for part in title_parts])

            # Fallback: use page ID as title
            return f"page-{page.get('id', 'untitled')[:8]}"

        except Exception:
            return "untitled"
