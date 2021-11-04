HOW TO USE THIS APP : 

Description: This is a backend application runnig in FastApi meant to store test files locally.

Use:
    In order to run this app FastApi and Uvicorn need to be installed or be included in the virtual environment.
    If such libraries are no installed use the requirements.txt file provided.

    In order to execute this app cd into the NotesApp folder.
    Activate the virtual enviroment. 
    cd into /app
    Run in the console :

        uvicorn main:app --reload
        
    Then look in your console and click on

        Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

    Once in the browser you can introduce the rquests manually or use the testing tool provided by FastApi by
    using the url :

       http://127.0.0.1:8000/docs
