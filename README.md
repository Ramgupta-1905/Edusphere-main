# Edusphere - College Portal Website

## Project Overview
Edusphere is a comprehensive college portal website built with HTML, CSS, and JavaScript. It provides separate interfaces for students and employees (teachers) to manage academic activities, attendance, results, and institutional communications.

## Project Structure

```
Edusphere-main/
├── index.html                                 # Main entry point (homepage)
│
├── assets/
│   ├── css/
│   │   ├── login.css                         # Login page styling
│   │   ├── student_dashboard.css             # Student dashboard styling
│   │   └── employee_dashboard.css            # Employee dashboard styling
│   │
│   ├── images/
│   │   ├── student_icon.png                  # Student portal icon
│   │   ├── employe_icon.png                  # Employee portal icon
│   │   └── background_index.jpg              # Homepage background
│   │
│   └── js/
│       └── script.js                         # Shared JavaScript utilities
│
├── pages/
│   ├── login/
│   │   ├── student_login.html                # Student login page
│   │   └── employee_login.html               # Employee/Teacher login page
│   │
│   ├── dashboards/
│   │   ├── student_dashboard.html            # Student main dashboard
│   │   └── employee_dashboard.html           # Employee/Teacher main dashboard
│   │
│   └── grids/
│       ├── attendance.html                   # Student attendance grid
│       ├── profile.html                      # Student profile grid
│       ├── results.html                      # Student results/grades grid
│       ├── company_visit.html                # Company visits information
│       ├── syllabus.html                     # Syllabus page (placeholder)
│       ├── timetable.html                    # Class timetable (placeholder)
│       ├── assignments.html                  # Assignments page (placeholder)
│       ├── question_papers.html              # Question papers page (placeholder)
│       ├── events.html                       # College events (placeholder)
│       ├── support.html                      # Support center (placeholder)
│       ├── notifications.html                # Notifications page (placeholder)
│       ├── academic_calendar.html            # Academic calendar (placeholder)
│       └── settings.html                     # Settings page (placeholder)
│
├── components/
│   └── sidebar.html                          # Reusable sidebar component
│
├── backend/
│   ├── mainconnection.py                     # MongoDB connection setup
│   └── database/
│       └── logindata.py                      # Login database operations
│
├── README.md                                 # Project documentation (this file)
└── .gitignore                                # Git ignore file
```

## File Connections & Navigation Flow

### Entry Point
- **index.html** → Main page with two options:
  - Student Portal (links to `pages/login/student_login.html`)
  - Employee Portal (links to `pages/login/employee_login.html`)

### Student Portal Flow
```
index.html
    ↓
pages/login/student_login.html (login page with CSS from assets/css/login.css)
    ↓
pages/dashboards/student_dashboard.html (CSS from assets/css/student_dashboard.css)
    ├── pages/grids/attendance.html
    ├── pages/grids/profile.html
    ├── pages/grids/results.html
    └── pages/grids/company_visit.html
```

### Employee Portal Flow
```
index.html
    ↓
pages/login/employee_login.html (login page with CSS from assets/css/login.css)
    ↓
pages/dashboards/employee_dashboard.html (CSS from assets/css/employee_dashboard.css)
```

## CSS File Organization

| File | Purpose | Used In |
|------|---------|---------|
| `assets/css/login.css` | Login form styling | Both student and employee login pages |
| `assets/css/student_dashboard.css` | Student dashboard grid layout | Student dashboard page |
| `assets/css/employee_dashboard.css` | Employee dashboard styling | Employee dashboard page |

## Image Assets

| File | Purpose | Location |
|------|---------|----------|
| `student_icon.png` | Student portal button icon | index.html |
| `employe_icon.png` | Employee portal button icon | index.html |
| `background_index.jpg` | Homepage background | index.html |

## Page Descriptions

### Core Pages

#### index.html
- **Purpose**: Homepage with portal selection
- **Features**: Two buttons to access Student or Employee portals
- **Links**: 
  - Student → `pages/login/student_login.html`
  - Employee → `pages/login/employee_login.html`

#### Student Login (pages/login/student_login.html)
- **Purpose**: Authentication for students
- **Form Fields**: Username, Password
- **Action**: Redirects to `pages/dashboards/student_dashboard.html`
- **Styling**: Uses `assets/css/login.css`

#### Employee Login (pages/login/employee_login.html)
- **Purpose**: Authentication for employees/teachers
- **Form Fields**: Username, Password
- **Action**: Redirects to `pages/dashboards/employee_dashboard.html`
- **Styling**: Uses `assets/css/login.css`

#### Student Dashboard (pages/dashboards/student_dashboard.html)
- **Purpose**: Main student portal with quick access to all features
- **Features**: 
  - Grid layout of dashboard cards
  - Quick navigation menu
  - Links to all student grid pages
- **Styling**: Uses `assets/css/student_dashboard.css`
- **Navigation Links**:
  - Attendance → `pages/grids/attendance.html`
  - Profile → `pages/grids/profile.html`
  - Results → `pages/grids/results.html`
  - Company Visits → `pages/grids/company_visit.html`

#### Employee Dashboard (pages/dashboards/employee_dashboard.html)
- **Purpose**: Main employee/teacher portal
- **Features**: Dashboard cards for teacher-specific functions
- **Styling**: Uses `assets/css/employee_dashboard.css`

### Student Grid Pages (pages/grids/)

#### attendance.html
- **Purpose**: View attendance records with charts
- **Features**:
  - Personal info header
  - Attendance table by date
  - Total attendance summary
  - Chart visualizations
  - Sidebar navigation
- **Sidebar Links**: Back to dashboard, Profile, Attendance, Syllabus, etc.

#### profile.html
- **Purpose**: View detailed student profile
- **Sections**:
  - Profile header with photo
  - Academic information
  - Personal information
- **Sidebar Navigation**: All grid pages and back to dashboard

#### results.html
- **Purpose**: View academic results and grades
- **Tables**:
  - Sessional Test 1 Results
  - Sessional Test 2 Results
  - PUT (Practical/Unit Test) Results
- **Sidebar Navigation**: All grid pages and back to dashboard

#### company_visit.html
- **Purpose**: View company placements and internship visits
- **Features**:
  - Company cards with expandable details
  - Filter by month
  - Search functionality
  - Sidebar navigation

## Backend Integration

### Database Connection (backend/mainconnection.py)
```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['studentportal']
collection = db['studentportal.login']
```

### Login Database (backend/database/logindata.py)
- Handles login credentials
- Manages user authentication data

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: FontAwesome 6.0
- **Charts**: Chart.js
- **Backend**: Python
- **Database**: MongoDB
- **Responsive Design**: CSS Grid & Flexbox

## Features

### For Students
- View attendance records with visual charts
- Access academic results and grades
- Review personal profile information
- Explore company placements and visits
- Responsive sidebar navigation

### For Employees/Teachers
- Dashboard with quick access links
- Teacher-specific management tools
- Assignment and grade management
- Student information access

## Usage Instructions

### Accessing the Portal

1. **Open the application**:
   - Navigate to `index.html` in your browser

2. **Choose Portal Type**:
   - Click on "Student" to access student portal
   - Click on "Employee" to access employee portal

3. **Login**:
   - Enter credentials on the login page
   - Click LOGIN to proceed to dashboard

4. **Navigate**:
   - Use dashboard cards to access specific features
   - Use sidebar menu for quick navigation between pages

## File Linking Best Practices

### From Index Page
```html
<!-- Links to login pages with proper paths -->
<a href="pages/login/student_login.html">Student Portal</a>
<a href="pages/login/employee_login.html">Employee Portal</a>
```

### From Login to Dashboard
```html
<!-- After successful login, redirect to dashboard -->
<button formaction="../dashboards/student_dashboard.html">LOGIN</button>
```

### From Dashboard to Grid Pages
```html
<!-- Quick links from dashboard to specific pages -->
<a href="../grids/attendance.html">Attendance</a>
<a href="../grids/profile.html">Profile</a>
```

### CSS Link from Nested Pages
```html
<!-- CSS files referenced from nested directories -->
<link rel="stylesheet" href="../../assets/css/login.css">
<link rel="stylesheet" href="../../assets/css/student_dashboard.css">
```

## Responsive Design

All pages are designed to be responsive and work across different screen sizes:
- Desktop (1200px and above)
- Tablet (768px - 1199px)
- Mobile (below 768px)

## Future Enhancements

- [ ] Add backend API integration
- [ ] Implement real database connectivity
- [ ] Add real-time notifications
- [ ] Email notifications system
- [ ] Mobile app version
- [ ] Live class scheduling
- [ ] Assignment submission system
- [ ] Discussion forums

## Development Setup

1. Clone the repository
2. Ensure Python and MongoDB are installed for backend operations
3. Update `backend/mainconnection.py` with your MongoDB credentials
4. Open `index.html` in a web browser

## Project Author
Ram Gupta

## GitHub Repository
https://github.com/Ramgupta-1905/Edusphere

## License
[Specify your license here]

## Support
For questions or issues, please contact: ram.gupta@university.edu
