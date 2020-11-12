

class Bofhoutput():

    def __init__(self,ctx):
        self.ctx = ctx


    def dropItHot(self,output):
        output = output.replace('@everyone', '@\u200beveryone')
        return self.ctx.send(output)

