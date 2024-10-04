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
- ![image](https://github.com/user-attachments/assets/a1b61106-569a-4278-a9af-8d22bd0ad59b)
- ![image](https://github.com/user-attachments/assets/b93cb7e3-0ede-4919-9900-f519c669823a)
- ![image](https://github.com/user-attachments/assets/72095ec6-41a0-451e-81fb-e61065b95327)
- ![image](https://github.com/user-attachments/assets/f402b72f-b4f2-4f7b-9706-275501a95831)
- ![image](https://github.com/user-attachments/assets/99fc1a92-3dfc-4b54-a372-5956fce324d2)
- ![image](https://github.com/user-attachments/assets/211a32ed-e65a-4287-a0ff-d3449039d0b9)
- ![image](https://github.com/user-attachments/assets/a981b974-63d7-4181-bcc6-a6f950db9782)
- ![image](https://github.com/user-attachments/assets/b74a99c4-2a30-40ce-94d9-ee94bd23764d)
- ![image](https://github.com/user-attachments/assets/3d9d2a5c-c8b2-444a-85bf-5996f53978ac)
- 











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
