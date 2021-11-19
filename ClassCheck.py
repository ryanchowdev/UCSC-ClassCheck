# ClassCheck.py
#
# A web scraper for detecting availability of UCSC classes.
#
# Author: https://github.com/ryanyc2k
import time
import requests
from bs4 import BeautifulSoup
import tkinter as tk

# Set up Tkinter GUI
window = tk.Tk()
window.title("UCSC Class Checker")

frame_instr = tk.Frame(window)
frame_status = tk.Frame(window)
frame_entry = tk.Frame(window)
frame_button = tk.Frame(window)
    
instr = tk.Label(
    frame_instr,
    text=('Enter the class URL. '
        'From MyUCSC > Enrollment > Class Search, click on the class you want and copy the URL.\n'
        'It should look like https://pisa.ucsc.edu/...'
        ),
    height=3
)

status = tk.Label(
    frame_status,
    font='bold',
    text='STATUS: '
)

entry = tk.Entry(
    frame_entry,
    width=100,
)

button = tk.Button(
    frame_button,
    text='Go!',
    width=5,
    command=lambda:process(entry)
)

# Process input from text entry
def process(entry):
    url = entry.get()
    entry.delete(0, tk.END)
    scrape(url)

# Get data from the URL
def scrape(target):
    url = target
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    class_name = soup.find('div', {'class':'col-xs-12'}).findNext('h2', {'style':'margin:0px;'}).string.lstrip()
    capacity = int(soup.find('dt', text='Enrollment Capacity').findNext('dd').string)
    enrolled = int(soup.find('dt', text='Enrolled').findNext('dd').string)
    available = enrolled < capacity

    message_1 = f'     STATUS: {enrolled}/{capacity} spots filled. '
    message_2 = 'Class is AVAILABLE!' if available else 'Class is not available.'
    localtime = time.asctime(time.localtime(time.time()))

    window.title(class_name)
    status.config(text=localtime+message_1+message_2)
    if available:
        print('\a')  # Beep to alert user

    window.after(3000, lambda:scrape(url))  # Sleep for 3s

def main():
    # Sample URL
    # https://pisa.ucsc.edu/cs9/prd/sr9_2013/index.php?action=detail&class_data=YToyOntzOjU6IjpTVFJNIjtzOjQ6IjIyMTgiO3M6MTA6IjpDTEFTU19OQlIiO3M6NToiMjIzOTIiO30%3D

    # ----------------------------------------
    # |               instr                  |
    # |                                      |
    # |              status                  |
    # | entry                         button |
    # ----------------------------------------

    frame_instr.grid(row=0, column=0)
    frame_status.grid(row=1, column=0, pady=5)
    frame_entry.grid(row=2, column=0, padx=5)
    frame_button.grid(row=2, column=1, padx=5)
    instr.pack()
    status.pack()
    entry.pack()
    button.pack()
    
    window.mainloop()

if __name__=='__main__':
    main()