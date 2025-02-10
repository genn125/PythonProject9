

user_profile=[{'nam':7,'comment_qt':8},{'na': 25364, 'comment_qty1': 6666},{'n': 78,'comment_qty3':99}]
qwer1, qwer2, qwer3 = user_profile

def user_info(name,comment_qty):


    return name,comment_qty


print(user_info(qwer2['na'],qwer2['comment_qty1']))
print(user_info(qwer1['nam'],qwer1['comment_qt']))
print(user_info(name=qwer3['n'],comment_qty=qwer3['comment_qty3']))

