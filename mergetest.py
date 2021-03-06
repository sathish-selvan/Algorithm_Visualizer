import time

global final 

final = []

def mergesort(data,left,right,draw_data,time_taken):
    
    if left < right:
        middle=(left+right)// 2
        mergesort(data,left,middle, draw_data, time_taken)
        mergesort(data,middle+1,right,draw_data,time_taken)
        # print(data[left:middle+1], data[middle+1:right+1])
        merge(data,left,middle,right,draw_data,time_taken)
        
        

def merge(data,left,middle,right,draw_data,time_taken):
    draw_data(data, getColorArray(len(data), left, middle,right))
    time.sleep(time_taken)
    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1

        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

        draw_data(data,["green" if x >= left and x <= right else "white" for x in range(len(data))])

def getColorArray(length, left, middle,right):
    colorArray = []
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append('yellow')
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")



    return colorArray


