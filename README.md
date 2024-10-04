# Graphic Design Blog
## Table of Contents
Project Overview
- Purpose: A Graphic Design Blog where users can share, manage, and explore creative content.
- Main Features: User registration, login, profile management, and CRUD operations for blog posts.
- Target Audience: Graphic designers, artists, and design enthusiasts.

Features
- User Registration & Login: Users can sign up, log in, and manage their accounts.
- Favourites & Likes: Users can like and save blog posts.
- Profile Management: Update profile info and view saved content.
- CRUD for Blog Posts: Users can create, edit, delete, and manage their posts.

User Stories
![User Stories](https://github.com/user-attachments/assets/12ba0869-863f-4436-bfd3-7e17ae6a8a79)

Technologies Used
- Backend: Django, Python
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Database: PostgreSQL
- Media Storage: Cloudinary
- Libraries: Crispy Forms, Summernote, Django-Allauth

Installation & Setup
- Install dependencies: pip install -r requirements.txt
- Set up .env file with credentials.
- Apply migrations: python manage.py migrate
- Create a superuser: python manage.py createsuperuser
- Run the server: python manage.py runserver

Usage
- Navigate through the site, register or log in, and manage blog posts from the dashboard. Users can create, edit, delete, and view posts and save favorites posts.

Database Schema

Design
- Wireframes: ![Desktop wireframe](https://github.com/user-attachments/assets/c6b63baa-ec13-4c96-bb71-8e94ff680e05)![Tablet Wireframe](https://github.com/user-attachments/assets/2538c111-d881-47d1-a35c-61925651bfa8)![Mobile Wireframe](https://github.com/user-attachments/assets/ebce2c3b-1731-4f6f-a83e-e660515817b0)
- Responsive layout using Bootstrap for mobile and desktop.

- User Flow
- UI/UX Design

Testing
- Automated Testing: Django unit tests for models and views.
- Manual Testing: Includes registration, login, CRUD, and UI responsiveness.

Deployment
- Deployed using Heroku for backend and Cloudinary for static/media files.
- Set up environment variables, and ensure DEBUG=False in production.

Future Enhancements
- Image uploads to posts.
- Post comments and like feature.
- Enhanced profile customization with social links.

Credits
- Libraries like Django-Allauth, Crispy Forms, Bootstrap.
- Help and guidence from Code Institute and various online resources like chatgpt, w3school, etc.
