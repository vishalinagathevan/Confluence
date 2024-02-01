import requests
from bs4 import BeautifulSoup

def get_confluence_page_html(space_key, page_title, username, api_token):
    # Replace 'YOUR_CONFLUENCE_INSTANCE_URL', 'YOUR_SPACE_KEY', 'YOUR_PAGE_TITLE', 'YOUR_USERNAME', and 'YOUR_API_TOKEN'
    # confluence_url = "https://your-confluence-instance-url"
    confluence_url = "https://vishalinagathevan.atlassian.net/wiki/home"
    api_url = f"{confluence_url}/rest/api/content"
    # https://vishalinagathevan.atlassian.net/wiki/rest/api/content/131199?expand=body.storage
    params = {
        'spaceKey': space_key,
        'title': page_title,
        'expand': 'body.view'
    }
    auth = (username, api_token)

    response = requests.get(api_url, params=params, auth=auth)
    print(f"response {response.text}")
    if response.status_code == 200:
        data = response.json()
        page_body = data.get('body', {}).get('view', {}).get('value', '')
        return page_body
    else:
        print(f"Failed to retrieve Confluence page. Status code: {response.status_code}")
        return None

def extract_table_data(html_content):
    # Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    
    if table:
        # Extract table data as a list of lists
        table_data = []
        for row in table.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
            table_data.append(row_data)
        return table_data
    else:
        print("No table found on the Confluence page.")
        return None

# Replace 'YOUR_SPACE_KEY', 'YOUR_PAGE_TITLE', 'YOUR_USERNAME', and 'YOUR_API_TOKEN'
space_key = "My first space"
page_title = "Application Table"
username = "VISHALI"
api_token = "ATATT3xFfGF0G41sSHD_tTUjTJJ1IsmIwgUaw0ZH-ZK1lVSu13gUY3Wz_Ojw60WAeoMsTYCOId-ZPqAOKmrIy_S02zZLy0EcSVZGauTP5BnfXvCP4ztsCosocb6l0AMamjls7Kruq39R_uC4ZkKKspvFANHOf-mn6jtnJsRuZPLCMq6c_eRMqa4=B3965E25"

html_content = get_confluence_page_html(space_key, page_title, username, api_token)
print(f"html_content {html_content}")
# if html_content:
#     table_data = extract_table_data(html_content)
    
#     if table_data:
#         print("Table Data:")
#         for row in table_data:
#             print(row)
