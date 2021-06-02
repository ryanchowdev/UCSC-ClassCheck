# ClassCheck.py
#
# A web scraper for detecting availability of UCSC classes.
#
# Author: https://github.com/ryanyc2k
import requests
from bs4 import BeautifulSoup
import tkinter as tk

window = tk.Tk()

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
        print('\a') # beep
    else:
        print('CLASS NOT AVAILABLE')

    window.after(3000, lambda:scrape(url)) # sleep for 3s

def main():
    # sample URL
    # https://pisa.ucsc.edu/cs9/prd/sr9_2013/index.php?action=detail&class_data=YToyOntzOjU6IjpTVFJNIjtzOjQ6IjIyMTgiO3M6MTA6IjpDTEFTU19OQlIiO3M6NToiMjIzOTIiO30%3D
    
    instruction = tk.Label(
        window,
        text='Enter the class URL. It should look like https://pisa.ucsc.edu/...',
        height=5
    )

    entry = tk.Entry(
        window,
        width=150,
    )

    button = tk.Button(
        window,
        text='Go!',
        height=1,
        command=lambda: get_url(entry)
    )

    instruction.pack()
    button.pack()
    entry.pack()

    window.mainloop()

if __name__=='__main__':
    main()