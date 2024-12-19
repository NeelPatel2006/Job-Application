Shortlisted = []
Rejected = []
Processed_Applications = set()  

Min_Age = 18
Min_Experience = 2

while True:
    print("\nEnter a Choice Between:")
    print("1. Enter a Job Application")
    print("2. View Shortlisted Job Applications")
    print("3. View Rejected Job Applications")
    print("4. Exit!")
    choice = input("Enter your choice: ")

    if choice == "1":
        num_application = int(input("Enter the number of applications you want to enter: "))

        for _ in range(num_application):
            application_id = input("\nEnter Application ID: ").strip()

            if application_id in Processed_Applications:
                print(f"Application ID {application_id} already exists! Skipping...")
                continue

            
            name = input("Enter Name: ")
            Age = int(input("Enter Age: "))
            Experience = int(input("Enter Experience (in years): "))
            Qualification = input("Enter Qualification (e.g., phD, Master's, Bachelor's): ").strip()

            
            if Age >= Min_Age:
                if Experience >= Min_Experience:
                    if Qualification in ("phD", "Master's", "Bachelor's"):
                        Shortlisted.append(
                            f"Application {application_id} is shortlisted for the job\n"
                            f"Name: {name}\nAge: {Age}\nExperience: {Experience}\nQualification: {Qualification}"
                        )
                    else:
                        print("Required Qualification is (e.g., phD, Master's, Bachelor's)...")
                        Rejected.append(
                            f"Application {application_id} not shortlisted due to qualification criteria: {Qualification}\n"
                            f"Name: {name}\nAge: {Age}\nExperience: {Experience}\nQualification: {Qualification}"
                        )
                else:
                    Rejected.append(
                        f"Application {application_id} not shortlisted due to insufficient experience (minimum {Min_Experience} years).\n"
                        f"Name: {name}\nAge: {Age}\nExperience: {Experience}\nQualification: {Qualification}"
                    )
            else:
                Rejected.append(
                    f"Application {application_id} not shortlisted due to insufficient age (minimum {Min_Age} years).\n"
                    f"Name: {name}\nAge: {Age}\nExperience: {Experience}\nQualification: {Qualification}"
                )


            Processed_Applications.add(application_id)

    elif choice == "2":
        print("\nShortlisted Applications:")
        if Shortlisted:
            for application in Shortlisted:
                print(application)
        else:
            print("No shortlisted applications.")

    elif choice == "3":
        print("\nRejected Applications:")
        if Rejected:
            for application in Rejected:
                print(application)
        else:
            print("No rejected applications.")

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
