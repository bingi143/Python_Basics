def method(Power_value):
    if(0<=Power_value<31):
        for i in range(1,Power_value):
            v=1
            for k in range(i):
                v=v*2
            print(2,"^",i,"=",v)
Power_value=int(input("Enter Power value:"))
method(Power_value)