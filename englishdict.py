d={}
print("welcome to eng")
while True:
    print('1.建立字典')
    print('2.列出所有字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗')
    print('6.離開')
    op = input("請輸選項")
    if op =='6':
        break
    elif op == "1":
        while 1==1:
            voc = input("輸英單字(零結束)")
            if voc == '0':
                break
            if voc not in d:
                vocc = input('中文')
                d[voc] = vocc
            else:
                print("存在")
    elif op =="2":
        s = sorted(d)
        for i in s:
            print(i,':',d[i])
    elif op == '3':
        while 1==1:
            voc = input('輸英單字(零結束)')
            if voc == '0':
                break
            if voc in d:
                print(voc,"中文",d[voc])
            else:
                print('沒有')
    elif op=='4':
        while 1==1:
            a = 0
            ch = input('輸中單字(零結束)')
            if ch == '0':
                break
            for k,v in d.items():
                if v ==ch:
                    print(ch,'英文',k)
                    ch==1
            if ch==0:
                print("沒有")
    elif op == '5':
        s = 0
        for k,v in d.items():
            print(k)
            i = input(":")
            if i==v:
                s+=1
                print('答對')
                
            else:
                print('達錯')
        print(s)
            
            
    
    