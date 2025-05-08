import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

# Global metrics
comparison_count = 0
swap_count = 0

def reset_metrics():
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0

def bubble_sort(arr):
    global comparison_count, swap_count
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparison_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
            yield arr

def insertion_sort(arr):
    global comparison_count, swap_count
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparison_count += 1
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1
            yield arr
        arr[j + 1] = key
        yield arr

def merge_sort(arr):
    global comparison_count, swap_count
    def merge_sort_helper(arr, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            yield from merge_sort_helper(arr, start, mid)
            yield from merge_sort_helper(arr, mid, end)
            left = arr[start:mid]
            right = arr[mid:end]
            i = j = 0
            for k in range(start, end):
                comparison_count += 1
                if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                swap_count += 1
                yield arr
    yield from merge_sort_helper(arr, 0, len(arr))

def quick_sort(arr):
    global comparison_count, swap_count
    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            yield from quick_sort_helper(arr, low, pivot_index)
            yield from quick_sort_helper(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        global comparison_count, swap_count
        pivot = arr[low]
        left = low + 1
        right = high - 1
        done = False
        while not done:
            while left <= right and arr[left] <= pivot:
                left += 1
                comparison_count += 1
            while arr[right] >= pivot and right >= left:
                right -= 1
                comparison_count += 1
            if right < left:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]
                swap_count += 1
            yield arr
        arr[low], arr[right] = arr[right], arr[low]
        swap_count += 1
        yield arr
        return right

    yield from quick_sort_helper(arr, 0, len(arr))

def visualize_sort(sort_algorithm):
    reset_metrics()
    array = [random.randint(1, 100) for _ in range(30)]
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(array)), array, align='edge')
    ax.set_title(f"{sort_algorithm.__name__.replace('_', ' ').title()} Visualization")
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update(arr):
        for bar, val in zip(bars, arr):
            bar.set_height(val)
        text.set_text(f"Comparisons: {comparison_count}  Swaps: {swap_count}")

    start_time = time.time()
    anim = animation.FuncAnimation(fig, update, frames=sort_algorithm(array[:]), interval=100, repeat=False)
    plt.show()
    duration = time.time() - start_time
    print(f"\nFinal Report for {sort_algorithm.__name__.replace('_', ' ').title()}:")
    print(f"Total comparisons: {comparison_count}")
    print(f"Total swaps: {swap_count}")
    print(f"Time taken: {duration:.2f} seconds")

# Run any one of the sorting algorithms here
if __name__ == '__main__':
    visualize_sort(bubble_sort)  # Options: bubble_sort, insertion_sort, merge_sort, quick_sort