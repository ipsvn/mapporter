from pathlib import Path
import os

cs_install = Path(os.environ["CS_INSTALL"])
csgo_gamedir = cs_install / "csgo"
cs2_gamedir = cs_install / "game" / "csgo"
hammer_bin = cs_install / "bin" / "hammerplusplus.exe"
import_script_dir = cs_install / "game" / "csgo" / "import_scripts"
import_script_bin = import_script_dir / "import_map_community.exe"

java_home = Path(os.environ["JAVA_HOME"])
java_bin = java_home / "bin" / "java.exe"
