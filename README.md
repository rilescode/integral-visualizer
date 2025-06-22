# Integral Visualizer

A Django web application for visualizing mathematical integrals.

## Live Demo

### Website: https://integral-visualizer.vercel.app/

## Prerequisites

- Python 3.8+
- Git
- pip (Python package manager)

## Local Development Setup

### Windows Installation

1. **Download and Setup**

   ```bash
   # Clone or download the repository
   git clone <repository-url>
   cd integral-visualizer
   ```

2. **Create Virtual Environment**

   ```bash
   # Install virtualenv wrapper
   pip install virtualenvwrapper-win

   # Create virtual environment
   mkvirtualenv integral-visualizer

   # Activate environment
   workon integral-visualizer
   ```

3. **Install Dependencies**

   ```bash
   # Install all dependencies from requirements.txt
   pip install -r requirements.txt
   ```

4. **Run Development Server**

   ```bash
   # Navigate to project directory (where manage.py is located)
   cd src  # or wherever manage.py is located

   # Run migrations
   python manage.py migrate

   # Collect static files
   python manage.py collectstatic --noinput --clear

   # Start development server
   python manage.py runserver
   ```

5. **Access Application**
   - Open your browser and go to `http://127.0.0.1:8000/`

### macOS/Linux Installation

1. **Download and Setup**

   ```bash
   # Clone or download the repository
   git clone <repository-url>
   cd integral-visualizer
   ```

2. **Create Virtual Environment**

   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate virtual environment
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   # Install all dependencies from requirements.txt
   pip install -r requirements.txt
   ```

4. **Run Development Server**

   ```bash
   # Run migrations
   python manage.py migrate

   # Collect static files
   python manage.py collectstatic --noinput --clear

   # Start development server
   python manage.py runserver
   ```

5. **Access Application**
   - Open your browser and go to `http://127.0.0.1:8000/`

## Development Commands

```bash
# Activate virtual environment
workon integral-visualizer  # Windows
source venv/bin/activate    # macOS/Linux

# Run development server
python manage.py runserver

# Run migrations
python manage.py migrate

# Make migrations (after model changes)
python manage.py makemigrations

# Collect static files
python manage.py collectstatic

# Create superuser account
python manage.py createsuperuser
```
