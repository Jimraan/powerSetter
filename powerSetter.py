import copy
import time

def power_set(S):
    if len(S) == 0:
        return [[]]

    x = S[-1]
    list1 = power_set(S[:-1])
    list2 = copy.deepcopy(list1)

    for i in list2:
        i.append(x)

    return list1 + list2

def k_subsets_naive(S, k):
    list2 = [[]]
    if k == len(S):
        return [[]]
    
    list1 = power_set(S)

    for i in list1:
        if(len(i) == k):
            list2.append(i)
    list2.remove([])

    return list2

def k_subsets_better(S, k):
    if k == len(S):
        return [S]
    else:
        copy_set = copy.deepcopy(S)
        x = copy_set.pop(1)
        result = k_subsets_better(copy_set, k)
        sets = power_set(S)
        [result.append(sets) for sets in sets if len(sets) == k and sets not in result]

        return result


if __name__ == "__main__":
    print(power_set([1, 2]))
    print()

    start_time = time.process_time()
    print(k_subsets_naive([1, 2, 4, 5, 3, 7, 9, 44, 77, 21], 3))
    end_time = time.process_time()
    print("Naive runtime: " + str(end_time - start_time))
    print()

    start_time = time.process_time()
    print(k_subsets_better([1, 2, 4, 5, 3, 7, 9, 44, 77, 21], 3))
    end_time = time.process_time()
    print("Better time: " + str(end_time - start_time))
    print("Wait... it's worse??")
        

