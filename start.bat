@ECHO OFF
call venv\Scripts\activate.bat
start cmd.exe /C "D: && cd D:\OLOPSC_CLINIC\olopsc_clinic && python manage.py runserver"
start http://127.0.0.1:8000/