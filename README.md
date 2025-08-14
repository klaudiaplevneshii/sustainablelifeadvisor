# carbon
DJANGO &amp; PYTHON calculate a carbon footprint
# 🌱 Carbon Emissions Calculator - Django Project

This is a Django-based web application designed to calculate carbon emissions based on user inputs related to transport, energy use, and more. The core logic is handled in a single app called `landing`, with central project settings handled in the `carbon` directory.

---

## Project Structure

- **carbon/**: Main Django project folder (created via `django-admin startproject`). Key files:
  - `settings.py`: Add apps here under `INSTALLED_APPS`.
  - `urls.py`: Routes incoming URLs to the appropriate views. Includes:
    - `path('admin/', admin.site.urls)` – default Django admin path.
- **landing/**: The main Django app for handling views, templates, and logic.
  - Most of the application logic is written here.
  - Routes are handled in `landing/urls.py`.
  - Views for processing and returning user input are defined in `views.py`.

---

## Setup Instructions

### 1. Environment Setup

Create and activate a virtual environment:

pip install django pillow whitenoise 
python manage.py migrate
python manage.py runserver


### 2. Install Dependencies

Install the required Python packages:

```bash
pip install django pillow whitenoise
```

> `Whitenoise` is used for serving static files when deploying the app to a server.

---

```bash
pip install markdown 
```

# Running the Project

After installing the dependencies, apply the database migrations, and then run the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

##  How It Works

### Backend (Views)

1. In `views.py`, the logic starts by handling the incoming `POST` request.
2. It extracts data from `request.POST` (such as transport, energy usage, etc.).
3. Data is passed to a utility function (in `utils.py`) that calculates carbon emissions.
4. The result is stored in a variable and passed to the template via a `context` dictionary.
5. Django renders the `form.html` template with the result.

```python
context = {
    'result': calculated_value
}
return HttpResponse(template.render(context, request))
```

### Frontend (Templates)

- The `form.html` file is styled using **Tailwind CSS** for a professional UI.
- Dynamic values like the carbon result are injected directly into the HTML (e.g., line 66–71).
- The form submits via `POST`, and data is handled in the corresponding view.

---

## Static Files

- Static files (CSS, JS) are handled by Django's static system.
- `STATIC_URL` is defined in `settings.py`.
- When deploying to production, `Whitenoise` helps serve these static files efficiently.

---

## Checklist

- [x] Django setup with `startproject` and `startapp`
- [x] App registered in `INSTALLED_APPS`
- [x] URL routing for `landing` app
- [x] Tailwind CSS integration
- [x] Emissions calculation logic implemented in `utils.py`
- [x] Form handling and dynamic rendering
- [x] Ready for deployment with static file handling

---

## Notes

- All main logic resides in the `landing` app.
- Only one app is used for simplicity.
- Admin panel (`admin.site.urls`) is available by default for managing users and models.

---

## Testing Locally

To test the form and emissions calculation:

1. Start the server: `python manage.py runserver`
2. Go to the form page.
3. Input values related to transport, energy, etc.
4. Submit the form and view results dynamically rendered on the page.


```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
