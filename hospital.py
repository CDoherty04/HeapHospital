from maxheap import MaxHeap
from filehandler import file_handler
from patient import Patient


class Hospital:

    def __init__(self, file_name):
        self.lines = file_handler(file_name)
        self.priority_queue = MaxHeap()

    def run(self):
        """handles function calls and user input for the program"""

        print("\n-----------------------------\n")

        for line in self.lines:
            instruction = line.split(" ")

            match instruction[0].upper():

                # A patient arrives
                case "ARRIVE":
                    try:
                        # Fill out the patient's information
                        new_patient = Patient(instruction[1], instruction[2], instruction[3],
                                              instruction[4], instruction[5])

                        # Add them to the queue
                        new_patient.set_arrival(self.priority_queue.length()+1)
                        self.priority_queue.add(new_patient)
                    except IndexError:
                        print("There seems to be a problem processing this patients information, "
                              "we'll have to turn them away.\n")

                # Displays the information of the next patient in line
                case "NEXT":
                    if self.priority_queue.length() < 1:
                        print("There is no next patient\n")
                    else:
                        print("Next patient:")
                        print(self.priority_queue.get_max())
                        print()

                # Treats the patient with the highest severity level, who is next in line
                case "TREAT":
                    if self.priority_queue.length() < 1:
                        print("There is no patient to treat\n")
                    else:
                        self.priority_queue.remove()

                # Displays patient count
                case "COUNT":
                    count = self.priority_queue.length()
                    if count == 1:
                        print("There is 1 patient waiting\n")
                    else:
                        print(f"There are {count} patients waiting\n")

                # Default case
                case _:
                    print("Invalid input, continuing...\n")
