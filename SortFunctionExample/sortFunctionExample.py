# sort() method = used with lists
# sort() function = used with iterables

# I
# students = ["Squidward", "Sandy", "Patcick", "Spongebob", "Mr.Krabs"]

# students.sort(reverse=True)

# II
# students = ("Squidward", "Sandy", "Patcick", "Spongebob", "Mr.Krabs")

# sorted_students = sorted(students, reverse=True)

# for i in sorted_students:
#     print(i)

students = [("Squidward", "F", 60),
            ("Patrick", "A", 33),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

grade = lambda grades:grades[1]
students.sort(key=grade, reverse=True)
# sorted_students = sorted(students, key=grades) # for tuples

for i in students:
    print(i)