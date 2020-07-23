import csv
import requests
import pytest


def read_test_data_from_csv():
    test_data = []
    with open('gpv.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            test_data.append(row)
    return test_data


@pytest.mark.parametrize('path', read_test_data_from_csv())
def test_gpv(path):
    base_url = 'http://10.211.15.228:30181'
    headers = {'accept': 'application/json', 'Content-type': 'application/json'}
    auth = ('admin', 'admin')
    endpoint = f'{base_url}{path[0]}'
    print(f'Endpoint: {endpoint}')
    # response = requests.get(endpoint, auth=auth, headers=headers)
    # assert response.status_code == 200

