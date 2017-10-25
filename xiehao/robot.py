# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/10/20 下午11:11'

from werobot import WeRoBot
import re

robot = WeRoBot(enable_session=False,
                token='xh940723',
                APP_ID='wx9d44897679b1465f',
                APP_SECRET='915c1037f622b90e6e6e3d94a032351b'
                )

@robot.text
def echo(message):
    try:
        # 提取消息
        msg = message.content.strip().lower().encode('utf8')
        # 解析消息
        if  re.compile(".*?你好.*?").match(msg) or\
            re.compile(".*?嗨.*?").match(msg) or\
            re.compile(".*?哈喽.*?").match(msg) or\
            re.compile(".*?hello.*?").match(msg) or\
            re.compile(".*?hi.*?").match(msg) or\
            re.compile(".*?who are you.*?").match(msg) or\
            re.compile(".*?你是谁.*?").match(msg) or\
            re.compile(".*?你的名字.*?").match(msg) or\
            re.compile(".*?什么名字.*?").match(msg) :
            return "你好~\n我是机器人，主人还没给我起名字 T_T\n有什么能帮您的吗？（绅士脸）"
        elif re.compile(".*?厉害.*?").match(msg):
            return '承让承让 (๑•̀ㅂ•́)ﻭ✧'
        elif re.compile(".*?吉鹏.*?").match(msg):
            return '是傻逼'
        elif re.compile(".*?miss you.*?").match(msg):
            return 'I miss you,too'
        elif re.compile(".*?我爱你.*?").match(msg):
            return '我也爱你'
        elif re.compile(".*?love you.*?").match(msg):
            return 'I love you,too'
        elif re.compile(".*?美女.*?").match(msg):
            return '我是男生哦♂'
        elif re.compile(".*?帅哥.*?").match(msg):
            return '谢谢夸奖 (๑•̀ㅂ•́)ﻭ✧'
        elif re.compile(".*?傻逼.*?").match(msg):
            return '爸爸不想理你'
        return '听不懂你在说什么耶'
    except Exception as e:
        print e


@robot.key_click("music")
def abort():
    return "日落大道"


@robot.key_click("givefive")
def abort():
    return "谢谢你的鼓励！我会做得更好"

