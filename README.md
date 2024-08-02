**SETUP** 
- Install Python ( preferably 3) & UBUNTU ( preferably )
- python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org fastapi "uvicorn[standard]" python-jose "python-jose[cryptography]" "passlib[bcrypt]" jinja2 fastapi_utils psutil python-multipart pandas xlrd requests openpyxl typing pymysql
- Download and Install https://slproweb.com/download/Win64OpenSSL_Light-3_3_1.exe and add that BIN path to Environment Variables.
- From FASTAPI folder, need to create Private Key using below command
  - openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
- Install MySQL on Windows using : https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-web-community-8.0.39.0.msi 
- Install HeidiSQL on Windows using : https://www.heidisql.com/downloads/releases/HeidiSQL_12.8_64_Portable.zip

**How to execute on Windows**
- From current directory run the command to run the server on 8080 port by default
  - python -m uvicorn main:app --reload --host %COMPUTERNAME% --port 8000
  - python -m uvicorn main:app --reload --host %COMPUTERNAME% --port 8000 --ssl-keyfile ./ssl_keys/key.pem --ssl-certfile ./ssl_keys/cert.pem
- For Production
  - python -m uvicorn main:app --host %COMPUTERNAME% --port 8000 --workers 10