def slot(q,slot1,slot2,slot3):
    q=[1<q<1000]
#    q=48
    t=0
#    slot1=int(3)
#    slot2=10
#    slot3=4
    while True:
        if q==0:
            print(f"Martha plays {t} before going broke")
            break
        if slot1%35==0:
            q+=30 and q==q-1 and slot1==slot1+1 and t==t+1 
        elif slot1% 35!=0:
            q==q-1 and slot1==slot1+1 and t==t+1
        if slot2%100==0:
            q+=60 and q==q-1 and slot2==slot2+1 and t==t+1 
        elif slot2% 100!=0:
            q==q-1 and slot2==slot2+1 and t==t+1
        if slot3%10==0:
            q+=9 and q==q-1 and slot3==slot3+1 and t==t+1 
        elif slot3% 10!=0:
            q==q-1 and slot3==slot3+1 and t==t+1

slot(77,4,9.3,1)
        