str1 = input("")
str1 = str1.lower()
normal_string="".join(ch for ch in str1 if ch.isalnum())
st =""
st.join(normal_string)
w = ""
for i in st:
    w = i + w
 
if (st == w):
    print("True")
else:
    print("False")

