 - **企业微信群机器人（一对多）**

企业微信通知有两种方式，一种是企业微信群机器人（一对多）；一种是企业微信通知（一对一）
企业微信通知是一个应用采用api方法，群通知是采用webhook。
两种方法都是采用相同语法的富文字(markdown)。因此同一个信息能同时发送企业微信通知和群通知。

> **企业微信群机器人（一对多）：**
优点：取得一个webhook就能发送消息，一对多的通知
缺点：得先有三个以上企业微信账号，才能成立聊天群

> **企业微信通知（一对一）：**
优点：有企业微信账号就能建企业微信通知，一对一的通知
缺点：需要取得corpid、AgentID、secret。代码逻辑比较复制


![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/bot_demo.png)


这篇代码是介绍**企业微信群机器人（一对多）**。企业微信通知（一对一） 请参考[这一篇](https://github.com/litonchen/qywx)


 - [ ] **- 群机器人**
群机器人不能单独使用，必须先建立企业微信聊天群才能建立群机器人。创立企业微信群后，复制webhook就行。
**1.复制webhook**
![enter image description here](https://raw.githubusercontent.com/litonchen/wx_bot/main/png/6.webhook.png)
