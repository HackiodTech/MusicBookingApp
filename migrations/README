# Music Booking App API

## Project Overview
The **Music Booking App API** is a RESTful API built with Flask and PostgreSQL that allows users and artists to interact with a music event booking platform. The API enables users to register, log in, create and manage events, book artists, and view available events.

### Key Features:
- User and artist registration & authentication (JWT-based)
- Event creation & management
- Artist booking system
- Secure and scalable database design using SQLAlchemy
- Protected API routes using Flask-JWT-Extended
- Postman collection for easy testing

---
## Technologies Used
- **Backend:** Flask, Flask-RESTful, Flask-JWT-Extended
- **Database:** PostgreSQL, SQLAlchemy
- **Authentication:** JWT (JSON Web Token)
- **Migrations:** Flask-Migrate
- **Other Tools:** Postman (for testing), Git & GitHub (version control)

---
## Installation Instructions
Follow these steps to set up and run the project locally:

```bash
# Clone the repository
git clone <repo-url>
cd <project-directory>

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up the database
flask db upgrade

# Run the application
flask run
```

The API will now be accessible at `http://127.0.0.1:5000/`

---
## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user or artist
- `POST /api/auth/login` - Authenticate a user and return JWT

### User Profile
- `GET /api/profile` - View user profile
- `PUT /api/profile` - Edit user profile

### Events
- `POST /api/events/create` - Create a new event (users & artists can create)
- `GET /api/events` - View all available events
- `GET /api/events/<event_id>` - View a specific event

### Booking
- `POST /api/bookings` - Book an artist for an event

### Example Request & Response
#### Register a User
**Request:**
```json
{
  "email": "user@example.com",
  "password": "securepassword",
  "username": "user123",
  "role": "user"
}
```
**Response:**
```json
{
  "data": {
    "message": "User Successfully registered"
  }
}
```

#### Login
**Request:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "token": "<JWT_TOKEN>",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "role": "user"
  }
}
```

---
## Testing Your Endpoints

1. Open **Postman**
2. Import the provided Postman collection (`postman_collection.json`)
3. Ensure the API is running locally (`flask run`)
4. Test endpoints by sending requests with valid data

---
## Future Implementations & Considerations

### 1. Email Notifications
- Send email confirmations when users book an artist.
- Notify artists when they are booked for an event.

### 2. Payment Integration
- Implement payment gateways like Paystack, Stripe, or Flutterwave.
- Allow users to pay for event bookings securely.

### 3. Third-Party Integrations
- Add Google & Facebook authentication for easier sign-up.
- Integrate with external calendar services for scheduling.

### 4. Role-Based Access Control (RBAC)
- Implement different permission levels for users, artists, and admins.

---
## Contribution
Feel free to contribute by submitting issues or creating pull requests.

---
## License
This project is licensed under the MIT License.
