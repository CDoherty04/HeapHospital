from maxheap import MaxHeap
from filehandler import file_handler


class Hospital:

    def __init__(self, file_name):
        self.instructions = file_handler(file_name)
        self.priority_queue = MaxHeap()

    def run(self):
        """handles function calls and user input for the program"""

        for instruction in self.instructions:

            match instruction.split(" ")[0]:

                # A patient arrives
                case "ARRIVE":
                    pass

                # Displays the information of the next patient in line
                case "NEXT":
                    pass

                # Treats the next patient in line
                case "TREAT":
                    pass

                # Displays patient count
                case "COUNT":
                    count = self.priority_queue.length()
                    if count == 1:
                        print("There is 1 patients waiting\n")
                    else:
                        print(f"There are {count} patients waiting\n")

                # Default case
                case _:
                    print("Invalid input, continuing...")
