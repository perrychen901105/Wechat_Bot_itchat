import itchat, time
from itchat.content import *


# itchat.send('欢迎使用本系统', toUserName='filehelper')

# print('success')

# 获取自己的用户信息，返回自己的属性字典
# print(itchat.search_friends())

REAL_SINCERE_WISH = u'祝%s新年快乐！'

ALREADY_SET = False
# friendList = itchat.get_friends(update=True)[1:]
# for friend in friendList:
#     # 如果是演示目的，把下面的方法改为print即可
#     print(SINCERE_WISH % (friend['DisplayName']
#         or friend['NickName']), friend['UserName'])
#     time.sleep(.5)


# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text

@itchat.msg_register(msgType=[TEXT],isFriendChat=True,isGroupChat=False,isMpChat=False)
def recv_msg(msg):
    print(msg)
    if msg['Text'] == "100":
        ALREADY_SET = True
        itchat.send('输入群名，添加好友', toUserName='filehelper')
    else:
        if msg['Text'] == "Test":
            itchat.send('输入200, 加好友', toUserName='filehelper')
        else:
            chatroomName="Test"
            print(chatroomName)
            itchat.get_chatrooms(update=True)
            chatrooms = itchat.search_chatrooms(name=chatroomName)
            if chatrooms is None:
                print(u'没有找到群聊：' + chatroomName)
            else:
                chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
                for friend in chatroom['MemberList']:
                    friend = itchat.search_friends(userName=friend['UserName'])
                    # 如果是演示目的，把下面的方法改为print即可
                    if friend != None:
                        # print(friend)
                        print(friend['UserName'])
                        itchat.add_friend(userName=friend['UserName'], status=2)
                        # itchat.add_member_into_chatroom('Test', [friend['UserName']])
                        # itchat.send_msg('Text message', toUserName=friend['UserName'])
                        # print(REAL_SINCERE_WISH % (friend['DisplayName']
                            # or friend['NickName']), friend['UserName'])
                        # itchat.send('hello', toUserName='Test')
                        itchat.send('欢迎使用本服务', toUserName=friend['UserName'])
                        time.sleep(.5)
                        
                    else:
                        print('no msg')

# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     print(msg)
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print(msg)

itchat.auto_login()
print('logining...')
itchat.send('输入100发消息', toUserName='filehelper')
itchat.run(True)
print('already run ...')

# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# def text_reply(msg):
#     msg.user.send('%s: %s' % (msg.type, msg.text))

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)

# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')

# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg.isAt:
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))

# itchat.auto_login(True)
# itchat.run(True)
