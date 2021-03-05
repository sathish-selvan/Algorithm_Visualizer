import time
global lis

def partition(data, head, tail,draw_data,time_taken):
    global lis
    border = head
    pivot = data[tail]
    for j in range(head,tail):
        if data[j] < pivot:
            data[border], data[j] =  data[j], data[border]
            border += 1

            lis2 = ["green" if  x ==j else lis[x] for x in range(len(data))] 
            
            
            draw_data(data, lis2)
            time.sleep(time_taken)


    data[border], data[tail] =  data[tail], data[border]
    print(data)
    print(border)
    return border



def quick_sort(data, head, tail,draw_data,time_taken):
    global lis
    if head < tail:
        partitionIdx = partition(data, head, tail,draw_data,time_taken)
        lis[partitionIdx] = "green"
        
        
        draw_data(data,lis)
        time.sleep(time_taken)
        print(lis)
        quick_sort(data, head, partitionIdx-1,draw_data,time_taken)
        quick_sort(data, partitionIdx+1, tail,draw_data,time_taken)


def main(data, head, tail,draw_data,time_taken):
    global lis
    lis = ["red" for x in range(len(data))]
    quick_sort(data, head, tail,draw_data,time_taken)
    lis = ["green" for x in range(len(data))]
    draw_data(data,lis)
    time.sleep(time_taken)
