m=int(input("marks of maths: "))
s=int(input("marks of science: "))
e=int(input("marks of english: "))

total_marks=m+s+e
avg_marks=total_marks/3
percentage=(total_marks/300)*100

grade=""
if(percentage > 90):
   grade ="A"
elif percentage>80 and percentage<=90:
   grade = "B"
elif percentage>70 and percentage<=80:
   grade ="C"
else:
    grade = "P"
print(f"total_marks: {total_marks}\n avg_marks:{avg_marks} \n grade{grade}")
