import requests

# Send a web request
def send_request(username, password, message, url):
    headers = {"username": username, "password": password}

    try:
        response = requests.post(url, headers=headers, data=message)
        if response.status_code == 200:
            return response.content
        else:
            return f"Request failed with status code {response.status_code}: {response.reason}"
    except Exception as error:
        return f"An error occurred: {error}"

# Read the username and password
def read_credentials(filename):
    try:
        with open("credentials.txt", "r") as file:
            data = file.readlines()
            return data
    except Exception as error:
        return f"An error occurred: {error}"   

# Main function
def main():
    # Get username and password    
    credentials = read_credentials("credentials.txt")

    # Parameters
    username = credentials[0].strip()
    password = credentials[1].strip()
    message = '{"text": "Hello, world!"}'
    url = "https://webhook.site/2fc46539-0f46-4d80-866c-0e54ca2713e5"

    # Call the function
    output = send_request(username, password, message, url)

    # Print the output of the request
    print(output)

if __name__ == "__main__":
    # Call the main function
    main()