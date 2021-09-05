from simple_history.admin import SimpleHistoryAdmin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

class EntityAdmin(SimpleHistoryAdmin, SafeDeleteAdmin):
    list_display = (highlight_deleted,) + ('created', 'updated', ) + SafeDeleteAdmin.list_display 