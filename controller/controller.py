from model.model import Model
from modules.fb_api import FbRequest


class AudienceManager:
    """
     Higher level class used for managing the App functionalities provided trough the modules in the modules folder:
     - Sending GET requests to the Facebook API to retrieve available ad targeting interests based on the query parameters
     - Storing and retrieving the access token used for calling the API in sqlite DataBase
    """

    @classmethod
    def get_interest(cls,keyword, limit):
        access_token = Model.get_token()
        if access_token:
            res = FbRequest.get_by_interest(keyword, limit, access_token[1])
            if "data" in res.keys():
                if len(res["data"]) >0:
                    audiences = "AUDIENCE  /SIZE/ \n\n"
                    audiences += f"Results found: {len(res['data'])}\n\n"
                    for audience in res["data"]:
                        audiences += f"{audience['name']}      /{audience['audience_size_lower_bound']} users/\n"
                    return audiences
                else:
                    return "No Audiences Found"
            elif "error" in res.keys():
                message = res["error"]["message"]
                return message
        else:
            return None

    @classmethod
    def get_suggestion(cls, keyword, limit):
        access_token = Model.get_token()
        if access_token:
            res = FbRequest.get_by_suggest(keyword, limit, access_token[1])
            if "data" in res.keys():
                if len(res["data"]) > 0:
                    audiences = "AUDIENCE / SIZE \n\n"
                    audiences += f"Suggestions found: {len(res['data'])}\n\n"
                    for audience in res["data"]:
                        audiences += f"{audience['name']}      /{audience['audience_size_lower_bound']} users/\n"
                    return audiences
                else:
                    return "No Suggestions Found"
            elif "error" in res.keys():
                message = res["error"]["message"]
                return message
        else:
            return None


if __name__ == "__main__":

    # Used for testing in development

    res = AudienceManager.get_suggestion("golf", 67,"")
    print(res)