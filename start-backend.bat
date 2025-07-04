@echo off
echo Iniciando o servidor Django...
echo.
echo Usuario: admin
echo Senha: admin123456
echo.
echo Acesse: http://localhost:8000/admin
echo API: http://localhost:8000/api/
echo.
python manage.py runserver
pause 