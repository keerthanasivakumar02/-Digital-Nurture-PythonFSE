# Hands-On 10 – Microservices Architecture

## Overview

This project demonstrates a simple Microservices Architecture by splitting a Course Management System into independent services.

---

# Service Decomposition

| Service Name | Responsibility | Endpoints | Database |
|--------------|----------------|-----------|----------|
| Course Service | Manage courses | /api/courses | SQLite (course_service/database.db) |
| Student Service | Manage students and enrollment | /api/students | SQLite (student_service/database.db) |
| Auth Service | User registration, login and token validation (Concept) | /api/auth | Separate Auth Database |
| Notification Service | Email notifications (Concept) | /api/notifications | Separate Notification Database |

---

# Microservices Implemented

## Course Service (Port 5001)

Responsibilities:

- Create Course
- Get All Courses
- Get Course by ID

Database:

- course_service/database.db

---

## Student Service (Port 5002)

Responsibilities:

- Create Student
- Get All Students
- Get Student by ID
- Enroll Student

Database:

- student_service/database.db

During enrollment, the Student Service sends an HTTP request to the Course Service to verify that the course exists.

---

## API Gateway (Port 5000)

Responsibilities:

- Acts as the single entry point for clients.
- Routes Course requests to Course Service.
- Routes Student requests to Student Service.

Example Routing:

- `/api/courses/*` → Course Service
- `/api/students/*` → Student Service

---

# Inter-Service Communication

This project uses **Synchronous HTTP Communication**.

Student Service communicates with Course Service using the Python `requests` library.

Example Flow:

Client

↓

API Gateway

↓

Student Service

↓

Course Service

---

# Handling Service Failure

If Course Service is unavailable, Student Service catches the connection error and returns:

- HTTP Status: **503 Service Unavailable**

This prevents the application from crashing.

---

# Synchronous vs Asynchronous Communication

## Synchronous (HTTP)

Advantages

- Easy to implement
- Immediate response
- Simple debugging

Disadvantages

- Services depend on each other
- If one service is unavailable, the request fails
- Tight coupling

---

## Asynchronous (RabbitMQ / Kafka)

Advantages

- Loose coupling
- Better scalability
- Reliable event processing
- Services work independently

Disadvantages

- More complex
- Eventual consistency
- Requires additional infrastructure

---

# When to Use RabbitMQ or Kafka

Message queues such as RabbitMQ or Kafka are useful when:

- Sending email notifications
- Processing payments
- Order processing
- Logging
- Background jobs
- High-volume event processing

They allow services to communicate without waiting for an immediate response.

---

# API Gateway Pattern

The API Gateway provides:

- Single entry point for clients
- Request routing
- Authentication (production systems)
- Rate limiting (production systems)
- SSL termination (production systems)

In this project, the API Gateway forwards requests to the appropriate microservice using the Python `requests` library.

---

# Conclusion

This project demonstrates:

- Monolithic application decomposition
- Independent microservices
- Separate databases
- HTTP-based inter-service communication
- API Gateway implementation
- Basic microservices architecture using Flask