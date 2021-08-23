import Date

class TemperatureData:
    def __init__(self, month_in, year_in, min_temp, max_temp, snow_fall):
        self.date = Date.Date(month_in, year_in)
        self.minTemperature = min_temp
        self.maxTemperature = max_temp
        self.snowFall = snow_fall
        