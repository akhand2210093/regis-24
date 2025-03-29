# Regis-24

## Overview
Regis-24 is a Django-based backend for a student registration system. It allows students to register securely using Google reCAPTCHA verification and receive confirmation emails upon successful registration. Additionally, administrators can view the list of registered students.

## Features
- **Student Registration**: Users can register with their name and email.
- **Google reCAPTCHA Verification**: Prevents bot registrations.
- **Email Confirmation**: Sends a confirmation email upon successful registration.
- **Student List Retrieval**: Provides a list of all registered students.
- **Secure API Endpoints**: Ensures data integrity and security.

## Live Deployment
The project is deployed and can be accessed at:  
🔗 **[Regis-24 Registration System](https://regis-24.onrender.com)**

## API Endpoints

### Student Registration
- **Register Student**: `POST /students/register/`
  - Required fields: `name`, `email_id`, `recaptcha`
  - Sends a confirmation email upon successful registration.

### Student List
- **View Registered Students**: `GET /students/`

## License
This project is licensed under the MIT License.

## Contributors
- Your Name (@yourgithub)

## Acknowledgements
Special thanks to all contributors who helped build this project.

