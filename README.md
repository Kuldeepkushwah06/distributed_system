# Distributed Database Simulation Project

## Project Overview

This project demonstrates a distributed database simulation using Django and SQLite, showcasing concurrent database insertions with threading and basic data validation across multiple database files.



## Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kuldeepkushwah06/distributed_system.git
cd distributed_db_project
```

### 2. Create and Activate Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

## Project Components

### Database Models

The project includes three main models:

1. **UserModel**
   - Stores user information
   - Attributes: id, name, email
   - Validates unique entries
   - Stored in `users.db`

2. **ProductModel**
   - Stores product information
   - Attributes: id, name, price
   - Validates non-negative prices
   - Stored in `products.db`

3. **OrderModel**
   - Stores order information
   - Attributes: id, user_id, product_id, quantity
   - Validates non-negative quantities
   - Stored in `orders.db`

### Concurrent Insertion Simulation

The project uses Python's `threading` module to simulate concurrent database insertions. Key features:

- Creates separate threads for users, products, and orders
- Handles potential integrity errors
- Logs invalid data entries
- Ensures thread-safe insertions

## Running the Project

### 1. Create Databases Directory

```bash
mkdir databases
```

### 2. Run Migrations (Optional for SQLite)

```bash
# Create migrations
python manage.py makemigrations main

# Apply migrations to all databases
python manage.py migrate --database=default
python manage.py migrate --database=orders
python manage.py migrate --database=products
```

### 3. Run Insertion Simulation

```bash
python manage.py run_insertions
```

## Data Validation and Error Handling

The project implements several validation checks:

- Prevents duplicate entries across all models
- Ensures non-negative prices for products
- Validates order quantities
- Logs error messages for invalid data





## Logging and Error Reporting

Invalid entries are reported via console output:
- Duplicate entries
- Invalid prices
- Invalid quantities

## Performance Considerations

- Uses threading for concurrent insertions
- Separate SQLite databases for each model
- Minimal overhead with lightweight validation

## Potential Improvements

1. Implement more robust error handling
2. Add comprehensive logging mechanism
3. Create a configuration file for test data
4. Implement database connection pooling
5. Add more extensive data validation

## Troubleshooting

- Ensure write permissions in the project directory
- Check Python and Django versions compatibility
- Verify virtualenv activation

