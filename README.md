# theme-switcher

Scheduled task to toggle between light and dark themes on windows.

## Installation

1. Clone this repo into `C:\Scripts\`

```ps
$ git clone https://github.com/Reptarsrage/theme-switcher.git C:\Scripts\theme-switcher
```

2. Install the dependencies by running:

```ps
$ cd C:\Scripts\theme-switcher
$ python -m venv venv
$ .\venv\Scripts\activate
$ pip install -r requirements.txt
```

3. Open Task Scheduler and import `C:\Scripts\theme-switcher\Switch Theme.xml`.

4. On the "General" tab, click "Change User or Group..." button, type in your username.
   Ensure it's correct by clicking "Check Names" before clicking "OK".

5. On the "Triggers" tab, highlight the trigger and click "Edit" then click "Change User..." and type in your username.
   Ensure it's correct by clicking "Check Names" before clicking "OK".
