# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model (`bookshelf/models.py`):
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created in Django Admin:
- **Viewers** → has `can_view`
- **Editors** → has `can_create`, `can_edit`
- **Admins** → has all permissions

## Views
Protected with `@permission_required`:
- `book_list` → requires `can_view`
- `book_create` → requires `can_create`
- `book_edit` → requires `can_edit`
- `book_delete` → requires `can_delete`
