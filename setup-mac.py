from cx_Freeze import setup, Executable

setup(
    name="Activity Monitor",
    version="1.0",
    description="A Python Activity Monitor",
    executables=[Executable("activity-monitor.py")],
)