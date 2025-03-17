Very basic web scraper I use to pick out securities for my portfolio. 
Basically, it retrieves the 5-year monthly prices of a given security and you can copy it to clipboard and paste to excel.

**SET-UP FOR ABSOLUTE BEGINNERS:**
I'm gonna assume you've never touched a piece of code before and don't have Python on your computer.
1. Open your terminal and paste this: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. Now paste this: brew install python
3. Download **all** the files
4. Create a folder on your desktop, name it stock_scraper
5. Move all of the files to the folder on your desktop
6. On terminal, paste this: cd Desktop/stock_scraper
7. Paste this on terminal: python3 -m venv venv
8. Paste this: pip install -r requirements.txt
9. Finally, paste this: flask --app stock_track run
