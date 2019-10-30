#!/usr/bin/python
# coding:utf-8
 


f = open("1.txt")            
line = f.readline()           
while line:
    st=line.strip('\r\n')
    str=st.split("	")
       
    num1 = float(str[0])
    num2 = float(str[1])
    num3 = float(str[2])
    num4 = float(str[3])
    num5 = float(str[4])
    num6 = float(str[5])
    num7 = float(str[6])
    num8 = float(str[7])
    num9 = float(str[8])
    num10 = float(str[9])
    num11 = float(str[10])
    num12 = float(str[11])
    num13 = float(str[12])

    garde = (num1*3+num2*3+num3*3+num4*3+num5*2)/14*0.8 + (num6*2+num7*1+num8+num9+num10*2+num11*2+num12*2+num13*2)/13*0.2
    print(garde)

    
	
    line = f.readline()
f.close()
