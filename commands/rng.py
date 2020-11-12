import random
from discord.ext import commands
from helpers import Bofhoutput

class RNG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='flip',description='Flip a coin with optional number of times (default 1)')
    @commands.guild_only()
    async def flip(sync,ctx,limit : int = 1):
        out = Bofhoutput.Bofhoutput(ctx)
        roll_history = []
        if limit > 1000000:
            limit = 1000000
        if limit < 1:
            limit = 1
        for i in range(limit):
            flip = random.randint(0,1)
            if flip == 0:
                roll_history.append("Heads")
            else:
                roll_history.append("Tails")

        result = "Flips: {}\nHeads: {}\nTails: {}".format(limit, roll_history.count("Heads"), roll_history.count("Tails"))

        await out.send(result)

    @commands.command(name='roll',description='Roll one or more dice in NdN format (default 1d6)')
    @commands.guild_only()
    async def roll(self, ctx, dice : str = '1d6'):
        out = Bofhoutput.Bofhoutput(ctx)
        try:
            rolls, limit = map(int, dice.split('d'))
            if rolls > 1000000:
                rolls = 1000000
            if limit > 1000000:
                limit = 1000000
            if rolls < 1:
                rolls = 1
            if limit < 1:
                limit = 6
        except Exception:
            await out.send('Format has to be in NdN format (eg: 1d6)!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await out.send(result)

    @commands.command(name='choose',description='Choose between multiple items')
    @commands.guild_only()
    async def choose(self, ctx, *choices : str):
        out = Bofhoutput.Bofhoutput(ctx)
        try:
            choice = random.choice(choices)
        except Exception:
            await out.send('You must supply something to choose from!')
            return

        chosen = random.choice(choices)
        await out.send(chosen)


def setup(bot):
    bot.add_cog(RNG(bot))
