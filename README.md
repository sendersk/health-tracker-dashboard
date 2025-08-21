# Health Tracker Dashboard

A web application for tracking daily health habits such as **exercise**, **meditation**, and **sleep**.
The app lets you enter data for a chosen day and visualize your progress on interactive dashboards.

Built with **Flask** and **SQLAlchemy**, it provides a simple yet extendable framework for health tracking.

---

## Features
- Add daily health data:
  - Exercise time
  - Meditation time 
  - Sleep duration
- Store and manage records using **SQLAlchemy ORM**
- View dashboards that summarize your progress over time
- Responsive interface built with HTML templates and CSS
- Ready-to-extend for more metrics or advanced visualizations

---

Tech Stack
- **Backend:** Python, Flask
- **Database & ORM:** SQLAlchemy(with SQLite as default engine)
- **Frontend:** Jinja2 templates (HTML, CSS)
- **Forms:** WTForms

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sendersk/health-tracker-dashboard.git
    cd health-tracker-dashboard
    ```
2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    REM macOS/Linux
    source venv/bin/activate
    REM Windows
    venv\Scripts\activate
   
    pip install -r requirements.txt
    ```
3. Initialize the database:
    ```bash
    python seed.py
    ```
4. Run the app:
    ```bash
    python app.py
    ```
5. Open your browser at: http://127.0.0.1:5000

---

## Project Structure
```php
health-tracker-dashboard/
│── app.py              # Main application entry point (Flask app)
│── forms.py            # WTForms definitions
│── seed.py             # Script to initialize database
│── instance/
│   └── health_data.db  # SQLite database (created/managed via SQLAlchemy)
│── templates/
│   ├── base.html       # Base layout
│   ├── index.html      # Homepage
│   ├── form.html       # Form for adding data
│   └── dashboard.html  # Dashboard with visualizations
│── static/
│   └── css/
│       └── style.css   # Main stylesheet
│── .gitignore
```
---

## Future Improvements
- Provide charts and graphs for trends
- Export data to CSV/Excel
- Mobile-friendly layout
- Display data filtered by a specific time range (e.g. week, month, custom range)