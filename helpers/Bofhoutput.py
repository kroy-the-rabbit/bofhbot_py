

class Bofhoutput():

    def __init__(self,ctx):
        self.ctx = ctx


    def send(self,output):
        output = output.replace('@everyone', '@\u200beveryone')
        output = output.replace('@here', '@\u200bhere')
        return self.ctx.send(output)

