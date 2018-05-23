file1=open("new1.txt","w")
file1.write("hello world!! howz u all?")
file1.close()
file1= open("new1.txt","a")
file1.write("\nhy i m himani")
file1.close()
with open("new1.txt","a") as f:
     f.write("\nmy name is himani tilayacha.")
     
