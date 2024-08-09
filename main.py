import time
import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Generating a random list of integers
arr = [random.randint(1, 1000) for _ in range(1000)]

# Copying the original array to ensure both algorithms sort the same array
arr_for_bubble = arr.copy()
arr_for_merge = arr.copy()

# Timing Bubble Sort
start_time = time.time()
bubble_sort(arr_for_bubble)
end_time = time.time()
print(f"Bubble Sort time: {end_time - start_time} seconds")

# Timing Merge Sort
start_time = time.time()
merge_sort(arr_for_merge)
end_time = time.time()
print(f"Merge Sort time: {end_time - start_time} seconds")
