import requests


def get_news(question):
    API_KEY = '6a1af4c3bef59e466a12c511f33c2cb279979d1aa32cd67cb103f05b6318cfcb'
    url = f'https://serpapi.com/search.json?engine=google_news&q={question}&api_key={API_KEY}'  # Include API key in URL

    response = requests.get(url)

    data = response.json()
    articles = []  # Create an empty list to store articles

    for result in data['news_results']:
        articles.append({  # Add each article's info to the list
            'title': result['title'],
            'source_name': result['source']['name']
        })

    return articles  # Return the list of articles after processing all results


# Example usage with loop to print all articles
news = get_news('What is the latest news on COVID-19?')
