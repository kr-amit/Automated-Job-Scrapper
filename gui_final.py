''' GUI for JobFinder program'''
from Tkinter import *
import ttk
from ttk import *
import pymongo
import tkMessageBox
#function to find jobs as per user input
def find_job(*args):
    tree=ttk.Treeview(frame)
    tree.grid(column=0,row=0,sticky=(N,S,W,E))
    s=ttk.Scrollbar(frame,orient=VERTICAL,command=tree.yview)
    s.grid(column=0,row=0,sticky=(N,S,E))
    tree['yscrollcommand']=s.set
    #tree['xscrollcommand']=t.set
    term=str(search_entry.get())
    client=pymongo.MongoClient()
    db=client.jobs
    jobs=[]
    cursor1=db.monsterindia.find({'$text':{'$search':term}})
    cursor2=db.fresherworld.find({'$text':{'$search':term}})
    cursor3=db.careerbuilder.find({'$text':{'$search':term}})
    for dat in cursor1:
        jobs.append(dat)
    for dat in cursor2:
        jobs.append(dat)
    for dat in cursor3:
        jobs.append(dat)
    #inserting data into the gui frame
    for i in range(len(jobs)):
        try:
            k=str(i)+'. '+jobs[i]['title']
            tree.insert('',i,jobs[i]['title'],text=k)
            tree.insert(jobs[i]['title'],'end',text='comapany: '+jobs[i]['company'])
            tree.insert(jobs[i]['title'],'end',text='skils: '+jobs[i]['skills'])
            tree.insert(jobs[i]['title'],'end',text='Location: '+jobs[i]['location'])
            tree.insert(jobs[i]['title'],'end',text='Link: '+jobs[i]['url'])
        except:
            tree.insert('',i,'NA',text='--title unavilable--')



#text description
st='''

                ---------JOB FINDER---------

This software aims to provide an efiicient way to
find IT jobs for people in a hassle free way.

Features:-

 1.Search by company name,location or relevant skills
   or a combination of keywords.

 2.Register to recieve job alerts.

 3.Refine your search under advanced serach'''

#function to store user contatct details for email notifications
def reg_user(*args):
    username=str(fname_entry.get())
    usermail=str(mail_entry.get())
    usercity=str(city_entry.get())
    userskills=str(skills_entry.get())
    conn=pymongo.MongoClient()
    db=conn.users
    db.userdetails.insert_one(
    {
    "name":username,
    "email":usermail,
    "city":usercity,
    "skills":userskills
    })
    new.withdraw()




#fuction to create register window
def register_user():
    make_visible()
    fname=ttk.Label(new,text="Name")
    mail=ttk.Label(new,text="E-Mail ID")
    cityname=ttk.Label(new,text="City Name")
    skill=ttk.Label(new,text="skills ")
    register=ttk.Button(new,text="Register",command=reg_user)
    Quit=ttk.Button(new,text="cancel",command=quit_new)
    register.grid(column=2,row=6,columnspan=2,sticky=(N,S,W))
    Quit.grid(column=4,row=6,columnspan=2,sticky=(N,S,W))
    fname.grid(column=0,row=2,sticky=(N,S,W))
    mail.grid(column=0,row=3,sticky=(N,S,W))
    cityname.grid(column=0,row=4,sticky=(N,W,S))
    skill.grid(column=0,row=5,sticky=(N,W,S))
    fname_entry.grid(column=3,row=2,columnspan=3,sticky=(N,S,E,W))
    mail_entry.grid(column=3,row=3,columnspan=3,sticky=(N,S,E,W))
    city_entry.grid(column=3,row=4,columnspan=3,sticky=(N,S,E,W))
    skills_entry.grid(column=3,row=5,columnspan=3,sticky=(N,S,E,W))
    for child in new.winfo_children(): child.grid_configure(padx=5, pady=5)
    new.columnconfigure(0,weight=2)
    new.columnconfigure(3,weight=2)
    new.columnconfigure(2,weight=2)
    #ttk.Sizegrip(new).grid(column=999, row=999, sticky=(S,E))

    new.geometry('320x250+450+250')



'''
def close_new():
    new.destroy()
'''

#functio to display latest trends in the job market
def latest_trends(*args):
    t=Toplevel(root)
    skill1=ttk.Label(t,text="most demanded skills",relief=RAISED)
    skill2=ttk.Label(t,text="In demand skill")
    skill3=ttk.Label(t,text="In demand skill")
    skill4=ttk.Label(t,text="In demand skill")
    skill5=ttk.Label(t,text="In demand skill")
    skill1.grid(column=2,row=1,columnspan=2,sticky=(N,S,E,W))
    skill2.grid(column=0,row=3,columnspan=2,sticky=(N,S,W))
    skill3.grid(column=0,row=4,columnspan=2,sticky=(N,S,W))
    skill4.grid(column=0,row=5,columnspan=2,sticky=(N,S,W))
    skill5.grid(column=0,row=6,columnspan=2,sticky=(N,S,W))
    skill2['text']="Java"
    skill3['text']="C/C++"
    skill4['text']="UI design"
    skill5['text']="Dot net developer"
    for child in new.winfo_children(): child.grid_configure(padx=5, pady=10)
    #t.columnconfigure(0,weight=2)
    #t.rowconfigure(1,weight=2)
    t.geometry("250x200+225+250")


#handle the close/quit operation
def on_closing():
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()


#to make the register window visible
def make_visible():
    global new
    new.deiconify()
#to close the registration window
def quit_new():
    global new
    new.withdraw()

def on_register():
    global new
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            new.destroy()



#creation of main window
root=Tk()
new=Toplevel(root)
new.withdraw()
fname_entry=ttk.Entry(new,width=10,textvariable="username")
mail_entry=ttk.Entry(new,width=10,textvariable="preference")
city_entry=ttk.Entry(new,width=10,textvariable="city")
skills_entry=ttk.Entry(new,width=10,textvariable="skills")

root.title("Find Your Dream Job")
#all the frames and widgets are initialised
mainframe=ttk.Frame(root,padding="3 3 12 12")
frame=ttk.Frame(mainframe,borderwidth=5,relief="sunken",width=175,height=100)
namelbl=ttk.Label(mainframe,text=st)
register=ttk.Button(mainframe,text="Register",command=register_user)
trends=ttk.Button(mainframe,text="latest trends",command=latest_trends)
search_entry=ttk.Entry(mainframe,width=30,textvariable="search")
searchJob=ttk.Button(mainframe,text="find",command=find_job)
Quit=ttk.Button(mainframe,text="quit!",command=on_closing)
tree=ttk.Treeview(frame)
tree.grid(column=0,row=0,sticky=(N,S,W,E))

frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)


#widgets and frames are placed according to grid layout
mainframe.grid(column=0,row=0,sticky=(N,S,E,W))
frame.grid(column=0,row=0,columnspan=3,rowspan=2,sticky=(N,S,E,W))
namelbl.grid(column=3,row=0,columnspan=2,sticky=(N,S,W))
search_entry.grid(column=3,row=1,columnspan=3,sticky=(N,W,E))
register.grid(column=0,row=3)
trends.grid(column=1,row=3)
searchJob.grid(column=3,row=3)
Quit.grid(column=4,row=3)
#s.grid(column=0,row=0)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
search_entry.focus()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=3)
mainframe.columnconfigure(1, weight=3)
mainframe.columnconfigure(2, weight=3)
mainframe.columnconfigure(3, weight=1)
mainframe.columnconfigure(4, weight=1)
mainframe.rowconfigure(1, weight=1)
root.geometry("800x500+350+175")
ttk.Sizegrip(root).grid(column=999, row=999, sticky=(S,E))
root.protocol("WM_DELETE_WINDOW", on_closing)
#key bindings
root.bind('<Return>',find_job)
root.mainloop()
