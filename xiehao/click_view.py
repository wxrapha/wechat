# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/10/21 上午8:44'

from werobot import WeRoBot

import sys
reload(sys)
sys.setdefaultencoding('utf8')

robot = WeRoBot()
robot.config["APP_ID"] = "wx9d44897679b1465f"
robot.config["APP_SECRET"] = "915c1037f622b90e6e6e3d94a032351b"
client = robot.client
client.create_menu(
    {
        "button":[
            {
                "type": "view",
                "name": "授权",
                "url": "http://www.xiehaoo.com/web_auth/"
            },
            {
                "type":"scancode_push",
                "name":"扫一扫",
                "key": "sys"

            },
            {
                "name": "菜单",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "粉丝列表",
                        "url": "http://www.xiehaoo.com/allfans/",
                    },
                    {
                        "type": "view",
                        "name": "个人信息",
                        "url": 'http://www.xiehaoo.com/wechat_info',
                    },
                ]
            }]
})

