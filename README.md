
# Late Show Flask API

## Overview
This repository contains the backend API for the "Late Show" application, built using Flask. The API provides endpoints to manage shows, bookings, and users. It integrates SQLAlchemy for database management and is set up with a virtual environment for dependency management.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- RESTful API for managing shows and bookings.
- CRUD operations for database entities (e.g., Shows, Users, Bookings).
- Input validation and error handling.
- Modular Flask application structure.

## Technologies Used
- **Framework:** Flask
- **Database Management:** SQLAlchemy (SQLite3)
- **Environment Management:** Python venv
- **API Testing:** Flask-Testing

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Moringa-SDF-PTO7/lateshow-irene-musau.git
   cd lateshow-irene-musau
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Run the Flask application:
   ```bash
   flask run
   ```

## Usage
- Access the API at `http://127.0.0.1:5000/`.
- Use tools like Postman or cURL to interact with the endpoints.


## Testing
Run tests to ensure the API is working as expected:
```bash
pytest
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes and push to your branch:
   ```bash
   git push origin feature-name
   ```
4. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
