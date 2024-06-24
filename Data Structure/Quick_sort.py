def swap(start,end,elements):
    if start != end :
        temp = elements[start]
        elements[start] = elements[end]
        elements[end] = temp 
      
def partition(elements,start, end):
    pivit_index = start 
    pivit = elements[pivit_index]   
  
    while start < end : 
        while elements[start] <= pivit: 
            start += 1   

        while elements[end] > pivit: 
            end -= 1 

        if start < end:
            swap(start,end,elements) 

    swap(pivit_index,end,elements) 

    return end  

def quicksort(elements,start,end):
    if start < end:   
        pi = partition(elements,start,end) 
        quicksort(elements,start,pi - 1)   #    left Partition 
        quicksort(elements,pi+1, end)      #    Right Partition 

if __name__ == '__main__':  
    elements = [11,9,29,7,2,15,28]
    quicksort(elements,0,len(elements)-1)  
    print(elements)   