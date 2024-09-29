from actors import (
    addition,
    multiplication,
    add_list_items,
    multiply_list_items,
    list_multiplication,
    item_one,
    item_two,
    add1,
    add2,
    backend,
)
import dramatiq


message = addition.send(2, 3)
print(message)
print(message.get_result(backend=backend, block=True, timeout=10000))

message = multiplication.send(4, 5)
print(message)
print(message.get_result(block=True, timeout=10000))


group_for_to_useingroup = dramatiq.group([item_one.message(), item_two.message()])


list1 = [10, 20, 30]
list2 = [40, 50, 60]

results = dramatiq.group(
    [
        add_list_items.message(list1),
        multiply_list_items.message(list2),
        (add_list_items.message(list1) | list_multiplication.message(list2)),
        group_for_to_useingroup,
    ]
).run()
for result in results.get_results(block=True, timeout=10000):
    print(result)


results = dramatiq.pipeline(
    [add_list_items.message(list1), list_multiplication.message(list2)]
).run()
print(results)
for result in results.get_results(block=True, timeout=20000):
    print(f"result is {result}")


pipe = (add1.message() | add2.message()).run()


print(f"final_result is {pipe.get_result(block=True,timeout=10000)}")


from actors import mul1, mul2, mul3, mul4

messages = dramatiq.pipeline(
    [
        mul1.message(),
        mul2.message_with_options(pipe_ignore=True),
        mul4.message(),
        mul3.message(),
    ]
).run()
print(messages)
print(messages.get_result(block=True, timeout=10000))
for intermediate_result in messages.get_results(block=True, timeout=10000):
    print(intermediate_result)
