import requests
import threading

def send_request(wallet_address):
    print(f"Processing wallet: {wallet_address}")
    headers = {
        # your headers here
    }
    data = f'------WebKitFormBoundary2AcnC7JOYcamR1S0\r\nContent-Disposition: form-data; name="wallet"\r\n\r\n{wallet_address}\r\n------WebKitFormBoundary2AcnC7JOYcamR1S0--\r\n'
    response = requests.post('https://nudledudle.tech/api/v1/register', headers=headers, data=data)
    # Handle the response here

# Read wallet addresses from file
wallet_addresses = []
with open('public.txt', 'r') as file:
    wallet_addresses = [line.strip() for line in file]

# Creating and starting threads
threads = []
for wallet_address in wallet_addresses:
    thread = threading.Thread(target=send_request, args=(wallet_address,))
    threads.append(thread)
    thread.start()

    # Optional: To avoid overwhelming the server, you can limit the number of concurrent threads
    if len(threads) >= 20:  # Adjust this number based on your requirement
        for t in threads:
            t.join()
        threads = []

# Wait for any remaining threads to finish
for thread in threads:
    thread.join()
