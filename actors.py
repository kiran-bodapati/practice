import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
from dramatiq.middleware import Pipelines



broker=RedisBroker(host='127.0.0.1',port=6379)
backend=RedisBackend(host='127.0.0.1',port=6379)
dramatiq.set_broker(broker)
broker.add_middleware(Results(backend=backend))
broker.add_middleware(Pipelines())



@dramatiq.actor(store_results=True)
def addition(x,y):
    return x+y

@dramatiq.actor(store_results=True)
def multiplication(a,b):
    return a*b

@dramatiq.actor(store_results=True)
def add_list_items(list1):
    total=0
    for i in list1:
          total+=i
    return total

@dramatiq.actor(store_results=True)
def multiply_list_items(list2):
     result=1
     for i in list2:
          result*=i
     return result

@dramatiq.actor(store_results=True)
def list_multiplication(list2,output_of_add_list_items):
     result=1
     for i in list2:
          result*=i
     final_result=result+output_of_add_list_items
     return final_result


@dramatiq.actor(store_results=True)
def item_one():
     return 5

@dramatiq.actor(store_results=True)
def item_two():
     return 10


@dramatiq.actor(store_results=True)
def add1():
     return 1

@dramatiq.actor(store_results=True)
def add2(x):
     return x+2




@dramatiq.actor(store_results=True)
def mul1():
   return 1

@dramatiq.actor(store_results=True)
def mul2():
   return 2

@dramatiq.actor(store_results=True)
def mul3(x):
   return x+3

@dramatiq.actor(store_results=True)
def mul4(y):
   return y+4
