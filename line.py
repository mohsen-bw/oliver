#-------------------------------------------------------------------------------
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender
from gtts import gTTS
from googletrans import Translator
#-------------------------------------------------------------------------------
line = LINE()
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))
linePoll = OEPoll(line)
phu = line.profile.mid
phumid = line.profile.mid
lineMID = line.profile.mid
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
#-------------------------------------------------------------------------------
settings = {       
    "welcome":False,
    "leave":False,
    "tag":False,
    "autoAdd":False,
    "autoLeave":False,
    "autoJoinTicket":False,
    "welcomepic":False,
    "leavepic":False,
    "potag":False,
    "messageadd":"phusui",
    "messagewelcome":"phusui",
    "messageleave":"phusui",
    "messagetag":"phusui",
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
#myProfile["displayName"] = lineProfile.displayName
#myProfile["statusMessage"] = lineProfile.statusMessage
#myProfile["pictureStatus"] = lineProfile.pictureStatus
#-------------------------------------------------------------------------------
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[คนที่อ่าน {} คน]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠🌟 "
            else:
                try:
                    textx += "╚══[กลุ่ม❤️ {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        phubot.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def logError(text):
    line.log("[ มีปัญหา ] " + str(text))
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
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False 
#-------------------------------------------------------------------------------
def myhelp():
    myHelp = """ชุดคำสั่ง
➣͜ คำสั่ง
➣͜ คท
➣͜ มิด
➣͜ ชื่อ
➣͜ ตัส
➣͜ ออน
➣͜ สปีด
➣͜ เช็คค่า
➣͜ เชิญ:มิดคนที่จะเชิญ
➣͜ ตั้งเข้า:ข้อความ
➣͜ ตั้งออก:ข้อความ
➣͜ ตั้งแทค:ข้อความ
➣͜ ตั้งแอด:ข้อความ
➣͜ เปิด/ปิดทักเข้า
➣͜ เปิด/ปิดทักเข้า2
➣͜ เปิด/ปิดทักออก
➣͜ เปิด/ปิดทักออก2
➣͜ เปิด/ปิดแทค
➣͜ เปิด/ปิดแทค2
➣͜ เปิด/ปิดแอด
➣͜ เปิด/ปิดออกแชท
➣͜ เปิด/ปิดมุดลิ้ง"""
    return myHelp
#-------------------------------------------------------------------------------
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] op0")
            return
        if op.type == 5:           
            if settings["autoAdd"] == True:
#            	line.findAndAddContactsByMid(op.param1)
                line.sendMessage(op.param1, str(settings["messageadd"]).format(str(line.getContact(op.param1).displayName)))
        if op.type == 17:
            if settings['welcome'] and "welcome" in settings:
                cnt = line.getContact(op.param2)
                line.sendMessage(op.param1,cnt.displayName + "\n" + str(settings["messagewelcome"]))
            if settings['welcomepic'] and "welcomepic" in settings:
                cnt = line.getContact(op.param2)
                line.sendImageWithURL(op.param1,"http://dl.profile.line.naver.jp/" + cnt.pictureStatus)
        if op.type == 15:
            if settings['leave'] and "leave" in settings:
                cnt = line.getContact(op.param2)
                line.sendMessage(op.param1,cnt.displayName + "\n" + str(settings["messageleave"]))
            if settings['leavepic'] and "leavepic" in settings:
                cnt = line.getContact(op.param2)
                line.sendImageWithURL(op.param1,"http://dl.profile.line.naver.jp/" + cnt.pictureStatus)
        if op.type == 24:            
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)          
#-------------------------------------------------------------------------------
        if op.type == 25:
            try:                
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from               
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != line.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:                        
#--------------------------SELFBOT-----------------------------------------------------
                        if text.lower() in ["คำสั่ง"]:
                            myHelp = myhelp()
                            line.sendMessage(to, str(myHelp))
                            line.sendContact(to, "u5a91f31a0882cae3e309576cc4bf1e5a")                        
                        elif text.lower() in ["มิด"]:
                            line.sendMessage(to,phu)                 
                        elif text.lower() in ["คท"]:
                            line.sendContact(to,phu)
                        elif text.lower() in ["ชื่อ"]:
                            G = line.getContact(phu)
                            line.sendMessage(msg.to,G.displayName)
                        elif text.lower() in ["ตัส"]:
                           phusui = line.getContact(phu)
                           line.sendMessage(to,phusui.statusMessage)
                        elif "login" in msg.text.lower():
                           def qrLogin():
                               Headers.update({'x-lpqs' : '/api/v4/TalkService.do'})
                               transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                               transport.setCustomHeaders(Headers)
                               protocol = TCompactProtocol.TCompactProtocol(transport)
                               client = LineService.Client(protocol)
                               qr = client.getAuthQrcode(keepLoggedIn=1, systemName="Illusion")
                               link = "line://au/q/" + qr.verifier
                               line.sendMessage(msg.to, link)
                               Headers.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                               json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers).text)
                               Headers.update({'x-lpqs' : '/api/v4p/rs'})
                               transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                               transport.setCustomHeaders(Headers)
                               protocol = TCompactProtocol.TCompactProtocol(transport)
                               client = LineService.Client(protocol)
                               req = LoginRequest()
                               req.type = 1
                               req.verifier = qr.verifier
                               req.e2eeVersion = 1
                               res = client.loginZ(req)
                               print('token bot By Illusion')
                               print('\n')
                               line.sendMessage(msg.to, res.authToken)
                               qrLogin()
                        elif text.lower() in ["สปีด"]:
                             start = time.time()
                             line.sendMessage(msg.to,"ความเร็วบอท.....")
                             line.sendMessage(msg.to,str(int(round((time.time() - start) * 1000)))+" ปิง")                        
                        elif text.lower() in ["ออน"]:
                            line.sendMessage(to,str(datetime.now() - start_runtime)[:-7].split(":")[0]+" วัน, "+str(datetime.now() - start_runtime)[:-7].split(":")[1]+" ชั่วโมง, "+str(datetime.now() - start_runtime)[:-7].split(":")[2]+" นาที,")
                        elif "เชิญ: " in msg.text:
                            midd = msg.text.replace("เชิญ: ","")
                            line.findAndAddContactsByMid(midd)
                            line.inviteIntoGroup(msg.to,[midd])
                        elif text.lower() == 'เช็คค่า':
                            try:                       
                                ret_ = "╔════[ สถานะบอท ]═════┓"                        
                                if settings["autoAdd"] == True: ret_ += "\n╠✼ ออโต้แอด「เปิด」"
                                else: ret_ += "\n╠✼ ออโต้แอด「ปิด」"        
                                if settings["autoLeave"] == True: ret_ += "\n╠✼ ออกแชทรวมออโต้「เปิด」"
                                else: ret_ += "\n╠✼ ออกแชทรวมออโต้「ปิด」"                
                                if settings["welcome"] == True: ret_ += "\n╠✼ ข้อความทักคนเข้า「เปิด」"
                                else: ret_ += "\n╠✼ ข้อความทักคนเข้า「ปิด」"
                                if settings["tag"] == True: ret_ += "\n╠✼ ข้อความตอบกลับคนแทค「เปิด」"
                                else: ret_ += "\n╠✼ ข้อความตอบกลับคนแทค「ปิด」"
                                if settings["leave"] == True: ret_ += "\n╠✼ ข้อความทักคนออก「เปิด」"
                                else: ret_ += "\n╠✼ ข้อความทักคนออก「ปิด」"
                                if settings["welcomepic"] == True: ret_ += "\n╠✼ ส่งรูปกับคอนแทคคนเข้า「เปิด」"
                                else: ret_ += "\n╠✼ ส่งรูปกับคอนแทคคนเข้า「ปิด」"
                                if settings["leavepic"] == True: ret_ += "\n╠✼ ส่งรูปกับคอนแทคคนออก「เปิด」"
                                else: ret_ += "\n╠✼ ส่งรูปกับคอนแทคคนออก「ปิด」"
                                if settings["potag"] == True: ret_ += "\n╠✼ ส่งรูปกับคอนแทคคนแทค「เปิด」"
                                else: ret_ += "\n╠✼ ส่งรูปกับคอนแทคคนแทค「ปิด」"                        
                                ret_ += "\n╚════[ สถานะบอท ]═════┛"
                                line.sendMessage(to, str(ret_))
                            except Exception as e:
                               line.sendMessage(to, str(e))
                        elif "ตั้งเข้า:" in msg.text.lower():
                             c = msg.text.replace("ตั้งเข้า:","")
                             if c in [""," ","\n",None]:
                                 line.sendMessage(to,"ไม่สำเร็จ")
                             else:
                                 settings['messagewelcome'] = c
                                 line.sendMessage(to,"สำเร็จแล้ว")
                        elif "ตั้งออก:" in msg.text.lower():
                             c = msg.text.replace("ตั้งออก:","")
                             if c in [""," ","\n",None]:
                                 line.sendMessage(to,"ไม่สำเร็จ")
                             else:
                                 settings['messageleave'] = c
                                 line.sendMessage(to,"สำเร็จแล้ว")
                        elif "ตั้งแทค:" in msg.text.lower():
                             c = msg.text.replace("ตั้งแทค:","")
                             if c in [""," ","\n",None]:
                                 line.sendMessage(to,"ไม่สำเร็จ")
                             else:
                                 settings['messagetag'] = c
                                 line.sendMessage(to,"สำเร็จแล้ว")
                        elif "ตั้งแอด:" in msg.text.lower():
                             c = msg.text.replace("ตั้งแอด:","")
                             if c in [""," ","\n",None]:
                                 line.sendMessage(to,"ไม่สำเร็จ")
                             else:
                                 settings['messageadd'] = c
                                 line.sendMessage(to,"สำเร็จแล้ว")
                        elif text.lower() == "เปิดทักออก":
                            if settings['leave'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['leave'] = True
                            else:
                                if settings['leave'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดทักออก":
                            if settings['leave'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['leave'] = True
                            else:
                                if settings['leave'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "เปิดทักเข้า":
                            if settings['welcome'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['welcome'] = True
                            else:
                                if settings['welcome'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดทักเข้า":
                            if settings['welcome'] == True:
                                line.sendMessage(to,"ปิดแล้วครับ")
                                settings['welcome'] = False
                            else:
                                if settings['welcome'] == False:
                                   line.sendMessage(to,"ปิดแล้วครับ")
                        elif text.lower() == "เปิดทักออก2":
                            if settings['leavepic'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['leavepic'] = True
                            else:
                                if settings['leavepic'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดทักออก2":
                            if settings['leave'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['leave'] = True
                            else:
                                if settings['leave'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "เปิดทักเข้า2":
                            if settings['welcomepic'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['welcomepic'] = True
                            else:
                                if settings['welcomepic'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดทักเข้า2":
                            if settings['welcomepic'] == True:
                                line.sendMessage(to,"ปิดแล้วครับ")
                                settings['welcomepic'] = False
                            else:
                                if settings['welcomepic'] == False:
                                   line.sendMessage(to,"ปิดแล้วครับ")
                        elif text.lower() == "เปิดแทค":
                            if settings['tag'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['tag'] = True
                            else:
                                if settings['tag'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดแทค":
                            if settings['tag'] == True:
                                line.sendMessage(to,"ปิดแล้วครับ")
                                settings['tag'] = False
                            else:
                                if settings['tag'] == False:
                                   line.sendMessage(to,"ปิดแล้วครับ")
                        elif text.lower() == "เปิดแทค2":
                            if settings['potag'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['potag'] = True
                            else:
                                if settings['potag'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดแทค2":
                            if settings['potag'] == True:
                                line.sendMessage(to,"ปิดแล้วครับ")
                                settings['potag'] = False
                            else:
                                if settings['potag'] == False:
                                   line.sendMessage(to,"ปิดแล้วครับ")
                        elif text.lower() == "เปิดออกแชท":
                            if settings['autoLeave'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['autoLeave'] = True
                            else:
                                if settings['autoLeave'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดออกแชท":
                            if settings['autoLeave'] == True:
                                line.sendMessage(to,"ปิดแล้วครับ")
                                settings['autoLeave'] = False
                            else:
                                if settings['autoLeave'] == False:
                                   line.sendMessage(to,"ปิดแล้วครับ")
                        elif text.lower() == "เปิดแอด":
                            if settings['autoAdd'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['autoAdd'] = True
                            else:
                                if settings['autoAdd'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดแอด":
                            if settings['autoAdd'] == True:
                                line.sendMessage(to,"ปิดแล้วครับ")
                                settings['autoAdd'] = False
                            else:
                                if settings['autoAdd'] == False:
                                   line.sendMessage(to,"ปิดแล้วครับ")
                        elif text.lower() == "เปิดมุดลิ้ง":
                            if settings['autoJoinTicket'] == False:
                                line.sendMessage(to,"เปิดแล้วครับ")
                                settings['autoJoinTicket'] = True
                            else:
                                if settings['autoJoinTicket'] == True:
                                    line.sendMessage(to,"เปิดแล้วครับ")
                        elif text.lower() == "ปิดมุดลิ้ง":
                            if settings['autoJoinTicket'] == True:
                                line.sendMessage(to,"ปิดแล้วครับ")
                                settings['autoJoinTicket'] = False
                            else:
                                if settings['autoJoinTicket'] == False:
                                   line.sendMessage(to,"ปิดแล้วครับ")  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['tag'] == True:                    
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = [ cName ]
                             ret_ = random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_ )
                                          line.sendMessage(to,str(settings["messagetag"]))       
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potag'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          line.sendContact(msg.to, mi_d)
                                          break                        
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "เข้าไปในกลุ่ม {} เรียบร้อยแล้วครับ" % str(group.name))       
#-------------------------------------------------------------------------------                    
            except Exception as error:
              print(error)
#-------------------------------------------------------------------------------                                   
    except Exception as error: 
      print(error)
while True:
    try:
        ops = linePoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                lineBot(op)
                linePoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
