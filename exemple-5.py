files=['hello.txt','test.py','yo.pdf','joe.txt','numpy.py','starwars.pdf']
pdf_list=[]
i=0
pdf_count=0
while i< len(files):
    if ".pdf" in files[i]:
        pdf_list.append(files[i])
        pdf_count+=1
    i+=1
print(str(pdf_count)+" fichier(s) trouvé")
print(pdf_list)