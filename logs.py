import securechat
v=0
"""
f=open('logs.txt','a')
def writer(message):
    f.write(message)
    f.write('\n')
"""

def writer(message):
    f = open('logs.txt', 'a')
    f.write(message)
    f.write('\n')
    f.close()
