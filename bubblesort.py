import time

def bubble_sort(data,draw_data,time_taken):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                lis2 = ["green" if  x ==j+1 else "red" for x in range(len(data)-i)] + ["green" for x in range(i)]
                print(lis2)
                draw_data(data, lis2)
                time.sleep(time_taken)
        lis = ["red" for x in range(len(data)-(i+1))] + ["green" for x in range(i+1)]
        draw_data(data,lis)

    draw_data(data,["green" for x in range(len(data))])
