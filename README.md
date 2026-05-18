# a365labs - Office 365 & OS License Services Website

A simple, professional Flask website for a365labs that serves Office 365 and Operating System licenses.

## Features

- **Home Page**: Welcoming hero section with key features
- **About Page**: Company mission and value proposition
- **Services Page**: Detailed service offerings and pricing information
- **Contact Page**: Contact form with validation and message handling
- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Professional Styling**: Clean, modern UI with consistent branding

## Project Structure

```
a365labs/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation and footer
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── services.html     # Services page
│   ├── contact.html      # Contact page
│   └── 404.html          # 404 error page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── main.js       # JavaScript functionality
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
   ```bash
   cd a365labs
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask development server**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to**
   ```
   http://localhost:5000
   ```

3. **Navigate through the website**
   - Home: `/` or click the logo
   - About: `/about`
   - Services: `/services`
   - Contact: `/contact`

## Configuration

### Environment Variables

You can customize the following in `app.py`:

- `debug=True`: Enable debug mode (change to `False` for production)
- `host='0.0.0.0'`: Server host (localhost by default in production)
- `port=5000`: Server port

### Contact Form

The contact form currently logs submissions to the console. To enable email sending:

1. Install an email library: `pip install python-dotenv smtplib`
2. Add SMTP configuration in `app.py`
3. Update the contact form handler to send emails

## Customization

### Branding

- Update company name throughout templates (search "a365labs")
- Modify colors in `static/css/style.css` (`:root` CSS variables)
- Update contact information in `templates/contact.html`

### Services

- Edit service descriptions in `templates/services.html`
- Add or remove feature cards as needed

### Content

- All page content can be edited in the respective HTML template files
- Update pricing, service offerings, and company information

## Deployment

### Production Deployment

For production deployment, consider:

1. **Change Flask settings**
   - Set `debug=False` in `app.py`
   - Use a production WSGI server (Gunicorn, uWSGI)

2. **Environment variables**
   - Store sensitive data in environment variables
   - Use `.env` file with `python-dotenv`

3. **Deployment Options**
   - **Azure App Service**: Deploy using Azure CLI or VS Code extension
   - **Heroku**: Push repository and deploy
   - **DigitalOcean**: Use App Platform or Droplet
   - **AWS**: Use Elastic Beanstalk or EC2

### Azure Deployment (Recommended)

```bash
# Install Azure CLI
# Configure Azure credentials
# Deploy to App Service
az webapp deployment source config-zip --resource-group <group> --name <app-name> --src <zip-file>
```

## Features to Add

- Email integration for contact form submissions
- Blog or resource section
- Pricing calculator
- Live chat support
- Payment integration
- License inventory management
- User login/accounts

## Support

For questions or issues, contact: info@a365labs.com

## License

© 2026 a365labs. All rights reserved.
