import time
from Wegmans.web import Web
from Wegmans.schedule import Schedule
from Wegmans.cal import Calendar


# Variables
email = 'EMAIL GOES HERE'
password = 'PASSWORD GOES HERE'
schedule = []


# Opens firefox to Mywegmansconnect
browser = Web(executable_path=r"/users/kyle/pycharmprojects/scripts/geckodriver")
browser.get('https://wegmans.sharepoint.com/Pages/default.aspx')
browser.sign_in(email, password)

# Navigate to labor pro and open schedule
browser.click_button_id('idBtn_Back')
browser.click_button_link_text('My Resources')
browser.click_button_link_text('My Schedule in LaborPro')

# Switching to new window
browser.switch_to.window(browser.window_handles[1])
time.sleep(10)
browser.switch_frame(0)  # Dynamic frame id
browser.click_button_link_text("Access Your Schedule")

# Switching to schedule tab
time.sleep(5)
browser.switch_to.window(browser.window_handles[2]) # change to two
browser.click_button_link_text('Next')

# Scraping data and creating lists
all_cells = browser.find_elements_by_class_name('cellContents')
cell_text = [] # A list of all the text from all_cells
for item in all_cells:
    cell_text.append(item.text)

schedule = Schedule(cell_text)
schedule.create_shifts()

# Uploading data to Google Calendar
cal = Calendar()
for shift in schedule.shifts:
    cal.create_event(shift.job, shift.start, shift.hours)
