# TripTrack

TripTrack is a web application built for travelers who want to preserve their cherished memories or discover the adventures of others. Users can store photos and videos, publish travel articles, and provide comprehensive reviews of destinations.

## Features

- User registration and authentication (signup, login, logout)
- Create trips with associated notes and media (photos/videos)
- Update and delete trips or notes
- Publish travel articles and destination reviews
- Responsive interface styled with Tailwind CSS

## Tech Stack

- **Backend:** Python, Django 5.0
- **Frontend:** Tailwind CSS, Django templates
- **Database:** SQLite (default; configurable)
- **Forms:** crispy_forms, crispy_tailwind
- **Media Management:** Django media storage (for images/videos)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MahinShahriar/TripTrack.git
   cd TripTrack
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup Tailwind for Django:
   - Follow the [django-tailwind documentation](https://django-tailwind.readthedocs.io/en/latest/installation.html) for installation and configuration.

4. Perform migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Configuration

- Static files are served from `/static/`
- Media uploads (photos/videos) use `/media/`
- Local apps: `trip` (core trip management)
- Third-party apps: `tailwind`, `crispy_forms`, `crispy_tailwind`
- See `TripTrack/settings.py` for further configuration.

## Usage

- Visit the homepage to sign up or log in.
- Create new trips and add notes with media.
- View, update, or delete your trips and notes.
- Access the admin panel at `/admin/` for advanced controls.

## License

This project does not yet specify a license.

## Author

- [MahinShahriar](https://github.com/MahinShahriar)

---
*For more details, see the source code and Django settings in this repository.*
