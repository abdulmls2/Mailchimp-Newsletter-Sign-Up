# Import necessary modules
from django.shortcuts import render
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

# Your Mailchimp API key and list ID
api_key = ""  # enter your api_key from Mailchimp
list_id = "" # enter the given list_id from Mailchimp


# Function to subscribe a user to the newsletter
def subscribe(request):
    if request.method == "POST":
        # Getting user's input from the form
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']

        # Initializing the Mailchimp user with API key
        mailchimpClient = Client()
        mailchimpClient.set_config({
            "api_key": api_key,
        })

        # Create a dictionary with user information for subscription
        userInfo = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": firstName,
                "LNAME": lastName
            }
        }

        try:
            # Adding a user to the Mailchimp audience list
            mailchimpClient.lists.add_list_member(list_id, userInfo)

            # Rendering a success page if subscription is successful
            return render(request, "app/success.html")
        except ApiClientError as error:
            # Handling API client errors and rendering an error page
            print(error.text)
            return render(request, "app/error.html")

    # Render the home page
    return render(request, "app/home.html")
