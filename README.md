# PrimeHomes Constructions - Django Website

A modern construction company website built with Django, HTML, and Bootstrap 5. This project provides a complete solution for construction companies to showcase their services, projects, and manage their online presence.

## Features

### User-Facing Features
- **Home Page**: Hero section, company stats, featured services, projects, and testimonials
- **Services Page**: Complete list of construction services with icons and descriptions
- **Projects Page**: Portfolio of completed projects with filtering by category
- **About Page**: Company information, team details, and values
- **Contact Page**: Contact form with Google Maps integration
- **Reviews Page**: Client testimonials with rating system and submission form

### Admin Features
- **Django Admin Panel**: Full CRUD operations for all content
- **Admin Dashboard**: Statistics overview and quick access to management
- **Content Management**: Manage services, projects, testimonials, and contact messages
- **Company Settings**: Update company information, contact details, and social media links
- **Image Upload**: Support for service and project images

### Technical Features
- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Modern UI**: Clean, professional design with animations and hover effects
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Form Validation**: Client-side and server-side validation
- **AJAX Support**: Dynamic form submissions and content loading
- **Image Handling**: Automatic image resizing and optimization

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   # If using git
   git clone <repository-url>
   cd construction_company
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the website**
   - Main website: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### For Website Visitors
1. **Browse Services**: View all construction services offered
2. **View Projects**: Explore completed projects with category filtering
3. **Read Reviews**: See what clients say about the company
4. **Contact**: Fill out the contact form to get in touch
5. **Submit Reviews**: Share your experience with the company

### For Administrators
1. **Login to Admin Panel**: Use your superuser credentials
2. **Manage Content**:
   - **Services**: Add, edit, or remove construction services
   - **Projects**: Upload project images and update project details
   - **Testimonials**: Approve or remove client reviews
   - **Messages**: View and respond to contact form submissions
   - **Company Info**: Update company details, contact information, and social media links

3. **Admin Dashboard**: Access quick statistics and management tools

## Project Structure

```
construction_company/
├── construction_company/     # Main Django project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── core/                    # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin panel configuration
│   └── urls.py              # App URL patterns
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   └── core/                # App-specific templates
│       ├── home.html        # Home page
│       ├── services.html    # Services page
│       ├── projects.html    # Projects page
│       ├── about.html       # About page
│       ├── contact.html     # Contact page
│       ├── testimonials.html # Reviews page
│       └── admin_dashboard.html # Admin dashboard
├── static/                  # Static files
│   ├── css/
│   │   └── style.css        # Custom CSS
│   └── js/
│       └── main.js          # Custom JavaScript
├── media/                   # Uploaded files (created automatically)
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Database Models

### Service
- Title, description, icon, color, image
- Used for displaying construction services

### Project
- Title, description, category, status, image
- Used for showcasing completed projects

### Testimonial
- Name, rating, comment, creation date
- Used for client reviews and testimonials

### ContactMessage
- Name, email, phone, subject, message, read status
- Used for contact form submissions

### CompanyInfo
- Company details, contact information, social media links, statistics
- Used for company information display

## Customization

### Styling
- Edit `static/css/style.css` to customize colors, fonts, and layout
- Modify Bootstrap classes in templates for layout changes
- Update `settings.py` for theme colors and branding

### Content
- Use Django admin panel to update all content
- Add new services, projects, and testimonials
- Update company information and contact details

### Functionality
- Modify `views.py` to add new features
- Update `urls.py` to add new pages
- Edit templates to change page layouts

## Deployment

### Production Settings
1. Update `settings.py`:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Set up proper database (PostgreSQL recommended)
   - Configure static and media file serving

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Set up a production server (Gunicorn, uWSGI, etc.)

### Recommended Hosting
- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS with Django deployment
- **AWS**: Scalable cloud hosting
- **PythonAnywhere**: Django-specific hosting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support or questions:
- Create an issue in the repository
- Contact the development team
- Check the Django documentation

## Changelog

### Version 1.0.0
- Initial release
- Complete website with all features
- Admin panel with full CRUD operations
- Responsive design with Bootstrap 5
- Image upload functionality
- Contact and testimonial forms

---

**Built with ❤️ using Django and Bootstrap 5** 