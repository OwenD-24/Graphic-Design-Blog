# Graphic Design Blog

# Table of Contents
- <a href="#project-overview">Project Overview</a>
- <a href="#features">Features</a>
- <a href="#user-stories">User Stories</a>
- <a href="#technologies-used">Technologies Used</a>
- <a href="#installation-and-setup">Installation and Setup</a>
- <a href="#usage">Usage</a>
- <a href="#database-schema">Database Schema</a>
- <a href="#ui-and-ux-design">UI and UX Design</a>
- <a href="#user-flow">User Flow</a>
- <a href="#testing">Testing</a>
- <a href="#bug-fixes-and-manual-testing-with-screenshots">Bug Fixes and Manual Testing with Screenshots</a>
- <a href="#deployment">Deployment</a>
- <a href="#future-enhancements">Future Enhancements</a>
- <a href="#credits">Credits</a>

# Project Overview
- **Purpose**: A Graphic Design Blog where users can share, manage, and explore creative content.
- **Main Features**: User registration, login, profile management, and CRUD operations for blog posts.
- **Target Audience**: Graphic designers, artists, and design enthusiasts.

# Features
- **User Registration & Login**: Users can sign up, log in, and manage their accounts.
- **Favourites & Likes**: Users can like and save blog posts.
- **Profile Management**: Update profile info and view saved content.
- **CRUD for Blog Posts**: Users can create, edit, delete, and manage their posts.

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
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL
- **Media Storage**: Cloudinary
- **Libraries**: Crispy Forms, Summernote, Django-Allauth

# Installation and Setup
- Install dependencies: `pip install -r requirements.txt`
- Set up `.env` file with credentials.
- Apply migrations: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Run the server: `python manage.py runserver`

# Usage
- Navigate through the site, register or log in, and manage blog posts from the dashboard. Users can create, edit, delete, and view posts and save favorite posts.

# Database Schema
- The diagram below represents users, profiles, blog posts, and favorites with relationships between them.
- ![image](https://github.com/user-attachments/assets/147164a1-b75a-46fe-901c-2298c4f4a803)

# UI and UX Design
- Wireframes:
  - Desktop ![image](https://github.com/user-attachments/assets/ca57f0a7-73a3-42cc-9d14-156a7207bfae)
  - Tablet ![image](https://github.com/user-attachments/assets/4a4444b6-cf4a-4af7-86c1-ea1e2696d961)
  - Mobile ![image](https://github.com/user-attachments/assets/66f2ff3e-e07e-481a-86cf-4508235390c0)

- Responsive layout using Bootstrap for mobile and desktop.
  ![image](https://github.com/user-attachments/assets/ebe95a08-90a4-4379-8489-f7262d562800)

# User Flow
- ![image](https://github.com/user-attachments/assets/ea733ea5-38fa-4e1e-a640-e504198872e9)

# Testing
- **Automated Testing**:
   Django Unit Tests: Covered models and views to confirm correct data handling, template rendering, and appropriate HTTP responses.
- **Manual Testing**: 
   - User Actions: Verified user flows like registration, login, CRUD operations (Create, Read, Update, Delete) to ensure smooth user experience and access control.
   - UI Responsiveness: Checked the interface across different devices for layout adaptability and readability.

# Bug Fixes and Manual Testing with Screenshots
- **UI Responsiveness Test**: 
   - Ensured that the layout and styling of the application adapt well to various screen sizes, ensuring good mobile and desktop usability.
     
  ![image](https://github.com/user-attachments/assets/99046d14-be0f-430a-81f1-1e2c596c8c62)

- **Registration and Login Test**: 
   - Tested the registration and login flows to ensure users can create accounts, log in, and access their profiles.
     
  ![image](https://github.com/user-attachments/assets/5976ac7b-d552-4d7c-adc3-e3ee4476352d)
  ![image](https://github.com/user-attachments/assets/8fdc7034-ea4d-4094-9407-fca6257777a0)

- **Create and Read Posts Test**:
   - Verified that users can create new posts and view them in the blog feed. Confirmed that newly created posts appear correctly.
     
  ![image](https://github.com/user-attachments/assets/01f84240-1dcc-4faa-ad4f-6216c4344fd9)
  ![image](https://github.com/user-attachments/assets/fbf7e2d4-ce3f-4869-93dc-29bdee31376c)

- **Update Post Test**:
   - Ensured that users can edit their posts and that updates save correctly.
     
  ![image](https://github.com/user-attachments/assets/916d8e36-601e-416f-819c-6875a1f949f6)

- **User Settings Email Error Handling**:
  - Screenshot showing the user settings page with improved error handling for invalid email formats.
    
  ![New Bug Fixes 1](https://github.com/user-attachments/assets/a17f4d4b-5f98-4183-9fb5-70fb15f8658a)

- **Footer Link Visibility on Mobile**:
  - Screenshot highlighting the fix for the missing footer links in the site's mobile version.
    
  ![New Bug Fixes 2](https://github.com/user-attachments/assets/c8e38c2b-e494-4996-81c3-b521d4eb9ae8)

- **Error Message Fix for Empty Blog Post Submission**:
  - Screenshot displaying a corrected error message that appeared when users attempted to submit an empty blog post.
    
  ![New Bug Fixes 3](https://github.com/user-attachments/assets/91c6787b-7f38-4985-a9ba-22a790824cd9)

- **User Profile Avatar Fix**:
  - Screenshot showing updated user profile page with fixed avatar display and link styling.
    
  ![New Bug Fixes 4](https://github.com/user-attachments/assets/0ea4c468-fc93-4d08-b64d-25e3366cc077)

- **Mobile View Styling Fix for Blog Post**:
  - Screenshot showing the fix for styling issues in the mobile view of the blog post page.
    
  ![New Bug Fixes 5](https://github.com/user-attachments/assets/45ddabf7-bb23-446e-ae40-ad6d44510201)

- **Registration Form Fix**:
  - Screenshot of the new registration form showing a fix for the missing "password confirmation" field.
    
  ![New Bug Fixes 6](https://github.com/user-attachments/assets/af3b5819-85f2-4602-bdfe-25096a33c694)

- **Successful Post Creation Display**:
  - Screenshot indicating that a successful post creation was properly displayed, confirming the fix for display issues with post rendering.
    
  ![New Bug Fixes 7](https://github.com/user-attachments/assets/328eff33-4784-4eb2-b653-556b66a98cd2)

- **Fixed Blog Post Validation**:
  - Screenshot showing a fixed issue where users could not save a new blog post due to missing form validation checks.
    
  ![New Bug Fixes 8](https://github.com/user-attachments/assets/1842e555-f237-4550-a142-d91a119a5a54)

- **Delete Function 500 Error**:
   - Issue: A 500 error was encountered during post deletion due to an incorrect URL name in `post_confirm_delete.html`.
   - Fix: Updated the action URL in the form from `post-delete` to `blog-delete`, aligning with the URL name in `urls.py`.
   - Testing: 
     - Verified that posts are now deletable without errors and redirect correctly, even in production.
       
  ![image](https://github.com/user-attachments/assets/0135edf2-2131-423a-9d10-489fb0fcf251)

- **User Authentication Checks**:
   - Checked that only authenticated users could create, update, or delete posts, enforcing security and access control.
     
  ![image](https://github.com/user-attachments/assets/8c6c8454-657c-489e-ae23-a0a6e0d149e2)

- **Form Validation Test**:
   - Verified that all forms (registration, post creation, update) show validation errors for invalid inputs, maintaining data integrity.
     
  ![image](https://github.com/user-attachments/assets/d5b6a56b-cb02-4938-98f7-3cd3061ca490)

- **Bug-Free Navigation and Links Test**:
   - Tested site navigation links to ensure they route correctly, allowing users to browse between pages without issues.
     
  ![image](https://github.com/user-attachments/assets/b12c38f7-e40f-4703-908f-0a4f3a4a6ec4)

# Deployment
- Deployed using Heroku for backend and Cloudinary for static/media files.
- Set up environment variables, and ensure `DEBUG=False` in production.

# Future Enhancements
- Image uploads to posts.
- Post comments and like feature.
- Enhanced profile customization with social links.

# Credits
- Libraries like Django-Allauth, Crispy Forms, Bootstrap.
- Help and guidance from Code Institute and various online resources like ChatGPT, W3Schools, etc.

