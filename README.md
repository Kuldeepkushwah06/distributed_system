# Distributed Database Simulation Project

## Project Overview

This project demonstrates a distributed database simulation using Django and SQLite, showcasing concurrent database insertions with threading and basic data validation across multiple database files.

## Project Structure

```
distributed_db_project/
│
├── manage.py
├── distributed_db/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── data_models/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── migrations/
│   └── management/
│       └── commands/
│           └── simulate_insertions.py
│
└── databases/
    ├── users.db
    ├── orders.db
    └── products.db
```

## Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

## Setup and Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
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
python manage.py migrate
```

### 3. Run Insertion Simulation

```bash
python manage.py simulate_insertions
```

## Data Validation and Error Handling

The project implements several validation checks:

- Prevents duplicate entries across all models
- Ensures non-negative prices for products
- Validates order quantities
- Logs error messages for invalid data

## Simulated Data Examples

### Users
- 10 user entries (including a duplicate)
- Unique and potential duplicate email scenarios

### Products
- 10 product entries
- Includes a negative price test case

### Orders
- 10 order entries
- Tests various edge cases like zero and negative quantities
- Includes references to non-existent products

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

## License

[Specify your license here]

## Contributing

[Add contribution guidelines if applicable]
