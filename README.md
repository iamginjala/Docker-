# Docker-


# Task Tracker Web Application with Docker

This repository contains a **Task Tracker Web Application** built using Django and Bootstrap. The application is containerized using Docker to ensure seamless deployment and scalability.

## Features

- Task management system with secure user authentication.
- CRUD operations for managing tasks.
- Responsive user interface using Bootstrap.
- Containerized deployment using Docker.
- Hosted on AWS EC2 with persistent storage using S3.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.11+
- Docker and Docker Compose
- Git

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/iamginjala/Docker.git
   cd Docker
   ```

2. **Set Up the Environment**

   Create a `.env` file in the project directory for environment variables:

   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=*
   DATABASE_URL=sqlite:///db.sqlite3
   ```

3. **Build and Run the Docker Container**

   ```bash
   docker-compose up --build
   ```

4. **Access the Application**

   The application will be available at `http://127.0.0.1:8000`.

---

## Project Structure

```
.
├── tasks/                     # Django app for task management
├── templates/                 # HTML templates
├── static/                    # Static files (CSS, JS)
├── Dockerfile                 # Docker build configuration
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Docker Configuration

### Dockerfile

```dockerfile
# Base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```


## Deployment on AWS EC2

1. **Launch an EC2 Instance**
   - Use an Amazon Linux 2 or Ubuntu instance.
   - Install Docker and Docker Compose on the instance.

2. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

3. **Run Docker**
   ```bash
   docker-compose up --build
   ```

4. **Access the Application**
   Use the public IP of the EC2 instance to access the application.

---

## Contributing

Feel free to open issues or submit pull requests for improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Docker Documentation](https://docs.docker.com/)

