# Python Scripts
**Repository containing Python scripts made for simplifying common tasks.** :sunglasses:

## Scripts:
1. [Duplicate](https://github.com/Pro-Panda/Python-Scripts/tree/master/Duplicate): List (and remove) all duplicate files from your PC
2. [Excel-Attd](https://github.com/Pro-Panda/Python-Scripts/tree/master/Excel-Attd): Mark attendance in an Excel sheet based on BITS ID
3. [Alarm-Clock](https://github.com/Pro-Panda/Python-Scripts/tree/master/alarm-clock): Schedule weekly and daily alarms.
4. [Site-Blocker](https://github.com/Pro-Panda/Python-Scripts/tree/master/site-blocker): Block and unblock websites on your PC
   
## How to use:
 - Duplicate

   ```bash
   python filecmp.py /path/to/folder
   ```
 - Excel-Attd

    ```bash
    python update.py /path/to/attendance_list /path/to/excel_sheet <Attd Column No.>
    ```
 - Alarm-Clock

   - CLI Version
     ```bash
     python alarm-clock-cli.py option h m s
     ```
        | Option | Task                               | Example                           |
        |--------|------------------------------------|-----------------------------------|
        | 0      | Ring Immediately                   | python alarm-clock-cli.py 0       |
        | 1      | Create a new scheduled alarm       | python alarm-clock-cli.py 1 10 10 |                   
        | 2      | Delete an existing scheduled alarm | python alarm-clock-cli.py 2       |
    
   - GUI Version
     ```bash
     python alarm-clock-gui.py
     ``` 

## Improvements:
*Feel free to open an issue or send a feature pull request*

 - [Alarm-Clock](https://github.com/siddhantkhandelwal/Python-Scripts/tree/master/alarm-clock):
   - CLI Version
    - Add an option to snooze the alarm.
    - Create logs specific to the script. Will help in keeping track of alarms independent of the cron-tab.
   - GUI Version
    - Add options to add alarms, create different frames for different tasks.
    - Improve the look of the app.

