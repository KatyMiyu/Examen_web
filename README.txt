Pasos para ver nuestra pagina web:

git clone https://github.com/KatyMiyu/Examen_web.git

--Crear el ambiente virtual
python -m venv myvenv 
py -m venv myvenv 
--Activar el ambiente virtual
cd .\myvenv\Scripts\
.\activate
--Luego debes ingresar a la carpeta de Examen_web
cd .\Examen_web\
--Realizar la instalacion de requirements.txt
pip install -r .\requirements.txt
--Iniciar el servidor 
python manage.py runserver
-- Acceder al la pagina
http://127.0.0.1:8000/index