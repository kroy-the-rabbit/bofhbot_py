import discord
from discord.ext import commands
#from cogs.utils.checks import get_user


'''Module for moderator commands.'''


class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,hidden=True)
    async def kick(self, ctx, user, *, reason=""):

        if "Mods" not in [role.name for role in ctx.author.roles]:
            await ctx.send(content='Go away, not enough permissions.')
            return

        if len(ctx.message.mentions) == 0:
            await ctx.send(content='Did not find anybody to kick.')
            return;


        real_user = ctx.message.mentions[0]

        if "Mods" in [role.name for role in real_user.roles]:
            await ctx.send(content='Cannot kick {}. Protected'.format(user))
            return



        if len(reason):
            await ctx.send("Kicking {} because: {}".format(user,reason))
        else:
            await ctx.send("You've got it, kicking {}".format(user))


        await real_user.kick(reason=reason)

    """Kicks a user (if you have the permission)."""

    """
    user = get_user(ctx.message, user)
    if user:
    try:
    await user.kick(reason=reason)
    return_msg = "Kicked user `{}`".format(user.mention)
    if reason:
    return_msg += " for reason `{}`".format(reason)
    return_msg += "."
    await ctx.message.edit(content=self.bot.bot_prefix + return_msg)
    except discord.Forbidden:
    await ctx.message.edit(content=self.bot.bot_prefix + 'Could not kick user. Not enough permissions.')
    else:
    return await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user.')
    """

def setup(bot):
    bot.add_cog(Mod(bot))
