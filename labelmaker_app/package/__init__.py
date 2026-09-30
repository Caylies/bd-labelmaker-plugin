from typing import TYPE_CHECKING

from plugin import Plugin

from .cog import LabelmakerCog
from .plugin import setup_plugin

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

plugin: Plugin | None = None

async def setup(bot: "BallsDexBot"):
    global plugin

    plugin = Plugin("bd-labelmaker-plugin")

    await setup_plugin(plugin)
    await bot.add_cog(LabelmakerCog(bot))

async def teardown(bot: "BallsDexBot"):
    if plugin:
        plugin.unload()
