def budget(k,m,b):
            price = []
            for i in range(len(k)):
                temp = k[i]
                for j in range(len(m)):
                    if(temp+m[j] <= b):
                        price.append(temp + m[j])                                                   
            max_num = max(price)
            if(max_num < b):
                return max_num
            else:
                return -1                

            # l=-1
            # for i in range(len(k)):
            #     for j in range(len(m)):
            #         if k[i]+m[j]>l  and k[i]+m[j]<b:
            #             l = k[i]+m[j]
            # return l                        

                                  




print(budget([40,50,60],[5,8,12],60))  
print(budget([5,1,1],[4],5))                        

