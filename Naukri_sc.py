import requests
import pandas as pd

url = 'https://www.naukri.com/jobapi/v3/search'

headers = {
    'Accept': 'application/json',
    'Appid': '109',
    'Authorization': 'Bearer eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTQ1MTY1Mjc3LCJzdWIiOiIxNTQxNjE2NjEiLCJ1ZF91c2VybmFtZSI6ImFzdW5pbHJhdGhvZDMwOTJAZ21haWwuY29tIiwidWRfaXNFbWFpbCI6dHJ1ZSwiaXNzIjoiSW5mb0VkZ2UgSW5kaWEgUHZ0LiBMdGQuIiwidXNlckFnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiaXBBZHJlc3MiOiIyMjMuMTc4LjIwOS4xMjQiLCJ1ZF9pc1RlY2hPcHNMb2dpbiI6ZmFsc2UsInVzZXJJZCI6MTU0MTYxNjYxLCJzdWJVc2VyVHlwZSI6ImpvYnNlZWtlciIsInVzZXJTdGF0ZSI6IkFVVEhFTlRJQ0FURUQiLCJ1ZF9lbWFpbFZlcmlmaWVkIjp0cnVlLCJ1ZF9pc1BhaWRDbGllbnQiOmZhbHNlLCJ1c2VyVHlwZSI6ImpvYnNlZWtlciIsInNlc3Npb25TdGF0VGltZSI6IjIwMjMtMTItMTRUMTA6MDY6MTQiLCJ1ZF9lbWFpbCI6ImFzdW5pbHJhdGhvZDMwOTJAZ21haWwuY29tIiwidXNlclJvbGUiOiJ1c2VyIiwiZXhwIjoxNzA4OTcxNTUwLCJ0b2tlblR5cGUiOiJhY2Nlc3NUb2tlbiIsImlhdCI6MTcwODk2Nzk1MCwianRpIjoiNmZmMjMzMjZhNTU2NGVkZThlMzQyN2RkYjRkNThmMDMifQ.nR6UpBsoCUezY76JEw3HzoDi0d1v9ldpXCJEexz0fIgaQvmudfonXNowjAf6n-Xjp5S0EUUmCZwStM6udrY8BQWjKXqQVcmQzKhYwnhcxwBpDRldgMd810J7RLSglO-OKWlzANQgvNyZUet_tKliVmfQ82l3K-9toD2zEuUNYcPDsIhCxj4FvNBeV8kfexMoIUzthbZ0X-LGvxFaJf4ANNx5E02f_nn5mWAgm10OJ3OLqoFYvPqocc0DyvNs--au0-G0pV07Z5OQVeiYj0kFytgoCr4VFDJATJV_zjje9yKeMJ6rKN_-Ghgsn_BP3fBMvQh9O_obYZOCEWWU8zieWQ',
    'Clientid': 'd3skt0p',
    'Content-Type': 'application/json',
    'Dnt': '1',
    'Gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
    'Referer': 'https://www.naukri.com/web-scraping-jobs?k=web%20scraping&nignbevent_src=jobsearchDeskGNB',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Systemid': 'Naukri',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

total_results = 40000
results_per_page = 20
total_pages = min((total_results + results_per_page - 1) // results_per_page, 20)  # Limit to 20 pages

job_listings = []

for page_no in range(1, total_pages + 1):
    params = {
        'noOfResults': 20,
        'urlType': 'search_by_keyword',
        'searchType': 'adv',
        'keyword': 'web scraping',
        'pageNo': page_no,
        'k': 'web scraping',
        'nignbevent_src': 'jobsearchDeskGNB',
        'src': 'jobsearchDesk',
        'latLong': '18.5663488_73.8525184'
    }
    
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        job_listings.extend(data.get('jobDetails', []))
        print(f"Processed page {page_no}/{total_pages}")
    else:
        print(f"Failed to fetch data from page {page_no}:", response.status_code)

# Create a DataFrame from job_listings
df = pd.DataFrame(job_listings)

# Save DataFrame to CSV file
df.to_csv('job_listings.csv', index=False)

print("DataFrame saved to 'job_listings.csv'")
