def insertion_sort(elements):

    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i - 1  
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor 
 
    return elements

elements = [10,9,8,7,6,5,4,3]
insertion_sort(elements) 
print(elements)
