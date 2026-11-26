class Clock:
    def __init__(self, hour, minute):
        """
        hour: clock hour
        minutes: clock min
        Convert everything to total minutes and normalize across a 24-hour             day (1440 minutes)
        """ 
        total_minutes = (hour * 60 + minute) % 1440
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return False
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        # Simply pass the added minutes into a new Clock; __init__ handles the rollover
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        # Simply subtract the minutes; Python's modulo (%) handles negative results perfectly
        return Clock(self.hour, self.minute - minutes)

