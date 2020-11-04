from discord.ext import commands
import time

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.send("pong!!\n{}ms".format(round((t2-t1)*1000)))
        #await ctx.send("pong! {0:.2f}ms".format(self.bot.latency * 1000))


def setup(bot):
    bot.add_cog(Ping(bot))
