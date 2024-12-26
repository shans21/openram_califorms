import os
from bs4 import BeautifulSoup
import csv

def extract_sram_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract configuration data
    config_table = soup.find_all('table')[0]  # Assuming the first table contains config data
    config_data = {}
    for row in config_table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == 2:
            config_data[cells[0].text.strip()] = cells[1].text.strip()

    # Extract timing data
    timing_table = soup.find_all('table')[2]  # Assuming the third table contains timing data
    timing_data = {}
    for row in timing_table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == 4:
            timing_data[cells[0].text.strip()] = cells[2].text.strip()
    
    # Extract power data
    power_table = soup.find_all('table')[3]  # Assuming the fourth table contains power data
    power_data = {}
    for row in power_table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == 4:
            mode = cells[1].text.strip()
            power_value = float(cells[2].text.strip())
            power_data[mode] = power_value
    
    # Calculate average power
    avg_power = (power_data.get('Read Rising', 0) + 
                 power_data.get('Read Falling', 0) +
                 power_data.get('Write Rising', 0) +
                 power_data.get('Write Falling', 0)) / 4 + power_data.get('leakage', 0)
    
    # Extract frequency
    frequency_row = soup.find('td', text='Operating Frequency (F)').find_next('td')
    frequency = frequency_row.text.strip() if frequency_row else "N/A"
    
    return {
        'RW Ports': config_data.get('NUM_RW_PORTS', 'N/A'),
        'R Ports': config_data.get('NUM_R_PORTS', 'N/A'),
        'W Ports': config_data.get('NUM_W_PORTS', 'N/A'),
        'Word Size': config_data.get('WORD_SIZE', 'N/A'),
        'Num Words': config_data.get('NUM_WORDS', 'N/A'),
        'Library': 'freepdk45',
        'Area (µm²)': config_data.get('Area ', 'N/A'),
        'Frequency': frequency,
        'Access Time': timing_data.get('dout1[31:0] cell rise', 'N/A'),
        'Avg. Power': f"{avg_power:.6f} mW"
    }

def get_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    folder_path = 'out_files'  # Current directory
    html_files = get_html_files(folder_path)
    
    headers = ['RW Ports', 'R Ports', 'W Ports', 'Word Size', 'Num Words', 
               'Library', 'Area (µm²)', 'Frequency', 'Access Time', 'Avg. Power']
    
    with open('sram_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        for html_file in html_files:
            with open(html_file, 'r') as file:
                html_content = file.read()
            
            sram_data = extract_sram_data(html_content)
            writer.writerow(sram_data)
    
    print("Data has been written to sram_data.csv")

if __name__ == "__main__":
    main()

