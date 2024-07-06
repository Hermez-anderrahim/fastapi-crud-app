# My crud app

This documentation provides an overview of how I used FastAPI and Supabase in my SuperFastAPI app.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Supabase Integration](#supabase-integration)
- [Conclusion](#conclusion)

## Introduction

In this app, I utilized FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. FastAPI is easy to use, highly efficient, and provides automatic interactive documentation.

## Installation

To install the required dependencies for this app, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/superFastapi.git
   ```

2. Navigate to the project directory:

   ```
   cd superFastapi
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the SuperFastAPI app, follow these steps:

1. Make sure you have activated the virtual environment (see the [Installation](#installation) section).

2. Start the FastAPI server:

   ```
   uvicorn main:app --reload
   ```

3. Open your web browser and navigate to `http://localhost:8000` to access the app.

## Supabase Integration

In this app, I integrated Supabase, an open-source Firebase alternative, to handle the database operations. Supabase provides a set of tools and libraries to simplify working with PostgreSQL databases.

To integrate Supabase into your FastAPI app, follow these steps:

1. Sign up for a Supabase account at [https://supabase.io](https://supabase.io).

2. Retrieve your Supabase project URL and API key.

3. Update the app's configuration file (`config.py`) with your Supabase project URL and API key.

4. Use the Supabase Python library (`supabase-py`) to interact with the database. Refer to the Supabase documentation for more details on how to use the library.

## Conclusion

This documentation provides an overview of how I used FastAPI and Supabase in my SuperFastAPI app. By following the installation and usage instructions, you can run the app locally and explore its features. Feel free to modify and extend the app according to your requirements.

For any further assistance, please refer to the official FastAPI and Supabase documentation.
