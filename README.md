# Hair Haven

---

## Installation instuctions

---

---

### clone the repository from https://github.com/Mitchkal/project.git

### cd into the cloned repository > with git checkout development

### change into the developemnt banch with git checkout

### create a virtual environment with > python3 -m venv <virtual-environment-name>

### Activate the virtual environment with > source <virtal-environment-name>/bin/activate

### Install dependency requirements with > pip install -r requirements.txt

## Starting

---

### cd into the webfunctions directory

### Ensure you copy the firebase key.json file into the webfunctions directory; key.json will contain the firebase authentication keys.

### Start the Flask application with > flask --app app run

### Access the web application at > http://localhost:5000/

## Current Features

### Product display

### Add to cart

### Remove from cart

### View Cart content

To Do

- [x] Create backend with product, customer models
- [x] Create and integrate Backend endpoints for:

  - [x] Get and return products from backend storage
  - [x] Update products in the inventory
  - [] post product reviews
  - [] perform user signup
  - [] perform user login
  - [] Perform order processing and checkout functions
  - [] Get order shipment status

- [x] Create Frontend to display products, add, remove product from cart, view cart
- [] Add user Authentication - signup and signin with Flask authentication
- [] Add Checkout and stripe payment capabilities
- [] Resolve lagging functionalities, Possibly add caching, etc.
- [] Shift to mongodb for backend storage
- [] Create admin console to facilitate inventory update, view sales etc.
- [] Shift to the Flask WSGI development server- Gunicorn
- etc.
