from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import argparse
import random
import threading
from concurrent.futures import ThreadPoolExecutor


def visit_site(url, visit_number):
    """
    Single site visit function for threading
    """
    print(f"\nStarting Visit #{visit_number}")

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920,1080")

    # Create new browser instance
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Clear browser data
        driver.execute_cdp_cmd('Network.clearBrowserCache', {})
        driver.execute_cdp_cmd('Network.clearBrowserCookies', {})

        # Random delay to seem more human-like
        time.sleep(1 + random.random() * 2)

        # Visit the site
        driver.get(url)

        # Simulate reading time
        time.sleep(3 + random.random() * 3)

    except Exception as e:
        print(f"Error in visit #{visit_number}: {str(e)}")
    finally:
        driver.quit()
        print(f"Completed Visit #{visit_number}")


def simulate_concurrent_visits(url, visits):
    """
    Simulate concurrent first-time visits to a website
    
    Args:
        url (str): The website URL to visit
        visits (int): Number of times to visit the site
    """
    max_concurrent = 10  # Fixed at 10 concurrent visits
    print(f"Starting {visits} concurrent visits to {url}")
    print(f"Maximum concurrent visits: {max_concurrent}")

    # Use ThreadPoolExecutor to manage concurrent visits
    with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
        # Create a list of futures
        futures = [
            executor.submit(visit_site, url, i + 1) for i in range(visits)
        ]

        # Wait for all futures to complete
        for future in futures:
            future.result()


def main():
    parser = argparse.ArgumentParser(
        description='Simulate concurrent first-time visits to a website')
    parser.add_argument('url', help='The URL to visit')
    parser.add_argument('visits',
                        type=int,
                        help='Number of times to visit the site')

    args = parser.parse_args()

    simulate_concurrent_visits(args.url, args.visits)
    print("\nAll visits completed!")


if __name__ == "__main__":
    main()
