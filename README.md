# E-Stock Application

E-Stock is a web and mobile application designed for stock and sales management. This application provides functionalities for both administrators and clients, ensuring a seamless experience in managing products, orders, and payments.

## Features

### For Administrators:
- Secure authentication using JWT
- CRUD operations for Products, Categories, and Users
- Management of stock movements (entries/exits)
- Order management (status, details)
- Payment validation
- Management of client debts
- Generation of reports (sales, stock, payments)
- Alert system for critical stock levels

### For Clients:
- User registration and login
- Browse product catalog
- Add products to cart
- Place orders
- Payment options (including deferred payment)
- Order and payment history

### Additional Features:
- Push notifications via Firebase
- Online payment integration with Stripe or MyNITA API
- Admin dashboard with key performance indicators (KPIs)

## Tech Stack
- **Backend**: Django 4, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Frontend**: React Native with Expo (and React Native Web)
- **Notifications**: Firebase Cloud Messaging (FCM)
- **Payment**: Stripe API (with potential MyNITA integration)

## Deployment
- **Backend**: Docker image with deployment on Render, Railway, or VPS (using Gunicorn + Nginx)
- **Frontend Web**: Deployed on Vercel, Netlify, or Render
- **Mobile**: Built with Expo for distribution on Play Store and App Store

## Getting Started

### Prerequisites
- Python 3.x
- Node.js and npm
- PostgreSQL
- Docker (optional)

### Backend Setup
1. Navigate to the `backend` directory.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm start
   ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.