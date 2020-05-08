import ipfshttpclient

def base():
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
    print("Klient ", client)

    res = client.add('test.txt')
    print("res ", res)

    print(client.cat(res['Hash']))


