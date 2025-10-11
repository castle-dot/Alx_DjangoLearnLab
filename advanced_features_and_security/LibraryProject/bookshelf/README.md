# Permissions and Groups Setup in Django

## Custom Permissions:
1. `can_view`: Allows users to view articles.
2. `can_create`: Allows users to create articles.
3. `can_edit`: Allows users to edit articles.
4. `can_delete`: Allows users to delete articles.

## Groups:
1. **Admins**:
   - Has all permissions: `can_view`, `can_create`, `can_edit`, `can_delete`.
   
2. **Editors**:
   - Has `can_create` and `can_edit` permissions.
   
3. **Viewers**:
   - Has `can_view` permission only.

## Permissions Enforcement:
- We use the `@permission_required` decorator in views to enforce permissions. For example:
  ```python
  @permission_required('bookshelf.can_edit', raise_exception=True)
  def edit_article(request, article_id):
      # View logic here
