import re
import datetime
import pickle
from Wegmans.shift import Shift


def test(): #TEMP
    file = open('/Users/kyle/pycharmprojects/Main_project/store.pckl', 'rb')
    list1 = pickle.load(file)
    schedule = Schedule(list1)
    schedule.create_shifts()
    for item in schedule.shifts:
        print(item.hours)


class Schedule:  # Organizes shift objects
    def __init__(self, content):
        self.content = content
        self.shifts = []

    def grab_data(self, data, index):  # Takes a list and index and converts list item to a list
        data = data[index].split(' ')
        return data

    def get_hours(self):  # Returns list of hours worked each day
        hours = self.grab_data(self.content, 2)
        del hours[:2]  # Keeps only the data in the list
        return hours

    def get_jobs(self):  # Returns list of each job title
        jobs = re.findall(r'FE \w+', self.content[3])
        return jobs

    def get_dates(self):  # Returns a list of 7 date objects of the week
        start_date = (re.findall(r'\d+/\d\d/\d\d\d\d', self.content[0])[0])
        start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y')
        dates = []
        for i in range(7):
            dates.append((start_date + datetime.timedelta(days=i)).date())
        return dates

    def get_start_times(self):  # Returns list of time objects for start times
        start_times = (re.findall(r'\d+:\d\d\s\wM-', self.content[5]))
        count = 0
        new_start_times = []
        for item in start_times:
            new_start_times.append(datetime.datetime.strptime(item, '%I:%M %p-').time())
            count += 1
        return new_start_times

    def create_shifts(self):  # Creates a list of Shift objects and saves the hours, start and job to each shift
        hours = self.get_hours()
        jobs = self.get_jobs()
        times = self.get_start_times()
        dates = self.get_dates()
        shift_num = 0
        for i in range(7):
            if hours[i] != '0:00':
                self.shifts.append(Shift(hours=float(hours[i])))
                self.shifts[shift_num].job = jobs[shift_num]
                self.shifts[shift_num].start = datetime.datetime.combine(dates[i], times[shift_num])
                shift_num += 1

#test()