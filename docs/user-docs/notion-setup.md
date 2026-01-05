# Notion Setup Guide

Complete guide to setting up Notion for use with the Markdown Extractor.

## Table of Contents

- [Creating a Notion Integration](#creating-a-notion-integration)
- [Getting Your API Token](#getting-your-api-token)
- [Sharing Pages with the Integration](#sharing-pages-with-the-integration)
- [Understanding Permissions](#understanding-permissions)
- [Troubleshooting Permissions](#troubleshooting-permissions)

---

## Creating a Notion Integration

### Step 1: Access Notion Integrations

1. Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **"+ New integration"**

### Step 2: Configure Integration

**Basic Information**:
- **Name**: `ClaudeCode` (or any name you prefer)
- **Associated workspace**: Select your workspace
- **Logo**: Optional

**Capabilities** (Required):
- ✅ **Read content**: Must be enabled
- ✅ **Read user information**: Optional (helps with metadata)
- ❌ **Update content**: Not needed
- ❌ **Insert content**: Not needed

**Content Capabilities**:
- ✅ **Read content**: Enable this
- Type: "Internal integration" is fine for personal use

### Step 3: Submit

1. Click **"Submit"**
2. Your integration is created!

---

## Getting Your API Token

### Copy the Token

After creating the integration:

1. You'll see **"Internal Integration Token"**
2. Click **"Show"** then **"Copy"**
3. The token looks like: `secret_abc123xyz789...`

**⚠️ Keep this token secure!** It gives access to any pages you share with the integration.

### Configure the CLI Tool

```bash
notion-md configure --token secret_YOUR_TOKEN_HERE
```

**Where it's stored**: `~/.notion-md/config.yaml` (secure, read-only permissions)

---

## Sharing Pages with the Integration

**Critical**: The integration can **only access pages you explicitly share** with it.

### Share a Single Page

1. Open the Notion page you want to extract
2. Click **"Share"** (top right corner)
3. Click **"Invite"**
4. Search for your integration name (e.g., "ClaudeCode")
5. Select the integration
6. Click **"Invite"**

**Permission level**: The integration gets "Can view" access

### Share a Page and All Sub-Pages (Recommended!)

When your page has child pages or linked content:

1. Open the **top-level page**
2. Click **"Share"** (top right)
3. Click **"Invite"** and select your integration
4. **Important**: Look for **"Include sub-pages"** checkbox
5. ✅ **Check "Include sub-pages"**
6. Click **"Invite"**

This shares the entire page tree at once!

---

## Understanding Permissions

### What Needs Sharing

For complete content extraction, you need to share:

#### 1. ✅ **Main Page** (Required)
The page you're extracting must be shared with the integration.

**How to check**:
- Open the page
- Look for your integration name in the "Shared" section
- If not there, it's not shared!

#### 2. ✅ **Child Pages** (If page has links to other pages)
Any pages linked from the main page need separate sharing (unless you used "Include sub-pages").

**How to identify**:
- Look for blue hyperlinks to other pages
- "Child page" blocks
- Links in callouts or paragraphs

**How to share**:
- Click each linked page
- Share with integration
- **OR** use "Include sub-pages" on parent page

#### 3. ✅ **Synced Block Sources** (If page has synced content)
Synced blocks (reusable content) have a source page that needs sharing.

**How to identify**:
- Content that appears in multiple places
- Look for the "synced" indicator in Notion

**How to share**:
- Navigate to the source block's page
- Share with integration

#### 4. ❌ **Databases** (Not yet supported)
Database content won't be extracted even if shared.

**Current limitation**: MVP doesn't support databases (Phase 2 feature)

---

## Complete Extraction Checklist

Before running `notion-md extract <URL>`:

### Pre-Extraction Checklist

- [ ] Integration created
- [ ] API token copied and configured
- [ ] Main page shared with integration
- [ ] All child/linked pages shared (or used "Include sub-pages")
- [ ] Synced block source pages shared (if applicable)

### Quick Test

```bash
# Test your configuration
notion-md status

# Should show:
# [OK] API token configured
# [OK] API connection successful!
```

---

## Sharing Strategies

### Strategy 1: Share Individual Pages (Manual)

**When to use**: Extracting a few specific pages

**Steps**:
1. Open each page
2. Share → Invite → Select integration
3. Repeat for all pages

**Pros**: Precise control
**Cons**: Time-consuming for many pages

---

### Strategy 2: Share Workspace/Folder (Bulk)

**When to use**: Extracting many pages from a workspace

**Steps**:
1. Navigate to workspace root or folder
2. Click "Share" on the folder
3. Invite integration
4. ✅ Enable "Include sub-pages"

**Pros**: Shares everything at once
**Cons**: Gives integration access to more pages

---

### Strategy 3: Share Specific Workspace Section

**When to use**: Organizing project documentation

**Steps**:
1. Create a dedicated "Exports" or "Documentation" folder in Notion
2. Move/link pages you want to extract there
3. Share the entire folder with integration
4. Use "Include sub-pages"

**Pros**: Organized, easy to manage
**Cons**: Requires folder setup

---

## Troubleshooting Permissions

### Error: "Failed to fetch page"

**Cause**: Page not shared with integration

**Solution**:
1. Open the page in Notion
2. Click "Share"
3. Check if your integration appears in "Shared with"
4. If not, click "Invite" and add the integration

---

### Missing Content in Extracted File

**Symptom**: File extracts but content is incomplete

**Possible causes**:

#### A. Child Pages Not Shared
**Check**: Look for sections like "[Page Name - see separate import]"

**Solution**: Share the linked pages with integration

#### B. Synced Block Sources Not Shared
**Check**: Content seems missing but no error

**Solution**:
1. Find the synced block source (look for blue "synced" indicator)
2. Navigate to source page
3. Share with integration

#### C. Unsupported Block Types
**Check**: Look for warnings:
```
[WARNING] Unsupported block type 'column_list'
[WARNING] Unsupported block type 'child_database'
```

**Solution**: This is a current limitation (Phase 2 will add support)

---

### Verify Page Sharing

**Method 1: Check in Notion**
1. Open the page
2. Click "Share"
3. Look for your integration in the list
4. Should show "Can view" permission

**Method 2: Test Extraction**
```bash
notion-md extract "YOUR_PAGE_URL"
```

If it works, permissions are correct!

---

## Permission Best Practices

### 1. Use "Include Sub-Pages" for Complete Extraction
Always enable this when sharing to get all linked content.

### 2. Create a Dedicated Workspace Section
Keep exportable content organized in one place.

### 3. Review Shared Pages Periodically
Check which pages are shared:
- Notion Settings → "Connections"
- Shows all pages shared with integrations

### 4. Remove Integration Access When Not Needed
If you're done extracting:
- You can remove the integration from pages
- Or delete the integration entirely

### 5. Don't Share Sensitive Pages
Only share pages you want the integration to access.

---

## Understanding Notion's Permission Model

### How Notion Sharing Works

**Default**: Integration has NO access to any pages

**After Sharing**: Integration can:
- ✅ Read page content
- ✅ Read page metadata (title, creation date, etc.)
- ✅ Access child pages (if shared separately OR "Include sub-pages" was enabled)
- ❌ Modify content (read-only)
- ❌ Delete pages
- ❌ Share pages

### Permission Levels

When you share a page with an integration:
- **Can view**: Read-only access (what we need)
- **Can edit**: Not needed for extraction
- **Full access**: Not needed

The CLI tool only requires **"Can view"** permission.

---

## Workspace vs Page Sharing

### Workspace-Level Sharing
Gives integration access to the entire workspace.

**When to use**:
- Extracting many pages regularly
- Company/team setup with managed integration

**Risk**: Broad access to all content

### Page-Level Sharing (Recommended)
Gives integration access only to specific pages.

**When to use**:
- Personal use
- Selective extraction
- Security-conscious setups

**Benefit**: Fine-grained control

---

## Example: Setting Up for a Project

Let's say you have a project with multiple Notion pages to extract.

### Scenario

**Goal**: Extract all documentation for "Virgo Capital SOR Opportunity" project

**Notion structure**:
```
Virgo Capital Research (folder)
├── Strategic Overview (page)
│   ├── Market Analysis (child page)
│   └── Competitive Landscape (child page)
├── 2-Year Growth Plan (page)
│   └── 90-Day Execution Plan (child page)
└── Meeting Notes (page)
```

### Setup Steps

1. **Navigate to "Virgo Capital Research" folder in Notion**

2. **Share the folder**:
   - Click "Share" on the folder
   - Click "Invite"
   - Select "ClaudeCode" integration
   - ✅ **Enable "Include sub-pages"**
   - Click "Invite"

3. **Verify all pages are shared**:
   - Open each page
   - Check "Shared with" includes ClaudeCode

4. **Extract from terminal**:
   ```bash
   cd virgo-capital-sor-opportunity

   notion-md extract "https://notion.so/Strategic-Overview-abc123"
   notion-md extract "https://notion.so/2-Year-Growth-Plan-def456"
   notion-md extract "https://notion.so/Meeting-Notes-ghi789"

   # All saved to: ./user-context/notion-pages/
   ```

5. **Result**:
   ```
   user-context/notion-pages/
   ├── strategic-overview.md
   ├── 2-year-growth-plan.md
   ├── meeting-notes.md
   └── images/
       └── (all downloaded images)
   ```

---

## Security Considerations

### Token Security

**Do**:
- ✅ Store token in config file (`~/.notion-md/config.yaml`)
- ✅ Keep token secret
- ✅ Use different integrations for different projects if needed

**Don't**:
- ❌ Share your token publicly
- ❌ Commit token to git repositories
- ❌ Store in plain text files

### Integration Access

**Review regularly**:
- Which pages are shared
- Whether you still need the integration
- Remove access when done

**Audit trail**:
- Notion logs integration access
- Check "Settings → Connections" for active integrations

---

## Next Steps

After setup is complete:

1. ✅ Integration created and token configured
2. ✅ Pages shared with integration
3. ✅ Ready to extract!

**Continue to**:
- [Usage Guide](usage.md) - Learn how to extract pages
- [Troubleshooting Guide](troubleshooting.md) - Common issues

---

## FAQ

### Q: Do I need to share pages every time I extract?
**A**: No! Once shared, pages stay shared. You only share once.

### Q: Can the integration modify my pages?
**A**: No. It has read-only "Can view" access.

### Q: What if I delete the integration?
**A**: All shared pages lose access. You'd need to create a new integration and re-share.

### Q: Can I use the same integration across multiple workspaces?
**A**: Each integration is workspace-specific. Create separate integrations for different workspaces.

### Q: How do I revoke access?
**A**: Open the page → Share → Click X next to the integration name.

### Q: Does "Include sub-pages" share future child pages?
**A**: Yes! Any child pages added later are automatically shared.

---

## Additional Resources

- [Notion API Documentation](https://developers.notion.com/)
- [Notion Integrations Guide](https://www.notion.so/help/create-integrations-with-the-notion-api)
- [CLI Usage Guide](usage.md)
