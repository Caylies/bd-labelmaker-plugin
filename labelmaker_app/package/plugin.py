from typing import TYPE_CHECKING

from ballsdex.settings import settings
from discord import ButtonStyle, Interaction
from discord.ui import Button
from plugin import Plugin, get_component

from labelmaker_app.models import Label

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

BallSpawnView = get_component("BallSpawnView")


def _format_response(view, interaction: Interaction["BallsDexBot"], response: str) -> str:
    return response.format(
        user=interaction.user.mention,
        collectibles=settings.plural_collectible_name,
        collectible=settings.collectible_name,
        ball=view.model.country,
        rarity=view.model.rarity,
        emoji=str(view.bot.get_emoji(view.model.emoji_id)),
        discord=settings.discord_invite,
    )


async def setup_plugin(plugin: Plugin):
    labels: list[Label] = [label async for label in Label.objects.filter(enabled=True)]

    @plugin.after(BallSpawnView.__init__)
    def add_label_buttons(_, self, bot: "BallsDexBot", model) -> None:
        state = plugin.state(self)

        state["label_map"] = {} 

        for label in labels:

            async def callback(
                interaction: Interaction["BallsDexBot"], current_label: Label = label
            ) -> None:
                await interaction.response.send_message(
                    _format_response(self, interaction, current_label.response),
                    ephemeral=current_label.ephemeral,
                )

            button = Button(
                label=label.label,
                style=ButtonStyle(label.style),
                emoji=label.emoji if label.emoji != "" else None,
            )
            button.callback = callback

            state["label_map"][button] = label
            self.catch_row.add_item(button)

    @plugin.after(BallSpawnView.mark_caught)
    def style_on_catch(_, self):
        state = plugin.state(self)

        if not state["label_map"]:
            return

        for button, label in state["label_map"].items():
            button.label = label.caught_label or label.label
            button.style = ButtonStyle(label.caught_style or label.style)
            button.emoji = label.caught_emoji or None
            button.disabled = label.caught_disable

    @plugin.before(BallSpawnView.on_timeout)
    def style_on_timeout(self):
        state = plugin.state(self)

        if not state["label_map"]:
            return

        for button, label in state["label_map"].items():
            if not self.caught:
                button.label = label.despawn_label or label.label
                button.style = ButtonStyle(label.despawn_style or label.style)
                button.emoji = label.despawn_emoji or None

            button.disabled = True
