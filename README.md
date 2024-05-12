

## Installation Guide

### Step 1: Install Python
1. Download Python from [python.org/downloads](https://www.python.org/downloads/).
2. **Important:** During the installation, ensure to select the option **"Add Python.exe to Path"**.

### Step 2: Install MySQL
1. Download MySQL from [MySQL Downloads](https://dev.mysql.com/downloads/installer/) or directly via [this link](https://dev.mysql.com/downloads/file/?id=528489).
2. Install MySQL by selecting **"Server Only"** during the setup.
3. Proceed with the installation by clicking **"Next"** until you are prompted to set a password. Remember this password as it will be required later.

### Step 3: Configure MySQL
1. Search for **"MySQL Command Line Client"** on your computer and open it.
2. Log in using the password set during installation.
3. Once logged in, create a new database by running: `CREATE DATABASE ems;`.
4. Switch to the new database with: `USE ems;`.

### Step 4: Clone and Set Up the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/iemtejas/Club-Smith.git
   ```
2. Install `virtualenv` and set up the project environment:
   ```bash
   pip install virtualenv
   cd Club-Smith
   virtualenv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Step 5: Configure Django
1. Navigate to the `event` folder within the cloned repository, open `settings.py`, and locate the `DATABASES` configuration.
2. Update the password under the `DATABASES` dictionary with the one created during MySQL setup:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'ems',
           'USER': 'root',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': 3306
       }
   }
   ```
3. Save and close the file.

### Step 6: Load Sample Data
1. Navigate to the `Database with Sample Data` folder in the cloned repository, and copy the path of `ems.sql`.
2. Convert all backslashes in the file path to forward slashes and remove any surrounding quotes.
3. Return to MySQL Command Line, ensure `ems` is in use (`USE ems;`), and import the database schema:
   ```sql
   SOURCE /path/to/ems.sql;
   ```

### Step 7: Final Steps
1. Return to the command prompt, activate the virtual environment, and finalize the Django setup:
   ```bash
   cd Club-Smith
   .\venv\Scripts\activate
   python manage.py migrate
   python manage.py runserver
   ```
2. To access the Django admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

### Running the Application
To run the project, navigate to the project directory, activate the virtual environment, and start the server:
```bash
cd Club-Smith
.\venv\Scripts\activate
python manage.py runserver
```

---

