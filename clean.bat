@echo off
echo Cleaning up Python cache files...


del /s /q *.pyc
del /s /q *.pyo


for /d /r %%x in (__pycache__) do rd /s /q %%x

echo Cleanup completed.
pause
