# driVE Platform

I added some instructions below that might be helpful if you run into trouble/are new to Git (they're AI-generated, so they may not be perfect).



## Getting Started - Step by Step Guide

Follow these instructions to get the app running on your computer.

### Step 1: Install Required Software

You'll need to install these programs first:

1. **Python 3.12 or newer**
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Download and install Python
   - During installation, CHECK the box that says "Add Python to PATH"

2. **uv (Python package manager)**
   - Open Terminal (Mac) or Command Prompt (Windows)
   - Type this command and press Enter:
     ```bash
     pip install uv
     ```

3. **Git (for downloading the project)**
   - Go to [git-scm.com/downloads](https://git-scm.com/downloads)
   - Download and install Git
   - Use default settings during installation

### Step 2: Download the Project

1. **Open Terminal/Command Prompt**
   - Mac: Press `Cmd + Space`, type "Terminal", press Enter
   - Windows: Press `Windows key`, type "cmd", press Enter

2. **Navigate to where you want the project**
   ```bash
   cd Desktop
   ```

3. **Download (clone) the project**
   ```bash
   git clone https://github.com/helloimfrei/drive-app.git
   ```

4. **Go into the project folder**
   ```bash
   cd drive-app
   ```

### Step 3: Set Up the Database Connection

1. **Create your environment file**
   - In the `drive_app` folder, you'll see a file called `.env_example`
   - Make a copy of this file and name it `.env` (no "example" part)

   Mac/Linux:
   ```bash
   cp drive_app/.env_example drive_app/.env
   ```

   Windows:
   ```bash
   copy drive_app\.env_example drive_app\.env
   ```

2. **Edit the .env file**
   - Replace the placeholder values with your actual database information:
   ```
   DATABASE_URL=mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost:3306/YOUR_DATABASE_NAME
   ```

   For example, if:
   - Username: `root`
   - Password: `mypassword123`
   - Database name: `drive_db`

   Your line would look like:
   ```
   DATABASE_URL=mysql+pymysql://root:mypassword123@localhost:3306/drive_db
   ```

   - Save the file

### Step 4: Install Project Dependencies

1. **Make sure you're in the project folder**
   ```bash
   pwd
   ```
   (This shows your current location - it should end with "drive-app")

2. **Install all required packages using uv**
   ```bash
   uv sync
   ```

   This will:
   - Create a virtual environment (isolated Python space for this project)
   - Install Flask, SQLAlchemy, and all other dependencies
   - This might take a minute or two

### Step 5: Run the Application

1. **Start the Flask app**
   ```bash
   uv run python drive_app/app.py
   ```

2. **Open your web browser**
   - Go to: `http://localhost:5000`
   - You should see the driVE homepage!

3. **View the listings page**
   - Go to: `http://localhost:5000/listing`
   - You'll see all listings from your database in a table

### Step 6: Stop the Application

When you're done working:
- In Terminal/Command Prompt, press `Ctrl + C`
- This stops the Flask server

---

## Troubleshooting

### "Command not found" or "not recognized"
- Make sure Python and Git are installed properly
- Restart your Terminal/Command Prompt after installing

### "Access denied" or database connection errors
- Check your `.env` file has the correct username, password, and database name
- Make sure your MySQL/MariaDB server is running

### Port already in use
- Another program is using port 5000
- Stop other Flask apps, or change the port in `app.py`

### Package installation fails
- Try running: `uv sync --reinstall`
- Make sure you have internet connection

---

## Project Structure

```
drive-app/
├── drive_app/
│   ├── app.py              # Main Flask application
│   ├── .env                # Database credentials (YOU create this)
│   ├── .env_example        # Template for .env file
│   ├── static/             # CSS, images, JavaScript files
│   │   ├── logo.png
│   │   └── style.css
│   └── templates/          # HTML files
│       ├── base.html       # Base template with navbar
│       ├── index.html      # Homepage
│       └── listing.html    # Listings table page
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependency versions
└── README.md               # This file!
```

---

## Daily Workflow

Once you have everything set up, here's what to do each time you work on the project:

1. **Open Terminal/Command Prompt**

2. **Go to the project folder**
   ```bash
   cd path/to/drive-app
   ```

3. **Make sure you have the latest code** (if working with a team)
   ```bash
   git pull
   ```

4. **Run the app**
   ```bash
   uv run python drive_app/app.py
   ```

5. **Do your work** - Edit files, test changes in browser

6. **Stop the app** when done - Press `Ctrl + C`

---

## Need Help?

- Check the Troubleshooting section above
- Ask your teammates
- Check Flask documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com/)

---

## For More Advanced Users

### Updating Dependencies
```bash
uv sync
```

### Running with custom host/port
```bash
uv run python drive_app/app.py --host=0.0.0.0 --port=8000
```

### Activating the virtual environment manually
```bash
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```
