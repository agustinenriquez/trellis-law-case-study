# Made by Agustin Enriquez for Trellis Law

# Django Number to English Converter

This is a Django application that provides an API to convert numbers to English words. It also includes a landing page where users can input a number and get the English representation of it.

## Usage

    - Install docker
    - Run docker compose up
    - Access the application in your web browser at `http://localhost:8000`.

## API Endpoints

- `GET /num_to_english?number=<number>`
- `POST /num_to_english` (with JSON body: `{"number": "<number>"}`)
- `GET /test?number=<number>`

## Dependencies

- Python 3.9
- Django 4.2
- Vue.js 2 
- Bootstrap 4.5
- Axios


