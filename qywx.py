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
        "markdown": {
            "content": mkd_msg
            }
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
