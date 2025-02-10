

user_profile=[{'nam':7,'comment_qt':8},{'a': 25364, 'b': 6666},{'n': 78,'comment_qty3':99}]

qwer1, qwer2, qwer3 = user_profile

def user_info(a,b): print(a,b)

user_info(a=qwer1['nam'],b=qwer1['comment_qt'])
user_info(**qwer2)
user_info(qwer3['n'],qwer3['comment_qty3'])


