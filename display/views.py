import requests
from django.shortcuts import render
from display.forms import DecisionMachineForm
import json


def get_template_dashboard(request):
    """Render view of form with their respective data"""

    form = DecisionMachineForm(request.POST)

    data_form = dict(request.POST)
    customer_range = None

    try:
        data_json = {
            "salary": data_form["salary"][0],
            "expenses": data_form["expenses"][0]
        }

        headers = {"Content-Type": "application/json"}
        url = "http://127.0.0.1:5000/calculate"
        response = requests.post(url, headers=headers, data=json.dumps(data_json))
        customer_range = response.json()
    except (KeyError):
        pass
    context = {
        "form": form,
        "data": customer_range
    }
    return render(request, "index.html", context=context)
