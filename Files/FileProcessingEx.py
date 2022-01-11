import sys
def computeModerateMarks(f1,f2,addpercent):
    try:
        fin=open(f1,'r')
        fout=open(f2,'w')
    except:
        print("FIle input error")  
    fline=fin.readline()
    while(fline!=''):
        line1=fline.split(',')
        id=line1[0]
        name=line1[1]
        mark=int(line1[2])
        modMark=mark+addpercent
        if(modMark>100):
            modMark=100
        mline=id+","+name+","+str(mark)+""
        fout.write(mline)
        fline=fin.readline()
    fin.close()
    fout.close()  

f1=input('Enter name of file1:')
f2=input('Enter name of file2:')
computeModerateMarks(f1,f2,3)

