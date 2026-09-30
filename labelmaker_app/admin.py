from django.contrib import admin

from labelmaker_app.models import Label


# Register your models here.
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("label", "emoji", "style", "enabled", "ephemeral")
    list_filter = ("enabled", "style", "ephemeral")
    search_fields = ("label", "response", "despawn_label", "caught_label")
    list_editable = ("enabled",)
    fieldsets = (
        ("Label configuration", {"fields": ("label", "emoji", "style", "response", "ephemeral", "enabled")}),
        (
            "Despawn state",
            {
                "classes": ("collapse",),
                "description": "Optional appearance overrides applied when a ball despawns.",
                "fields": ("despawn_label", "despawn_emoji", "despawn_style"),
            },
        ),
        (
            "Caught state",
            {
                "classes": ("collapse",),
                "description": "Optional appearance overrides applied when a ball is caught.",
                "fields": ("caught_label", "caught_emoji", "caught_style", "caught_disable"),
            },
        ),
    )
