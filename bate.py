#-------------------------------------------------------------------------------
#phusui self bot
#-------------------------------------------------------------------------------
from linepy import *
from akad import *
import json, requests, sys
#-------------------------------------------------------------------------------
phubot = LINE()
phubot.log("Auth Token : " + str(phubot.authToken))
phubot.log("Timeline Token : " + str(phubot.tl.channelAccessToken))
phubotPoll = OEPoll(phubot)
phu = phubot.profile.mid
#-------------------------------------------------------------------------------
settings = {    
    "alwayread":False,
    "welcome":False,
    "leave":False,
    "autoLeave":False,
    "autoAdd":False,
    "messageadd":"phusui",
    "messagewelcome":"phusui",
    "messageleave":"phusui",
}
def logError(text):
    phubot.log("[ มีปัญหา ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1        
#-------------------------------------------------------------------------------
def helpPhusuiselfbot():
    helpPhusuiselfbot = """help byphusui
-help
-me
-uid
-name
-runtime
-speed
-welcome [text]
-welcome on/off
-leave on/off
-leave [text]
-autoleave on/off
-autoadd on/off
-add [text]"""
    return helpPhusuiselfbot
#-------------------------------------------------------------------------------
def phusuiBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] op0")
            return
        if op.type == 5:           
            if settings["autoAdd"] == True:
                phubot.sendMessage(op.param1, str(settings["messageadd"]).format(str(phubot.getContact(op.param1).displayName)))
        if op.type == 17:
            if settings['welcome'] and "welcome" in settings:
                cnt = phubot.getContact(op.param2)
                phubot.sendMessage(op.param1,cnt.displayName + "\n" + str(settings["messagewelcome"]))
        if op.type == 15:
            if settings['leave'] and "leave" in settings:
                cnt = phubot.getContact(op.param2)
                phubot.sendMessage(op.param1,cnt.displayName + "\n" + str(settings["messageleave"]))
        if op.type == 24:            
            if settings["autoLeave"] == True:
                phubot.leaveRoom(op.param1)
#-------------------------------------------------------------------------------          
#-------------------------------------------------------------------------------            
        if op.type == 25:
            try:
                print("[ 25 ] phusuiselfbot")
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                phuza = text.lower()
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != phubot.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:                        
#--------------------------SELFBOT----------------------------------------------------- 
                        if phuza in ["/help"]:
                            helpsuiselfbot = helpPhusuiselfbot()
                            phubot.sendMessage(to, str(helpsuiselfbot))
                            phubot.sendContact(to, "u5a91f31a0882cae3e309576cc4bf1e5a")                        
                        elif phuza in ["/uid"]:
                            phubot.sendMessage(to,phu)
                        elif phuza in ["/me"]:
                            phubot.sendContact(msg.to,phu)
                        elif phuza in ["/name"]:
                            G = phubot.getContact(phu)
                            phubot.sendMessage(msg.to,G.displayName)
                        elif phuza in ["/speed"]:
                             start = time.time()
                             phubot.sendMessage(msg.to,"speedbyphu.....")
                             phubot.sendMessage(msg.to,str(int(round((time.time() - start) * 1000)))+" ms")
                        elif phuza in ["/runtime"]:
                            phubot.sendMessage(to,str(datetime.now() - start_runtime)[:-7].split(":")[0]+" ???, "+str(datetime.now() - start_runtime)[:-7].split(":")[1]+" ????, "+str(datetime.now() - start_runtime)[:-7].split(":")[2]+" ??????,")
                        elif "/welcome:" in phuza():
                             c = msg.text.replace("/welcome:","")
                             if c in [""," ","\n",None]:
                                 phubot.sendMessage(to,"no")
                             else:
                                 settings['messagewelcome'] = c
                                 phubot.sendMessage(to,"ok")
                        elif "/leave" in phuza():
                             c = msg.text.replace("/leave:","")
                             if c in [""," ","\n",None]:
                                 phubot.sendMessage(to,"no")
                             else:
                                 settings['messageleave'] = c
                                 phubot.sendMessage(to,"ok")
                        elif "/add" in phuza():
                             c = msg.text.replace("/add:","")
                             if c in [""," ","\n",None]:
                                 phubot.sendMessage(to,"no")
                             else:
                                 settings['messageadd'] = c
                                 phubot.sendMessage(to,"ok")
                        elif phuza == "/leave on":
                            if settings['leave'] == False:
                                phubot.sendMessage(to,"เปิดแล้วครับ")
                                settings['leave'] = True
                            else:
                                if settings['leave'] == True:
                                    phubot.sendMessage(to,"เปิดแล้วครับ")
                        elif phuza == "/leave off":
                            if settings['leave'] == False:
                                phubot.sendMessage(to,"เปิดแล้วครับ")
                                settings['leave'] = True
                            else:
                                if settings['leave'] == True:
                                    phubot.sendMessage(to,"เปิดแล้วครับ")
                        elif phuza == "/welcome on":
                            if settings['welcome'] == False:
                                phubot.sendMessage(to,"เปิดแล้วครับ")
                                settings['welcome'] = True
                            else:
                                if settings['welcome'] == True:
                                    phubot.sendMessage(to,"เปิดแล้วครับ")
                        elif phuza == "/welcome off":
                            if settings['welcome'] == True:
                                phubot.sendMessage(to,"ปิดแล้วครับ")
                                settings['welcome'] = False
                            else:
                                if settings['welcome'] == False:
                                   phubot.sendMessage(to,"ปิดแล้วครับ")
                        elif phuza == "/autoleave on":
                            if settings['autoLeave'] == False:
                                phubot.sendMessage(to,"เปิดแล้วครับ")
                                settings['autoLeave'] = True
                            else:
                                if settings['autoLeave'] == True:
                                    phubot.sendMessage(to,"เปิดแล้วครับ")
                        elif phuza == "/autoleave off":
                            if settings['autoLeave'] == True:
                                phubot.sendMessage(to,"ปิดแล้วครับ")
                                settings['autoLeave'] = False
                            else:
                                if settings['autoLeave'] == False:
                                   phubot.sendMessage(to,"ปิดแล้วครับ")
                        elif phuza == "/autoadd on":
                            if settings['autoAdd'] == False:
                                phubot.sendMessage(to,"เปิดแล้วครับ")
                                settings['autoAdd'] = True
                            else:
                                if settings['autoAdd'] == True:
                                    phubot.sendMessage(to,"เปิดแล้วครับ")
                        elif phuza == "/autoadd off":
                            if settings['autoAdd'] == True:
                                phubot.sendMessage(to,"ปิดแล้วครับ")
                                settings['autoAdd'] = False
                            else:
                                if settings['autoAdd'] == False:
                                   phubot.sendMessage(to,"ปิดแล้วครับ")
#-------------------------------------------------------------------------------                    
            except Exception as error:
              print(error)
#-------------------------------------------------------------------------------
    except Exception as error: 
      print(error)
while True:
    try:
        ops = phubotPoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                phusuiBot(op)
                phubotPoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
