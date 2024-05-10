import requests
import base64
import time
import os

API_DOCUMENTATION_URL = "https://developers.convertio.co/api/docs/"
API_KEY = "<Convertio API KEY>"
URL = "https://api.convertio.co/convert"
INPUT_FILE_PATH = "resources/test.png"


def image_to_base64(image_name=INPUT_FILE_PATH):
    """
    Converts from image to base64 to base64 string
    """
    with open(image_name, "rb") as image_file:
        st = base64.b64encode(image_file.read())
        return st.decode("utf-8")


def create_session():
    return requests.Session()


def start_conversion(ses, filename=INPUT_FILE_PATH):
    """
    Returns the Json response as well as the id to use it later
    Important: the base64 image has to be passed as string without the b''
    """
    filedata = str(image_to_base64(filename))

    # Creating the options and the data objects, see documentation
    options = {"ocr_enabled": True, "ocr_settings": {"langs": ["jpn"]}}
    data = {"apikey":API_KEY, "input":"base64", "filename":filename, "file": filedata, "outputformat":"txt", "options":options}

    # Posting the data and grabbing the json response and id
    response = ses.post(URL, json=data)
    json = response.json()
    id = json.get("data").get("id")

    # Printing results
    print("[ Convertion start JSON response ] -> ", json)
    print("[ Convertion ID ] -> ", id)
    return json, id


def download_file_from_url(fileinurl, fileout):
    """
    Download a file from an url, uses response.content
    """
    response = requests.get(fileinurl, allow_redirects=True)
    with open(fileout, "wb") as f:
        f.write(response.content)


def get_file_from_id(ses, id, output_file="response.txt"):
    """
    Having got the id, ask the API to give the status of our convertion
    Resulting on showing the completed file url in order to download it
    """
    res_url = URL + "/" + id + "/status"
    # res_url = "https://api.convertio.co/convert/"+ id +"/status"
    while True:
        """
        Checks the status of the convertion request until it goes to step finish
        Then picks up the output url file 
        """
        response = ses.get(res_url)
        json = response.json()
        print("Conv JSON: ", json)
        if json.get("status") == "ok" and json.get("data").get("step") == "finish":
            break
        time.sleep(4)
    file_url = json.get("data").get("output").get("url")
    print("FILE URL: ", file_url)
    download_file_from_url(file_url, output_file)
    return json


def get_file_content(text_file):
    with open(text_file, "rt", encoding="utf-8") as f:
        final_text = f.read()
    # if os.path.exists(text_file):
    #     os.remove(text_file)
    return final_text


def create_file_with_kanji(filename=INPUT_FILE_PATH, output_file="response.txt"):
    ses = create_session()
    conv_json, id = start_conversion(ses, filename)
    last_json = get_file_from_id(ses, id, output_file)


def get_kanji(filename=INPUT_FILE_PATH, output_file="temp/response.txt"):
    create_file_with_kanji(filename, output_file)
    result = get_file_content(output_file)
    return result


def main():
    t = get_kanji(INPUT_FILE_PATH)
    print(t)

if __name__ == "__main__":
    main()
    
