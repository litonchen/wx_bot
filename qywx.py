import json,requests

###############    企业微信：群通知      ###############  
def sent_work_msg(webhook_url,content ):
    data = {"msgtype": "markdown", 
            "markdown": 
            {"content": content}}
    r = requests.post(webhook_url, data=json.dumps(data))
    return r.text, r.status_code
# send_work_msg("ptrade测试:企业微信群发",bot_url)

def sent_work_markdown(webhook_url,mkd_msg):
    mkd={
        "msgtype": "markdown",
        "markdown":  mkd_msg
        }
    body = json.dumps(mkd)
    res = requests.post(webhook_url,data=body)
    return res.text, res.status_code
# sent_work_markdown(bot_url,mkd_msg)

def sent_work_img(webhook_url,img):
    with open(img, 'rb') as file:
        #转换图片成base64格式
        data = file.read()
        encodestr = base64.b64encode(data)
        image_data = str(encodestr, 'utf-8')
    #图片的MD5值
    with open(img, 'rb') as file:
        md = hashlib.md5()
        md.update(file.read())
        image_md5 = md.hexdigest()       
    mkt = {"msgtype": "image",
            "image": {"base64": image_data,
                      "md5": image_md5
                     }
            }    
    body = json.dumps(mkt)
    res = requests.post(webhook_url,data=body)
    
###############    企业微信：机器人      ###############     
def get_token(corpid, secret):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
      "corpid": corpid,
      "corpsecret": secret
    }
    r = requests.get(url=Url, params=Data)
    token = r.json()['access_token']
    return token

def sendImg(access_token,agentid,media_id):
    #print('media_id:',media_id)
    data = {
           "touser": "@all", 
           "toparty": "@all",         
           "msgtype" : "image",
           "agentid" : agentid,
           "image": {
               "media_id": media_id
           },
           "safe":0
        }
    r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token), data=json.dumps(data))

def send_txt(access_token,agentid,meg_txt) :
    data = {
           "touser": "@all", 
           "toparty": "@all",         
           "agentid" : agentid,
           "msgtype": "text",  # 消息类型，此时固定为text
           "text": {
               "content": meg_txt,  # 文本内容，最长不超过2048个字节，必须是utf8编码
                }
    }
    r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token), data=json.dumps(data))

def send_markdown(access_token,agentid,mkd_msg) :  
    send_data = {
           "touser": "@all", 
           "toparty": "@all",         
           "agentid" : agentid,        
           "msgtype": "markdown",  # 消息类型，此时固定为markdown
           "markdown": {
                       "content": mkd_msg
                   }
               }
    r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token), data=json.dumps(send_data))
    # log.info(('markdown：%s'%send_data))
