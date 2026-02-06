import requests
 
DATAHUB_GQL_ENDPOINT = "http://datahub-gms:8080/graphql"
 
HEADERS = {
    "Content-Type": "application/json"
}
 
SEARCH_QUERY = """
{
  search(input: {
    type: DATASET,
    query: "*",
    start: 0,
    count: 100
  }) {
    searchResults {
      entity {
        urn
      }
    }
  }
}
"""
 
def main():
    print("Starting DataHub governance job...")
 
    try:
        response = requests.post(
            DATAHUB_GQL_ENDPOINT,
            json={"query": SEARCH_QUERY},
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
    except Exception as e:
        print("DataHub API not reachable:", e)
        return
 
    datasets = response.json()["data"]["search"]["searchResults"]
 
    for d in datasets:
        urn = d["entity"]["urn"]
        print(f"Found dataset: {urn}")
        # Owner check and tag mutation would go here
 
if __name__ == "__main__":
    main()
