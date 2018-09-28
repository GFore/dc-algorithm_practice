#write a function that sorts (ascending) the input list of integers using the Bubble Sort algorithm

# for full length of numlist, compare [i] to [i+1] and sort them
# repeat for len(numlist) - x, x = 1, 2, ... len(numlist)-1

def bubblesort(nlist):

    end_pos = len(nlist)-1

    while end_pos > 1:
        for i in range(end_pos):
            if nlist[i] > nlist[i+1]:  # then swap them
                nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
            print(num_list)
        end_pos -= 1

num_list = [1, 222, 1000, 10, 0, 9, 7, 8, 1, 3, 6, 5, 2, 4]
print(num_list)
bubblesort(num_list)
print(num_list)