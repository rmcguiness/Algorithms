# Define a function to create the sorting and pass in an array as the parameter
def bubble_sort(arr):
    # Get the length of the array
    arr_len = len(arr)
    # Loop through the array to access the elements in it, including the last one - outer loop
    for i in range(arr_len-1):
        # declare a flag variable to check if a swap has occured - for optimization
        flag = 0
        # create a loop to compare each element of the array till the last one
        for j in range(0, arr_len-i-1):
            # compare 2 adjacent elements and sort them in ascending order
            if arr[j] > arr[j+1]:
                # Swap the elements if they are not in the right order
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                # break out of the loop at 0
                if flag == 0:
                    break
    # return value must be in the outer loop block
    return arr

arr = [5, 3, 4, 1, 2]
print("List sorted with bubble sort in ascending order: ", bubble_sort(arr))