import platform
from pathlib import Path

data_directory = Path(__file__).resolve().parent / "Data"
platform_info = platform.platform()
platform_info = platform_info.lower()
if ("win" in platform_info):
    executable_path = data_directory / "executable-win" / "executable-win" / "lmco.exe"
elif ("linux" in platform_info):
    executable_path = data_directory / "executable-linux" / "lmco"
elif ("macos" in platform_info):
    if ("arm" in platform_info):
        executable_path = data_directory / "executable-mac-arm" / "lmco"
    else:
        executable_path = data_directory / "executable-mac-intel" / "lmco"
data_path = data_directory / "executable-win" / "executable-win" / "data" / "burak-initial-dataset-v4-zbr"
json_path = data_path / "json"
design_path = data_path / "Generative_Design_Data"
