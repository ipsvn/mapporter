from pywinauto import Desktop, Application, timings
from pathlib import Path
import subprocess
import os
from paths import java_bin, hammer_bin, cs_install, csgo_gamedir, cs2_gamedir, import_script_dir, import_script_bin

def decompile_bsp(bsp_path, vmf_path):
    subprocess.Popen(
    [
        java_bin,
        "-cp",
        "bspsrc.jar",
        "info.ata4.bspsrc.app.src.cli.BspSourceCli",
        "-o",
        str(vmf_path),
        "--unpack_embedded",
        str(bsp_path)
    ]
).communicate()

def resave_hammer(vmf_path):
    app = Application(backend="win32").start(
        f'"{str(hammer_bin)}" {str(vmf_path)}',
        wait_for_idle=False
    )

    main_window = app.window(title_re=f'.*{vmf_path.name}.*')
    main_window.wait("ready")
    print("hammer is ready")

    main_window.menu_select("File->Save")
    main_window.menu_select("File->Exit")

def run_import_tool(content_dir, s2addon, map_name):
    args = [
        import_script_bin,
        str(csgo_gamedir),
        str(content_dir),
        str(cs2_gamedir),
        s2addon,
        map_name,
        "-usebsp"
    ]
    print(f"Running import tool with args {args}")
    environ = os.environ
    subprocess.Popen(
        args,
        cwd=import_script_dir,
        env={
            **environ,
            "PATH": environ["PATH"] + ";" + str(cs_install / "game" / "bin" / "win64")
        }
    ).communicate()

def launch_tools(addon_name):
    subprocess.Popen(
        [
            cs_install / "game" / "bin" / "win64" / "csgocfg.exe",
            "-addon",
            addon_name,
            "-retail",
            "-gpuraytracing",
            "-vulkan"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )