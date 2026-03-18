
# Porsche UI Tests (unittest + Selenium)

## Description
The test runs automatically in Chrome, Firefox, and Edge.

## Run from Terminal (required)
All commands must be executed in Terminal.

## Prerequisites
- Python 3
- Google Chrome installed
- Mozilla Firefox installed
- Microsoft Edge installed
- Selenium
- webdriver-manager

## Install dependencies
```bash
python3 -m pip install selenium webdriver-manager

###  Quick Check
python3 -c "import selenium, webdriver_manager; print('OK')"

## Run tests
### Run All Tests
python3 -m unittest UnitestPorsche.porscheUnitestCrossBrowser

### Run ONE specific test
python3 -m unittest UnitestPorsche.porscheUnitestCrossBrowser.ChromeDriverPorsche.test_TC_P_011


