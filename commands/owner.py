
from discord.ext import commands


class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def command_load(self, ctx, *, command: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: commands.owner"""

        try:
            self.bot.load_extension(command)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def command_unload(self, ctx, *, command: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: commands.owner"""

        try:
            self.bot.unload_extension(command)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def command_reload(self, ctx,*, command: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: commands.owner"""

        try:
            self.bot.reload_extension(command)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


def setup(bot):
    bot.add_cog(Owner(bot))
