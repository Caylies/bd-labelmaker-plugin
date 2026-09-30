import emoji
from django.db import models
from django.core.exceptions import ValidationError
from discord import ButtonStyle


def validate_unicode_emoji(value: str):
    if value and not emoji.is_emoji(value):
        raise ValidationError(f"'{value}' is not a valid Unicode emoji.")


class ButtonStyleChoices(models.IntegerChoices):
    PRIMARY = ButtonStyle.primary.value
    SECONDARY = ButtonStyle.secondary.value
    SUCCESS = ButtonStyle.success.value
    DANGER = ButtonStyle.danger.value


class Label(models.Model):
    label = models.CharField(max_length=80, help_text="The label's text.")
    emoji = models.CharField(
        blank=True,
        max_length=10,
        validators=(validate_unicode_emoji,),
        help_text="A single standard Unicode emoji for the button.",
    )
    style = models.SmallIntegerField(
        choices=ButtonStyleChoices, default=ButtonStyleChoices.SECONDARY, help_text="The label's button color."
    )

    response = models.TextField(
        max_length=2000, help_text="The response that will be sent after pressing the label's button."
    )
    ephemeral = models.BooleanField(
        default=False, help_text="Whether the label will only be visible to the user who interacted with it."
    )
    enabled = models.BooleanField(default=True, help_text="Whether the label will appear.")

    despawn_label = models.CharField(blank=True, max_length=80, help_text="The label's text after a ball despawns.")
    despawn_emoji = models.CharField(
        blank=True,
        max_length=10,
        validators=(validate_unicode_emoji,),
        help_text="A single standard Unicode emoji for the button after a ball despawns.",
    )
    despawn_style = models.SmallIntegerField(
        null=True, blank=True, choices=ButtonStyleChoices, help_text="The label's button color after a ball despawns."
    )

    caught_label = models.CharField(blank=True, max_length=80, help_text="The label's text after a ball is caught.")
    caught_disable = models.BooleanField(
        default=True, help_text="Whether the label will disable after a ball is caught."
    )
    caught_emoji = models.CharField(
        blank=True,
        max_length=10,
        validators=(validate_unicode_emoji,),
        help_text="A single standard Unicode emoji for the button after a ball is caught.",
    )
    caught_style = models.SmallIntegerField(
        null=True, blank=True, choices=ButtonStyleChoices, help_text="The label's button color after a ball is caught."
    )
