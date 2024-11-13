class Time:
    def __init__(self, hour=0, minute=0):
        self.hour = hour % 24  
        self.minute = minute % 60 

    def tick(self):
        self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour = (self.hour + 1) % 24

    def __sub__(self, other):
        if not isinstance(other, Time):
            raise TypeError("Subtraction only supported between Time objects")
        self_minutes = self.hour * 60 + self.minute
        other_minutes = other.hour * 60 + other.minute
        diff_minutes = abs(self_minutes - other_minutes)
        hours = diff_minutes // 60
        minutes = diff_minutes % 60
        return hours, minutes

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def getTime(self):
        return self.hour, self.minute

    def setTime(self, hour, minute):
        self.hour = hour % 24
        self.minute = minute % 60

    def __lt__(self, other):
        if not isinstance(other, Time):
            raise TypeError("Comparison only supported between Time objects")
        
        return (self.hour, self.minute) < (other.hour, other.minute)

    def __len__(self):
        return self.hour * 60 + self.minute

