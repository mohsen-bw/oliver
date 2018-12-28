#PHUSUI TEAM DELETE
#Ki4
from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender
_session = requests.session()
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#===============================================================================#
line = LINE()
#line = LINE()
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))
#ki = LINE("Ew6zlqE4ry6weugebDtf.s0F19RdwonJdLC5Lh1l7BW.ToGQj8Rlowkj4i74UtEHzjkwR821ab1pafE8db/lgZg=")
#kk = LINE("EwDeWDA0ukTVpdwjM3Pd.CQ21dgoQa8cJvr/gfRG7lq.Gt3bwffxfVwc/KQJafyT7XsQcFXu/ljJ/kU7Lj1J1G4=")
#kc = LINE("EwzTf0ofsvsYI3OeQIO7.qnieITaY618vb6NfpWw2TW.bb8T+LfENadUEIAWgJ5cSjy8HLhqNCEq8isr7Vvudb4=")
#ke = LINE("Ewvd1Z0gur9AraTEiZtc.oWkzrd9xecC1x9phdvVKZa.quuxm8b8OQRwZ0cJtzXJDFgu6B+VZPT0dS4g4WpxdBM=")
print ("""
TEAM DELETE
╔══╗
║█████╗ 
║██╔══██╗
║██║    ██╗
║██║████╔╝
║██╔════╝
║██║
╚══╝
BY PHUSUI""")
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()
#kiMID = ki.profile.mid
#kkMID = kk.profile.mid
#kcMID = kc.profile.mid
#keMID = ke.profile.mid
oepoll = OEPoll(line)
mid = line.getProfile().mid
Rfu = [line]
#Exc = [ki,kk,kc,ke]
RfuBot=[lineMID]
Family=["u5a91f31a0882cae3e309576cc4bf1e5a",lineMID]
Creator=['u5a91f31a0882cae3e309576cc4bf1e5a']
admiin=['u5a91f31a0882cae3e309576cc4bf1e5a']
Fam = RfuBot + Family + Creator
msg_dict = {}
msg_image={}
msg_video={}
msg_sticker={}
unsendchat = {}
temp_flood = {}
wbanlist = []
wblacklist = []
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#

settings = {
    "RText": True,
    "autoAdd": False,
    "autoBlock": False,
    "autoJoin": True,
    'autoCancel':{"on":True,"members":10},	
    "autoLeave": True,
    "autoRead": False,
    "autoReply": False,
    "botcancel": False,
    "leaveRoom": False,
    "detectMention": False,
    "checkSticker": False,
    "checkContact": False,
    "checkPost": False,
    "kickMention": False,
    "potoMention": False,
    "delayMention": False,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "Nk": False,
    "Api": False,
    "Aip": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "detectMentionPM": False,
    "dwhitelist": False,
    "gift": False,
    "likeOn": False,
    "timeline": False,
    "commentOn":False,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture": [],
    "changePictureProfile": False,    
    "changeVideo": False,
    "chatMessage": "dih",
    "unsendMessage": False,
    "UnsendPesan": False,
    "Timeline": False,
    "autoJoinTicket": False,
    "welcome":"""「 กรุณาตั้งข้อความด้วยครับ 」""",
    "kick":"""「 กรุณาตั้งข้อความด้วยครับ 」""",
    "bye":"""「 กรุณาตั้งข้อความด้วยครับ 」""",
    "Respontag":"""「 กรุณาตั้งข้อความด้วยครับ 」""",
    "eror":"คุณใช้คำสั่งผิด กรุณาศึกษาวิธีใช้ หรือสอบถามกับผู้สร้าง โดยพิมคำสั่ง *.ผส*เพื่อแสดง คท ของผู้สร้าง",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "notag": False,
    "pcancel": False,
    "pinvite": False,
    "pmMessage": "ว่างัยครับว่างเดื้ยวเห็นข้อความจะมาตอบนะครับ",
    "qrp": False,
    "readerPesan": " แอบทมายเดะจิ้มตาบอด",
    "replyPesan": "Sorry , i'm busy right now.",
    "responGc": False,
    "responcall": False,
    "responcallgc": False,
    "restartPoint": "c07540238e0ddffa5187313406f7f3c67",
    "server": "VPS",
    "ksticker": False,
    "timeRestart": "18000",   
    "phu":"「 กรุณาตั้งข้อความด้วยครับ 」",
    "phusui":"BY PHU",
    "me":"「 PHUSUI 」",
    "icon":"「 PHUSUI 」",
    "message":"บัญชีนี้ถูกป้องกันโดย Selfbot By phuselfbotline ระบบได้ทำการบล็อคคุณอัตโนมัติเนื่องจากคุณยังไม่ได้ยืนยันตัวตนกับผู้สร้างบอท\nสามารถยืนตัวตนได้ง่ายโดยการพิม unblockกับphuseltbotlineระบบจะทำการปลดบล็อคท่านโดยอัตโนมัต",
    "comment":"""「 กรุณาตั้งข้อความด้วยครับ 」""",
   "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],    
    "addSticker": {
        "name": "",
        "status": False,
    },    
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "คนแอด": {
                "STKID": "52002736",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "คนออก": {
                "STKID": "51626533",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "คนเตะ": {
                "STKID": "52002767",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "คนแอบ": {
                "STKID": "13188540",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "คนแทค": {
                "STKID": "52002734",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "ภู": {
                "STKID": "52002734",
                "STKPKGID": "11537",
                "STKVER": "1"                
            },
            "sleepSticker": "",
            "คนเข้า": {
                "STKID": "51626494",
                "STKPKGID": "11538",
                "STKVER": "1"
            }
        }
    },
    "mimic": {
       "copy": False,
       "status": False,
       "target": {}
    }
}
RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
    "autoBlock": False,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""
setTime = {}
setTime = rfuSet['setTime']
contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
mulai = time.time() 
msg_dict = {}
lineProfile.displayName = myProfile["displayName"]
lineProfile.statusMessage = myProfile["statusMessage"]
lineProfile.pictureStatus = myProfile["pictureStatus"]
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)                        
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)      
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    line.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            line.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)
def cloneProfile(mid):
    contact = line.getContact(mid)
    if contact.videoProfile == None:
        line.cloneContactProfile(mid)
    else:
        profile = line.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        line.updateProfile(profile)
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = line.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = line.getProfileDetail(mid)['result']['objectId']
    line.updateProfileCoverById(coverId)
def waktu(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days,hours = divmod(hours,24)
	return '【%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที】' % (days, hours, mins, secs)
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
    except Exception as error:
        logError(error)
        phusui.sendMessage(to, "[ INFO ] Error :\n" + str(error))                        
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]           
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': lineMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)
def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def backupData():
    try:
        backup = Settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1       
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def eghelp():
    egHelp ="""📤help
📤me"""
    return egHelp
def kihelp():
    kiHelp ="""┌♥️BY:PHUSUI♥️┘
★ลุย ข้อความ
★คิก1-4: ข้อความ
★ตัส1-4: ข้อความ 
★แจก
★คิก
★สังหาร1-4 [@]
★ลูกน้องมา
★ถอยทัพ 
★[1-4]มา
★ถอย[1-4]
★ยกค้างเชิญ"""
    return kiHelp
def myhelp():
    myHelp = """┌𖡨คำสั่งบอท𖡨┘
➤คท = ส่งคอนแทคตัวเรา
➤เทส = ดูความเร็วของเชลบอท
➤ชื่อ = ดูชื่อของเรา
➤ตัส = ดูสเตตัสของเรา
➤ดิส = ส่งรูปโปรไฟล์เรา
➤ปก = ส่งรูปปกของเรา
➤เชคค่า = ดูการตั้งค่าของบอท
➤ข้อมูล = ส่งข้อมูลของเรา
➤บอท = ข้อมูลเกี่ยวกับบอท
➤ออน = เช็คเวลาการใช้งานบอท
➤รีบอท = รีบอทเอาลิ้งใหม่
➤ผู้สร้าง = ส่งคทผู้พัฒนาบอท
➤พูด [ข้อความ] = สั่งสิริพูดตามที่เราสั่ง
➤ยกเลิก [เลข] = สั่งยกเลิกข้อความ
➤รัว เริ่ม [เลข] [ข้อความ] = สั่งสแปมข้อความ
➤ตั้งแทค {ข้อความ} = ตั้งข้อความตอบกลับคนแทค
➤ตั้งเข้า {ข้อความ} = ตั้งข้อความต้อนรับคนเข้า
➤ตั้งออก {ข้อตวาม} = ตั้งข้อความอำลาคนอื่น
➤ตั้งเตะ {ข้อความ} = ตั้งข้อความแจ้งเตือนคนเตะกัน
➤ตั้งแอบ {ข้อความ} = ตั้งข้อความเมื่อคนแอบอ่าน
➤แทคแชท {ข้อความ} = ตั้งตอบกลับคนแทคแชทส่วนตัว
➤รันแชท {ข้อความ} = ตั้งข้อความสแปมส่งส่วนตัว
➤ไอคอน {ข้อความ} = ตั้งไอคอนตรงคอนแทคเรา
➤แทค = แทคคนทั้งห้อง
➤ดึง [ลงคท] = เชิญคนเข้ากลุ่ม
➤แอด = ผู้สร้างกลุ่ม
➤ชื่อกลุ่ม = ชื่อกลุ่ม
➤ไอดีกลุ่ม = ไอดีกลุ่ม
➤รูปกลุ่ม = รูปกลุ่ม
➤ลิ้ง = ขอลิ้งกลุ่ม
➤เปิด/ปิดลิ้ง = เปิดปิดลิ้งกลุ่ม
➤เปิด/ปิดบล็อค = เปิดปิดบล็อคคนแอด
➤เปิด/แอด = เปิดปิดรับแอดอัตโนมัติ
➤เปิด/ปิดทักเข้า = เปิดปิดต้อนรับคนเข้ากลุ่ม
➤เปิด/ปิดทักออก = เปิดปิดอำลาคนออกจากกลุ่ม
➤เปิด/ปิดเตะ = เปิดปิดข้อความเมื่อคนเตะกัน
➤เปิด/ปิดแทค = เปิดปิดข้อความตอบกลับคนแทค
➤เปิด/ปิดแทค2 = เปิดปิดส่งรูปโปรไฟล์คนแทค
➤เปิด/ปิดแทค3 = เปิดปิดแทคกลับคนแทค
➤เปิด/ปิดมุด = เปิดปิดมุดเข้ากลุ่มโดยลิ้ง
➤ข้อมูล [@] = แทคคนที่ต้องการดูข้อมูล
➤เช็ค [@] = เช็คกลุ่มที่อยู่ร่วมกัน
➤แทค [จำนวน] [@] = แทคตามจำนวนที่เราสั่ง
➤ไวรัส [จำนวน] [@] = ส่งไวรัสไปในแชทส่วนตัวตามจำนวนที่สั่ง
➤แสปม [จำนวน] [@] = ส่งข้อความไปในแชทที่เราตั้งไว้
➤ดึงหมด [@] = ดึงทุกอย่างเกี่ยวกับคนที่แทค
➤ดึงหมด = ดึงทุกอย่างในแชทส่วนตัว
➤เช็ค [@] = เช็คกลุ่มที่อยู่ร่วมกัน
➤เปลี่ยนดิส = ส่งรูปภาพเชลจะทำการอัพรูปไห้
➤เปลี่ยนรูปกลุ่ม = ส่งรูปภาพเชลจะทำการอัพรูปกลุ่มไห้"""
    return myHelp
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:                
                line.findAndAddContactsByMid(op.param1)                                
            if settings["autoBlock"] == True:               
                line.blockContact(op.param1)
                ki.blockContact(op.param1)
                kk.blockContact(op.param1)
                kc.blockContact(op.param1)
                ke.blockContact(op.param1)
            msgSticker = settings["messageSticker"]["listSticker"]["คนแอด"]
            if msgSticker != None:
                sid = msgSticker["STKID"]
                spkg = msgSticker["STKPKGID"]
                sver = msgSticker["STKVER"]
                sendSticker(op.param1, sver, spkg, sid)        
        if op.type == 13:
            print(op.param1)
            print(op.param2)
            print(op.param3)
            if mid in op.param3:
                G = line.getGroup(op.param1)
                if setting["autoJoin"] == True:
                    if setting["autoCancel"]["on"] == True:
                        if len(G.members) <= setting["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif setting["autoCancel"]["on"] == True:
                    if len(G.members) <= setting["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in setting["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 15:
          #  print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["Lv"] == True:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                msgSticker = settings["messageSticker"]["listSticker"]["คนออก"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        if op.type == 19:
            #print ("[ 15 ]  NOTIFIED LEAVE GROUP")
            if settings["Nk"] == True:
                if "{gname}" in settings['kick']:
                    gName = line.getGroup(op.param1).name
                    msg = settings['kick'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["คนเตะ"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                    if "@!" in settings['kick']:
                        msg = msg.split("@!")
                        return sendMention(op.param2, op.param2, msg[0], msg[1])
                    return sendMention(op.param2, op.param2, "Hallo ", msg)
                msgSticker = settings["messageSticker"]["listSticker"]["คนเตะ"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
                #sendMention(op.param1, op.param2, "อุ๊ต๊ะ", "\n{}".format(str(settings['kick'])))
        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["Wc"] == True:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                msgSticker = settings["messageSticker"]["listSticker"]["คนเข้า"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
#      if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
        if op.type == 24:
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)                      
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = line.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 line.sendText(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 line.sendText(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 line.sendText(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     line.findAndAddContactsByMid(target)
                                     line.inviteIntoGroup(msg.to,[target])
                                     line.sendText(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         line.findAndAddContactsByMid(invite)
                                         line.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         line.sendText(msg.to,"ðﾟﾘﾧตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุðﾟﾘﾩอาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญðﾟﾘﾨ")
                                         settings["winvite"] = False
                                         break
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendText(msg.to,"รับทราบ")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendText(msg.to,"decided not to comment")

               elif settings["dblack"] == True:
                   if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"ลบจากรายการที่ถูกแบนแล้ว")
                        settings["dblack"] = False

                   else:
                        settings["dblack"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendText(msg.to,"Sudah Ada")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")

               elif settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
                        settings["dblacklist"] = False

                   else:
                        settings["dblacklist"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
        if op.type == 25:
            msg = op.message
            text = msg.text
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
#==============================================================================#
                if "รัว " in msg.text.lower():
                    spl = re.split("รัว ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'คำสั่ง' or text.lower() == 'help':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                if text.lower() == 'คำสั่ง2':                    
                    egHelp = eghelp()
                    line.sendMessage(to, str(egHelp))
                if text.lower() == 'คำสั่ง3':                    
                    kiHelp = kihelp()
                    line.sendMessage(to, str(kiHelp))
#==============================================================================#
                elif text.lower() in ["ตี๋"]:
                   line.sendMessage(to, "ตี๋หิด")
                elif text.lower().startswith("คิก "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")                    
                    ki.sendMessage(to, say)
                    kk.sendMessage(to, say)
                    kc.sendMessage(to, say)
                    ke.sendMessage(to, say)                
                elif text.lower() == 'ล็อคอิน':
              	   line.sendMessage(to, "กดลิ้งนี้เพื่อออกการเชื่อมต่อเซลล์เลยครับ\n line://nv/connectedDevices/")                             
                elif text.lower() == 'ทดสอบ':     
                    start = time.time()
                    line.sendMessage(to, "『◉กำลังทดสอบความเร็วของคิก◉』")
                    elapsed_time = time.time() - start                                                   
                    line.sendMessage(to, "█▒... 10.0%")
                    line.sendMessage(to, "██▒... 20.0%")
                    line.sendMessage(to, "███▒... 30.0%")
                    line.sendMessage(to, "████▒... 40.0%")
                    line.sendMessage(to, "█████▒... 50.0%")
                    line.sendMessage(to, "██████▒... 60.0%")
                    line.sendMessage(to, "██████▒... 70.0%")
                    line.sendMessage(to, "████████▒... 80.0%")
                    line.sendMessage(to, "█████████▒... 90.0%")
                    line.sendMessage(to, "███████████..100.0%")
                    ki.sendMessage(to, "█▒... 10.0%")
                    ki.sendMessage(to, "██▒... 20.0%")
                    ki.sendMessage(to, "███▒... 30.0%")
                    ki.sendMessage(to, "████▒... 40.0%")
                    ki.sendMessage(to, "█████▒... 50.0%")
                    ki.sendMessage(to, "██████▒... 60.0%")
                    ki.sendMessage(to, "██████▒... 70.0%")
                    ki.sendMessage(to, "████████▒... 80.0%")
                    ki.sendMessage(to, "█████████▒... 90.0%")
                    ki.sendMessage(to, "███████████..100.0%")
                    kc.sendMessage(to, "█▒... 10.0%")
                    kc.sendMessage(to, "██▒... 20.0%")
                    kc.sendMessage(to, "███▒... 30.0%")
                    kc.sendMessage(to, "████▒... 40.0%")
                    kc.sendMessage(to, "█████▒... 50.0%")
                    kc.sendMessage(to, "██████▒... 60.0%")
                    kc.sendMessage(to, "██████▒... 70.0%")
                    kc.sendMessage(to, "████████▒... 80.0%")
                    kc.sendMessage(to, "█████████▒... 90.0%")
                    kc.sendMessage(to, "███████████..100.0%")
                    ke.sendMessage(to, "█▒... 10.0%")
                    ke.sendMessage(to, "██▒... 20.0%")
                    ke.sendMessage(to, "███▒... 30.0%")
                    ke.sendMessage(to, "████▒... 40.0%")
                    ke.sendMessage(to, "█████▒... 50.0%")
                    ke.sendMessage(to, "██████▒... 60.0%")
                    ke.sendMessage(to, "██████▒... 70.0%")
                    ke.sendMessage(to, "████████▒... 80.0%")
                    ke.sendMessage(to, "█████████▒... 90.0%")
                    ke.sendMessage(to, "███████████..100.0%")                                          
                    ki.sendMessage(msg.to, "[ %s ความเสถียรของบอท ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ปิง ]")
                    kk.sendMessage(msg.to, "[ %s ความเสถียรของบอท ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ปิง ]")
                    kc.sendMessage(msg.to, "[ %s ความเสถียรของบอท ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ปิง ]")
                    ke.sendMessage(msg.to, "[ %s ความเสถียรของบอท ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ปิง ]")                
                elif text.lower() == 'แจก':
                        line.sendGift(msg.to,'1487739','sticker')
                        ki.sendGift(msg.to,'1487739','sticker')
                        kk.sendGift(msg.to,'1487739','sticker')
                        kc.sendGift(msg.to,'1487739','sticker')
                        ke.sendGift(msg.to,'1487739','sticker')      
                elif msg.text.lower().startswith("ยกเลิก "):
                    args = msg.text.replace("ยกเลิก ","")
                    mes = 0
                    try:
                        mes = int(args[1])
                    except:
                        mes = 1
                    M = line.getRecentMessagesV2(to, 101)
                    MId = []
                    for ind,i in enumerate(M):
                        if ind == 0:
                            pass
                        else:
                            if i._from == line.profile.mid:
                                MId.append(i.id)
                                if len(MId) == mes:
                                    break
                    def unsMes(msg_id):
                      line.unsendMessage(msg_id)
                    for i in MId:
                      thread1 = threading.Thread(target=unsMes, args=(i,))
                      thread1.start()
                      thread1.join()
                    line.sendMessage(msg.to, ' 「 ยกเลิกข้อความทำงาน 」\nยกเลิกแล้ว {} คำ'.format(len(MId)))        
                elif text.lower().startswith("ลุย "):
                    if msg.toType == 2:
                        G = line.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ki.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ki.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")                    
                    ki.sendMessage(to, say)
                    ki.leaveGroup(to) 
                elif '1มา' in text.lower():
                    if msg.toType == 2:
                        G = line.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ki.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ki.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                elif '2มา' in text.lower():
                    if msg.toType == 2:
                        G = line.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            kk.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            kk.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)      
                elif '3มา' in text.lower():
                    if msg.toType == 2:
                        G = line.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            kc.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            kc.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)      
                elif '4มา' in text.lower():
                    if msg.toType == 2:
                        G = line.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ke.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ke.acceptGroupInvitationByTicket(to, Ti)                            
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)                
                elif 'ลูกน้องมา' in text.lower():
                    if msg.toType == 2:
                        G = line.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ki.acceptGroupInvitationByTicket(to, Ti)
                            kk.acceptGroupInvitationByTicket(to, Ti)
                            kc.acceptGroupInvitationByTicket(to, Ti)
                            ke.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ki.acceptGroupInvitationByTicket(to, Ti)
                            kk.acceptGroupInvitationByTicket(to, Ti)
                            kc.acceptGroupInvitationByTicket(to, Ti)
                            ke.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                elif text.lower() == 'ถอยทัพ':
                    if msg.toType == 2:
                        ginfo = line.getGroup(to)
                        try:                      	
                            ki.leaveGroup(to)
                            kk.leaveGroup(to)
                            kc.leaveGroup(to)
                            ke.leaveGroup(to)
                        except:
                            pass
                elif text.lower() == 'ถอย1':
                    if msg.toType == 2:
                        ginfo = line.getGroup(to)
                        try:                      	
                            ki.leaveGroup(to)                            
                        except:
                            pass                       
                elif text.lower() == 'ถอย2':
                    if msg.toType == 2:
                        ginfo = line.getGroup(to)
                        try:                      	                           
                            kk.leaveGroup(to)                            
                        except:
                            pass     
                elif text.lower() == 'ถอย3':
                    if msg.toType == 2:
                        ginfo = line.getGroup(to)
                        try:                      	                            
                            kc.leaveGroup(to)                            
                        except:
                            pass              
                elif text.lower() == 'ถอย4':
                    if msg.toType == 2:
                        ginfo = line.getGroup(to)
                        try:                      	                            
                            ke.leaveGroup(to)
                        except:
                            pass              
                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")    
                elif text.lower() == 'สปีด' or text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "『กำลังทดสอบความเร็วของบอท』")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'ออน':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "เวลาการใช้งานบอท"                   
                    link = "http://line.me/ti/p/~botline2034"                    
                    eltime = time.time() - mulai
                    van = "【ระยะเวลาการทำงานของบอท】\n"+waktu(eltime)
                    line.sendFooter(receiver,van ,link ,icon,name)                    
                elif text.lower() == 'รีบอท':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "รีสตาร์ทบอท"                   
                    link = "http://line.me/ti/p/~botline2034"                    
                    line.sendFooter(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ .." ,link ,icon,name)
                    ki.sendFooter(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ .." ,link ,icon,name)
                    kk.sendFooter(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ .." ,link ,icon,name)
                    kc.sendFooter(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ .." ,link ,icon,name)
                    ke.sendFooter(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ .." ,link ,icon,name)
                    line.sendFooter(to, "『◉รีบอทเรียบร้อย◉』/nไปเอาลิ้งใหม่ได้เลย",link ,icon,name)
                    restartBot()                                  
                elif text.lower() == 'บอท':
                    try:
                        arr = []
                        owner = "u5a91f31a0882cae3e309576cc4bf1e5a"                        
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══「 ข้อมูลเรา 」"
                        ret_ += "\n╠❈ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠❈ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠❈ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠❈ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠❈ สถานะ ═ {}".format(contact.statusMessage)
                        ret_ += "\n╠❈ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══「 ข้อมูลเรา 」"
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "เกี่ยวกับเรา"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendContact(to, owner)
                        line.sendFooter(to, str(ret_),link ,icon,name)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                        line.sendImageWithURL(msg.to, "https://obs-us.line-apps.com/myhome/h/download.nhn?oid=b47baa544f21093f4dcfe97658f4a582")                                        
                elif msg.text.lower().startswith("กลุ่ม"):
                    line.sendMessage(to, "กำลังตรวจสอบข้อมูล...")
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        G = line.getGroupIdsJoined()
                        cgroup = line.getGroups(G)
                        ngroup = ""
                        for mention in mentionees:
                         for x in range(len(cgroup)):
                           gMembMids = [contact.mid for contact in cgroup[x].members]
                           if mention['M'] in gMembMids:
                                ngroup += "\n➢ " + cgroup[x].name + " | สมาชิก: " +str(len(cgroup[x].members))    
                        if ngroup == "":
                             line.sendMessage(to, "ไม่พบ")
                        else:
                             line.sendMessage(to, "➢ตรวจพบอยู่ในกลุ่ม %s"%(ngroup))
                elif text.lower() == 'ยกค้างเชิญ':    
#                    if msg.toType == 2:
#                        G = line.getGroup(to)
#                        if G.preventedJoinByTicket == False:
#                            line.updateGroup(G)
#                            invsend = 0
#                            Ti = line.reissueGroupTicket(to)
#                            ki.acceptGroupInvitationByTicket(to, Ti)                            
#                            G.preventedJoinByTicket = True
#                            line.updateGroup(G)
#                        else:
#                            G.preventedJoinByTicket = False
#                            line.updateGroup(G)
#                            invsend = 0
#                            Ti = line.reissueGroupTicket(to)
#                            ki.acceptGroupInvitationByTicket(to, Ti)                            
#                            G.preventedJoinByTicket = True
#                            line.updateGroup(G)                            
                                    if msg.toType == 2:
                                        group = ki.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//30
                                        ki.sendMessage(msg.to,"[ ยกค้างเชิญ จำนวน {} คน] \nรอสักครู่...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*30 : (i+1)*30]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                ki.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            ki.sendMessage(receiver,"พัก 10-15 วินาที แล้ว จะทำการ ยกต่อ 30 คน\nผู้สร้างบอทสนใจใช้บอทกรุณาติดต่อ≧∇≦\n☆➣ http://line.me/ti/p/~botline2034 \n☆➣ http://line.me/ti/p/~l581-1")
                                            time.sleep(random.uniform(15,10))
                                        ki.sendMessage(receiver,"[ ยกค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))                                        
                                        gname = ki.getGroup(receiver).name
                                        ki.sendMessage(Notify,"[ ยกค้างเชิญ >> "+gname+"  <<] \n จำนวน {} คน เรียบร้อยแล้ว\nผู้สร้างบอทสนใจใช้บอทกรุณาติดต่อ≧∇≦\n║͜͡☆➣ http://line.me/ti/p/~botline2034 \n☆➣ http://line.me/ti/p/~l581-1".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        ki.leaveGroup(receiver)                                								
                                    ki.sendMessage(receiver,"[ไม่มีคนให้ผมยกเชิญบาย]")     
                                    ki.sendContact(to, "u5a91f31a0882cae3e309576cc4bf1e5a")                               
                                    ki.sendMessage(receiver)
#==============================================================================#                             
#==============================================================================#
                elif text.lower() == 'เชคค่า':
                    try:
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ระบบตั้งค่า"                   
                        link = "http://line.me/ti/p/~botline2034"                      
                        ret_ = "╔════[ สถานะบอท ]═════┓"                        
                        if settings["autoAdd"] == True: ret_ += "\n╠✼ ออโต้แอด「เปิด」"
                        else: ret_ += "\n╠✼ ออโต้แอด「ปิด」"
                        if settings["autoBlock"] == True: ret_ += "\n╠✼ ออโต้บล็อค「เปิด」"
                        else: ret_ += "\n╠✼ ออโต้บล็อค「ปิด」"
                        if settings["autoJoinTicket"] == True: ret_ += "\n╠✼ มุดลิ้ง「เปิด」"
                        else: ret_ += "\n╠✼ มุดลิ้ง「ปิด」"
                        if settings["autoJoin"] == True: ret_ += "\n╠✼ เข้าห้องออโต้「เปิด」"
                        else: ret_ += "\n╠✼ เข้าห้องออโต้「ปิด」"
                        if settings["Api"] == True: ret_ += "\n╠✼ ตอบอัติโนมัติ「เปิด」"
                        else: ret_ += "\n╠✼ ตอบอัติโนมัติ「ปิด」"
                        if settings["Aip"] == True: ret_ += "\n╠✼ แสกนคำพูด+คำสั่งบิน「เปิด」"
                        else: ret_ += "\n╠✼ แสกนคำพูด+คำสั่งบิน「ปิด」"
                        if settings["Wc"] == True: ret_ += "\n╠✼ ข้อความต้อนรับสมาชิก「เปิด」"
                        else: ret_ += "\n╠✼ ข้อความต้อนรับสมาชิก「ปิด」"
                        if settings["Lv"] == True: ret_ += "\n╠✼ ข้อความอำลาสมาชิก「เปิด」"
                        else: ret_ += "\n╠✼ ข้อความอำลาสมาชิก「ปิด」"
                        if settings["Nk"] == True: ret_ += "\n╠✼ ข้อความแจ้งเตือนคนลบ「เปิด」"
                        else: ret_ += "\n╠✼ ข้อความแจ้งเตือนคนลบ「ปิด」"
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠✼ ปฏิเสธกลุ่มเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " →「เปิด」"
                        else: ret_ += "\n╠✼ ปฏิเสธกลุ่มเชิญ「ปิด」"						
                        if settings["autoLeave"] == True: ret_ += "\n╠✼ ออกแชทรวม 「เปิด」"
                        else: ret_ += "\n╠✼ ออกแชทรวม「ปิด」"
                        if settings["autoRead"] == True: ret_ += "\n╠✼ อ่านออโต้「เปิด」"
                        else: ret_ += "\n╠✼ อ่านออโต้「ปิด」"				
                        if settings["checkContact"] == True: ret_ += "\n╠✼ อ่านคท「เปิด」"
                        else: ret_ += "\n╠✼ อ่านคท「ปิด」"
                        if settings["checkPost"] == True: ret_ += "\n╠✼ เช็คโพส「เปิด」"
                        else: ret_ += "\n╠✼ เช็คโพส「ปิด」"
                        if settings["checkSticker"] == True: ret_ += "\n╠✼ เช็คติก「เปิด」"
                        else: ret_ += "\n╠✼ เช็คติก「ปิด」"
                        if settings["detectMention"] == True: ret_ += "\n╠✼ ตอบกลับคนแทค「เปิด」"
                        else: ret_ += "\n╠✼ ตอบกลับคนแทค「ปิด」"
                        if settings["potoMention"] == True: ret_ += "\n╠✼ แสดงภาพคนแทค「เปิด」"
                        else: ret_ += "\n╠✼ แสดงภาพคนแทค「ปิด」"
                        if settings["kickMention"] == True: ret_ += "\n╠✼ เตะคนแทค「เปิด」"
                        else: ret_ += "\n╠✼ เตะคนแทค「ปิด」"
                        if settings["delayMention"] == True: ret_ += "\n╠✼ แทคกลับคนแทค「เปิด」"
                        else: ret_ += "\n╠✼ แทคกลับคนแทค「ปิด」"
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠✼ กันเชิญ「เปิด」"
                        else: ret_ += "\n╠✼ กันเชิญ「ปิด」"
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠✼ กันยกเชิญ「เปิด」"
                        else: ret_ += "\n╠✼ กันยกเชิญ「ปิด」"
                        if RfuProtect["protect"] == True: ret_ += "\n╠✼ ป้องกัน「เปิด」"
                        else: ret_ += "\n╠✼ ป้องกัน「ปิด」"
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠✼ ป้องกันเปิดลิ้ง「เปิด」"
                        else: ret_ += "\n╠✼ ป้องกันเปิดลิ้ง「ปิด」"
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠✼ ป้องกันสมาชิก「เปิด」"
                        else: ret_ += "\n╠✼ ป้องกันสมาชิก「ปิด」"
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠✼ ป้องกันเข้ากลุ่ม「เปิด」"
                        else: ret_ += "\n╠✼ ป้องกันเข้ากลุ่ม「ปิด」"						
                        ret_ += "\n╚════[ สถานะบอท ]═════┛"
                        line.sendFooter(to, str(ret_),link ,icon,name)
                        line.sendMentionFooter(to, str(settings["me"]), sender, "https://line.me/ti/p/~botline2034", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~botline2034', 'type': 'mt', 'subText': str(settings["icon"]), 'a-installUrl': 'https://line.me/ti/p/~botline2034', 'a-installUrl': ' https://line.me/ti/p/~botline2034', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~botline2034', 'i-linkUri': 'https://line.me/ti/p/~botline2034', 'id': 'mt000000000a6b79f9', 'text': 'ᎠᎬᏞᎬᎢ', 'linkUri': 'https://line.me/ti/p/~botline2034'}, contentType=19)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))                
                elif text.lower() == 'เปิดแอด':
                    settings["autoAdd"] = True
                    settings["autoBlock"] = False
                    RfuProtect["autoAdd"] == True
                    RfuProtect["autoBlock"] == False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดรับแอดออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดบล็อค':
                    settings["autoBlock"] = True
                    settings["autoAdd"] = False
                    RfuProtect["autoBlock"] == True
                    RfuProtect["autoAdd"] == False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดบล็อคแอดออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดแอด':
                    settings["autoAdd"] = False
                    RfuProtect["autoAdd"] == False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดรับแอดออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดบล็อค':
                    settings["autoBlock"] = False
                    RfuProtect["autoBlock"] == False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดบล็อคแอดออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดเข้า':
                    settings["autoJoin"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดเข้าห้องออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดเข้า':
                    settings["autoJoin"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดเข้าห้องออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดรี':
                    settings["RText"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดรีข้อความที่ยกเลิกแล้ว",link ,icon,name)
                elif text.lower() == 'ปิดรี':
                    settings["RText"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดรีข้อความที่ยกเลิกแล้ว",link ,icon,name)
                elif "gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"ปิดใช้งานระบบปฏิเสธคำเชิญตามจำนวนสมาชิก")
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to, " สมาชิกในกลุ่มที่ไม่ถึง" + strnum + "จะถูกปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,str(settings["eror"]))
                        else:
                                line.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == 'เปิดออก':
                    settings["autoLeave"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดออกแชทรวมออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดออก':
                    settings["autoLeave"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดออกแชทรวมออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดอ่าน':
                    settings["autoRead"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดอ่านออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดอ่าน':
                    settings["autoRead"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดอ่านออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดติก':
                    settings["checkSticker"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดเชคติ๊กแล้ว",link ,icon,name)
                elif text.lower() == 'ปิดติก':
                    settings["checkSticker"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดเชคติ๊กแล้ว",link ,icon,name)
                elif text.lower() == 'เปิดมุด':
                    settings["autoJoinTicket"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดมุดลิ้งแล้ว",link ,icon,name)
                elif text.lower() == 'ปิดมุด':
                    settings["autoJoinTicket"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดมุดลิ้งแล้ว",link ,icon,name)
                elif text.lower() == 'เปิดเตะคท':
                    settings["kickContact"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "เปิดเตะคทแล้ว",link ,icon,name)
                elif text.lower() == 'ปิดเตะคท':
                    settings["kickContact"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT DETELE"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ปิดเตะคทแล้ว",link ,icon,name)
#==============================================================================#               
                elif text.lower() == "คท" or text.lower()  == "me":
                    line.sendMentionFooter(to, str(settings["me"]), sender, "https://line.me/ti/p/~botline2034", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~botline2034', 'type': 'mt', 'subText': str(settings["icon"]), 'a-installUrl': 'https://line.me/ti/p/~botline2034', 'a-installUrl': ' https://line.me/ti/p/~botline2034', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~botline2034', 'i-linkUri': 'https://line.me/ti/p/~botline2034', 'id': 'mt000000000a6b79f9', 'text': 'ᎠᎬᏞᎬᎢ', 'linkUri': 'https://line.me/ti/p/~botline2034'}, contentType=19)
                elif text.lower() == 'คิก':
                    line.sendContact(to, kiMID)
                    line.sendContact(to, kkMID)
                    line.sendContact(to, kcMID)
                    line.sendContact(to, keMID)                
                elif text.lower() == "ไอดี":
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendFooter(to, "MID :\n"+str(sender), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif msg.text.lower().startswith("เทส"):                   
                   start = time.time()
                   line.sendMessage(to, "รอสักครู่...  ")
                   elapsed_time = time.time() - start
                   line.sendMessage(to, "[ %s ความเร็วบอท ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ปิง ]")
                elif text.lower() == "ชื่อ":
                     h = line.getContact(lineMID)
                     userid = "https://line.me/ti/p/~" + line.profile.userid
                     line.sendFooter(to, "ชื่อเรา :\n"+str(h.displayName), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif text.lower() == "ตัส":
                    h = line.getContact(lineMID)
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendFooter(to, "ตัสเรา :\n"+str(h.statusMessage), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif text.lower() == "ข้อมูล":
                    contact = line.getContact(lineMID)
                    cu = line.getProfileCoverURL(lineMID)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendImageWithFooter(to, image, userid, image, line.getContact(sender).displayName)
                    line.sendImageWithFooter(to, path, userid, path, line.getContact(sender).displayName)
                    line.sendFooter(to, "ดิส\nมิด : "+str(sender)+"\nชื่อ : "+str(contact.displayName)+"\nตัส :\n"+str(contact.statusMessage), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif text.lower() == "ดิส":
                    h = line.getContact(lineMID)
                    image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendImageWithFooter(to, image, userid, image, line.getContact(sender).displayName)
                elif text.lower() == "ปก":
                    h = line.getContact(lineMID)
                    cu = line.getProfileCoverURL(lineMID)
                    image = str(cu)
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendImageWithFooter(to, image, userid, image, line.getContact(sender).displayName)                            
                elif text.lower() == 'ผู้สร้าง':                   
                    line.sendContact(to, "u5a91f31a0882cae3e309576cc4bf1e5a")                    
                elif text.lower() == 'คอมเม้น':                    
                    line.sendMessage(msg.to,str(settings["comment"])) 
                elif text.lower() == 'ทักคท':                    
                    line.sendMessage(msg.to,str(settings["me"]))                
                elif text.lower() == 'ส่วนตัว':                    
                    line.sendMessage(msg.to, str(settings["phu"]))
                elif text.lower() == 'ทักเข้า':               	    
                    line.sendMessage(msg.to, str(settings["welcome"]))
                elif text.lower() == 'ทักออก':                    
                    line.sendMessage(msg.to, str(settings["bye"]))
                elif text.lower() == 'ทักเตะ':               	    
                    line.sendMessage(msg.to, str(settings["kick"]))
                elif text.lower() == 'คนแอด':               	    
                    line.sendMessage(msg.to, str(settings["message"]))
                elif text.lower() == 'คนแทค':              	    
                    line.sendMessage(msg.to, str(settings["Respontag"]))
                elif text.lower() == 'แทคล่อง':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "ม่มีคนใส่ร่องหนในกลุ่มนี้ðﾟﾘﾂ")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'ไอดีล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีmidคนใส่ร่องหนðﾟﾤﾗ")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == 'คทล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้ðﾟﾘﾂ")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("ไอดี "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)                          
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                        for ls in lists:                           
                            line.findAndAddContactsByMid(ls)
                        line.sendMessage(to, "เพิ่มเพื่อนแล้ว!")
                elif msg.text.lower().startswith("ลบเพื่อน "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            line.deleteContact(ls)
                        line.sendMessage(to, "ลบออกจากการเป็นเพื่อนแล้ว!")                        
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("วีดีโอ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))             
                elif msg.text.lower().startswith("ดึงหมด "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                me = line.getContact(ls)
                                path = line.getProfileCoverURL(ls)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    line.sendMessage(msg.to,"「 ชื่อที่แสดง」\n" + me.displayName)
                                    line.sendMessage(msg.to,"「 ตัสที่แสดง 」\n" + me.statusMessage)
                                    line.sendMessage(msg.to,"「 มิดที่แสดง 」\n" +  to)
                                    line.sendMessage(to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    line.sendImageWithURL(to, str(path))
                                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                else:
                                    line.sendMessage(msg.to,"「 ชื่อที่แสดง 」\n" + me.displayName)
                                    line.sendMessage(msg.to,"「 ตัสที่แสดง 」\n" + me.statusMessage)
                                    line.sendMessage(msg.to,"「 มิดที่แสดง 」\n" + ls)
                                    line.sendMessage(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                    line.sendMessage(to, str(path))
                            else:
                                line.sendMessage(to, "Talk Exception You are not Related to LineChannel")
                    else:
                         line.sendMessage(to, "Talk Exception You are not Related to LineChannel")                                
                elif msg.text.lower().startswith("แปลงร่าง "):        
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
                            line.sendMentionFooter(to, 'copy\n', sender, "http://line.me/ti/p/~botline2034", "http://dl.profile.line-cdn.net/"+phusui.getContact(sender).pictureStatus, phusui.getContact(sender).displayName);phusui.sendMessage(to, phusui.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+phusui.getContact(sender).pictureStatus, 'i-installUrl': 'http://line.me/ti/p/~botline2034', 'type': 'mt', 'subText': " ", 'a-installUrl': 'http://line.me/ti/p/~botline2034', 'a-installUrl': ' http://line.me/ti/p/~botline2034', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'http://line.me/ti/p/~botline2034', 'i-linkUri': 'http://line.me/ti/p/~botline2034', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'http://line.me/ti/p/~botline2034'}, contentType=19)							
                            line.sendMessage(to,"คัดลอกบัญชีเรียบร้อยแล้ว", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+phusui.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'https://bit.ly/2JpqZ7H'})                               
                elif text.lower() == 'ดึงหมด':
                    if line != None:
                        me = line.getContact(to)
                        path = line.getProfileCoverURL(to)
                        path = str(path)
                        if settings["server"] == "VPS":
                            line.sendMessage(to,"「 ชื่อที่แสดง 」\n" + me.displayName)
                            line.sendMessage(to,"「 ตัสที่แสดง 」\n" + me.statusMessage)
                            line.sendMessage(to,"「 มิดที่แสดง 」\n" +  to)
                            line.sendMessage(to, text=None, contentMetadata={'mid': to}, contentType=13)
                            line.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                            line.sendImageWithURL(to, str(path))
                            line.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                        else:
                            line.sendMessage(to,"「 ชื่อที่แสดง 」\n" + me.displayName)
                            line.sendMessage(to,"「 ตัสที่แสดง 」\n" + me.statusMessage)
                            line.sendMessage(to,"「 มิดที่แสดง 」\n" +  to)
                            line.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            line.sendImageWithURL(to, str(path))
                    else:
                        line.sendMessage(to, "Talk Exception")                         
                elif msg.text in ["Allprotect on","เปิดกันห้อง"]:
                        settings["kickMention"] = True
                        settings["Aip"] = False
                        RfuProtect["protect"] = True
                        RfuProtect["cancelprotect"] = True
                        RfuProtect["inviteprotect"] = True 
                        RfuProtect["linkprotect"] = True 
                        RfuProtect["Protectguest"] = True
                        RfuProtect["Protectjoin"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด เปิดðﾟﾑﾌ")
						
                elif msg.text in ["Allprotect off","ปิดกันห้อง"]:
                        settings["kickMention"] = False
                        settings["Aip"] = False
                        RfuProtect["protect"] = False
                        RfuProtect["cancelprotect"] = False
                        RfuProtect["inviteprotect"] = False 
                        RfuProtect["linkprotect"] = False 
                        RfuProtect["Protectguest"] = False
                        RfuProtect["Protectjoin"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด ปิดðﾟﾑﾌ")
                        
                elif msg.text in ["Allmsg on","เปิดข้อความ"]:
                        settings["Wc"] = True
                        settings["Lv"] = True
                        settings["Nk"] = True
                        settings["autoRead"] = True
                        settings["checkSticker"] = True 
                        settings["checkContact"] = True 
                        settings["checkPost"] = True
                        settings["potoMention"] = True
                        settings["detectMention"] = True
                        settings["delayMention"] = True
                        settings["Api"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด เปิดðﾟﾑﾌ")
						
                elif msg.text in ["Allmsg off","ปิดข้อความ"]:
                        settings["Wc"] = False
                        settings["Lv"] = False
                        settings["Nk"] = False
                        settings["autoRead"] = True
                        settings["checkSticker"] = False 
                        settings["checkContact"] = False 
                        settings["checkPost"] = False
                        settings["detectMention"] = False
                        settings["potoMention"] = False
                        settings["delayMention"] = False
                        settings["Api"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด ปิดðﾟﾑﾌ")
#==============================================================================#
                elif msg.text.lower().startswith("เพิ่ม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("ลบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'เลียนแบบ':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "เลียนแบบ" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "เปิด":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "ปิด":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")                
                elif "หา:" in msg.text:
                    mmid = msg.text.replace("หา:","")
                    line.sendMessage(to, text=None, contentMetadata={'mid': mmid}, contentType=13)
                elif msg.text.lower().startswith("ไลน์ "):
                    id = msg.text.lower().replace("ไลน์ ","")
                    conn = line.findContactsByUserid(id)
                    if True:                                      
                        line.sendMessage(to,"http://line.me/ti/p/~" + id)
                        line.sendContact(to,conn.mid)
                elif "รัว " in msg.text:                
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ระบบรัวข้อความตามที่เราสั่ง"                   
                    link = "http://line.me/ti/p/~botline2034"                    
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("รัว "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "เริ่ม":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                             line.sendFooter(msg.to, teks ,link ,icon,name)
                        else:
                           line.sendFooter(msg.to, "Out of Range!" ,link ,icon,name)
                    elif txt[1] == "พอ":
                        if jmlh <= 100000:
                            line.sendFooter(msg.to, tulisan ,link ,icon,name)
                        else:
                            line.sendFooter(msg.to, "Out Of Range!" ,link ,icon,name)
#==============================================================================#
                elif text.lower() == 'แอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid                    
                    line.sendContact(to, GS)
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ใช้ได้แต่ในกลุ่มเท่านั้น"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "☝คนนี้แหล่ะคนสร้างกลุ่มนี้" ,link ,icon,name)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ใช้ได้แต่ในกลุ่มเท่านั้น"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ไอดีกลุ่ม \n" + gid.id ,link ,icon,name)
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ใช้ได้แต่ในกลุ่มเท่านั้น"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, "ชื่อกลุ่ม -> \n" + gid.name ,link ,icon,name)
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "ลิ้งของกลุ่ม\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "คนนี้คือผู้สร้างกลุ่มนี้"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่มðﾟﾑﾉ : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ใช้ได้แต่ในกลุ่มเท่านั้น"                   
                    link = "http://line.me/ti/p/~botline2034"
                    line.sendFooter(to, str(ret_),link ,icon,name)
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'สมาชิกกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'เช็คกลุ่ม':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))				                                     
                elif msg.text.lower().startswith("ถาม "):
                    kata = msg.text.lower().replace("ถาม ", "")
                    sch = kata.replace(" ","+")
                    with _session as web:
                        urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                        r = _session.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                        data = r.text
                        data = json.loads(data)
                        url = data["shorturl"]
                        ret_ = "「Ask」"
                        ret_ += "\n\nLink : {}".format(str(url))
                        line.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("บล็อคไอดี "):
                    user = msg.text.lower().replace("บล็อคไอดี ","")
                    line.blockContact(user)
                    line.sendMessage(to, "ทำการบล็อคไอดีนั้นแล้ว")                        
                elif "phu" in msg.text:
                    spl = msg.text.split("phu")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)
                elif "แตก" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                            line.sendMessage(msg.to,"แตก1สวยพี่สวย")                
                elif "มุด " in msg.text.lower():
                    spl = re.split("มุด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))
                elif msg.text.lower().startswith("โทร "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        members = [mem.mid for mem in group.members]
                        line.acquireGroupCallRoute(to)
                        line.inviteIntoGroupCall(to, contactIds=members)
                    else:
                        line.sendMessage(to, "เชิญแล้วฮ่าๆ".format(str(jml)))
                elif msg.text.lower().startswith("แทค "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
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
                                contact = line.getContact(receiver)
                                RhyN_(to, contact.mid)                
                elif msg.text.lower().startswith("แจก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
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
                                line.sendGit(msg.to,'1487739','sticker')
                                line.sendMessage(to, "ส่งของขวัญใน ส.ต แล้ว".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("ไวรัส "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
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
                                line.sendMessage(receiver, ".God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                line.sendMessage(to, "ไปดูแชทด้วยนะด้วยความหวังดี".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("ส่วนตัว "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
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
                                line.sendMessage(receiver, str(settings["phu"]))
                                line.sendMessage(to, "ไปดูแชทด้วยนะครับ")
                            else:
                                pass
                elif msg.text.lower().startswith("ทัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = line.getContact(to)
                        RhyN_(to, name.mid)
                elif msg.text.lower() == ".":
                    if msg.toType == 0:
                        sendMention(to, to, "", "")
                    elif msg.toType == 2:
                        group = line.getGroup(to)
                        contact = [mem.mid for mem in group.members]
                        mentionMembers(to, contact)
                elif msg.text.lower().startswith("คำห้ามพิม "):
                    wban = msg.text.lower().split()[1:]
                    wban = " ".join(wban)
                    wbanlist.append(wban)
                    line.sendMessage(to,"%s พิมคำนี้อาจมีปลิวนะ."%wban)
                elif msg.text.lower().startswith("ล้างคำห้ามพิม "):
                    wunban = msg.text.lower().split()[1:]
                    wunban = " ".join(wunban)
                    if wunban in wbanlist:
                        wbanlist.remove(wunban)
                        line.sendMessage(to,"%s ล้างออกจากคำสั่งห้ามพิมแล้ว."%wunban)
                    else:
                        line.sendMessage(to,"%s is not blacklisted."%wunban)
                elif msg.text.lower() == 'เช็คคำห้ามพิม':
                    tst = "คำห้ามพิม:\n"
                    if len(wbanlist) > 0:
                        for word in wbanlist:
                            tst += "- %s"%word
                        line.sendMessage(msg.to,tst)
                    else:
                        line.sendMessage(msg.to,"คำที่ห้ามพิมทั้งหมด")               
                elif text.lower() == 'แทค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//2
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += "@Alin \n"
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)                        
#                        line.sendFooter(to,"\n[ จำนวนแทคทั้งหมด {} คน]".format(str(len(nama))),link ,icon,name)                
                elif "ประกาศ " in msg.text:                	
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความประกาศ"
                    link = "http://line.me/ti/p/~botline2034"
                    bc = msg.text.replace("ประกาศ ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendFooter(i,"••••••[ข้อความประกาศแชท]••••••\n\n"+bc+"\n\n『◉⊰ᎢᎬᎪᎷ ᏴØᎢ ᎠᎬᏞᎬᎢ⊱◉』",link ,icon,name)
                elif "ประกาศแชท " in msg.text:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความประกาศ"
                    link = "http://line.me/ti/p/~botline2034"
                    bc = msg.text.replace("ประกาศแชท ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendFooter(i,"======[ข้อความประกาศแชท]======\n\n"+bc+"\n\n『◉⊰ᎢᎬᎪᎷ ᏴØᎢ ᎠᎬᏞᎬᎢ⊱◉』",link ,icon,name)
                    
                elif "ส่งรูปภามตามแชท: " in msg.text:
                    bc = msg.text.replace("ส่งรูปภาพตามแชท: ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
                elif "ส่งเสียงกลุ่ม " in msg.text:
                    bctxt = msg.text.replace("ส่งเสียงกลุ่ม ", "")
                    bc = ("บาย...ภู...เป็ด...เซลบอท...ไลน์")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "ส่งเสียงแชท " in msg.text:
                    bctxt = msg.text.replace("ส่งเสียงแชท ", "")
                    bc = ("บาย...ภู...เป็ด...เซลบอท...ไลน์")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')
                    
                elif text.lower() == 'ปฏิทิน':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ปฏิทิน"
                    link = "http://line.me/ti/p/~botline2034"
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "ðﾟﾌﾀปฏิทินðﾟﾌﾀ\n\n❄️⚡ðﾟﾎﾃ❄️⚡ðﾟﾎﾃ❄️⚡ðﾟﾎﾃ❄️⚡ðﾟﾎﾃðﾟﾌﾀ" + "\n\nðﾟﾐﾼ" + hasil + "\nðﾟﾐﾼ ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\nðﾟﾐﾼ เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "ðﾟﾌﾀ❄️⚡❄️⚡❄️⚡❄️⚡❄️⚡ðﾟﾌﾀ" + "\n\nBY: PHU SELF BOT LINE"
                    line.sendFooter(msg.to, readTime ,link ,icon,name)

                elif "รูปมา " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "กาตูน " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            phusui.sendImageWithURL(to, str(path))
      
                elif "ยูทูป " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "ค้น " in msg.text.lower():
                    spl = re.split("ค้น ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        line.sendText(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    else:
                                        line.sendText(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                    text = "ผลการค้นหาจาก Google:\n\n"
                                    for el in resp.findAll("h3",attrs={"class":"r"}):
                                        try:
                                                tmp = el.a["class"]
                                                continue
                                        except:
                                                pass
                                        try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                        except:
                                                continue
                                        text += el.a.text+"\n"
                                        text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                    text = text[:-2]
                                    if msg.toType != 0:
                                        line.sendText(msg.to,str(text))
                                    else:
                                        line.sendText(msg.from_,str(text))
                                except Exception as e:
                                    print(e)
                        
                elif "วีดีโอ " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "วีดีโอ ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "หนัง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "หนัง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "เพลง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "เพลง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["เปิดแอบ"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"เปิดระบบแสกนคนอ่านอัตโนมัติ")
                elif msg.text in ["ปิดแอบ"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "ปิดระบบแสกนคนอ่านแล้ว")

                elif text.lower() == 'ปิดเชล':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)
                elif text.lower() == "ลบแชท":
                        if msg._from in lineMID:
                            try:
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"ลบทุกการแชทเรียบร้อย")
                            except:
                                pass
                                print ("/ลบแชท")
                elif text.lower() == 'เพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="ðﾟﾎﾎรายชื่อเพื่อนทั้งหมดðﾟﾎﾎ"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\nðﾟﾎﾎรายชื่อเพื่อนทั้งหมดðﾟﾎﾎ\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["บล็อค"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════ไม่มีรายการบัญชีที่ถูกบล็อค═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════รายการบัญชีที่ถูกบล็อค════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["ไอดีเพื่อน"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════รายการไอดีเพื่อน═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════รายการ ไอดีเพื่อน═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == "/เว็บโป๊":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")
                elif msg.text == "/ประกาศ":
                	line.sendMessage(msg.to,str(settings["message1"]))
                elif msg.text.lower() == '/ดึงแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Typeðﾟﾑﾉ Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["?ไม่รับเชิญ"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)							
                        except:
                            pass
                elif msg.text in ["ไอดีทั้งห้อง"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="『◉⊰PHUSUI⊱◉』"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)
                    
                elif msg.text in ["เปิดเตะแทค"]:
                    settings["kickMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบเตะคนแท็ก(○ﾟεﾟ○)")
                
                elif msg.text in ["ปิดเตะแทค"]:
                    settings["kickMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบเตะคนแท็ก(○ﾟεﾟ○)")
                    
                elif msg.text in ["เปิดแทค","Tag on"]:
                        settings['detectMention'] = True
                        line.sendMessage(msg.to,"เปิดระบบตอบกลับคนแทค(○ﾟεﾟ○)")
                
                elif msg.text in ["ปิดแทค","Tag off"]:
                        settings['detectMention'] = False
                        line.sendMessage(msg.to,"ปิดระบบตอบกลับคนแทค(○ﾟεﾟ○)")

                elif msg.text in ["เปิดแทค2","Tag2 on"]:
                    settings["potoMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบส่งรูปคนแทค(○ﾟεﾟ○)")
                
                elif msg.text in ["ปิดแทค2","Tag2 off"]:
                    settings["potoMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบส่งรูปคนแทค(○ﾟεﾟ○)")
                    
                elif msg.text in ["เปิดแทค3","Tag3 on"]:
                    settings["delayMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบแทคกลับคนแทค(○ﾟεﾟ○)")
                
                elif msg.text in ["ปิดแทค3","Tag3 off"]:
                    settings["delayMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบแทคกลับคนแทค(ˉ(∞)ˉ)")
                elif msg.text.lower() == "เปิดแทคแชท":
                    settings["detectMentionPM"] = True
                    line.sendMessage(msg.to,"เปิดแทคแชทเรียบร้อยครับ")
                elif msg.text.lower() == "ปิดแทคแชท":
                    settings["detectMentionPM"] = False
                    line.sendMessage(msg.to,"ปิดแทคแชทเรียบร้อยครับ")
                elif msg.text.lower().startswith("แทคแชท "):
                    text = msg.text.lower().replace("แทคแชท ","")                    
                    settings["pmMessage"] = text
                    line.sendMessage(msg.to, "คำแทคแชท สต คือ : {}".format(str(settings["pmMessage"])))                   
                elif msg.text in ["เปิดกันบิน"]:
                    settings["Aip"] = True
                    line.sendMessage(msg.to,"เปิดระบบตรวจสอบคำหยาบกับบอทบิน^ω^")            
                elif msg.text in ["ปิดกันบิน"]:
                    settings["Aip"] = False
                    line.sendMessage(msg.to,"ปิดระบบตรวจสอบคำหยาบกับบอทบินแล้วʕ•ﻌ•ʔ")                    
                elif msg.text in ["เปิดพูด"]:
                    settings["Api"] = True
                    line.sendMessage(msg.to,"เปิดระบบApiข้อความ")                
                elif msg.text in ["ปิดพูด"]:
                    settings["Api"] = False
                    line.sendMessage(msg.to,"ปิดระบบApiข้อความแล้ว")                    
                elif 'ตั้งแอด ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแอด ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                         settings["message"] = spl
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")         
                elif 'ไอคอน ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ไอคอน ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                         settings["icon"] = spl
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                elif 'ทักคท ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ทักคท ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                         settings["me"] = spl
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")               
                elif 'คอมเม้น ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('คอมเม้น ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                         settings["comment"] = spl
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                elif 'รันแชท ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('รันแชท ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                         settings["phu"] = spl
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")                     
                elif 'ตั้งแทค ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแทค ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                         settings["Respontag"] = spl
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")                         
                elif 'ตั้งเตะ ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งเตะ ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                          settings["kick"] = spl
                          line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                elif 'ตั้งออก ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งออก ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                          settings["bye"] = spl
                          line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                elif 'ตั้งเข้า ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งเข้า ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                     else:
                          settings["welcome"] = spl
                          line.sendMessage(msg.to, "ตั้งข้อความเรียบร้อยแล้วครับ")
                elif msg.text.lower() == "เปิดเตะติก":
                        settings["sticker"] = True
                        line.sendMessage(to,"เปิดเตะคนรันสติกเกอรแล้ว")
                elif msg.text.lower() == "ปิดเตะติก":
                        settings["sticker"] = False
                        line.sendMessage(to,"ปิดเตะคนรันสติกเกอรแล้ว")              
                elif msg.text.lower() == "ติกออก":
                        msgSticker = settings["messageSticker"]["listSticker"]["คนออก"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกออก":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "คนออก"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติกคนออก":
                    settings["messageSticker"]["listSticker"]["คนออก"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว")
                elif msg.text.lower() == "ติกเตะ":
                        msgSticker = settings["messageSticker"]["listSticker"]["คนเตะ"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกเตะ":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "คนเตะ"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติกเตะ":
                    settings["messageSticker"]["listSticker"]["คนเตะ"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเตะแล้ว")
                elif msg.text.lower() == "ติกเข้า":
                        msgSticker = settings["messageSticker"]["listSticker"]["คนเข้า"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกเข้า":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "คนเข้า"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติกเข้า":
                    settings["messageSticker"]["listSticker"]["คนเข้า"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว")
                elif msg.text.lower() == "ติกภู":
                        msgSticker = settings["messageSticker"]["listSticker"]["ภู"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกภู":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "ภู"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติกเข้า":
                    settings["messageSticker"]["listSticker"]["ภู"] = None
                    line.sendMessage(to, "ลบสติกเกอรภูแล้ว")
                elif msg.text.lower()== "ติกแอด":
                        msgSticker = settings["messageSticker"]["listSticker"]["คนแอด"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower()== "ตั้งติกแอด":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "คนแอด"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติกแอด":
                    settings["messageSticker"]["listSticker"]["คนแอด"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนแอดแล้ว")
                elif msg.text.lower() == "ติกแทค":
                        msgSticker = settings["messageSticker"]["listSticker"]["คนแทค"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกแทค":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "คนแทค"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กคนแทค":
                    settings["messageSticker"]["listSticker"]["คนแทค"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว")
                elif msg.text.lower() == "ตั้งติกแอบ":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "คนแอบ"
                    line.sendMessage(to, "ส่งสติ๊กเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติกแอบ":
                    settings["messageSticker"]["listSticker"]["คนแอบ"] = None
                    line.sendMessage(to, "ลบสติ๊กเกอรคนแอบอ่านแล้ว")
                elif msg.text.lower() == "ติกแอบ":
                        msgSticker = settings["messageSticker"]["listSticker"]["คนแอบ"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)                
                elif msg.text in ["ดึง"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"ลงคทคนที่จะดึงเข้าห้องเลยครับ")                                                            
                elif msg.text in ["ดำ"]:
                  if msg._from in admin: 
                    settings["wblacklist"] = True
                    line.sendText(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["ขาว"]:
                  if msg._from in admin: 
                    settings["dblacklist"] = True
                    line.sendText(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["ล้างดำ"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบัญชีดำทั้งหมดเรียร้อย")
                    print ("Clear Ban")
                elif msg.text.lower() == "คทดำ":
                    if msg._from in lineMID:
                        if settings["blacklist"] == []:
                            line.sendMessage(to, "Nothing boss")
                        else:
                            for bl in settings["blacklist"]:
                                line.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif 'สอย' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka ðﾟﾘﾫ")                               
                elif 'เชิญ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki.inviteIntoGroup(msg.to,[target])
                               ki.sendMessage(receiver, "Typeðﾟﾑﾉ Invite Succes")
                           except:
                               ki.sendMessage(msg.to,"Typeðﾟﾑﾉ Limit Invite")
                elif "บล็อค @" in msg.text:
                    if msg.toType == 2:
                        print ("[block] OK")
                        _name = msg.text.replace("บล็อค @","")
                        _nametarget = _name.rstrip('  ')
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            sendMassage(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                   line.blockContact(target)
                                   sendMessage(msg.to, "Success block contact~")
                                except Exception as e:
                                   print (e)
                elif msg.text.lower() == 'บล็อค':
                    blockedlist = line.getBlockedContactIds()
                    sendMessage(msg.to, "Please wait...")
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="User Blocked List\n"
                    for ids in kontak:
                        msgs+="\n%i. %s" % (num, ids.displayName)
                        num=(num+1)
                        msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                        sendMessage(msg.to, msgs)                                
                elif msg.text in ["ไล่ดำ"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")
                elif "อัพชื่อ: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อเราแล้ว " + string)                        
                elif "คิก1: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_B = ki.getProfile()
                        profile_B.displayName = string
                        ki.updateProfile(profile_B)
                        ki.sendMessage(msg.to,"เปลี่ยนชื่อคิกแล้ว " + string)            
                elif "คิก2: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_C = kk.getProfile()
                        profile_C.displayName = string
                        kk.updateProfile(profile_C)
                        kk.sendMessage(msg.to,"เปลี่ยนชื่อคิกแล้ว " + string)                        
                elif "คิก3: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_D = kc.getProfile()
                        profile_D.displayName = string
                        kc.updateProfile(profile_D)
                        kc.sendMessage(msg.to,"เปลี่ยนชื่อคิกแล้ว " + string)        
                elif "คิก4: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_E = ke.getProfile()
                        profile_E.displayName = string
                        ke.updateProfile(profile_E)
                        ke.sendMessage(msg.to,"เปลี่ยนชื่อคิกแล้ว " + string)        
                elif "อัพตัส: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนตัสเราแล้ว " + string)                        
                elif "ตัส1: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_B = ki.getProfile()
                        profile_B.statusMessage = string
                        ki.updateProfile(profile_B)
                        ki.sendMessage(msg.to,"เปลี่ยนตัสคิกแล้ว " + string) 
                elif "ตัส2: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_C = kk.getProfile()
                        profile_C.statusMessage = string
                        kk.updateProfile(profile_C)
                        kk.sendMessage(msg.to,"เปลี่ยนตัสคิกแล้ว " + string) 
                elif "ตัส3: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_D = kc.getProfile()
                        profile_D.statusMessage = string
                        kc.updateProfile(profile_D)
                        kc.sendMessage(msg.to,"เปลี่ยนตัสคิกแล้ว " + string) 
                elif "ตัส4: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_E = ke.getProfile()
                        profile_E.statusMessage = string
                        ke.updateProfile(profile_E)
                        ke.sendMessage(msg.to,"เปลี่ยนตัสคิกแล้ว " + string) 
#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'เปิดกัน':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                elif msg.text.lower() == 'ปิดกัน':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                elif msg.text.lower() == 'กันยก':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                elif msg.text.lower() == 'ปิดกันยก':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                elif msg.text.lower() == 'กันเชิญ':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                elif msg.text.lower() == 'ปิดกันเชิญ':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                elif msg.text.lower() == 'กันลิ้ง':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                elif msg.text.lower() == 'ปิดกันลิ้ง':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                elif msg.text.lower() == 'กันกลุ่ม':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                elif msg.text.lower() == 'ปิดกันกลุ่ม':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                elif msg.text.lower() == 'กันเข้า':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                elif msg.text.lower() == 'ปิดกันเข้า':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                elif msg.text.lower() == 'เปิดหมด':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                elif msg.text.lower() == 'ปิดหมด':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == 'เปิดทักเข้า':
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม(○ﾟεﾟ○)")
                elif msg.text.lower() == 'ปิดทักเข้า':
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม(○ﾟεﾟ○)")
                                
                elif msg.text.lower() == 'เปิดเตะ':
                        if settings["Nk"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Nk"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม(○ﾟεﾟ○)")
                                
                elif msg.text.lower() == 'ปิดเตะ':
                        if settings["Nk"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว(○ﾟεﾟ○)")
                        else:
                            settings["Nk"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว(○ﾟεﾟ○)")

                elif msg.text.lower() == 'เปิดทักออก':
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม(○ﾟεﾟ○)")
                elif msg.text.lower() == 'ปิดทักออก':
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม(○ﾟεﾟ○)")
                                
                elif msg.text.lower() == 'เปิดคท':
                        if settings["checkContact"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบอ่านข้อมูลด้วยคอนแทค(○ﾟεﾟ○)")
                        else:
                            settings["checkContact"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบอ่านข้อมูลด้วยคอนแทคไว้อยู่แล้ว(○ﾟεﾟ○)")
                elif msg.text.lower() == 'ปิดคท':
                        if settings["checkContact"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบอ่านข้อมูลด้วยคอนแทค(○ﾟεﾟ○)")
                        else:
                            settings["checkContact"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบอ่านข้อมูลด้วยคอนแทคไว้อยู่แล้ว(○ﾟεﾟ○)")
                elif msg.text.lower() == 'เปิดโพส':
                        if settings["checkPost"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบเช็คโพสบนทามไลน์(○ﾟεﾟ○)")
                        else:
                            settings["checkPost"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบเช็คโพสบนทามไลน์อยู่แล้ว(○ﾟεﾟ○)")
                elif msg.text.lower() == 'ปิดโพส':
                        if settings["checkPost"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบเช็คโพสบนทามไลน์(○ﾟεﾟ○)")
                        else:
                            settings["checkPost"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบเช็คโพสบนทามไลน์ไว้อยู่แล้ว(○ﾟεﾟ○)")
                elif text.lower() == "เปลี่ยนดิส":
                    settings["changePictureProfile"] = True
                    line.sendMessage(to, "ส่งรูปภาพลงมาได้เลยครับผม(○ﾟεﾟ○)")
                elif text.lower() == "เปลี่ยนรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        line.sendMessage(to, "ส่งรูปภาพลงมาได้เลยครับผม(○ﾟεﾟ○)")
                elif text.lower() == "ดับไฟ":
                    line.sendContact(to, ':)','')

                elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้วขอรับ")
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
			
                elif "ลงดำ" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("ลงดำ","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"แบนสมาชิกทุกคนในห้องนี้แล้ว＼（○＾ω＾○）／")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")   
                elif 'แบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes added for the blacklist ")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")
                elif 'ล้างแบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")                
                elif msg.text in ["เช็คดำ"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ติดดำ")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")
                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))
            elif msg.contentType == 13:
                if settings["checkContact"] == True:
                    try:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        if line != None:
                            cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            line.sendImageWithURL(to, str(path))
                        except:
                            pass
                        ret_ = "[ รายการทั้งหมดจากการสำรวจด้วยคท ]"
                        ret_ += "\n ❣️ชื่อ : {}".format(str(contact.displayName))
                        ret_ += "\n ❣️ไอดี : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n ❣️ตัส : {}".format(str(contact.statusMessage))
                        ret_ += "\n ❣️รูปโปรไฟล์ : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n ❣️รูปปก : {}".format(str(cover))
                        ret_ += "\n[ 💥สิ้นสุดการสำรวจ💥 ]"
                        line.sendMessage(to, str(ret_))
                    except:
                        line.sendMessage(to, "เกิดข้อผิดพลาดในการสำรวจ")                
            elif msg.contentType == 1:
                if settings["changePictureProfile"] == True:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changePictureProfile"] = False
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "ทำการแปลงโฉมเสร็จเรียบร้อย")
                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "เปลี่ยนรูปโปรสำเร็จแล้วครับ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.updateGroupPicture(to, path)
                        line.sendFooter(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว" ,link ,icon,name)
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "ตั้งติกแล้ว " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "ตั้งติก {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""                  
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
#==============================================================================#          
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)    
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)                
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)     
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)                
        if op.type == 13:           
            if Fam in op.param1:
                if op.param3 in settings["blacklist"]:
                    if op.param2 not in Fam:
                        G = random.choice(OPL).getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        random.choice(OPL).updateGroup(G)
                        invsend = 0                      
                        Ticket = random.choice(OPL).reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        random.choice(OPL).sendMessage(op.param1,"Don't Invite Blacklist User (′・ω・`)")              
                        random.choice(OPL).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        random.choice(OPL).updateGroup(G)
                        settings["blacklist"][op.param2] = True
        if op.type == 19:            
            if op.param3 in lineMID:
                if op.param2 in kiMID:
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    invsend = 0
                    Ticket = ki.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    ki.updateGroup(G)
                    kk.updateGroup(G)
                    kc.updateGroup(G)
                    ke.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    ki.updateGroup(G)
                    ki.updateGroup(G)
                    kk.updateGroup(G)
                    kc.updateGroup(G)
                    ke.updateGroup(G)
                else:
                    G = ki.getGroup(op.param1)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    kk.kickoutFromGroup(op.param1,[op.param2])
                    kc.kickoutFromGroup(op.param1,[op.param2])
                    ke.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    invsend = 0
                    Ticket = ki.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    ki.updateGroup(G)
                    kk.updateGroup(G)
                    kc.updateGroup(G)
                    ke.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    ki.updateGroup(G)
                    ki.updateGroup(G)
                    kk.updateGroup(G)
                    kc.updateGroup(G)
                    ke.updateGroup(G)
            if op.param3 in kiMID:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        kk.updateGroup(G)
                        kc.updateGroup(G)
                        ke.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        kk.updateGroup(G)
                        kc.updateGroup(G)
                        ke.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        kk.updateGroup(G)
                        kc.updateGroup(G)
                        ke.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        kk.updateGroup(G)
                        kc.updateGroup(G)
                        ke.updateGroup(G)        
            if op.param3 in Creator:
                    if op.param2 in lineMID:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        kk.updateGroup(G)
                        kc.updateGroup(G)
                        ke.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        kk.updateGroup(G)
                        kc.updateGroup(G)
                        ke.updateGroup(G)
                    else:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        kk.updateGroup(G)
                        kc.updateGroup(G)
                        ke.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)    
                        kk.updateGroup(G)
                        kc.updateGroup(G)
                        ke.updateGroup(G)
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])
        
        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])

        if op.type == 5:
            if RfuProtect["autoBlock"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))        
            if RfuProtect["autoAdd"] == True:
                if (settings["comment"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
                    ki.sendMessage(op.param1,str(settings["message"]))
                    kk.sendMessage(op.param1,str(settings["message"]))
                    kc.sendMessage(op.param1,str(settings["message"]))
                    ke.sendMessage(op.param1,str(settings["message"]))
        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in settings["blacklist"] == {}:
                line.kickoutFromGroup(op.param1,[op.param2])
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                line.sendMessage(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
                ki.sendMessage(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
                kk.sendMessage(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
                kc.sendMessage(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
                ke.sendMessage(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")
        if op.type == 25:
#            if settings ["mutebot2"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "ตั้งติกสำเร็จแล้ว " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
        if op.type in [25,26]:
            msg = op.message
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                        try:
                            ret_ = "[ ข้อมูลของโพสนี้ ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = line.getContact(msg._from)
                                auth = "\n  ผู้เขียนโพส : {}".format(str(contact.displayName))
                            else:
                                auth = "\n  ผู้เขียนโพส : {}".format(str(msg.contentMetadata["serviceName"]))
                            purl = "\n  ลิ้งโพส : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                            ret_ += auth
                            ret_ += purl
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "สติ๊กเกอร์" in msg.contentMetadata:
                                stck = "\n  Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "ข้อความ" in msg.contentMetadata:
                                text = "\n ข้อความโดยย่อ : {}".format(str(msg.contentMetadata["text"]))
                                ret_ += text
                            ret_ += "\n[ สิ้นสุดการเช็คโพส ]"
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "เกิดข้อผิดะลาดในการเช็คโพสนี้")                            
        if op.type == 26:
            msg = op.message
            text = msg.text
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
                if settings ["Aip"] == True:
            	    if msg.text in ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ",".","ปลิว"]:
                        line.kickoutFromGroup(receiver,[sender])
                        line.sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")
                if settings ["Api"] == True:
            	    if msg.text in ["ภู","นาย","พี่ภู","จาร","เสือภู","น้องภู"]:                  	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"มีอะไรรึปล่าวครับถ้าสนใจเชลบอททักแชทมาเลยครับ",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["บอท","เซล","เซลบอท","selfbot","คนรึบอท","Help","help",".help","/help","คำสั่ง"]:                   	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"PHU SELF BOT LINE สนใจเชลบอทรึบอทต่างแอดมาทักสอบถามได้ http://line.me/ti/p/~botline2034",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["55","555","5555","55555","55+","555+","5555+","ขำ",".ขำ"]:                    	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"ฮ่าๆๆๆ..ขำไร...ถถถ...บ้าอ่อ",link ,icon,name)
                        line.sendMessage(msg.to, None, contentMetadata={"STKID":"56618796","STKPKGID":"11637","STKVER":"1"}, contentType=7)
                if settings ["Api"] == True:
                    if msg.text in ["แทค",".แทค",".แจ๊ะ","tag","tagall","!แทค","!แจ๊ะ"]:                   	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"แทคไรหนักหนาครับ...กำ",link ,icon,name)
                        line.sendMessage(msg.to, None, contentMetadata={"STKID":"147","STKPKGID":"2","STKVER":"100"}, contentType=7)
                if settings ["Api"] == True:
                    if msg.text in [".วัดรอบ","sp","speed",".สปีด","สปีด","ความเร็ว","!speed","!สปีด"]:                   	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"นั้นสปีดหรือเดอะแฟลช...เนี้ยแรงกว่านี้มีอีกไหม",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["@","แอด","แอดมิน","แอดกลุ่ม"]:                 	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"Siriv10:groupcreator",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["อย","อยู่ไหม","อยู่บ่"]:                    	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"อยู่ในใจเสมอ",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["@@","แอดรอง","รองแอด"]:                    	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"Siriv10:予備作成者",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["คท","me","/me","!me"]:
                        line.sendMentionFooter(to, 'คทคุณครับ', sender, "https://line.me/ti/p/~botline2034", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~botline2034', 'type': 'mt', 'subText': " ", 'a-installUrl': 'https://line.me/ti/p/~botline2034', 'a-installUrl': ' https://line.me/ti/p/~botline2034', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~botline2034', 'i-linkUri': 'https://line.me/ti/p/~botline2034', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'https://line.me/ti/p/~botline2034'}, contentType=19)
                if settings ["Api"] == True:
                    if msg.text in ["ล๊อก","ล็อค","ชุดล็อค","ล็อคบ้าน"]:       	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~botline2034"
                        line.sendFooter(msg.to,"ให้แอดมินก๊อปคำสั่งวางทีละอัน",link ,icon,name)
                        line.sendFooter(msg.to,"Set:iconlock:on",link ,icon,name)
                        line.sendFooter(msg.to,"Set:ownerlock:on",link ,icon,name)
                        line.sendFooter(msg.to,"Set:changenamelock:on",link ,icon,name)
                        line.sendFooter(msg.to,"Set:blockinvite:on",link ,icon,name)
                if settings["autoRead"] == True:
                        line.sendChatChecked(to, msg_id)
                        ki.sendChatChecked(to, msg_id)
                        kk.sendChatChecked(to, msg_id)
                        kc.sendChatChecked(to, msg_id)
                        ke.sendChatChecked(to, msg_id)
                if settings["RText"] == True:
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"info":"RText", "text":msg.text, "from":msg._from, "createdTime":msg.createdTime}
                if to in read["readPoint"]:
                   if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    if msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = "Sticker Info"
                        ret_ += "\nSTICKER ID : {}".format(stk_id)
                        ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                        ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                        line.sendMessage(to, text=None, contentMetadata={'STKID':'107', 'STKVER':'100', 'STKPKGID':'1'}, contentType=7)
                    elif msg.contentType == 1:
                        line.sendMessage(to, text=None, contentMetadata={"STKID": "190", "STKVER": "100", "STKPKGID": "3"}, contentType=7)
                    else:
                        if text is not None:
                            txt = text
                            line.sendMessage(msg.to,txt)
                elif msg.contentType == 7:
                    if settings["checkSticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            line.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            line.sendMessage(to, str(ret_))                            
                        except Exception as error:
                            line.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in lineMID:
                            try:
                                line.kickoutFromGroup(msg.to,[sender])
                                line.sendMessage("คุณพูดคำต้องห้าม จำเป็นต้องนำออก sorry(╯°□°）╯︵ ┻━┻")
                            except Exception as e:
                                print(e)
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
                                line.sendMessage(to, "เข้าไปในกลุ่มðﾟﾑﾉ %s ðﾟﾑﾈ เรียบร้อยแล้ว" % str(group.name))               
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    if settings["detectMentionPM"] == True:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                sendMention(sender, sender, "「ตอบแทคอัตโนมัติ」\n", "\n" + str(settings["pmMessage"]))
                                break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
        	             if settings['kickMention'] == True:
        		             contact = line.getContact(msg._from)
        		             cName = contact.displayName
        		             balas = ["เนื่องจากตอนนี้ผมเปิดระบบเตะคนแทคไว้ " + "\nðﾟﾑﾉ" + cName + "\nðﾟﾙﾏต้องขออภัยด้วยจริงๆðﾟﾙﾏBye!!!"]
        		             ret_ = "" + random.choice(balas)                     
        		             name = re.findall(r'@(\w+)', msg.text)
        		             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
        		             mentionees = mention["MENTIONEES"]
        		             for mention in mentionees:
        			               if mention['M'] in admin:
        				                  line.sendText(msg.to,ret_)
        				                  random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
        				                  break                                  
        			               if mention['M'] in lineMID:
        				                  line.sendText(msg.to,ret_)
        				                  random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
        				                  break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
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
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:                    
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
                                          line.sendMessage(to,str(settings["Respontag"]))
                                          msgSticker = settings["messageSticker"]["listSticker"]["คนแทค"]
                                          if msgSticker != None:
                                              sid = msgSticker["STKID"]
                                              spkg = msgSticker["STKPKGID"]
                                              sver = msgSticker["STKVER"]
                                              sendSticker(to, sver, spkg, sid)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['delayMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          sendMessageWithMention(to, contact.mid)                                          
                                          break        
        if op.type == 17:
           print ("ต้อนรับคนเข้ากลุ่ม")
           if settings["Wc"] == True:
             if op.param2 in lineMID:
                return 
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1, "🙏สวัสดียินดีต้อนรับสู่บ้านใหม่🙏\n {}".format(str(dan.displayName),str(tgb.name)) + "\n" + str(settings["welcome"]) + "\n 🔇เข้ามาแล้วอย่าลืมปิดการแจ้งเตือนน่ะครับ🔇\n  􀬁􀅳sparkle􏿿• 􂘁􀄗w􏿿􂘁􀄅e􏿿􂘁􀄌l􏿿􂘁􀄃c􏿿􂘁􀄏o􏿿􂘁􀄍m􏿿􂘁􀄅e􏿿 •􀬁􀅳sparkle􏿿")
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 19:
           print ("ข้อความคนเตะกัน")
           if settings["Nk"] == True:
             if op.param2 in lineMID:
                return             
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,"•-•อู้วหู้วสุดยอดไปเลย".format(str(dan.displayName)) + str(settings["kick"]))
             line.sendContact(op.param1, op.param2)             
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 15:
           print ("ข้อความอำลาคนออก")
           if settings["Lv"] == True:
             if op.param2 in lineMID:
                return             
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,"😂ลาก่อนครับ😂 {} ".format(str(dan.displayName),str(tgb.name)) + str(settings["bye"]) + "􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿")
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath)) 
#==============================================================================================================
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\nðﾟﾔﾰ" + Name
                            pref=['ออกมาคุยสิครับðﾟﾤﾣðﾟﾤﾣ']
                            sendMessageWithMention(op.param1, op.param2)
                            line.sendMessage(op.param1, str(random.choice(pref)) + '\n♪ ♬ ヾ(´︶`♡)ﾉ ♬ ♪')
                            line.sendContact(op.param1, op.param2)
                            msgSticker = settings["messageSticker"]["listSticker"]["คนแอบ"]
                            if msgSticker != None:
                                sid = msgSticker["STKID"]
                                spkg = msgSticker["STKPKGID"]
                                sver = msgSticker["STKVER"]
                                sendSticker(op.param1, sver, spkg, sid)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print (" [ PHU SELF BOT]  ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        

while True:
    try:
        ops = oepoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
