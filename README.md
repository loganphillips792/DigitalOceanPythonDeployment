# Installing Python dependencies

It is often useful to create a virtual environment for Python packages, since dealing with packages from different projects can often result in conflicts that are difficult to resolve. Here is how to do it with the built in venv tool in Python.

1. ```python3 -m venv ~/Desktop/DigitalOceanPythonDeploymentVenv```
2. ```source ~/Desktop/DigitalOceanPythonDeploymentVenv/bin/activate``` - this line activates the virtual environment so your Python will use an packages that are installed in it
3. ```which pip``` to verify what is being used (Should point to the one from the virtual environment)
4. ```~/Desktop/DigitalOceanPythonDeploymentVenv/bin/python3 -m pip install --upgrade pip```
5. ```pip install -r requirements.txt```


# To Run Application

## Environment file

```docker-compose build```
```docker-compose up```
Access page at http://127.0.0.1:8000/

```
docker exec -it  digitaloceanpythondeployment_db_1 bash
psql -U logan -d example
``` 

OR 

```docker exec -it digitaloceanpythondeployment_db_1 psql -U logan -d example```