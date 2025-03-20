import os
from asyncio import timeout

import requests
from dotenv import load_dotenv

load_dotenv()

# Scrape function
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/shaunzlim0123/186b928ff3c050d3d8b14ccb767f17e0/raw/2a8415562b101698c04a60fbce693a54dc729099/harrison-chase-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params={
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
    }

    return data


if __name__ == "__main__":
    pass