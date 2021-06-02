# ClassCheck.py
#
# A web scraper for detecting availability of UCSC classes.
#
# Author: https://github.com/ryanyc2k
import requests
from bs4 import BeautifulSoup
import tkinter as tk

window = tk.Tk()
window.title("UCSC Class Checker")

def get_url(entry):
    url = entry.get()
    entry.delete(0, tk.END)
    scrape(url)

def scrape(target):
    url = target
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    class_name = soup.find('div', {'class':'col-xs-12'}).findNext('h2', {'style':'margin:0px;'}).string
    capacity = int(soup.find('dt', text='Enrollment Capacity').findNext('dd').string)
    enrolled = int(soup.find('dt', text='Enrolled').findNext('dd').string)
    available = enrolled < capacity
        
    print(f'{class_name}\n')
    print(f'Status: {enrolled} / {capacity} spots filled.')
    if available:
        print('CLASS AVAILABLE')
        print('\a')   # Beep to notify user
    else:
        print('CLASS NOT AVAILABLE')

    window.after(3000, lambda:scrape(url))   # Sleep for 3s

def main():
    # Sample URL
    # https://pisa.ucsc.edu/cs9/prd/sr9_2013/index.php?action=detail&class_data=YToyOntzOjU6IjpTVFJNIjtzOjQ6IjIyMTgiO3M6MTA6IjpDTEFTU19OQlIiO3M6NToiMjIzOTIiO30%3D

    frame_instr = tk.Frame(window)
    frame_entry = tk.Frame(window)
    frame_button = tk.Frame(window)
    
    instr = tk.Label(
        frame_instr,
        text=('Enter the class URL. '
            'From MyUCSC > Enrollment > Class Search, click on the class you want and copy the URL.\n'
            'It should look like https://pisa.ucsc.edu/...'
            ),
        height=5
    )

    entry = tk.Entry(
        frame_entry,
        width=100,
    )

    button = tk.Button(
        frame_button,
        text='Go!',
        width=5,
        command=lambda:get_url(entry)
    )

    frame_instr.grid(row=0, column=0)
    instr.pack()
    frame_entry.grid(row=1, column=0, padx=5)
    entry.pack()
    frame_button.grid(row=1, column=1, padx=5)
    button.pack()

    window.mainloop()

if __name__=='__main__':
    main()