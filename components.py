import requests
from prettytable import PrettyTable

def get_latest_version(repo_name):
    url = f"https://api.github.com/repos/{repo_name}/releases/latest"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        latest_version = data['tag_name']
        return latest_version

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {repo_name} version: {e}")
        return None

if __name__ == "__main__":
    repositories = {
        "cAdvisor": "google/cadvisor",
        "Prometheus": "prometheus/prometheus",
        "Node Exporter": "prometheus/node_exporter",
        "Nginx Exporter": "nginxinc/nginx-prometheus-exporter",
        "Grafana": "grafana/grafana",
        "Prometheus Kafka Adapter": "Telefonica/prometheus-kafka-adapter"
    }

    table = PrettyTable()
    table.field_names = ["Repository", "Latest Version"]

    for name, repo in repositories.items():
        latest_version = get_latest_version(repo)

        if latest_version:
            table.add_row([name, latest_version])
        else:
            table.add_row([name, "Failed to fetch"])

    print(table)
