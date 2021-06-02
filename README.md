# UCSC-ClassCheck
A python BeautifulSoup web scraper that checks the availability of UCSC classes.  
NOTE: While this project does have full functionality, it is a work-in-progress and needs to be refined.  
In particular, the GUI is currently unfinished.  
  
## Running the web scraper locally
The following instructions are for UNIX-like operating systems.  
The web scraper will also work on Windows. You just need to ensure you have installed all the necessary packages.  

First, make sure you have python3 and python3-pip installed.  
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip
```
  
You must then install the following packages:  
```bash
pip3 install requests beautifulsoup4
```
  
You will also need tkinter if your python install does not come with it.  
  
Now you can run the web scraper.  
```bash
python3 ClassCheck.py
```
  
Or simply double click the icon to open it with python.