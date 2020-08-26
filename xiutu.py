import requests

from iotbot import Action
from iotbot import GroupMsg
from iotbot.decorators import equal_content
from iotbot.decorators import not_botself
from iotbot.sugar import Text
import random
# 屏蔽群 例：[12345678, 87654321]
blockGroupNumber = []

blockUserNumber =[]
# 屏蔽qq号 例：[12345678, 87654321]
# ==========================================

@not_botself()
def receive_group_msg(ctx: GroupMsg):
    userGroup = ctx.FromGroupId
    if (userGroup in blockGroupNumber):
        return

    c = ctx.Content
    if(c.startswith('秀图')):
        if (ctx.FromUserId in blockUserNumber):
            Action(ctx.CurrentQQ).send_group_pic_msg(
                ctx.FromGroupId,
                picUrl='http://c2cpicdw.qpic.cn/offpic_new/877228648/1587200498-3099922523-00FC667A29BC18F5B9FBBF1A6987756B/0',
                content='太丑了，不想发'
            )
        else:
            showType= random.randint(40000,40005)
            url = "http://q1.qlogo.cn/g?b=qq&nk="+str(ctx.FromUserId)+"&s=640"
            Action(ctx.CurrentQQ).send_group_pic_msg(
                ctx.FromGroupId,
                picUrl=url,
                content='[秀图'+str(showType)+']'
            )

