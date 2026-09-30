from typing import TYPE_CHECKING

from discord.ext import commands

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot


class LabelmakerCog(commands.Cog):
    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot
