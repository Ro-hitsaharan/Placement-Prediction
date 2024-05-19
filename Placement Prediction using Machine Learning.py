
import pandas as pd

data = pd.read_csv('Placement.csv')

import warnings

warnings.filterwarnings('ignore')

"""### 1. Display Top 5 Rows of The Dataset"""

data.head()

"""### 2. Check Last 5 Rows of The Dataset"""

data.tail()

"""### 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)"""

data.shape

print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])

"""### 4. Get Information About Our Dataset Like the Total Number of Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement"""

data.info()

"""### 5. Check Null Values In The Dataset"""

data.isnull().sum()

"""### 6. Get Overall Statistics About The Dataset"""

data.describe()

"""### 7. EDA"""

data.columns

"""#### How Many Students Got Placed?"""

data['status'].unique()

data['status'].value_counts()

"""#### Could you display the top 5 sci&tech students placed according to their salary?"""

data.columns

data[(data['degree_t']=="Sci&Tech") & (data['status']=="Placed")].sort_values(by="salary",ascending=False).head()

"""### 8. Data Preprocessing"""

data.head()

data = data.drop(['sl_no','salary'],axis=1)

data.head(1)

"""#### Encoding the Categorical Columns"""

data['ssc_b'].unique()

data['ssc_b'] = data['ssc_b'].map({'Central':1,'Others':0})

data.head(2)

data['hsc_b'].unique()

data['hsc_b'] = data['hsc_b'].map({'Central':1,'Others':0})

data.head(2)

data['hsc_s'].unique()

data['hsc_s'] = data['hsc_s'].map({'Science':2,'Commerce':1,'Arts':0})

data.head()

data['degree_t'].unique()

data['degree_t'] = data['degree_t'].map({'Sci&Tech':2,'Comm&Mgmt':1,'Others':0})

data.head(2)

data['specialisation'].unique()

data['specialisation'] =data['specialisation'].map({'Mkt&HR':1,'Mkt&Fin':0})

data.head(2)

data['workex'].unique()

data['workex'] = data['workex'].map({'Yes':1,'No':0})

data.head(2)

data['status'].unique()

data['status'] = data['status'].map({'Placed':1,'Not Placed':0})

data.head()



"""### 9. Store Feature Matrix In X and Response(Target) In Vector y"""

data.columns

X = data.drop('status',axis=1)
y= data['status']

y

"""### 10. Splitting The Dataset Into The Training Set And Test Set"""

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=42)

"""### 11. Import The models"""

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

"""### 12. Model Training"""

lr = LogisticRegression()
lr.fit(X_train,y_train)

svm = svm.SVC()
svm.fit(X_train,y_train)

knn=KNeighborsClassifier()
knn.fit(X_train,y_train)

dt=DecisionTreeClassifier()
dt.fit(X_train,y_train)

rf=RandomForestClassifier()
rf.fit(X_train,y_train)

gb=GradientBoostingClassifier()
gb.fit(X_train,y_train)

"""### 13. Prediction on Test Data"""

y_pred1 = lr.predict(X_test)
y_pred2 = svm.predict(X_test)
y_pred3 = knn.predict(X_test)
y_pred4 = dt.predict(X_test)
y_pred5 = rf.predict(X_test)
y_pred6 = gb.predict(X_test)

"""### 14. Evaluating the Algorithms"""

from sklearn.metrics import accuracy_score

score1=accuracy_score(y_test,y_pred1)
score2=accuracy_score(y_test,y_pred2)
score3=accuracy_score(y_test,y_pred3)
score4=accuracy_score(y_test,y_pred4)
score5=accuracy_score(y_test,y_pred5)
score6=accuracy_score(y_test,y_pred6)

print(score1,score2,score3,score4,score5,score6)

final_data = pd.DataFrame({'Models':['LR','SVC','KNN','DT','RF','GB'],
            'ACC':[score1*100,
                  score2*100,
                  score3*100,
                  score4*100,
                  score5*100,score6*100]})

final_data

import seaborn as sns

sns.barplot(final_data['Models'],final_data['ACC'])

"""### 15. Prediction on New Data"""

new_data = pd.DataFrame({
    'gender':0,
    'ssc_p':67.0,
    'ssc_b':0,
    'hsc_p':91.0,
    'hsc_b':0,
    'hsc_s':1,
    'degree_p':58.0,
    'degree_t':2,
    'workex':0,
    'etest_p':55.0,
     'specialisation':1,
    'mba_p':58.8,
},index=[0])

lr= LogisticRegression()
lr.fit(X,y)

p=lr.predict(new_data)
prob=lr.predict_proba(new_data)
if p==1:
    print('Placed')
    print(f"You will be placed with probability of {prob[0][1]:.2f}")
else:
    print("Not-placed")

prob

"""### 16. Save Model Using Joblib"""

import joblib

joblib.dump(lr,'model_campus_placement')

model = joblib.load('model_campus_placement')

model.predict(new_data)

"""### GUI"""

from tkinter import *
import joblib
import numpy as np
from sklearn import *
import tkinter.font as font
import pandas as pd

def show_entry_fields():
    text = clicked.get()
    if text == "Male":
        p1=1
        print(p1)
    else:
        p1=0
        print(p1)
    p2=float(e2.get())
    text = clicked1.get()
    if text == "Central":
        p3=1
        print(p3)
    else:
        p3=0
        print(p3)
    p4=float(e4.get())
    text = clicked6.get()
    if text == "Central":
        p5=1
        print(p3)
    else:
        p5=0
        print(p3)
    text = clicked2.get()
    if text == "Science":
        p6=2
        print(p6)
    elif text == "Commerce":
        p6=1
        print(p6)
    else:
        p6=0
        print(p6)
    p7=float(e7.get())
    text = clicked3.get()
    if text == "Sci&Tech":
        p8=2
        print(p8)
    elif text=="Comm&Mgmt":
        p8=1
        print(p8)
    else:
        p8=0
        print(p8)
    text = clicked4.get()
    if text == "Yes":
        p9=1
        print(p3)
    else:
        p9=0
        print(p3)
    p10=float(e10.get())
    text = clicked5.get()
    if text == "Mkt&HR":
        p11=1
        print(p11)
    else:
        p11=0
        print(p11)
    p12=float(e12.get())

    model = joblib.load('model_campus_placement')
    new_data = pd.DataFrame({
    'gender':p1,
    'ssc_p':p2,
    'ssc_b':p3,
    'hsc_p':p4,
    'hsc_b':p5,
    'hsc_s':p6,
    'degree_p':p7,
    'degree_t':p8,
    'workex':p9,
    'etest_p':p10,
     'specialisation':p11,
    'mba_p':p12,
},index=[0])
    result=model.predict(new_data)
    result1=model.predict_proba(new_data)

    if result[0] == 0:
        Label(master, text="Can't Placed").grid(row=31)
    else:
        Label(master, text="Student Will be Placed With Probability of",font=("Arial", 15)).grid(row=31)
        Label(master, text=round(result1[0][1],2)*100,font=("Arial", 15)).grid(row=33)
        Label(master, text="Percent",font=("Arial", 15)).grid(row=34)

master = Tk()
master.title("Campus Placement Prediction System")


label = Label(master, text = "Campus Placement Prediction System"
                          , bg = "green", fg = "white",font=("Arial", 20)) \
                               .grid(row=0,columnspan=2)


Label(master, text="Gender",font=("Arial", 15)).grid(row=1)
Label(master, text="Secondary Education percentage- 10th Grade",font=("Arial", 15)).grid(row=2)
Label(master, text="Board of Education",font=("Arial", 15)).grid(row=3)
Label(master, text="Higher Secondary Education percentage- 12th Grade",font=("Arial", 15)).grid(row=4)
Label(master, text="Board of Education",font=("Arial", 15)).grid(row=5)
Label(master, text="Specialization in Higher Secondary Education",font=("Arial", 15)).grid(row=6)
Label(master, text="Degree Percentage",font=("Arial", 15)).grid(row=7)
Label(master, text="Under Graduation(Degree type)- Field of degree education",font=("Arial", 15)).grid(row=8)
Label(master, text="Work Experience",font=("Arial", 15)).grid(row=9)
Label(master, text="Enter test percentage",font=("Arial", 15)).grid(row=10)
Label(master, text="branch specialization",font=("Arial", 15)).grid(row=11)
Label(master, text="MBA percentage",font=("Arial", 15)).grid(row=12)
clicked = StringVar()
options = ["Male","Female"]

clicked1 = StringVar()
options1 = ["Central","Others"]

clicked2 = StringVar()
options2 = ["Science","Commerce","Arts"]

clicked3 = StringVar()
options3 = ["Sci&Tech","Comm&Mgmt","Others"]

clicked4 = StringVar()
options4 = ["Yes","No"]

clicked5 = StringVar()
options5 = ["Mkt&HR","Mky&Fin"]

clicked6 = StringVar()
options6 = ["Central","Others"]
e1 = OptionMenu(master , clicked , *options )
e1.configure(width=13)
e2 = Entry(master)
e3 = OptionMenu(master , clicked1 , *options1 )
e3.configure(width=13)
e4 = Entry(master)
e5 = OptionMenu(master , clicked6 , *options6)
e5.configure(width=13)
e6 = OptionMenu(master , clicked2 , *options2)
e6.configure(width=13)
e7 = Entry(master)
e8 = OptionMenu(master , clicked3 , *options3)
e8.configure(width=13)
e9 = OptionMenu(master , clicked4 , *options4)
e9.configure(width=13)
e10 = Entry(master)
e11 = OptionMenu(master , clicked5 , *options5)
e11.configure(width=13)
e12 = Entry(master)


e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
e10.grid(row=10, column=1)
e11.grid(row=11, column=1)
e12.grid(row=12, column=1)
buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
Button(master, text='Predict',height= 1, width=8,activebackground='#00ff00',font=buttonFont,bg='black', fg='white',command=show_entry_fields).grid()

mainloop()

