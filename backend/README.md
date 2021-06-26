### Setup
    Download the files from this repo

    Change the directory to the folder where you downloaded files

    For installing required packages, execute the following command in terminal:

    pip install -r requirements.txt

    After successful installation execute the following commands:

    python manage.py migrate
    python manage.py runserver


### Admin
    Products List
    http://127.0.0.1:8000/

    Category List
    http://127.0.0.1:8000/category-list/

    Add Category
    http://127.0.0.1:8000/add-category/

    Add Products
    http://127.0.0.1:8000/add-product/

    Order List
    http://127.0.0.1:8000/order-list/

    Add Order
    http://127.0.0.1:8000/add-order/

### Login API
    http://127.0.0.1:8000/api/v1/token/login/

    User List & Sign Up
    http://127.0.0.1:8000/api/v1/users/

### Products API

    Products List
    http://127.0.0.1:8000/api/products/latest

    Products Search
    http://127.0.0.1:8000/api/products/search/

    Product Detail
    http://127.0.0.1:8000/api/products/chicken/friendship-bucket/

    Category Detail
    http://127.0.0.1:8000/api/products/chicken/

### Order API

    Order List API
    http://127.0.0.1:8000/api/v1/orders/list/

    Checkout API
    http://127.0.0.1:8000/api/v1/orders/checkout/