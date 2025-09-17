attendance=[18,20,19,15,21] 
#full attendance
for x in attendance:
    if x >= 20:
        print(f"{x} full attendance")
    else : print(f"{x} attendence is not full")
    
#count of how many days class full
day=0
for a in attendance:
    if a>=20:
        day= day+1
print(f"full days count{day}")

#total attendance
total=0
for b in attendance:
    total+=b
print(f"total count {total}")     
