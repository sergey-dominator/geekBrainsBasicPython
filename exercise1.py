class Date:
    day = None
    month = None
    year = None

    @classmethod
    def parse(cls, date):
        split_date = date.split("-")
        if len(split_date) != 3:
            raise ValueError("Wrong date format")

        try:
            cls.day = int(split_date[0])
            cls.month = int(split_date[1])
            cls.year = int(split_date[2])
        except ValueError:
            print("Wrong date type")
            cls.day = None
            cls.month = None
            cls.year = None

    @staticmethod
    def validate(date):
        # doesn't work for leap year
        day_of_month_count = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if 0 < date.month < 13:
            if 0 < date.day < day_of_month_count[date.month]:
                # doesn't support years BC
                if date.year >= 0:
                    print("It's correct date")
                else:
                    print("Wrong year")
            else:
                print("Wrong day of the month")
        else:
            print("Wrong month")

    def __str__(self):
        return f'Current date: {self.day}-{self.month}-{self.year}'


custom_date = Date()
custom_date.parse("12-1-1000")
print(custom_date)
Date.validate(custom_date)
