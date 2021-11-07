def moderate(marks, passMarks):
    if(marks==passMarks-1 or marks==passMarks-2):
        marks=passMarks
    return marks

passMarks=40
marks=int(input("Enter marks: "))
moderatedMarks=moderate(marks,passMarks)
print("Moderated marks: ",moderatedMarks)
