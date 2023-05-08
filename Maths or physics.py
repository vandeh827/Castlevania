class Maths:
    def _init_(self):
        self.questions = {
            "1+1": 2,
            "2*3": 6,
            "4/2": 2,
            "5-3": 2,
            "2**3": 8
        }

    def ask_question(self, question):
        return self.questions.get(question, "Invalid question")


class Physics:
    def _init_(self):
        self.questions = {
            "F=ma, what is the force when mass is 5kg and acceleration is 10m/s^2?": 50,
            "What is the formula for kinetic energy?": "KE = 1/2 * m * v^2",
            "What is the SI unit of force?": "Newton",
            "What is the law of gravitation?": "F = G * (m1 * m2) / r^2",
            "What is the unit of power?": "Watt"
        }

    def ask_question(self, question):
        return self.questions.get(question, "Invalid question")


# Main program
print("Welcome to the calculator program!")
while True:
    print("What subject do you want to learn about?")
    subject = input("Enter 'maths' or 'physics' (or 'quit' to exit): ")
    if subject.lower() == "quit":
        print("Goodbye!")
        break
    elif subject.lower() == "maths":
        maths = Maths()
        print("What operation do you want to perform?")
        operation = input("Enter a question (e.g. '2*3'): ")
        answer = maths.ask_question(operation)
        print(f"The answer to {operation} is: {answer}")
    elif subject.lower() == "physics":
        physics = Physics()
        print("What operation do you want to perform?")
        operation = input("Enter a question (e.g. 'What is the formula for kinetic energy?'): ")
        answer = physics.ask_question(operation)
        print(f"The answer to '{operation}' is: {answer}")
    else:
        print("Invalid subject. Please try again.")