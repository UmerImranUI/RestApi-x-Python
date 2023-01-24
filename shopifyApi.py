import requests
import creds
import time

def create_session():
    s=requests.Session()
    s.headers.update({
        "X-Shopify-Access-Token": creds.token,
        "Content-Type": "application/json"
    })

    def api_calls(r, *args, **kwargs):
        calls_left=r.headers['X-Shopify-Shop-Api-Call-Limit'].split("/")
        print(calls_left[0])
        if int(calls_left[0]) == 39:
            print('limit close, sleeping')
            time.sleep(5)

    s.hooks["response"] = api_calls
    return s

def main():
    sess=create_session()
    # for managing limit
    # for i in range(1,100):
    #     resp=sess.get(creds.url + "/admin/api/2021-07/products.json?limit=10")

    resp=sess.get(creds.url + "/admin/api/2021-07/products.json?limit=10")
    print(resp.json())

    # for links
    # print(resp.links['next']['url'])


if __name__ == '__main__':
    main()