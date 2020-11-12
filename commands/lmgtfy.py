import random
from discord.ext import commands
from discord.embeds import Embed
import urllib.parse

class LMGTFY(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lmgtfy',description='Be passive aggressive')
    @commands.guild_only()
    async def lmgtfy(self, ctx, *term : str):
        out = Bofhoutput.Bofhoutput(ctx)
        try:
            '''
            https://lmgtfy.app/q=asdf
            '''
            if len(term) == 0:
                raise TypeError("Needs a search term")
            link = "https://lmgtfy.app/?q={}".format(urllib.parse.quote(' '.join(term)))
            embedVar = Embed(
                title="Let me Google that for you",
                color=0xE5E242,
                url=link,
                description='There is this amazing resource named "Google".  I\'ve done the hard work for you, now all you need to do is click the link.'
            )
            await out.send(embed=embedVar)
            return
        except Exception as e:
            await out.send('You must supply a search term {}'.format(str(e)))
            return
        await out.send('You must supply a search term')


def setup(bot):
    bot.add_cog(LMGTFY(bot))
