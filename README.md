# Full-Stack Todo Application with Authentication

A comprehensive full-stack Todo application featuring Next.js frontend, FastAPI backend, and secure authentication with Better Auth. This application provides complete task management functionality with user authentication and data persistence.

## Features

### Frontend (Next.js 16+)
- Modern React application with App Router
- Responsive design with Tailwind CSS
- User authentication (login/register)
- Protected routes and dashboards
- Task management (CRUD operations)
- Real-time task updates
- Loading states and error handling

### Backend (FastAPI)
- RESTful API endpoints
- JWT-based authentication
- User session management
- Secure data validation
- Database integration with Neon PostgreSQL
- Rate limiting for security

### Authentication (Better Auth)
- Secure user registration and login
- JWT token generation and validation
- Session management
- Password hashing and security
- User data isolation

### Database (Neon PostgreSQL)
- SQLModel ORM integration
- Automatic schema migrations
- Secure data storage
- Connection pooling

## Tech Stack

- **Frontend**: Next.js 16+, React, TypeScript, Tailwind CSS
- **Backend**: Python, FastAPI, uvicorn
- **Authentication**: Better Auth with JWT
- **Database**: Neon Serverless PostgreSQL with SQLModel ORM
- **Deployment**: Ready for Vercel/Netlify (frontend), Railway/Render (backend)

## Prerequisites

- Node.js 18+ (for frontend)
- Python 3.9+ (for backend)
- PostgreSQL-compatible database (Neon recommended)
- Git

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Backend Setup

```bash
# Navigate to the backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration
```

### 3. Frontend Setup

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
# Edit .env.local with your configuration
```

## Environment Variables

### Backend (.env)
```env
DATABASE_URL=postgresql://user:password@localhost:5432/todo_app
BETTER_AUTH_SECRET=your-super-secret-jwt-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_DELTA=604800  # 7 days in seconds
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
```

## Running the Application

### 1. Start the Backend

```bash
# From the backend directory
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn src.main:app --reload --port 8000
```

### 2. Start the Frontend

```bash
# From the frontend directory
cd frontend
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Backend Docs: http://localhost:8000/docs

## API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout

### Tasks
- `GET /api/{user_id}/tasks` - Get user's tasks
- `POST /api/{user_id}/tasks` - Create a new task
- `PUT /api/{user_id}/tasks/{task_id}` - Update a task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{task_id}/complete` - Mark task as complete

## Database Migrations

Run database migrations using Alembic:

```bash
# From the project root
cd backend
alembic upgrade head
```

## Testing

### Backend Tests
```bash
cd backend
python -m pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Deployment

### Frontend Deployment
The Next.js frontend is ready for deployment to Vercel, Netlify, or any Node.js hosting service.

### Backend Deployment
The FastAPI backend can be deployed to Railway, Render, Heroku, or any cloud provider supporting Python applications.

## Security Features

- JWT token-based authentication
- Password hashing with bcrypt
- Rate limiting for auth endpoints
- Input validation and sanitization
- User data isolation
- CORS configuration

## Architecture

The application follows a modern full-stack architecture:

- **Frontend**: Next.js with React components and state management
- **Backend**: FastAPI with dependency injection and middleware
- **Authentication**: Better Auth with JWT tokens
- **Database**: SQLModel ORM with PostgreSQL
- **Security**: Multiple layers of validation and protection

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

[Specify your license here]

## Support

For support, please open an issue in the GitHub repository.