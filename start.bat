@ECHO OFF
call venv\Scripts\activate.bat
start cmd.exe /C "D: && cd D:\OLOPSC_CLINIC\olopsc_clinic && python manage.py runserver"
start http://localhost:8000/