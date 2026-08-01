import random
import time
import os
import streamlit as st
if os.path.exists("level_number.txt"):
 with open("level_number.txt","r") as f:
  rf= f.read().strip()
  if rf ==""or rf=="0" or rf=="0.0":
    file=1
  else:
   file=int(float(rf))

else:
 file=1
if 'level' not in st.session_state:
  st.session_state.level=int(file)
if 'ran' not in st.session_state or st.session_state.ran < 1:
  st.session_state.ran=int(20*st.session_state.level)
if 'num' not in st.session_state:
  st.session_state.num=0
if 'sc' not in st.session_state:
  st.session_state.sc=0
if 'count' not in st.session_state:
  st.session_state.count=0
if 'num1' not in st.session_state:
 st.session_state.num1=random.randint(1,int(st.session_state.ran))
if 'num2' not in st.session_state:
 st.session_state.num2=random.randint(1,int(st.session_state.ran))
if 'sign' not in st.session_state:
 st.session_state.sign=random.choice(['+','-','*','/'])
if 'feed' not in st.session_state:
 st.session_state.feed=0


num1 = st.session_state.num1
num2 = st.session_state.num2
sign = st.session_state.sign
if sign=='+':
 sc=num1+num2
if sign=='-':
 sc=num1-num2
if sign=='*':
 sc=num1*num2
if sign=='/':
 sc=num1//num2 
st.title("Welcome  ")
st.write(num1,sign,num2)
number=st.number_input("ادخل النتيجه ",step=1)
if st.button("تأكيد التخمين "):
  st.session_state.count += 1
  if number == sc:
   st.session_state.num += 1
   st.session_state.feed="correct"
  else:
   st.session_state.num =0
   st.session_state.feed="false" 
if st.session_state.feed=="correct":
  st.success("انك اسطوره يا عبقري الرياضه ")
  st.balloons()
  st.session_state.feed=None
  st.session_state.num1=random.randint(1,int(st.session_state.ran))
  st.session_state.num2=random.randint(1,int(st.session_state.ran))
  st.session_state.sign=random.choice(['+','-','*','/'])
  time.sleep(1)
  st.rerun()
if st.session_state.feed=="false":
  st.error(f"اجابتك خاطئة! الإجابة الصحيحة كانت : {sc}")
  st.session_state.feed=None
  st.session_state.num1=random.randint(1,int(st.session_state.ran))
  st.session_state.num2=random.randint(1,int(st.session_state.ran))
  st.session_state.sign=random.choice(['+','-','*','/'])
  time.sleep(1)
  st.rerun()

if st.session_state.num > 0 and st.session_state.num % 10 == 0:
  st.success("انت بطل! تحدي صديقك انه بالطبع لن يستطيع ان يصل لمستواك  ")
  if st.button("الليفل التالي "):
     st.balloons()
     st.session_state.level+=1
     st.session_state.num=0
     st.session_state.count=0
     with open("level_number.txt","w") as f:
      f.write(str(st.session_state.level))
st.write("your points are " ,st.session_state.num,"from",st.session_state.count,"Questions" )
st.write("you are in level",int(st.session_state.level))
