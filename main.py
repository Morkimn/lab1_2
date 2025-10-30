def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    try:
        n = int(input("Сколько чисел? ").strip())
        nums = []
        print("Введите числа (по одному в строке):")
        for _ in range(n):
            nums.append(float(input().strip()))
        direction = input("Направление (asc/desc): ").strip().lower()
        reverse = (direction == "desc")
        print(*bubble_sort(nums, reverse=reverse), sep=" ")
    except ValueError:
        print("Ошибка ввода.")
