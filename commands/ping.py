from discord.ext import commands
import time
from helpers import Bofhoutput

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        out = Bofhoutput.Bofhoutput(ctx)
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await out.send("pong!!\n{}ms".format(round((t2-t1)*1000)))


def setup(bot):
    bot.add_cog(Ping(bot))
