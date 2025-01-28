import time
from concurrent.futures import ThreadPoolExecutor, as_completed


lists = [
    [324, 643, 171, 208, 330, 306, 559, 927, 871, 284, 438, 644, 447, 893, 287],
    [993, 788, 192, 169, 549, 162, 324, 213, 277, 376, 391, 243, 749, 229, 545, 516, 260, 798],
    [725, 968, 492, 746, 823, 651, 546, 245, 378, 631, 593, 359, 823, 241],
    [450, 267, 913, 754, 134, 984, 763, 462, 229, 276, 749, 679]
]


def process_number(number):
    time.sleep(0.2)  
    return number * 2


def process_lists_with_threads(lists):
    first_list_sum = None  
    futures = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i, lst in enumerate(lists):
            futures.append((i, [executor.submit(process_number, num) for num in lst]))
        
        for index, future_list in futures:
            processed_numbers = [future.result() for future in future_list]
            list_sum = sum(processed_numbers)
            if first_list_sum is None:
                first_list_sum = list_sum
    return first_list_sum


if __name__ == "__main__":
    first_list_sum = process_lists_with_threads(lists)
    print(f"\nСумма чисел в первом обработанном списке: {first_list_sum}")
