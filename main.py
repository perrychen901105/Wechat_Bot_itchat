import itchat, time

itchat.auto_login()

itchat.send('欢迎使用本系统', toUserName='filehelper')

print('success')

# 获取自己的用户信息，返回自己的属性字典
print(itchat.search_friends())

SINCERE_WISH = u'祝%s新年快乐！'

# friendList = itchat.get_friends(update=True)[1:]
# for friend in friendList:
#     # 如果是演示目的，把下面的方法改为print即可
#     print(SINCERE_WISH % (friend['DisplayName']
#         or friend['NickName']), friend['UserName'])
#     time.sleep(.5)

itchat.get_chatrooms(update=True)