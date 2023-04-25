- **企业微信通知**


企业微信通知有两种方式，一种是对话机器人，一种是群通知。
对话机器人是一个应用，采用api方法，群通知是采用webhook。两种方法都是采用相同语法的富文字(markdown)。因此同一个信息能同时发送对话机器人和群通知。以下分别介绍：
**` `群机器人 对话机器人**
对于新同学来说，**建议先从群机器人入手**。只需要webhook就能建立一个机器人。

 - [ ] **- 群机器人**
群机器人不能单独使用，必须先建立企业微信聊天群才能建立群机器人。创立企业微信群后，复制webhook就行。
**1.复制webhook**
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/6.webhook.png)


 - [ ] **- 对话机器人**

对话机器人是一个微信企业号的应用，可以当成是一个已经加入对方企业微信的好友，因此能直接发送信息。

首先登入注册一个企业微信，登入[企业微信网页](https://work.weixin.qq.com/)：https://work.weixin.qq.com/
然后按照以下流程。
 **1. 创建企业**
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/1.newcorp.png)

 **2. 点击应用管理**
![点击应用管理](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/2.application.png?token=GHSAT0AAAAAACAP34VHG6LZBK5DZG5DY2OUZCHP3JQ)

**3.点击创建应用**
![创建应用](https://raw.githubusercontent.com/litonchen/wx_bot/main/3.create.png)
**4.命名应用**
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/4.name.png)

**5.复制AgentID、Secret**
![](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/5.secret.png?token=GHSAT0AAAAAACAP34VGJNMZ5IODBZLDYFDCZCHQN5Q)
