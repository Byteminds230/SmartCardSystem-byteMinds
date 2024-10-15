### The system admin's

1. **the Super-admin**:

 - **Responsibilities**:
        Overall management of the system.
        User management (adding, removing, and editing admin roles).
        Access to all pages and settings.
        Analytics and reporting functionalities.
- **Access**:
All system features and settings.


2. ** School-admin**:
- **Responsibilities**:
        Management of student records and attendance.
        Coordination of academic activities and schedules.
        Access to reporting features related to student performance.
- **Access**:
Pages related to student management, attendance tracking, and academic reporting.


3. **Discipline-admin**:
- **Responsibilities**:
        Handling discipline-related matters, such as behavior logs and incident reports.
        Implementing and monitoring discipline policies.
- **Access**:
Pages related to discipline management, including incident reporting and behavior tracking.

```javascript
// Pseudo code for rendering the dashboard based on role
function renderDashboard(userRole) {
    return (
        <div>
            <Header />
            <NavigationMenu role={userRole} />
            <MainContent>
                {userRole === "Super Admin" && <SuperAdminPage />}
                {userRole === "School Admin" && <SchoolAdminPage />}
                {userRole === "Discipline Admin" && <DisciplineAdminPage />}
                {/* Common pages accessible to all */}
                <CommonPage />
            </MainContent>
            <Footer />
        </div>
    );
}

// Example of dynamic navigation based on user role
function NavigationMenu({ role }) {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                {role === "Super Admin" && <li><Link to="/user-management">User Management</Link></li>}
                {role === "School Admin" && <li><Link to="/attendance">Attendance</Link></li>}
                {role === "Discipline Admin" && <li><Link to="/discipline">Discipline</Link></li>}
            </ul>
        </nav>
    );
}
```