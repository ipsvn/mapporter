import argparse
from pathlib import Path
import subprocess
import sys
import os
import shutil
from steps import decompile_bsp, resave_hammer, run_import_tool, launch_tools
from paths import cs_install, csgo_gamedir

arg_parser = argparse.ArgumentParser(
    prog="mapporter"   
)
arg_parser.add_argument("map_path")
arg_parser.add_argument("out_addon_name")
only_arg_group = arg_parser.add_mutually_exclusive_group()
only_arg_group.add_argument("-d", "--only_decompile", action="store_true", help="only decompile the bsp file (in case you want to make modifications before importing)")
only_arg_group.add_argument("-i", "--only_import", action="store_true", help="only import the map to CS2 (in case you already ran with --only_extract)")
arg_parser.add_argument("-l", "--launch-tools-after-finish", action="store_true", help="whether to run the CS2 Workshop Tools after finishing")
args = arg_parser.parse_args()
print(args)

map_path = Path(args.map_path)
out_addon_name = args.out_addon_name
launch_tools_after_finish = args.launch_tools_after_finish

do_decompile = True
do_import = True
if args.only_decompile:
    do_import = False
if args.only_import:
    do_decompile = False

print(do_decompile)
print(do_import)

map_name = map_path.stem

temp_out_folder = (Path("temp") / map_name).resolve()
temp_out_folder.mkdir(parents=True, exist_ok=True)
vmf_path = temp_out_folder / (map_name + ".vmf")

print(f"running with map {map_path}, temp folder {temp_out_folder} and addon name {out_addon_name}")

assets_path = temp_out_folder / map_name
maps_folder = assets_path / "maps"

pre_folders = []
if do_decompile:
    decompile_bsp(map_path, vmf_path)
    
    if not args.only_decompile:
        resave_hammer(vmf_path)
    
    vmf_path = vmf_path.replace(maps_folder / vmf_path.name)

    for asset_path in assets_path.iterdir():
        if not asset_path.is_dir() or asset_path.name == "maps":
            continue
        csgo_gamedir_subdir = csgo_gamedir / asset_path.name
        csgo_gamedir_subdir_backup = csgo_gamedir / (asset_path.name + ".pre-mapporter")
        if not csgo_gamedir_subdir_backup.exists():
            pre_folders.append({
                "path": csgo_gamedir_subdir_backup,
                "original_name": asset_path.name
            })
            shutil.copytree(csgo_gamedir_subdir, csgo_gamedir_subdir_backup, dirs_exist_ok=True)

        shutil.copytree(asset_path, csgo_gamedir_subdir, dirs_exist_ok=True)
        print(asset_path)

if do_import:
    addons_folder = cs_install / "content" / "csgo_addons"
    addon_template_folder = addons_folder / "addon_template"

    new_addon_folder = addons_folder / out_addon_name
    shutil.copytree(addon_template_folder, new_addon_folder, dirs_exist_ok=True)

    run_import_tool(assets_path, out_addon_name, map_name)

    if launch_tools_after_finish:
        launch_tools(out_addon_name)