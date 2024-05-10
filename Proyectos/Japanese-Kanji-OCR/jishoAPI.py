import requests

url = "https://jisho.org/api/v1/search/words?keyword="
s = requests.Session()



def get_word_kanji_reading(kanji):
    response = s.get("https://jisho.org/api/v1/search/words?keyword=" + kanji)
    json = response.json().get("data")[0]
    # print(json)
    meanings = json.get("senses")[0].get("english_definitions") # List
    # print(meanings)
    words = json.get("japanese") # Returns a list of dictionaries with word and reading keywords
    result = {"readings":words}
    result["meanings"] = meanings
    return result # Returns a dictionary with readings and the meanings

if __name__ == "__main__":
    print(get_word_kanji_reading("可也"))


