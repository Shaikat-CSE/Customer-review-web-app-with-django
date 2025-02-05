# Customer Review Project

This project is a web application for managing customer reviews of products. Users can view available products and share their experiences by writing reviews. Admin users can add new products to the list.

## Features

- View a list of available products
- Write reviews for products
- Admin functionality to add new products
- Data visualization for review analytics
  - Rating distribution
  - Yes/No responses
  - Multiple choice responses
  - Review timeline

## Tech Stack

- **Frontend:**
  - HTML
  - CSS (Tailwind CSS)
  - JavaScript (Chart.js)
- **Backend:**
  - Python
  - Django
- **Database:**
  - SQLite (default, can be replaced with PostgreSQL, MySQL, etc.)
- **Other:**
  - Virtualenv for environment management

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.x
- Django
- Virtualenv

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Shaikat-CSE/Customer-review-web-app-with-django.git
    cd customer_review
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`

## Usage

- **View Products:** Navigate to the homepage to see a list of available products.
- **Write Reviews:** Click on a product to view its details and submit a review.
- **Admin:** Log in as an admin to add new products.
- **Analytics:** Navigate to `/analytics/` to view data visualizations of the reviews.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.