class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary


    def get_salary(self):
        if self.position == "Manager":
            return self.__salary
        else:
            print("Access Denied!")


    def set_salary(self, new_salary):
        if self.position != "Manager":
            print("Access Denied! Only managers can change salary.")
            return

        if new_salary < 7_000_000:
            print("Error: Salary cannot be less than minimum legal amount.")
            return

        self.__salary = new_salary
        print("Salary updated successfully.")


    def del_salary(self):
        if self.position != "Manager":
            print("Access Denied! Only managers can delete salary.")
            return

        del self.__salary
        print("Salary record deleted.")

e1 = Employee("Ali", "Developer", 12000000)
e2 = Employee("Sara", "Manager", 25000000)

print(e1.get_salary())
print(e2.get_salary())

e1.set_salary(15000000)
e2.set_salary(6_000_000)
e2.set_salary(30_000_000)

e1.del_salary()
e2.del_salary()
