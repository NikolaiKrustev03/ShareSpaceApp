# ShareSpace

**ShareSpace** is a platform where users can share content like articles, images, and ideas on personalized boards. This README will guide you through setting up and running the project on your local machine.

---

## Setup Instructions

Follow these steps to set up and run the project on your local machine.

---

### Step 1: Clone the Repository
   Run the following command to clone the repository:

   ```bash
   git clone https://github.com/NikolaiKrustev03/ShareSpace.git
   cd ShareSpace
   ```

### Step 2: Set up virtual enviroment
Run the following commands:
Windows:
  ```bash
      -m venv venv
      venv\Scripts\activate
```
Linux:
  ```bash
      python3 -m venv venv
      source venv/bin/activate
```

### Step 3: Install dependencies
Run the following command
```bash
pip install -r requirements.txt
```

### Step 4: Create .env file
Before this, you need to generate a secret key for Django. You can use the following command in the terminal:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
In the root directory of your project (where manage.py is), create a .env file.
Inside the .env file, add environment variables for the SECRET_KEY and database configuration:
```bash
SECRET_KEY=your-generated-secret-key
DATABASE_NAME=your-database-name
DATABASE_USER=your-database-user
DATABASE_PASSWORD=your-database-password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```
### Step 5: Run migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```
Or from the menu on the top, select run manage.py task and run this command:
```bash
makemigrations
migrate
```
### Step 6: Run the server
You can either run it from the terminal:
```bash
python manage.py runserver
```
Or from the menu on the top, select run manage.py task and run this command:
```bash
runserver
```


