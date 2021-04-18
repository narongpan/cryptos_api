def make_response(entity: str, input):
    response = {}

    if input == None:
        response["error"] = {"message": "Not found."}
    else:
        data = {}

        if type(input) is list:
            data["count"] = len(input)

        data[entity] = input
        response["data"] = data

    return response
