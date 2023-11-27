# CS:GO bsp to CS2 addon
just a script to get cs2 addon from compiled csgo bsp

## How to use

- Ensure you have [Python](https://www.python.org/downloads/) installed.
- Install CS2 workshop tools and CSGO sdk on Steam
- Install Hammer++

1. Clone this repository:
   ```
   git clone https://github.com/ipsvn/mapporter.git
   cd mapporter
   ```
2. Download [bspsrc](https://github.com/ata4/bspsrc/releases/latest/download/bspsrc-jar-only.zip) and extract bspsrc.jar to the cloned folder
3. Create venv and activate it (optional):
   ```powershell
   python -m venv venv
   venv\Scripts\activate.ps1
   ```
   > This example is PowerShell
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set environment variables:
   - `JAVA_HOME` Java install (at least Java 19)
   - `CS_INSTALL` Counter-Strike Global Offensive install folder
  
   For example:
     ```
     $Env:JAVA_HOME = 'C:\Program Files\Eclipse Adoptium\jdk-21.0.1.12-hotspot\';
     $Env:CS_INSTALL = 'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\';
     ```
5. Run the thing
   
   ```
   usage: mapporter [-h] [-l] map_path out_addon_name

   positional arguments:
     map_path
     out_addon_name

   options:
     -h, --help            show this help message and exit
     -l, --launch-tools-after-finish
                           whether to run the CS2 Workshop Tools after finishing
   ```
   
   example:
   ```
   python .\port.py .\some_map.bsp some_map_ported
   ```

## Sidenote
the script runs hammer and sends user inputs to it (with pywinauto). this means it will take control of your computer for a second. this is because the bspsrc output causes errors with the source 2 import tool, so you have to open it in hammer and save it. this was the easiest solution lol, I am deeply sorry.