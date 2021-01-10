import django
from django.http import JsonResponse
import os
import joblib
import json
import pandas as pd
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()

def prediction(request) -> JsonResponse:
    response = {"status" : "400"}

    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError as e:
            response["error"] = f"Bad request : {e}"
        else:
            needed_keys = ["duration", "codec", "width", "height", "bitrate", "framerate",
                        "i", "p", "b", "frames", "i_size", "p_size", "b_size", "size",
                        "o_codec", "o_bitrate", "o_framerate", "o_width", "o_height", "umem"]
            codec = ["flv", "h264", "mpeg4", "vp8"]
            if sum([i in body for i in needed_keys]) == len(needed_keys):
                data = pd.DataFrame.from_dict(body)

                if data["codec"].dtypes == object:
                    data["codec"] = [codec.index(data["codec"].iloc[i]) for i in range(len(data["codec"]))]
                if data["o_codec"].dtypes == object:
                    data["o_codec"] = [codec.index(data["o_codec"].iloc[i]) for i in range(len(data["o_codec"]))]

                model = joblib.load("./api/model.sav")
                prediction = model.predict(data)
                response = {"status": "200", "result" : str(prediction)}
            else:
                response = {"status" : "401",
                 "error": f"missing key ! I need that in the body of the request : \n{needed_keys}"}
    else:
        response["error"] = "GET request, POST request with a body needed"

    return JsonResponse(response, safe=False)



