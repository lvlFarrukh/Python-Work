import csv
class patient():
    def __init__(self,name ,age ,phone ,address ,doctor_name ,doctor_type ,fee):
        """Contructor of class Patient"""
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.doctor_type = doctor_type
        self.doctor_name = doctor_name
        self.fee = fee

    def print_patient_sheet(self):
        print(f"!+{'-'*10}Patient Pay Slip{'-'*10}+!")
        print(f"\n\tName: {self.name}\n\tAge: {self.age}\n\tPhone Number: {self.phone}\n\tAddress: {self.address}\n\tDoctor Name: Dr.{self.doctor_name}\n\tSpecialized: {self.doctor_type}\n\tFee: {self.fee}")
        print("\n\tThank you For trust Us")
        print(f"!+{'-' * 36}+!")
    def generate_slip(self,file):
        self.file = file
        with open(self.file, "x") as slip:
            slip.write("!+----------Patient Pay Slip----------+!")
        with open(self.file,"a") as s:
            s.write(f"\n\tName: {self.name}\n\tAge: {self.age}\n\tPhone Number: {self.phone}\n\tAddress: {self.address}\n\tDoctor Name: Dr.{self.doctor_name}\n\tSpecialized: {self.doctor_type}\n\tFee: {self.fee}")
            s.write("\n\tThank you For trust Us")
            s.write("\n!+------------------------------------+!")
    def create_csv(self,flag):
        with open("patient_data.csv", "a") as pd:
            data_handler = csv.writer(pd, delimiter = ",")
            if flag == 1:
                data_handler.writerow(["Patient Name","Age","Phone Number","Address","Doctor Name"])
                data_handler.writerow([self.name, self.age, self.phone, self.address, self.doctor_name])
            else:
                data_handler.writerow([self.name,self.age,self.phone,self.address,self.doctor_name])
num_of_patient = 0
while(num_of_patient >= 0):
    dec = input("Continue[Y/N]: ").lower()
    if(dec == "n"):
        break
    else:
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        p_num = input("Enter Paitent Phone Number: ")
        Address = input("Enter Address: ")
        doc_name = input("Doctor For Consult: ")
        if doc_name.lower() == "hassan" or doc_name.lower() == "ali":
            doc_type = "Child Specialist"
            fee = "800"
        if doc_name.lower() == "farrukh" or doc_name.lower() == "taha":
            doc_type = "General Physican"
            fee = "500"
        pid777 = patient(name,age,p_num,Address,doc_name,doc_type,fee)
        pid777.print_patient_sheet()
        sheet_p = input("Print Slip[Y/N]: ").lower()
        if sheet_p == "y":
            num_of_patient += 1
            file = "patient" + str(num_of_patient) + ".txt"
            pid777.generate_slip(file)
        pid777.create_csv(num_of_patient)


