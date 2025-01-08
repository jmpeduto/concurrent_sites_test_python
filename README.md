# Concurrent Website Visitor

A Python script that simulates multiple concurrent first-time visits to a website using Selenium WebDriver. The script clears browser cache and cookies before each visit to simulate authentic first-time visitors.

## Features

- Concurrent website visits (10 simultaneous visits by default)
- Automatic cache and cookie clearing before each visit
- Human-like behavior simulation with random delays
- Progress tracking for each visit
- Error handling for failed visits

## Prerequisites

Before running this script, you need to have the following installed:

1. Python 3.x
2. Chrome browser
3. ChromeDriver (matching your Chrome version)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/concurrent-website-visitor.git
cd concurrent-website-visitor
```

2. Create and activate a virtual environment:
```bash
# Install required packages if not already installed
sudo apt install python3-full python3-venv

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

3. Install required packages:
```bash
pip install selenium
```

## Usage

1. Make sure your virtual environment is activated:
```bash
source venv/bin/activate
```

2. Run the script:
```bash
python website_visitor.py URL NUMBER_OF_VISITS
```

Example:
```bash
python website_visitor.py https://example.com 20
```
This will create 20 visits to example.com, with 10 concurrent visits running at a time.

### Parameters

- `URL`: The website URL you want to visit
- `NUMBER_OF_VISITS`: Total number of visits to make to the website

## Important Notes

- The script uses threading to manage concurrent visits
- Each visit opens in a new browser window
- Browser windows are automatically closed after each visit
- The script includes random delays to simulate human behavior
- Opening too many concurrent sessions might impact system performance
- Some websites might detect and block multiple simultaneous connections

## Troubleshooting

If you encounter any errors:

1. Make sure Chrome and ChromeDriver are installed and up to date
2. Verify that the ChromeDriver version matches your Chrome browser version
3. Check if the website allows automated access
4. Ensure you have enough system resources for the number of concurrent visits

## Contributing

Feel free to fork this repository and submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.