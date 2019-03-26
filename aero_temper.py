with open('temper.txt','r') as file:
    contents=file.read()
k=0
s=contents.split()
st=[]
for i in s:
    st.append(float(i))
for i in st:
    if st.count(i)==1:
        k=k+1
print("Максимальная температура: ", max(st),
      "\nМинимальная температура: ", min(st),
      "\nСредняя температура: ", sum(st)/len(st),
      "\nЧисло уникальных температур:  ", k)
