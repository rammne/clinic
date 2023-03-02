@ECHO OFF
call venv\Scripts\activate.bat
start cmd.exe /C "C: && cd C:\Users\TCC\Documents\Dont Delete\clinic 2\clinic && python manage.py runserver"
start http://127.0.0.1:8000/