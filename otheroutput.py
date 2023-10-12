class Army:
    def __init__(self, education, height, weight, age):
        self.education = education
        self.height = height
        self.weight = weight
        self.age = age

    def final_test(self):
        if self.education in ['SSC', 'HSC', 'BSC', 'MA', 'MSC', 'MBA', 'BCS', 'DAKHIL', 'DAKIL', 'DAKHEL', 'DEKHIL', 'DEKIL', 'DEKEL', 'DEKHEL', 'ALIM', 'ALAM', 'ALEM', 'ALIM', 'FAZEL', 'FAZIL', 'FEZEL', 'FEZEL', 'FEJIL', 'FEJEL', 'M.A', 'B.SC', 'M.SC', 'B.C.S', 'M.B.A']:
            if self.height >= 5.6:
                if 52 <= self.weight <= 65:
                    if 18 <= self.age <= 23:
                        return True
                    else:
                        print(f'Your age, ({self.age}) is not according to Army admission Law')
                else:
                    print(f'Your weight, ({self.weight}) is not according to Army admission Law')
            else:
                print(f'Your height, ({self.height}) is not according to Army admission Law')
        else:
            print(f'Your education, ({self.education}) is not according to Army admission Law')
        return False

    def medical(self):
        if self.final_test():
            medical_test = input("Has the candidate's medical test passed? (Yes or No)").upper()
            if medical_test == "YES":
                return True
            else:
                print("Sorry! Candidate's medical test is not passed.")
        else:
            print("False final")

    def training(self):
        if self.medical():
            training_info = input("Has the candidate successfully trained up all? (Yes or No)").upper()
            if training_info == "YES":
                print("Congratulations! You have passed all tests of BD Army. You are now a battalion of Bangladesh.")
            else:
                print("You have to be trained up in all aspects. Please wait a few days. Thank you.")
        else:
            print("Failed medical")

education = input("Enter your education: ").upper()
height = float(input("Height should be in feet unit. Enter your height: "))
weight = float(input('Enter your weight in KG: '))
age = float(input('Enter age of the candidate: '))
cp = Army(education, height, weight, age)
cp.training()
