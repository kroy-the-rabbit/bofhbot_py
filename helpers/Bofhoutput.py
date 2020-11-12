

class Bofhoutput():

    def __init__(self,ctx):
        self.ctx = ctx


    def send(self,output):
        output = output.replace('@everyone', '@\u200beveryone')
        return self.ctx.send(output)

