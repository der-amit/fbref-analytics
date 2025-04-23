from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_player_gca_table(url):
    # Setup Chrome options
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
    
    # Setup the webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Navigate to the page
        driver.get(url)
        
        # Wait for page to load fully - adjust if needed
        time.sleep(5)
        
        # Get the page HTML after JavaScript execution
        html_content = driver.page_source
        
        # Remove HTML comments (where the player table is likely hidden)
        html_content = html_content.replace('<!--', '').replace('-->', '')
        
        # Parse all tables with pandas
        tables = pd.read_html(html_content)
        
        # Look for player-level GCA table - it should have Player, Nation, Pos columns
        for table in tables:
            # Convert column names to strings for checking
            columns = [str(col) for col in table.columns]
            
            # Check for player table indicators
            has_player_col = any('Player' in col for col in columns)
            has_position_col = any('Pos' in col for col in columns)
            has_gca_col = any('GCA' in col for col in columns)
            
            if has_player_col and has_position_col and has_gca_col:
                return table
        
        return None
    
    except Exception as e:
        print(f"Selenium error: {e}")
        return None
    
    finally:
        # Always close the browser
        driver.quit()


url = 'https://fbref.com/en/comps/22/gca/Major-League-Soccer-Stats'
player_gca = scrape_player_gca_table(url)

if player_gca is not None:
    print(f"Successfully retrieved player GCA table with {len(player_gca)} rows")
    print(player_gca.head())
else:
    print("Failed to retrieve player GCA table")
    
player_gca.to_csv('data/player_gca_2025.csv')