# Installing Python dependencies

It is often useful to create a virtual environment for Python packages, since dealing with packages from different projects can often result in conflicts that are difficult to resolve. Here is how to do it with the built in venv tool in Python.

1. ```python3 -m venv ~/Desktop/RenderIOPythonDeployment```
2. ```source ~/Desktop/RenderIOPythonDeployment/bin/activate``` - this line activates the virtual environment so your Python will use an packages that are installed in it
3. ```which pip``` to verify what is being used (Should point to the one from the virtual environment)
4. ```~/Desktop/RenderIOPythonDeployment/bin/python3 -m pip install --upgrade pip```
5. ```pip install -r requirements.txt```