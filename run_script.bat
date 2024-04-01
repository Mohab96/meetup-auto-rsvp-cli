@echo off
:loop
python path\to\your\script.py
ping localhost -n 1800 > nul
goto loop