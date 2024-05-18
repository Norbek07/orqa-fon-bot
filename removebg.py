import requests

def remove_bg(FILE_NAME, color="white"):
    rasm = ''
    API_KEY = 'Y3Xhv4XqgNpZHKvFGWW2QeAp'

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': FILE_NAME,
            'size': 'auto',
            'bg_color': color
            #'bg_image_url':'image/url'
        },
        files = {
            #'_bg_image_file':open("bg.jpg","rb"),
        },
        headers={'X-Api-Key': API_KEY},
    )
    
    if response.status_code == requests.codes.ok:
        rasm = response.content
    else:
        print("Error:", response.status_code, response.text)
    return rasm
