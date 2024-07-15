import numpy as np 

def find_error(x,i):
    return (dt_list[i]-x)/dt_list[i]

#End time [s]
t_end=2
#Time increment [s]
h=0.1
#points
N=int(t_end/h+1)
#Time
t=np.linspace(0,t_end,N)
#x
x=np.linspace(0,t_end,N)

#Initial Condition
x[0]=1 

#Euler Method calculation
for i in range(N-1):
    k1=h*t[i]*x[i]
    k2=h*(t[i]+h/2)*(x[i]+k1/2)
    k3=h*(t[i]+h/2)*(x[i]+k2/2)
    k4=h*(t[i]+h)*(x[i]+k3)
    dx=(k1+2*k2+2*k3+k4)/6
    x[i+1]=x[i]+dx

with open('practice_true.csv','r') as f1:
    og_data=f1.readlines()
    
dt_list=[]
for i in range(1,len(og_data)):
    new_dt=og_data[i].split(',')
    dt=float(new_dt[1].replace('\n',''))
    dt_list.append(dt)

#Write to csv file
with open('practice_Euler2.csv','w',newline='') as f:
    f.write('time,h='+str(h)+',Error')
    f.write('\n')
    for i in range(N):
        f.write(str(t[i])+','+str(x[i])+','+str(find_error(x[i],i)))
        f.write('\n')

