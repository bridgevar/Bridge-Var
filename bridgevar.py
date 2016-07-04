import scratchapi
from scratchapi import *
scratch = scratchapi.ScratchUserSession('username', 'password')
stop = 0

def stopServer():
   stop = 1

def startServer():
    while True:
        if (ScratchUserSession.cloud.get_var("send",115433205) == "1"):
            baseproject1 = ScratchUserSession.cloud.get_var("test",115433205)
            ScratchUserSession.cloud.set_var('var', baseproject1, 115433970)
            ScratchUserSession.cloud.set_var('send', "0", 115433205)
            print("115433205 sent 115433970 " + baseproject1 + " succesfully!")
            
        if (ScratchUserSession.cloud.get_var("send",115433970) == "1"):
            baseproject1 = ScratchUserSession.cloud.get_var("var",115433970)
            ScratchUserSession.cloud.set_var('test', baseproject1, 115433205)
            ScratchUserSession.cloud.set_var('send', "0", 115433970)
            print("115433970 sent 115433205 " + baseproject1 + " succesfully!")
        if (stop == 1):
            break
    
if (scratch.tools.verify_session() == True):
    startServer()
else:
    print("Error logging you in!")

