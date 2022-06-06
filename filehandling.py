# ------------------------File Handling ------------------

# f1 = open("abc.txt", "r")
# # readline()  it use for the read the line in file
# lines = f1.read()
# print(lines)
#
# f2 = open("abc.txt", "r")
# lines2 = f2.readlines()
# for i in lines2:
#     print(i,end="")

# f1=open("abc.txt","w")
# f1.close()

# with open("abc.txt","w") as f2:
#     print(" no need for writing f2.close().")
#
# f1=open("abcmoo.txt","w")
# f1.writelines("HII, MY NAME IS MOHIT SHARMA.\n")
# f1.writelines("I AM A BAD BOY.\n")
# f1.writelines("I AM FROM GOVERDHAN.\n")
# f1.writelines("BEST FRIEND NAME :-")
# f1.writelines(" SATYAPRAKASH,LUVKUSH,HEMENDRA\n")
# f1.writelines("SALE POORE PAGAL HAI BC.")
# f1.close()

# f2=open("abcmoo.txt","a")
# f2.writelines("\nDON'T WHAT I AM WRITE ")
# f2.close()

# Q2.
# copy paste the one file content to another file.

# f1=open("abcmoo.txt","r")
# copy=f1.read()
# f2=open("abc.txt","w")
# f2.write(copy)
# f2.close()
# f1.close()

# Q 1.
# f1 = open("abcmoo.txt", "w")
# f1.writelines("My Name is Mohit Sharma.\n")
# f1.writelines("I AM A BAD BOY.\n")
# f1.writelines("I AM FROM GOVERDHAN.\n")
# f1 = open("abcmoo.txt","r")
# x=len(f1.readlines())
# print(x)
# f1.close()

# Q 3.
# f1 = open("abcmoo.txt", "w")
# f1.writelines("AAAAAAAAAAAAAaaaaaaaaaaaBBBBBBBBBBBBBBbbbbbbbbbbCCCCCcccc\n")
# f1.writelines("CCCCCbbbbbbbbbbBBaaaaaaaaaBBABAAAAABB\n")
# f1 = open("abcmoo.txt","r")
# text = f1.readlines()
# countA=0
# counta=0
# countB=0
# countb=0
# countC=0
# countc=0
# for i in text:
#     for j in i:
#         if 'A' == j:
#             countA+=1
#         elif 'B' == j:
#             countB+=1
#         elif 'a' == j:
#             counta+=1
#         elif 'b' == j:
#             countb+=1
#         elif 'C' == j:
#             countC+=1
#         elif 'c' == j:
#             countc+=1
#
# print(f"""
# The freacuency of A is: {countA}\n
# The freacuency of a is: {counta}\n
# The freacuency of B is: {countB}\n
# The freacuency of b is: {countb}\n
# The freacuency of C is: {countC}\n
# The freacuency of c is: {countc}\n
# """)
# f1.close()

# Q 4.
# f1=open("abcmoo.txt","r")
# copy1=f1.readlines()
# f1.close()
# f2=open("abc.txt","r")
# copy2=f2.readlines()
# f2.close()
# if copy1 == copy2:
#     print("same same")
# else:
#     print("different")