# Q6. WAP to mine a log file and find out whether it contains "python"
with open("log.txt","r") as f:
    content=f.read()
    
if("python" in content):
    print("yes python is present")
else:
    print("not found!")    


#   OR
with open("log.txt","r") as f:
    lines= f.readlines()
line=1
for line in lines:
    if "python" in line:
        print(f'Yes python is present, in line no:{line}')
        break
    line += 1    
else:
    print("No python is present")    
    