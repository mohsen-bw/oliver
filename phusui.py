from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#===============================================================================#
phusui = LINE()
phusui.log("Auth Token : " + str(phusui.authToken))
phusui.log("Timeline Token : " + str(phusui.tl.channelAccessToken))

print ("""
╔══╗
║█████╗ 
║██╔══██╗
║██║   ██╗
║██║████╔╝
║██╔════╝
║██║
╚══╝""")

phusuiMID = phusui.profile.mid
phusuiProfile = phusui.getProfile()
phusuiSettings = phusui.getSettings()
oepoll = OEPoll(phusui)
#==============================================================================#
settings = {    
    "alwayread":False,
    "server": "VPS",
    "welcomepic":False,
    "welcomemessage":False,
    "autoBlock":False,
    "autoadd":False,
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "contact":False,
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = phusuiProfile.displayName
myProfile["statusMessage"] = phusuiProfile.statusMessage
myProfile["pictureStatus"] = phusuiProfile.pictureStatus
#==============================================================================#
def logError(text):
    phusui.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as NIGGA:
        NIGGA.write("\n[%s] %s" % (str(time), text))
        
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            phusui.sendImageWithURL(to, str(path))
    except Exception as EXEC:
        logError(EXEC)

def cloneProfile(mid):
    contact = phusui.getContact(mid)
    if contact.videoProfile == None:
        phusui.cloneContactProfile(mid)
    else:
        profile = phusui.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        phusui.updateProfile(profile)
        pict = phusui.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = phusui.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = phusui.getProfileDetail(mid)['result']['objectId']
    phusui.updateProfileCoverById(coverId)

def backupProfile():
    profile = phusui.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = phusui.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
	
def restoreProfile():
    profile = phusui.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = phusui.downloadFileURL("http://dl.profile.line-cdn.net/{}".format(settings["myProfile"]["pictureStatus"]), saveAs="tmp/backupPicture.bin")
        phusui.updateProfilePicture(profile.pictureStatus)
        phusui.updateProfile(profile)
    else:
        phusui.updateProfile(profile)
        pict = phusui.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = phusui.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    phusui.updateProfileCoverById(coverId)

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        phusui.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as EA:
        logError(EA)
        phusui.sendMessage(to, "[ INFO ] Error :\n" + str(EA))

def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        phusui.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)  

def restartBot():
    print ("RESTART BOT BY PHU SUI")
    time.sleep(1)
    python = sys.executable
    os.execl(python, python, *sys.argv)
  
def sendMessageWithMention(to, phusuiMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(phusuiMID)+'}'
        text_ = '@x '
        phusui.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)    
 
start_runtime = datetime.now()

def phuhelp():
  phuHelp = """✰SELF PYTHON3✰
✫「help」
✫「me」
✫「myid」
✫「myname」
✫「mybio」
✫「mypic」
✫「mycover」
✫「myinfo」
✫「mid」
✫「contact」
✫「info」
✫「tag」 [number]
✫「restart」
✫「runtime」
✫「speed」
✫「unsend」
✫「mention」
✫「invitetocall」
✫「stag」 [number] {@}
✫「addfriend」 {@}
✫「delfriend」 {@}
✫「uid」 {@}
✫「bye」 {@}
✫「copy」 {@}
✫「cgroup」 {@}
✫「info」 {@}
✫「upname」 [text]
✫「blockid」 [mid]
✫「autoblock」 on/off
✫「autoadd」 on/off
✫「autoread」 on/off
✫「setmessageadd」: [text]
✫「welcomepic」 on/off
✫「welcomemessage」 on/off
✫「welcomemessage」: [text]
•─✯͜͡✯By Phusui of Midnight✯͜͡✯─•"""
  return phuHelp
respRemember = {}
#==============================================================================#
def phusuiBot(op):
    try:
        if op.type == 0:
            return  
            
        if op.type == 5:
            if settings['autoBlock'] == True:
                phusui.blockContact(op.param1)     
 
            if settings['autoadd'] == True:
                phusui.findAndAddContactsByMid(op.param1)
                if (settings["messageadd"] in [""," ","\n",None]):
                    pass
                else:
                    phusui.sendMessage(op.param1,str(settings["messageadd"])) 
 
        if op.type == 17:
            if settings['welcomemessage'] and "welcomemessage" in settings:
                cnt = phusui.getContact(op.param2)
                phusui.sendMessage(op.param1,cnt.displayName + "\n" + str(settings["welcomemessage"]))

            if settings['welcomepic'] and "welcomepic" in settings:
                cnt = phusui.getContact(op.param2)
                phusui.sendImageWithURL(op.param1,"http://dl.profile.line.naver.jp/" + cnt.pictureStatus)

            if settings["alwayread"]:
                phusui.sendChatChecked(msg.from_,msg.id)
            else:
                phusui.sendChatChecked(msg.to,msg.id)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != phusui.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return                   
#==============================================================================#     
                elif msg.text.lower() == "/help":                    
                    phuHelp = phuhelp()
                    phusui.sendMessage(to, str(phuHelp))
                    phusui.sendContact(to, "u5a91f31a0882cae3e309576cc4bf1e5a")       
                elif text.lower() in ["/me"]:
                   phusui.sendContact(to, phusuiMID)                	
                elif text.lower() in ["/myid"]:
                   phusui.sendMessage(to, phusuiMID)
                elif text.lower() in ["/myname"]:
                    me = phusui.getContact(phusuiMID)
                    phusui.sendMessage(msg.to, me.displayName)
                elif text.lower() in ["/mybio"]:
                    me = phusui.getContact(phusuiMID)
                    phusui.sendMessage(msg.to,me.statusMessage)
                elif text.lower() in ["/mypic"]:
                    me = phusui.getContact(phusuiMID)
                    phusui.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() in ["/mycover"]:
                    me = phusui.getContact(phusuiMID)
                    cover = phusui.getProfileCoverURL(phusuiMID)    
                    phusui.sendImageWithURL(msg.to, cover)
                elif text.lower() in ["/myinfo"]:             
                    phusui.sendContact(to, phusuiMID)
                    phusui.sendMessage(msg.to, phusuiMID)
                    me = phusui.getContact(phusuiMID)
                    phusui.sendMessage(msg.to, me.displayName)
                    me = phusui.getContact(phusuiMID)
                    phusui.sendMessage(msg.to,me.statusMessage)
                    me = phusui.getContact(phusuiMID)
                    phusui.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    me = phusui.getContact(phusuiMID)
                    cover = phusui.getProfileCoverURL(phusuiMID)    
                    phusui.sendImageWithURL(msg.to, cover)
                elif text.lower() in ["/mid"]:
                    phusui.sendMessage(to,to)
                elif text.lower() in ["/contact"]:
                    phusui.getContact(to,phusuiMID)
                elif text.lower() in ["/speed"]:
                    start = time.time()         
                    phusui.sendMessage(msg.to,"กำลังทดสอบ(｀・ω・´)")      
                    phusui.sendMessage(msg.to,str(int(round((time.time() - start) * 1000)))+" ปิง")
                elif text.lower() in ["/restart"]:
                    phusui.sendMessage(to, "กำลังเริ่มใหม่...")
                    time.sleep(1)
                    phusui.sendMessage(to, "SELF BOT BYPHUSUI")
                    phusui.sendMessage(to, "บอทได้ทำการเริ่มใหม่สำเร็จแล้ว")
                    restartBot()
                elif text.lower() in ["/runtime"]:
                    phusui.sendMessage(msg.to,str(datetime.now() - start_runtime)[:-7].split(":")[0]+" hour, "+str(datetime.now() - start_runtime)[:-7].split(":")[1]+" minute, "+str(datetime.now() - start_runtime)[:-7].split(":")[2]+" second,")
                elif text.lower() in ["/invitetocall"]:
                    exc = phusui.getGroup(msg.to).members
                    zxc = phusui.getProfile().mid
                    phusui.inviteIntoGroupCall(msg.to,[uid.mid for uid in exc if uid.mid != zxc])
                    phusui.sendMessage(msg.to,"เชิญเข้าร่วมการคอลเรียบร้อยแล้วครับ:)")                
                elif "/upname " in msg.text.lower():
                    spl = re.split("/upname ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = phusui.getProfile()
                        prof.displayName = spl[1]
                        phusui.updateProfile(prof)
                        phusui.sendMessage(msg.to,"เปลี่ยนชื่อสำเร็จแล้ว:)")
                elif msg.text.lower().startswith("/blockid "):
                    user = msg.text.lower().replace("/blockid ","")
                    phusui.blockContact(user)
                    phusui.sendMessage(to, "ทำการบล็อคไอดีนั้นแล้ว")        
                elif "/sh " in msg.text.lower():
                    spl = re.split("/sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            phusui.sendMessage(msg.to,subprocess.getoutput(spl[1]))
                        except:
                           pass
                elif "/uid " in msg.text.lower():
                    if msg.toType == 2:
                        red = re.compile(re.escape('/uid '),re.IGNORECASE)
                        namel = red.sub('',msg.text)
                        namel = namel.lstrip()
                        namel = namel.replace(" @","$spliter$")
                        namel = namel.replace("@","")
                        namel = namel.rstrip()
                        namel = namel.split("$spliter$")
                        gmem = phusui.getGroup(msg.to).members
                        for targ in gmem:
                           if targ.displayName in namel:
                               phusui.sendMessage(msg.to,targ.displayName+": "+targ.mid)
                elif "/bye" in msg.text.lower():
                    if msg.contentMetadata is not None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                           try:
                               phusui.kickoutFromGroup(msg.to,[target])
                           except:
                               phusui.kickoutFromGroup(msg.to,[target])
                        else:
                           pass
                elif msg.text.lower().startswith("/cgroup "):
                    phusui.sendMessage(to, "กำลังตรวจสอบข้อมูล...")
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        G = phusui.getGroupIdsJoined()
                        cgroup = phusui.getGroups(G)
                        ngroup = ""
                        for mention in mentionees:
                         for x in range(len(cgroup)):
                           gMembMids = [contact.mid for contact in cgroup[x].members]
                           if mention['M'] in gMembMids:
                                ngroup += "\n➢ " + cgroup[x].name + " | สมาชิก: " +str(len(cgroup[x].members))    
                        if ngroup == "":
                             phusui.sendMessage(to, "ไม่พบ")
                        else:
                             phusui.sendMessage(to, "***ตรวจพบอยู่ในกลุ่ม %s"%(ngroup))
                elif msg.text.lower().startswith("/copy "):        
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        if len(lists) != []:
                            ls = random.choice(lists)
                            cloneProfile(ls)
                            phusui.sendMentionFooter(to, 'copy\n', sender, "http://line.me/ti/p/~botline2034", "http://dl.profile.line-cdn.net/"+phusui.getContact(sender).pictureStatus, phusui.getContact(sender).displayName);phusui.sendMessage(to, phusui.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+phusui.getContact(sender).pictureStatus, 'i-installUrl': 'http://line.me/ti/p/~botline2034', 'type': 'mt', 'subText': " ", 'a-installUrl': 'http://line.me/ti/p/~botline2034', 'a-installUrl': ' http://line.me/ti/p/~botline2034', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'http://line.me/ti/p/~botline2034', 'i-linkUri': 'http://line.me/ti/p/~botline2034', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'http://line.me/ti/p/~botline2034'}, contentType=19)							
                            phusui.sendMessage(to,"คัดลอกบัญชีเรียบร้อยแล้ว", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+phusui.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://bit.ly/2JpqZ7H'})
                elif text.lower in ["/save"]:        
                    try:
                         backupProfile()
                         phusui.sendMessage(to, "บันทึกสถานะบัญชีเรียบร้อยแล้ว", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+phusui.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://bit.ly/2JpqZ7H'})
                    except Exception as e:
                         phusui.sendMessage(to, "ไม่สามารถบันทึกสถานะบัญชีได้", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+phusui.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://bit.ly/2JpqZ7H'})
                         phusui.sendMessage(msg.to, str(e))
                elif text.lower in ["/load"]:
                    try:
                         restoreProfile()
                         phusui.sendMentionFooter(to, 'ãloadã\n', sender, "http://line.me/ti/p/~botline2034", "http://dl.profile.line-cdn.net/"+phusui.getContact(sender).pictureStatus, phusui.getContact(sender).displayName);phusui.sendMessage(to, phusui.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+phusui.getContact(sender).pictureStatus, 'i-installUrl': 'http://line.me/ti/p/~botline2034', 'type': 'mt', 'subText': " ", 'a-installUrl': 'http://line.me/ti/p/~botline2034', 'a-installUrl': ' http://line.me/ti/p/~botline2034', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'http://line.me/ti/p/~botline2034', 'i-linkUri': 'http://line.me/ti/p/~botline2034', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'http://line.me/ti/p/~botline2034'}, contentType=19)							
                         phusui.sendMessage(to, "เรียกคืนสถานะบัญชีสำเร็จโปรดรอสักครู่จนกว่าโปรไฟล์จะเปลี่ยน", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+phusui.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://bit.ly/2JpqZ7H'})
                    except Exception as e:
                         phusui.sendMessage(to, "ไม่สามารถเรียกคืนสถานะบัญชีได้", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+phusui.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://bit.ly/2JpqZ7H'})
                         phusui.sendMessage(msg.to, str(e))
                elif msg.text.lower().startswith("/addfriend "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                        for ls in lists:                           
                            phusui.findAndAddContactsByMid(ls)
                        phusui.sendMessage(to, "เพิ่มเพื่อนแล้ว!")
                elif msg.text.lower().startswith("/delfriend "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            phusui.deleteContact(ls)
                        phusui.sendMessage(to, "ลบออกจากการเป็นเพื่อนแล้ว!")     
                elif msg.text.lower().startswith("/info "):
                    if phusui != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                me = phusui.getContact(ls)
                                path = phusui.getProfileCoverURL(ls)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    phusui.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                    phusui.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                    phusui.sendMessage(msg.to,"「 MID 」\n" +  to)
                                    phusui.sendMessage(to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                    phusui.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    phusui.sendImageWithURL(to, str(path))
                                    phusui.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                else:
                                    phusui.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                    phusui.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                    phusui.sendMessage(msg.to,"「 MID 」\n" + ls)
                                    phusui.sendMessage(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                    phusui.sendMessage(to, str(path))
                            else:
                                phusui.sendMessage(to, "Talk Exception You are not Related to LineChannel")
                    else:
                         phusui.sendMessage(to, "Talk Exception You are not Related to LineChannel")
                elif msg.text.lower().startswith("/tag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = phusui.getContact(to)
                        RhyN_(to, name.mid)
                elif msg.text.lower() == ".":
                    if msg.toType == 0:
                        sendMention(to, to, "", "")
                    elif msg.toType == 2:
                        group = phusui.getGroup(to)
                        contact = [mem.mid for mem in group.members]
                        mentionMembers(to, contact)
                elif msg.text.lower().startswith("/stag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = phusui.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = phusui.getContact(receiver)
                                RhyN_(to, contact.mid)                   
                elif text.lower() == '/mention':
                    group = phusui.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20(a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        phusui.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        phusui.sendMessage(to, "Total {} Mention".format(str(len(nama))))                        
                elif msg.text.lower().startswith("/unsend "):
                    args = msg.text.replace("/unsend ","")
                    mes = 0
                    try:
                       mes = int(args[1])
                    except:
                       mes = 1
                    M = phusui.getRecentMessagesV2(to, 101)
                    MId = []
                    for ind,i in enumerate(M):
                       if ind == 0:
                           pass
                       else:
                           if i._from == phusui.profile.mid:
                               MId.append(i.id)
                               if len(MId) == mes:
                                   break
                    def unsMes(msg_id):
                     phusui.unsendMessage(msg_id)
                    for i in MId:
                     thread1 = threading.Thread(target=unsMes, args=(i,))
                     thread1.start()
                     thread1.join()
                    phusui.sendMessage(msg.to, ' 「 ยกเลิกข้อความทำงาน 」\nยกเลิกแล้ว {} คำ:)'.format(len(MId)))
                elif text.lower() == '/info':
                    if phusui != None:
                        me = phusui.getContact(to)
                        path = phusui.getProfileCoverURL(to)
                        path = str(path)
                        if settings["server"] == "VPS":
                            phusui.sendMessage(to,"「 Display Name 」\n" + me.displayName)
                            phusui.sendMessage(to,"「 Status Message 」\n" + me.statusMessage)
                            phusui.sendMessage(to,"「 MID 」\n" +  to)
                            phusui.sendMessage(to, text=None, contentMetadata={'mid': to}, contentType=13)
                            phusui.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                            phusui.sendImageWithURL(to, str(path))
                            phusui.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                        else:
                            phusui.sendMessage(to,"「 Display Name 」\n" + me.displayName)
                            phusui.sendMessage(to,"「 Status Message 」\n" + me.statusMessage)
                            phusui.sendMessage(to,"「 MID 」\n" +  to)
                            phusui.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            phusui.sendImageWithURL(to, str(path))
                    else:
                        phusui.sendMessage(to, "Talk Exception")        
                elif "/setmessageadd:" in msg.text.lower():
                    settings['messageadd'] = msg.text.replace("/setmessageadd:","")
                    phusui.sendMessage(msg.to,"ตั้งค่าสำเร็จ!!!")  
                elif "/welcomemessage:" in msg.text.lower():
                     c = msg.text.replace("/welcomemessage:","")
                     if c in [""," ","\n",None]:
                         phusui.sendMessage(msg.to,"เกิดข้อผิดพลาด!!")
                     else:
                         settings['welcomemessage'] = c
                         phusui.sendMessage(msg.to,"ตั้งค่าข้อความสำเร็จแล้วครับ")
                elif msg.text.lower() == "/welcomepic on":
                    if settings['welcomepic'] == False:
                        phusui.sendMessage(msg.to,"เปิดต้อนรับรูปเรียบร้อย:)")
                        settings['welcomepic'] = True
                    else:
                        if settings['welcomepic'] == True:
                            phusui.sendMessage(msg.to,"เปิดต้อนรับรูปเรียบร้อย(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/welcomepic off,":
                    if settings['welcomepic'] == True:
                        phusui.sendMessage(msg.to,"ปิดต้อนรับรูปเรียบร้อย(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings['welcomepic'] = False
                    else:
                        if settings['welcomepic'] == False:
                            phusui.sendMessage(msg.to,"ปิดต้อนรับรูปเรียบร้อย(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/autoblock on":
                    if settings['autoBlock'] == True:
                        phusui.sendMessage(msg.to,"เปิดการบล็อคอัตโนมัติ(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings['autoBlock'] = False
                    else:
                        if settings['autoBlock'] == False:
                            phusui.sendMessage(msg.to,"เปิดการบล็อคอัตโนมัติ(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/autoblock off":
                    if settings['autoBlock'] == False:
                        phusui.sendMessage(msg.to,"ปิดการบล็อคอัตโนมัติ(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings['autoBlock'] = True
                    else:
                        if settings['autoBlock'] == True:
                            phusui.sendMessage(msg.to,"ปิดการบล็อคอัตโนมัติ(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/autoadd on":
                    if settings['autoadd'] == False:
                        phusui.sendMessage(msg.to,"เปิดการรับเพื่อนอัตโนมัติ(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings['autoadd'] = True
                    else:
                        if settings['autoadd'] == True:
                            phusui.sendMessage(msg.to,"เปิดการรับเพื่อนอัตโนมัติ(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/autoadd off":
                    if settings['autoadd'] == True:
                        phusui.sendMessage(msg.to,"ปิดการรับเพื่อนอัตโนมัติ(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings['autoadd'] = False
                    else:
                        if settings['autoadd'] == False:
                            phusui.sendMessage(msg.text,"ปิดการรับเพื่อนอัตโนมัติ(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/welcomemessage on":
                    if settings['welcomemessage'] == False:
                        phusui.sendMessage(msg.to,"เปิดต้อนรับข้อความเรียบร้อย(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings['welcomemessage'] = True
                    else:
                        if settings['welcomemessage'] == True:
                            phusui.sendMessage(msg.to,"เปิดต้อนรับข้อความเรียบร้อย(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/welcomemessage off":
                    if settings['welcomemessage'] == True:
                        phusui.sendMessage(msg.to,"ปิดต้อนรับข้อความเรียบร้อย(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings['welcomemessage'] = False
                    else:
                        if settings['welcomemessage'] == False:
                            phusui.sendMessage(msg.to,"ปิดต้อนรับข้อความเรียบร้อย(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/autoread off":
                    if settings["alwayread"] == True:
                        phusui.sendMessage(msg.to,"ปิดอ่านอัตโนมัติแล้ว(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings["alwayread"] = False
                    else:
                        if settings["alwayread"] == False:
                            phusui.sendMessage(msg.to,"ปิดอ่านอัตโนมัติแล้ว(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                elif msg.text.lower() == "/autoread on":
                    if settings["alwayread"] == False:
                        phusui.sendMessage(msg.to,"เปิดอ่านอัตโนมัติแล้ว(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")
                        settings["alwayread"] = True
                    else:
                        if settings["alwayread"] == True:
                            phusui.sendMessage(msg.to,"เปิดอ่านอัตโนมัติแล้ว(∩｀-´)⊃━━☆ﾟ.*･｡ﾟ")                               
#==============================================================================#
    except Exception as FUCKING:
        logError(FUCKING)
while True:
    try:
        ops = oepoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                phusuiBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
