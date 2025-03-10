**Isle Map Updater**

**Description**
Opens islemaps.com in a new Chrome window and updates your map location anytime you copy your coordinates in-game.

**Installation**
Clone the repository:

git clone https://github.com/yourusername/your-repo.git

Navigate to the project directory:

cd your-repo

**Install dependencies:**
pip install selenium 
pip install pywin32

Install Chromedriver from https://googlechromelabs.github.io/chrome-for-testing/

Update the script (line 29) webdriver executable path to your chromedriver.exe path. 
cService = webdriver.ChromeService(executable_path='C:/Users/Boxca/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
Example:
cService = webdriver.ChromeService(executable_path='YOUR FILE PATH GOES HERE')

**Usage**
Run the script, it will open a new Chrome window and load islemaps.com. You can move this window to a 2nd monitor. In-game, hit TAB and copy your coordinates. It should put a pin on the map. If you have nothing on your clipboard initially nothing will happen, so move a few feet and copy coordinates again and it should update.

**Contributing**
Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature-branch).

Open a Pull Request.

**License**
[MIT](https://choosealicense.com/licenses/mit/)
