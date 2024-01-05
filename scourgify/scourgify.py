import sys
import csv

def main():

    #Expects the user to provide two command-line arguments
    if len(sys.argv) == 3:

        #the name of an existing CSV file to read as input
        before = sys.argv[1].strip()

        after = sys.argv[2].strip()


        if before.endswith(".csv") == True and after.endswith(".csv") == True:

            #columns are assumed to be, in order, name and house
            try:
                #open file as csvfile
                with open(before) as csvfile:

                    #asign reader the whole file as dictionary
                    reader = csv.DictReader(csvfile)

                    #initialize students as a list
                    students = []

                    #for each row in reader, that has the whole file
                    for row in reader:

                        #add a new dictionary to the list
                        students.append({"name": row["name"], "house": row["house"]})

                    #for each item(dict) in the students list (each student)
                    for student in students:

                        #get the value of the key "name"
                        name = student.get("name")

                        #split name in first and last
                        last, first = name.rsplit(sep=", ")

                        #assign first and last to the corresponding key in the student dict
                        student["first"] = first
                        student["last"] = last

                #open the after file on writing mode
                with open(after, "w") as csvfile:

                    #assign the DictWriter to the variable writer
                    writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"], extrasaction="ignore")

                    #write the header
                    writer.writeheader()

                    #write everything on the students list
                    writer.writerows(students)









                #the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
                #Converts that input to that output, splitting each name into a first name and last name
                #Assume that each student will have both a first name and last name.


            #if the first cannot be read, the program should exit via sys.exit with an error message.
            except FileNotFoundError:
                sys.exit("CSV file not found")

        else:
            sys.exit("Not a CSV file")

    #If the user does not provide exactly two command-line arguments,
    elif len(sys.argv) < 3:
        sys.exit("Not enough command-line arguments")

    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()
