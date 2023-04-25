import qywx as wx
#### 群发机器人的webhook ####
bot_url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6c67e6ae-8986-4651-8e89-bab9755c7a1b"
#############################



# 发送短信
content = "企业微信群机器人通知"
wx.sent_work_msg(bot_url,content)

# 发送富文字
mkd_msg = {
        "content": "# **今日交易**<font color=\"warning\">**总结**</font>\n" +  # 标题 （支持1至6级标题，注意#与文字中间要有空格）
                    "#### **浮动盈亏：{}**\n".format("30310 ") +  # 加粗：**需要加粗的字**
                    "> 本日交易：<font color=\"info\"> {} </font> \n".format(" 成交明细 ") +  # 引用：> 需要引用的文字
                    "> 卖出204001，单笔十万：<font color=\"warning\">{} 十万</font> \n".format('10')  +  # 字体颜色(只支持3种内置颜色)
                    "> 卖出131810，单笔千元：<font color=\"warning\">{} 千元</font>".format("5")   # 绿色：info、灰色：comment、橙红：warning
            }
wx.sent_work_markdown(bot_url,mkd_msg)
