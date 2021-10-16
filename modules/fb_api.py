import requests
import pprint


fb_interest_url = "https://graph.facebook.com/v12.0/search?type=adinterest&q={}&limit={}&access_token={}"
fb_suggest_url = "https://graph.facebook.com/v12.0/search?type=adinterestsuggestion&interest_list=['{}']&limit={}&access_token={}"


class FbRequest:
    """
    This class is used for sending requests to the FB API and deserializing the json response that it receives
    """

    @classmethod
    def get_by_interest(cls, keyword, limit, access_token):
        url = fb_interest_url.format(keyword, limit, access_token)
        response = requests.get(url)
        return response.json()

    @classmethod
    def get_by_suggest(cls,keyword,limit,access_token):
        keyword = keyword.capitalize()
        url = fb_suggest_url.format(keyword, limit, access_token)
        response = requests.get(url)
        return response.json()


if __name__ == "__main__":

    # Used for testing in development

    res = FbRequest.get_by_interest("juice", 67, "")
    # res = FbRequest.get_by_suggest("loan",94,"")
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(res)
    if "data" in res.keys():
        # for n in res["data"]:
        #     print(n["name"],n["audience_size"])
        pp.pprint(res["data"])
    elif "error" in res.keys():
        print("error")