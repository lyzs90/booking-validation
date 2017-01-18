# Booking Validation Module

This module is for answering [Smove's](https://www.smove.sg/) Booking Validation Problem, which seeks a single permutation for a sequence of car bookings to minimise the total number of relocations. Relocations occur when the car has to be moved for the next booking.

## Getting started

```bash
# get the source from the Git repository
git clone https://github.com/lyzs90/booking-validation.git
cd booking-validation

# set up the Python environment
python3 -m venv venv
source venv/bin/activate  `#venv\Scripts\activate for Windows`
pip install -r requirements.txt

# run the module
python validate.py -f tests/bookingvalidation.json

# run with increased iterations (default: 500)
python validate.py -f tests/bookingvalidation.json -i 1000
```

## Testing
```bash
# run test suite
pytest
```

## Documentation

Use Sphinx to generate documentation for the module.

```bash
mkdir docs
sphinx-apidoc -F -o docs ./
```

Uncomment & edit docs/conf.py:

```bash
import sys, os
sys.path.insert(0, os.path.abspath('../'))
html_theme = "classic"
```

Generate the html:

```bash
cd docs
make html
```
