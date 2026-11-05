W=[2,3,4,4,5,6,1,2,2,2,1,8,2]
def Emerald(N,Weight):
    current_num=0
    sum=0
    for i in range(N):
        if Weight[i]%2==0:
            current_num+=Weight[i]
            if current_num>sum:
                sum=current_num
        elif Weight[i] % 2 ==1:
            sum=0
    return sum
print(Emerald(13,W))
W = [2,3,4,4,5,6,1,2,2,2,1,8,2]

def Emerald(N, Weight):
    current_num = 0
    total = 0
    for i in range(N):
        if Weight[i] % 2 == 0:        
            current_num += Weight[i]
            if current_num > total:
                total = current_num   
        else:                         
            current_num = 0           
    return total

print(Emerald(13, W))