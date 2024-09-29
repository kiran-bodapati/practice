def set_multiply(set1):
    result=1
    for i in set1:
        print(i)
        result*=i
    return result





set1={38,39.23,47,52}
final_result=set_multiply(set1)
print(f"final_result is {final_result}")