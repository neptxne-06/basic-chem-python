import csv
import webbrowser
from PIL import Image,ImageTk
from pathlib import Path
import tkinter
from tkinter import *
from tkinter import messagebox

op=Path(__file__).parent
ap= op/Path(r"C:\Users\Preksha Menon\Desktop\Spyder\CompProjectSEM1\images")
loadscr=None
usr=None
total=None

def img(path: str) -> Path:
    obj=ap/Path(path)
    return ImageTk.PhotoImage(file=obj)

def check():
    global usr
    if name.get()!='':
        usr=name.get()
        load(home,mn)
    else:
        messagebox.showinfo(':(','Please enter a username to proceed.')

def load(cur,frame):
    global loadscr
    cur.destroy()
    loadscr=Frame(root,bg='LightBlue1')
    loadscr.pack(fill=BOTH,expand=True)
    Label(loadscr,text='loading...',fg='navy',bg='LightBlue1',font='arial 50').place(x=520,y=350)
    root.after(800,frame)
    
def mn():
    global loadscr
    global usr
    loadscr.destroy()
    menu=Frame(root,bg='LightBlue1')
    menu.pack(fill=BOTH,expand=True)
    Label(menu,text='                                                                                     \n\n',bg='white',font='arial 40').place(x=-1,y=-1)
    Label(menu,text='ChemViz',font='fixedsys 70',fg='navy',bg='white').place(x=60,y=30)
    Label(menu,text=f'Hello, {usr}',font='arial 20',fg='navy',bg='white').place(x=65,y=120)
    Button(menu,text='EXIT',bg='navy',fg='white',font='Symbola 30',command=root.destroy).place(x=1130,y=700)
    Button(menu,text='      Periodic Table                                                                         ',bg='blue4',fg='white',font='arial 35',command=lambda:[load(menu,pt)]).place(x=-5,y=250)
    Button(menu,text='      Mass Calculator                                                                        ',bg='blue4',fg='white',font='arial 35',command=lambda:[load(menu,mc)]).place(x=-5,y=390)
    Button(menu,text='      Name Reactions                                                                         ',bg='blue4',fg='white',font='arial 35',command=lambda:[load(menu,nr)]).place(x=-5,y=530)
 
def pt():
    global loadscr
    loadscr.destroy()
    file=open('data.csv','r')
    cr=csv.reader(file)
    ele_lst=[]
    for ele in cr:
        if len(ele)>0:
            ele_lst.append(ele)
    file.close()
    main_ele=ele_lst[1:57]+ele_lst[72:89]+ele_lst[104:]
    rest_ele=ele_lst[57:72]+ele_lst[89:104]
    ptable=Frame(root,bg='LightBlue1')
    ptable.pack(fill=BOTH,expand=True)
    main_layout = [['x' ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,'x'],
                   ['x' ,'x' ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
                   ['x' ,'x' ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
                   ['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
                   ['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
                   ['x' ,'x' ,'' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
                   ['x' ,'x' ,'' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x']]
    sec_layout  = [['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
                   ['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x']]
    col={'Metal':'dodger blue','Nonmetal':'DodgerBlue3','Metalloid':'DodgerBlue4','Alkali Metal':'blue','Alkaline Earth Metal':'medium blue','Transition Metal':'blue4','Halogen':'RoyalBlue1','Noble Gas':'RoyalBlue3','Actinide':'SteelBlue3','Lanthanide':'SteelBlue1'}
    def single_main(cur):
        Label(ptable,text='                                 \n\n\n',font='arial 30').place(x=350,y=120)
        if len(main_ele[cur][4])<10:
            x=450
        elif len(main_ele[cur][4])<15:
            x=425
        elif len(main_ele[cur][4])<18:
            x=400
        else:
            x=350
        Label(ptable,text=main_ele[cur][2]+'\n'+main_ele[cur][0]+'\n'+main_ele[cur][3]+'\n'+main_ele[cur][4],fg=col[main_ele[cur][4]],font=(4,30)).place(x=x,y=120)
    def single_rest(cur):
        Label(ptable,text='                                 \n\n\n',font='arial 30').place(x=350,y=120)
        if len(rest_ele[cur][4])<9:
            x=450
        else:
            x=425
        Label(ptable,text=rest_ele[cur][2]+'\n'+rest_ele[cur][0]+'\n'+rest_ele[cur][3]+'\n'+rest_ele[cur][4],fg=col[rest_ele[cur][4]],font=(4,30)).place(x=x,y=120)
    Label(ptable,text='                                 \n\n\n',font='arial 30').place(x=350,y=120)
    n=0
    for i in main_layout:
        for j in i:
            if j=='x':
                Label(ptable,text='          \n\n',font='arial 13',bg=col[main_ele[n][4]]).place(x=20+70*(i.index(j)),y=120+70*(main_layout.index(i)))
                el=Label(ptable,text=main_ele[n][2]+'\n   '+main_ele[n][1]+'   \n',font='arial 13',bg=col[main_ele[n][4]],fg='white')
                el.place(x=20+70*(i.index(j)),y=120+70*(main_layout.index(i)))
                el.bind('<Button-1>',lambda e,n=n: single_main(n))
                el.bind('<Double-1>',lambda e,n=n: webbrowser.open(main_ele[n][5]))
                main_layout[main_layout.index(i)][i.index(j)]='o'
                n+=1
    n=0
    for i in sec_layout:
        for j in i:
            if j=='x':
                Label(ptable,text='          \n\n',font='arial 13',bg=col[rest_ele[n][4]]).place(x=50+70*(i.index(j)),y=630+70*(sec_layout.index(i)))
                el=Label(ptable,text=rest_ele[n][2]+'\n   '+rest_ele[n][1]+'   \n',font='arial 13',bg=col[rest_ele[n][4]],fg='white')
                el.place(x=50+70*(i.index(j)),y=630+70*(sec_layout.index(i)))
                el.bind('<Button-1>',lambda e,n=n: single_rest(n))
                el.bind('<Double-1>',lambda e,n=n: webbrowser.open(rest_ele[n][5]))
                sec_layout[sec_layout.index(i)][i.index(j)]='o'
                n+=1
    Button(ptable,text='BACK',bg='navy',fg='white',font='Symbola 30',command=lambda:[load(ptable,mn)]).place(x=1110,y=700)
    Label(ptable,text='      Periodic Table      ',fg='navy',font='fixedsys 70').place(x=-2,y=-2)

def mc():
    global loadscr,total
    loadscr.destroy()
    masscalc=Frame(root,bg='LightBlue1')
    masscalc.pack(fill=BOTH,expand=True)
    Button(masscalc,text='BACK',bg='navy',fg='white',font='Symbola 30',command=lambda:[load(masscalc,mn)]).place(x=1110,y=700)
    Label(masscalc,text='     Mass Calculator     ',fg='navy',font='fixedsys 70').place(x=-2,y=-2)
    options={}
    total=0
    file=open('data.csv','r')
    cr=csv.reader(file)
    cr=list(cr)
    del cr[0]
    for i in cr:
        if len(i)>0:
            options[i[0]]=(i[1],i[3])
    file.close()
    def add(ele):
        global total
        if ele!="":
            disp['text']+=(str(options[ele])+'\n')
            total+=float(options[ele][1])
            total=round(total,4)
            tot['text']=f'TOTAL:\n{total}'
    def rem(ele):
        global total
        if ele!="":
            temp=disp['text'].split('\n')
            for i in temp:
                if i==str(options[ele]):
                    temp.remove(i)
                    temp='\n'.join(temp)
                    disp['text']=temp
                    total=round(total,4)
                    total-=float(options[ele][1])
                    tot['text']=f'TOTAL:\n{total}'
                    break
    sel=StringVar(root)
    op=OptionMenu(masscalc,sel,*(options.keys()))
    op.place(x=50,y=150)
    op.config(width=20, font=("Arial", 20))
    Button(masscalc,text='ADD',font='arial 30',bg='dodger blue',fg='white',command=lambda:[add(sel.get())]).place(x=50,y=210)
    Button(masscalc,text='REMOVE',font='arial 30',bg='dodger blue',fg='white',command=lambda:[rem(sel.get())]).place(x=50,y=300)
    disp=Label(masscalc,bg='blue2',fg='white',text='',font='arial 30')
    disp.place(x=450,y=150)
    tot=Label(masscalc,bg='navy',fg='white',text=f'TOTAL:\n{total}',font='arial 30')
    tot.place(x=50,y=660)

def nr():
    def get_rec(r):
        if r!="":
            images.delete('all')
            r=f'{r}.png'
            image=img(r)
            root.image=image
            images.create_image(620,450,image=image)
    global loadscr
    loadscr.destroy()
    namerec=Frame(root,bg='LightBlue1')
    namerec.pack(fill=BOTH,expand=True)
    images=Canvas(namerec,bg='#bfefff',bd = 0,highlightthickness = 0,relief = "raised")
    images.pack(fill=BOTH,expand=True)
    Button(namerec,text='BACK',bg='navy',fg='white',font='Symbola 30',command=lambda:[load(namerec,mn)]).place(x=1110,y=700)
    Label(namerec,text='      Name Reactions       ',fg='navy',font='fixedsys 70').place(x=-2,y=-2)
    options=['Appel Reaction','Baeyer-Villiger oxidation','Bartoli indole synthesis','Baylis-Hillman reaction','Beckmann rearrangement','Biginelli reaction','Birch reduction','Buchwald-Hartwig amination','Cannizzaro reaction','Claisen condensation','Claisen rearrangement','Clemmensen reduction','Cope rearrangement','Corey-Kim oxidation','Curtius rearrangement','Dakin-West reaction','Dieckmann condensation','Diels-Alder reaction','Eschenmoser-Claisen rearrangement','Eschweiler-Clarke reaction','Finkelstein reaction','Fischer esterification','Fischer indole synthesis','Friedel-Crafts acylation','Friedel-Crafts alkylation','Fries rearrangement','Gabriel synthesis','Grignard reaction','Heck reaction','Hell-Volhard-Zelinsky reaction','Henry reaction','Hofmann elimination','Hofmann rearrangement','Ireland-Claisen rearrangement','Johnson-Claisen rearrangement','Jones oxidation','Knoevenagel condensation','Knorr pyrazole synthesis','Kolbe-Schmitt reaction','Kumada cross-coupling','Luche reduction','Mannich reaction','Michael addition','Mitsunobu reaction','Mukaiyama aldol addition','Negishi cross-coupling','Oppenauer oxidation','Pauson-Khand reaction','Perkin reaction','Pictet-Spengler reaction','Prins reaction','Reformatsky reaction','Reimer-Tiemann reaction','Ritter reaction','Robinson annulation','Sandmeyer reaction','Schmidt reaction','Schotten-Baumann reaction','Sharpless epoxidation','Sonogashira cross-coupling','Staudinger reaction','Stille cross-coupling','Strecker amino acid synthesis','Suzuki cross-coupling','Swern oxidation','Ullmann reaction','Vilsmeier-Haack reaction','Wagner-Meerwein rearrangement','Williamson ether synthesis','Wittig reaction','Wolff-Kishner reduction','Wolff rearrangement','Wurtz reaction','Yamaguchi esterification']
    sel=StringVar(root)
    op=OptionMenu(namerec,sel,*options)
    op.place(x=400,y=150)
    op.config(width=20, font=("Arial", 20))
    Button(namerec,text='->',font='arial 20',bg='navy',fg='white',command=lambda:[get_rec(sel.get())]).place(x=800,y=150)

root=Tk()
root.attributes('-fullscreen',True)

home=Frame(root,bg='navy')
home.pack(fill=BOTH,expand=True)
images=Canvas(home,bg='#ffffff',bd = 0,highlightthickness = 0,relief = "raised")
images.pack(fill=BOTH,expand=True)
grid=img('grid.png')
images.create_image(400,200,image=grid)
molec1=img('mol1.png')
images.create_image(1150,150,image=molec1)
molec2=img('mol2.png')
images.create_image(100,695,image=molec2)
Label(home,text='ChemViz',font='fixedsys 150',fg='navy',bg='white').place(x=395,y=120)
Label(home,text='Enter your name:',fg='navy',bg='white',font='arial 20').place(x=400,y=410)
name=Entry(home,font='arial 30',bg='LightBlue1')
name.place(x=400,y=450)
Button(home,text='ENTER',font='arial 40',bg='blue4',fg='white',command=lambda:[check()]).place(x=400,y=550)

root.mainloop()