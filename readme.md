# if you are starting this project for the first time 
.\.venv\Scripts\activate
pip install -r requirements.txt
# whenever someone adds a new package please update the reqirements.txt
pip freeze > requirements.txt

fastapi dev main.py
# for production use
 fastapi run  
 # API docs
 http://127.0.0.1:8000/docs      

