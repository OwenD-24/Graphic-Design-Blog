# Graphic Design Blog
## Table of Contents

# Project Overview
- Purpose: A Graphic Design Blog where users can share, manage, and explore creative content.
- Main Features: User registration, login, profile management, and CRUD operations for blog posts.
- Target Audience: Graphic designers, artists, and design enthusiasts.

# Features
- User Registration & Login: Users can sign up, log in, and manage their accounts.
- Favourites & Likes: Users can like and save blog posts.
- Profile Management: Update profile info and view saved content.
- CRUD for Blog Posts: Users can create, edit, delete, and manage their posts.

# User Stories
- ![image](https://github.com/user-attachments/assets/a1b61106-569a-4278-a9af-8d22bd0ad59b)
- ![image](https://github.com/user-attachments/assets/b93cb7e3-0ede-4919-9900-f519c669823a)
- ![image](https://github.com/user-attachments/assets/72095ec6-41a0-451e-81fb-e61065b95327)
- ![image](https://github.com/user-attachments/assets/f402b72f-b4f2-4f7b-9706-275501a95831)
- ![image](https://github.com/user-attachments/assets/99fc1a92-3dfc-4b54-a372-5956fce324d2)
- ![image](https://github.com/user-attachments/assets/211a32ed-e65a-4287-a0ff-d3449039d0b9)
- ![image](https://github.com/user-attachments/assets/a981b974-63d7-4181-bcc6-a6f950db9782)
- ![image](https://github.com/user-attachments/assets/b74a99c4-2a30-40ce-94d9-ee94bd23764d)
- ![image](https://github.com/user-attachments/assets/3d9d2a5c-c8b2-444a-85bf-5996f53978ac)
- ![image](https://github.com/user-attachments/assets/4ac00a82-0d84-45ee-be6f-f12d1c1594f1)

# Technologies Used
- Backend: Django, Python
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Database: PostgreSQL
- Media Storage: Cloudinary
- Libraries: Crispy Forms, Summernote, Django-Allauth

# Installation & Setup
- Install dependencies: pip install -r requirements.txt
- Set up .env file with credentials.
- Apply migrations: python manage.py migrate
- Create a superuser: python manage.py createsuperuser
- Run the server: python manage.py runserver

# Usage
- Navigate through the site, register or log in, and manage blog posts from the dashboard. Users can create, edit, delete, and view posts and save favorites posts.

# Database Schema
- The diagram below represents users, profiles, blog posts and favourites with relationships between them.
![image](https://github.com/user-attachments/assets/147164a1-b75a-46fe-901c-2298c4f4a803)

# UI/UX Design
- Wireframes:
- Desktop ![image](https://github.com/user-attachments/assets/ca57f0a7-73a3-42cc-9d14-156a7207bfae)
- Tablet ![image](https://github.com/user-attachments/assets/4a4444b6-cf4a-4af7-86c1-ea1e2696d961)
- Mobile ![image](https://github.com/user-attachments/assets/ab6dcc47-2a48-4fb9-b06c-78082f328855)


- # Responsive layout using Bootstrap for mobile and desktop.
  ![image](https://github.com/user-attachments/assets/ebe95a08-90a4-4379-8489-f7262d562800)

- # User Flow
- ![image](https://github.com/user-attachments/assets/ea733ea5-38fa-4e1e-a640-e504198872e9)

# Testing
- Automated Testing:
   Django Unit Tests: Covered models and views to confirm correct data handling, template rendering, and appropriate HTTP responses.
- Manual Testing: 
   User Actions: Verified user flows like registration, login, CRUD operations (Create, Read, Update, Delete) to ensure smooth user experience and access control.
  
   UI Responsiveness: Checked the interface across different devices for layout adaptability and readability.
  
# Bug Fixes and Manual Testing with Screenshots
- UI Responsiveness Test
   - Ensured that the layout and styling of the application adapt well to various screen sizes, ensuring good mobile and desktop usability.
  ![image](https://github.com/user-attachments/assets/99046d14-be0f-430a-81f1-1e2c596c8c62)
- Registration and Login Test
  - Tested the registration and login flows to ensure users can create accounts, log in, and access their profiles.
  ![image](https://github.com/user-attachments/assets/5976ac7b-d552-4d7c-adc3-e3ee4476352d)
  ![image](https://github.com/user-attachments/assets/8fdc7034-ea4d-4094-9407-fca6257777a0)
- Create and Read Posts Test
  - Verified that users can create new posts and view them in the blog feed. Confirmed that newly created posts appear correctly.
  ![image](https://github.com/user-attachments/assets/01f84240-1dcc-4faa-ad4f-6216c4344fd9)
  ![image](https://github.com/user-attachments/assets/fbf7e2d4-ce3f-4869-93dc-29bdee31376c)
- Update Post Test
  - Ensured that users can edit their posts and that updates save correctly.
  ![image](https://github.com/user-attachments/assets/916d8e36-601e-416f-819c-6875a1f949f6)
- Delete Function 500 Error
  - Issue: A 500 error was encountered during post deletion due to an incorrect URL name in post_confirm_delete.html.
  - Fix: Updated the action URL in the form from post-delete to blog-delete, aligning with the URL name in urls.py.
  - Testing:
    - Verified that posts are now deletable without errors and redirect correctly, even in production.
  ![image](https://github.com/user-attachments/assets/0135edf2-2131-423a-9d10-489fb0fcf251)
- User Authentication Checks
  - Checked that only authenticated users could create, update, or delete posts, enforcing security and access control.
  ![image](https://github.com/user-attachments/assets/8c6c8454-657c-489e-ae23-a0a6e0d149e2)
- Form Validation Test
  - Verified that all forms (registration, post creation, update) show validation errors for invalid inputs, maintaining data integrity.
  ![image](https://github.com/user-attachments/assets/d5b6a56b-cb02-4938-98f7-3cd3061ca490)
- Bug-Free Navigation and Links Test
  - Tested site navigation links to ensure they route correctly, allowing users to browse between pages without issues.
  ![image](https://github.com/user-attachments/assets/b12c38f7-e40f-4703-908f-0a4f3a4a6ec4)

# Deployment
- Deployed using Heroku for backend and Cloudinary for static/media files.
- Set up environment variables, and ensure DEBUG=False in production.

 # Future Enhancements
- Image uploads to posts.
- Post comments and like feature.
- Enhanced profile customization with social links.

# Credits
- Libraries like Django-Allauth, Crispy Forms, Bootstrap.
- Help and guidence from Code Institute and various online resources like chatgpt, w3school, etc.
