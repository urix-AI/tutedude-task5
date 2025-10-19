
students={
    'bhuvnesh':92,
    'kushali':26,
    'xyz':56
}
a = str(input("enter a number : "))

if a in students :
    print(f"{a} scored {students[a]}")
else:
    print(f"{a} student not found")

