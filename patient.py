class Patient:
    """Class that holds necessary information for a hospital patient"""

    def __init__(self, first_name, last_name, age, illness, severity):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.illness = illness
        self.severity = severity
        self.arrival_order = 0

    def set_arrival(self, order):
        """Allows the hospital to change the order of arrival compared to other patients"""

        self.arrival_order = order

    def __gt__(self, other):
        """Compares by severity, then age, then arrival order"""

        if self.severity > other.severity:
            return True
        if self.severity == other.severity:

            # If severity isn't greater than, but it is equal, then check age
            if self.age > other.age:
                return True
            if self.age == other.age:

                # If age isn't greater than, but it is equal, then check arrival order
                if self.arrival_order < other.arrival_order:
                    return True

        # Otherwise it must be less than
        return False

    def __repr__(self):
        """The patient's information is displayed in a well formatted way"""

        return (f"Name: {self.last_name}, {self.first_name}.\nAge: {str(self.age)}\nSuffers from: "
                f"{self.illness}\nIllness severity: {str(self.severity)}\nArrival order: {self.arrival_order}")
