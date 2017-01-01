# Booking Validation Module

This module is for answering [Smoove's](https://www.smove.sg/) Booking Validation Problem, which seeks a single permutation for a sequence of car bookings to minimise the total number of relocations. Relocations occur when the car has to be moved for the next booking.

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