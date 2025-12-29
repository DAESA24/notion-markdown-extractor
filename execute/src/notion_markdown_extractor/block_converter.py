"""Block-to-Markdown conversion logic for Notion blocks."""

from typing import List, Dict, Any, Optional, Callable
import click


class BlockConverter:
    """Converts Notion API blocks to Markdown format."""

    def __init__(self, storage=None):
        """
        Initialize block converter.

        Args:
            storage: Storage instance for image downloads (optional)
        """
        self.storage = storage
        self.output_path = None  # Set when converting for image downloads

    def convert_blocks_to_markdown(
        self,
        blocks: List[Dict[str, Any]],
        output_path: Optional[str] = None,
        page_title: Optional[str] = None
    ) -> str:
        """
        Convert list of Notion blocks to complete Markdown document.

        Args:
            blocks: List of block objects from Notion API
            output_path: Output file path (needed for image downloads)
            page_title: Optional page title to include as H1 at the top

        Returns:
            Complete markdown document as string
        """
        self.output_path = output_path
        markdown_lines = []

        # Add page title as H1 if provided
        if page_title:
            markdown_lines.append(f"# {page_title}")

        for block in blocks:
            md_content = self.convert_block_to_markdown(block)
            if md_content:
                markdown_lines.append(md_content)

        return "\n\n".join(markdown_lines)

    def convert_block_to_markdown(self, block: Dict[str, Any], indent_level: int = 0) -> str:
        """
        Convert single Notion block to Markdown.

        Args:
            block: Block object from Notion API
            indent_level: Indentation level for nested blocks

        Returns:
            Markdown string for the block
        """
        block_type = block.get("type")

        # Map block types to converter functions
        converters = {
            "paragraph": self._convert_paragraph,
            "heading_1": self._convert_heading_1,
            "heading_2": self._convert_heading_2,
            "heading_3": self._convert_heading_3,
            "bulleted_list_item": self._convert_bulleted_list,
            "numbered_list_item": self._convert_numbered_list,
            "quote": self._convert_quote,
            "code": self._convert_code,
            "callout": self._convert_callout,
            "toggle": self._convert_toggle,
            "divider": self._convert_divider,
            "image": self._convert_image,
            "file": self._convert_file,
            "table": self._convert_table,
            "table_row": self._convert_table_row,
            "child_page": self._convert_child_page,
            "synced_block": self._convert_synced_block,
        }

        # Get converter function for block type
        converter = converters.get(block_type)

        if converter:
            md_content = converter(block, indent_level)

            # Handle nested children if present
            if block.get("children"):
                children_md = []
                # Synced blocks are transparent containers - don't add indentation
                child_indent = indent_level if block_type == "synced_block" else indent_level + 1

                for child in block["children"]:
                    child_md = self.convert_block_to_markdown(child, child_indent)
                    if child_md:
                        children_md.append(child_md)

                if children_md:
                    # Add children with proper spacing
                    md_content += "\n" + "\n\n".join(children_md)

            return md_content
        else:
            # Log unsupported block type
            print(f"[WARNING] Unsupported block type '{block_type}'")
            return ""

    def _convert_paragraph(self, block: Dict[str, Any], indent_level: int) -> str:
        """
        Convert paragraph block to markdown.

        Note: In Markdown, paragraphs should NOT be indented except when they are
        children of list items. Indenting by 4+ spaces creates code blocks.
        """
        text = self._extract_rich_text((block.get("paragraph") or {}).get("rich_text", []))
        # Only apply indentation if this is nested in a list (indent_level from list items)
        # For now, don't indent paragraphs to avoid code block formatting
        return text if text else ""

    def _convert_heading_1(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert heading_1 block to markdown."""
        text = self._extract_rich_text((block.get("heading_1") or {}).get("rich_text", []))
        return f"# {text}"

    def _convert_heading_2(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert heading_2 block to markdown."""
        text = self._extract_rich_text((block.get("heading_2") or {}).get("rich_text", []))
        return f"## {text}"

    def _convert_heading_3(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert heading_3 block to markdown."""
        text = self._extract_rich_text((block.get("heading_3") or {}).get("rich_text", []))
        return f"### {text}"

    def _convert_bulleted_list(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert bulleted_list_item block to markdown."""
        text = self._extract_rich_text((block.get("bulleted_list_item") or {}).get("rich_text", []))
        indent = "  " * indent_level
        return f"{indent}- {text}"

    def _convert_numbered_list(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert numbered_list_item block to markdown."""
        text = self._extract_rich_text((block.get("numbered_list_item") or {}).get("rich_text", []))
        indent = "  " * indent_level
        return f"{indent}1. {text}"

    def _convert_quote(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert quote block to markdown."""
        text = self._extract_rich_text((block.get("quote") or {}).get("rich_text", []))
        return f"> {text}"

    def _convert_code(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert code block to markdown with syntax highlighting."""
        code_block = block.get("code") or {}
        text = self._extract_rich_text(code_block.get("rich_text", []))
        language = code_block.get("language", "")

        return f"```{language}\n{text}\n```"

    def _convert_callout(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert callout block to blockquote with emoji."""
        callout = block.get("callout") or {}
        icon = callout.get("icon") or {}
        emoji = icon.get("emoji", "[!]") if icon.get("type") == "emoji" else "[!]"
        text = self._extract_rich_text(callout.get("rich_text", []))

        return f"> {emoji} {text}"

    def _convert_toggle(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert toggle block to flattened heading + content."""
        toggle = block.get("toggle") or {}
        text = self._extract_rich_text(toggle.get("rich_text", []))

        # Use heading level based on context (default to ###)
        return f"### {text}"

    def _convert_divider(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert divider block to markdown horizontal rule."""
        return "---"

    def _convert_image(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert image block to markdown image with local download."""
        image = block.get("image") or {}
        image_type = image.get("type")

        # Get image URL
        if image_type == "external":
            image_url = (image.get("external") or {}).get("url", "")
        elif image_type == "file":
            image_url = (image.get("file") or {}).get("url", "")
        else:
            return ""

        # Get caption for alt text
        caption_parts = image.get("caption", [])
        alt_text = self._extract_rich_text(caption_parts) if caption_parts else "image"

        # Download image if storage is available
        if self.storage and self.output_path and image_url:
            local_path = self.storage.download_image(image_url, self.output_path, alt_text)
            if local_path:
                return f"![{alt_text}]({local_path})"

        # Fallback: use URL directly
        return f"![{alt_text}]({image_url})"

    def _convert_file(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert file block to markdown link."""
        file = block.get("file") or {}
        file_type = file.get("type")

        # Get file URL
        if file_type == "external":
            file_url = (file.get("external") or {}).get("url", "")
        elif file_type == "file":
            file_url = (file.get("file") or {}).get("url", "")
        else:
            return ""

        # Get caption for link text
        caption_parts = file.get("caption", [])
        link_text = self._extract_rich_text(caption_parts) if caption_parts else "file"

        return f"[{link_text}]({file_url})"

    def _convert_table(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert table block to markdown table."""
        # Table structure requires processing table_row children
        # This is a placeholder - full implementation needs children processing
        return "<!-- Table block detected - see child rows -->"

    def _convert_table_row(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert table_row block to markdown table row."""
        table_row = block.get("table_row") or {}
        cells = table_row.get("cells") or []

        # Convert each cell
        cell_texts = [self._extract_rich_text(cell) for cell in cells]

        # Join cells with pipes
        return "| " + " | ".join(cell_texts) + " |"

    def _convert_child_page(self, block: Dict[str, Any], indent_level: int) -> str:
        """Convert child_page reference to placeholder with page name."""
        child_page = block.get("child_page") or {}
        page_title = child_page.get("title", "Linked Page")

        return f"[{page_title} - see separate import]"

    def _convert_synced_block(self, block: Dict[str, Any], indent_level: int) -> str:
        """
        Convert synced_block to markdown.

        Synced blocks are Notion's reusable content blocks. They come in two types:
        - Original/source blocks: synced_from is null, has children content
        - Reference blocks: synced_from points to source block, may have children

        For Option 1 (simple approach): We just convert the children content directly.
        This means if a synced block appears multiple times on the page, the content
        will appear multiple times in the markdown (matching Notion's behavior).

        Args:
            block: Synced block object from Notion API
            indent_level: Indentation level for nested blocks

        Returns:
            Markdown string with synced block content
        """
        synced_block = block.get("synced_block") or {}
        synced_from = synced_block.get("synced_from")

        # Both source and reference blocks have children that were fetched recursively
        # by the notion_client, so we just need to convert those children
        # The children are already in block.get("children")

        # Note: We return empty string here because the children will be processed
        # by the parent convert_block_to_markdown function's children handling logic
        # This allows synced blocks to work exactly like other container blocks
        return ""

    def _extract_rich_text(self, rich_text_array: List[Dict[str, Any]]) -> str:
        """
        Extract and format rich text from Notion rich text array.

        Args:
            rich_text_array: Array of rich text objects from Notion API

        Returns:
            Formatted markdown string with annotations
        """
        if not rich_text_array:
            return ""

        result_parts = []

        for text_obj in rich_text_array:
            # Get plain text content
            plain_text = text_obj.get("plain_text", "")
            if not plain_text:
                continue

            # Get annotations
            annotations = text_obj.get("annotations", {})

            # Apply markdown formatting based on annotations
            formatted_text = plain_text

            # Code (highest priority)
            if annotations.get("code", False):
                formatted_text = f"`{formatted_text}`"

            # Bold
            if annotations.get("bold", False):
                formatted_text = f"**{formatted_text}**"

            # Italic
            if annotations.get("italic", False):
                formatted_text = f"*{formatted_text}*"

            # Strikethrough
            if annotations.get("strikethrough", False):
                formatted_text = f"~~{formatted_text}~~"

            # Handle links
            if text_obj.get("href"):
                href = text_obj.get("href")
                formatted_text = f"[{formatted_text}]({href})"

            result_parts.append(formatted_text)

        return "".join(result_parts)
