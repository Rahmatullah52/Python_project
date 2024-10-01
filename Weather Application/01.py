from tkinter import *
from datetime import *
import requests

#requset

URL = 'https://api.open-meteo.com/v1/forecast?latitude=47.6062&longitude=-122.3321&hourly=temperature_2m&timezone=America%2FLos_Angeles&forecast_days=1'

location = 'delhi technologicaluniversity'
PARAM = {'adress':location}
info = requests.get(url=URL,params=PARAM)
data = info.json()
# print(data)
temp = data["hourly"]["temperature_2m"]


#time
nowtimes = datetime.now()
now_hour = nowtimes.hour



root = Tk()
root.title('Live Weather')
root.geometry('420x350')
root.resizable(False,False)
root.config(bg='#5FC0D8')

# frame

frm1 = Frame(root,height=40,width=300,bg='#5FC0D8')
frm1.pack(side=TOP)

frm2 = Frame(root,height=40,width=300,bg='#5FC0D8')
frm2.pack(side=TOP)

frm3 = Frame(root,height=40,width=300,bg='#5FC0D8')
frm3.pack(side=TOP)

frm4 = Frame(root,height=40,width=300,bg='#5FC0D8')
frm4.pack(side=TOP)

frm5 = Frame(root,height=40,width=300,bg='#5FC0D8')
frm5.pack(side=TOP)

frm6 = Frame(root,height=40,width=300,bg='#5FC0D8')
frm6.pack(side=TOP)

frm7 = Frame(root,height=40,width=300,bg='#5FC0D8')
frm7.pack(side=TOP)

frm8 = Frame(root,height=40,width=300,bg='#5FC0D8')
frm8.pack(side=TOP)

#Label

lbl1 = Label(frm6, text='Temp  Is ?? c',bg='#5FC0D8',fg=('#202020'))
lbl1.pack(padx=5, pady=5)

lbl2 = Label(frm5,text='For Get Temp Of Any hour , Click on it' ,bg='#5FC0D8',fg=('#202020'))
lbl2.pack(padx=5, pady=5)

lbl3 =Label(frm7,text='Click to see live weather' ,bg='#5FC0D8',fg=('#202020'))
lbl3.pack(padx=5, pady=5)



# variable

tempp = None

# Defination

def glw():
    tempp = temp[now_hour]
    lbl3.config(text=f'Live Weather of {now_hour}, Is {tempp} c')

def h00():
    tempp = temp[0]    
    lbl1.config(text=f'Temp Is {tempp} C')

def h01():
    tempp = temp[1]    
    lbl1.config(text=f'Temp Is {tempp} C')

def h02():
    tempp = temp[2]    
    lbl1.config(text=f'Temp Is {tempp} C')

def h03():
    tempp = temp[3]    
    lbl1.config(text=f'Temp Is {tempp} C')

def h04():
    tempp = temp[4]    
    lbl1.config(text=f'Temp Is {tempp} C') 

def h05():
    tempp = temp[5]    
    lbl1.config(text=f'Temp Is {tempp} C')  

def h06():
    tempp = temp[6]    
    lbl1.config(text=f'Temp Is {tempp} C')  

def h07():
    tempp = temp[7]    
    lbl1.config(text=f'Temp Is {tempp} C') 

def h08():
    tempp = temp[8]    
    lbl1.config(text=f'Temp Is {tempp} C')   

def h09():
    tempp = temp[9]    
    lbl1.config(text=f'Temp Is {tempp} C')  

def h10():
    tempp = temp[10]    
    lbl1.config(text=f'Temp Is {tempp} C')   

def h11():
    tempp = temp[11]    
    lbl1.config(text=f'Temp Is {tempp} C')

def h12():
    tempp = temp[12]    
    lbl1.config(text=f'Temp Is {tempp} C')

def h13():
    tempp = temp[13]    
    lbl1.config(text=f'Temp Is {tempp} C')

def h14():
    tempp = temp[14]    
    lbl1.config(text=f'Temp Is {tempp} C')

def h15():
    tempp = temp[15]    
    lbl1.config(text=f'Temp Is {tempp} C') 

def h16():
    tempp = temp[16]    
    lbl1.config(text=f'Temp Is {tempp} C')  

def h17():
    tempp = temp[17]    
    lbl1.config(text=f'Temp Is {tempp} C')  

def h18():
    tempp = temp[18]    
    lbl1.config(text=f'Temp Is {tempp} C') 

def h19():
    tempp = temp[19]    
    lbl1.config(text=f'Temp Is {tempp} C')   

def h20():
    tempp = temp[20]    
    lbl1.config(text=f'Temp Is {tempp} C')  

def h21():
    tempp = temp[21]    
    lbl1.config(text=f'Temp Is {tempp} C')    

def h22():
    tempp = temp[22]    
    lbl1.config(text=f'Temp Is {tempp} C')   

def h23():
    tempp = temp[23]    
    lbl1.config(text=f'Temp Is {tempp} C')  

def h24():
    tempp = temp[24]    
    lbl1.config(text=f'Temp Is {tempp} C')                         

# button

btn0 = Button(frm8,text='Live weather', command=glw)
btn0.pack(padx=10)


btn1 = Button(frm1,text='00',command=h00)
btn1.pack(padx=10,side=LEFT,pady=10)

btn2 = Button(frm1,text='01',command=h01)
btn2.pack(padx=10,side=LEFT)

btn3 = Button(frm1,text='02', command=h02)
btn3.pack(padx=10,side=LEFT)

btn4 = Button(frm1,text='03',command=h03)
btn4.pack(padx=10,side=LEFT)

btn5 = Button(frm1,text='04',command=h04)
btn5.pack(padx=10,side=LEFT)

btn6 = Button(frm1,text='05', command=h05)
btn6.pack(padx=10,side=LEFT)

#***********************************************

btn7 = Button(frm2,text='06',command=h06)
btn7.pack(padx=10,side=LEFT,pady=10)

btn8 = Button(frm2,text='07',command=h07)
btn8.pack(padx=10,side=LEFT)

btn9 = Button(frm2,text='08',command=h08)
btn9.pack(padx=10,side=LEFT)

btn10 = Button(frm2,text='09',command=h09)
btn10.pack(padx=10,side=LEFT)

btn11 = Button(frm2,text='10',command=h10)
btn11.pack(padx=10,side=LEFT)

btn12 = Button(frm2,text='11',command=h11)
btn12.pack(padx=10,side=LEFT)

#2***********************************************

btn13 = Button(frm3,text='12',command=h12)
btn13.pack(padx=10,side=LEFT,pady=10)

btn14 = Button(frm3,text='13',command=h13)
btn14.pack(padx=10,side=LEFT)

btn15 = Button(frm3,text='14',command=h14)
btn15.pack(padx=10,side=LEFT)

btn16 = Button(frm3,text='15',command=h15)
btn16.pack(padx=10,side=LEFT)

btn17 = Button(frm3,text='16',command=h16)
btn17.pack(padx=10,side=LEFT)

btn18 = Button(frm3,text='17',command=h17)
btn18.pack(padx=10,side=LEFT)

#***********************************************

btn19 = Button(frm4,text='18',command=h18)
btn19.pack(padx=10,side=LEFT,pady=10)

btn20 = Button(frm4,text='19',command=h19)
btn20.pack(padx=10,side=LEFT)

btn21 = Button(frm4,text='20',command=h20)
btn21.pack(padx=10,side=LEFT)

btn22 = Button(frm4,text='21',command=h21)
btn22.pack(padx=10,side=LEFT)

btn23 = Button(frm4,text='22',command=h22)
btn23.pack(padx=10,side=LEFT)

btn24 = Button(frm4,text='23',command=h23)
btn24.pack(padx=10,side=LEFT)

# footer 
lbl4 =Label(frm8,text='The App Created By Rahmatullah Hussaini@' ,bg='#5FC0D8',fg=('#202020'))
lbl4.pack(padx=5, pady=5)

root.mainloop()

