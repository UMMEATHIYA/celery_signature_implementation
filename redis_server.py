# celery -A tasks worker --loglevel=info

from celery import signature 
from tasks import add

result = signature('tasks.add', args=(2,2), countdown=10)
print(result)
print(add.signature((2,2), countdown=10))
print(add.s(2,2,debug=True))

s = add.signature((2,2), {'debug': True}, countdown=10)
print(s.args)

####################
print(s.kwargs)

#####################
print(s.options)

#print(add.apply_async(args, kwargs, **options))
#res = add.signature(args, kwargs, **options).apply_async()

res = add.apply_async((2,2),countdown=1)
print(res)

res2 = add.signature((2,2), countdown=1).apply_async()
print(res2)

##############PARTIALS##############################
###########With a signature, you can execute the task in a worker#############

r1 = add.s(2,2).delay()
print("This is r1 result" r1)

r2 = add.s(2,2).apply_async(countdown=1)
print("This is r2 result" r2)

###########PARTIALS###########################
