
import requests

CONFIDENCE_THRESHOLD = 0.90


def get_incident(instance, sys_id, user, pwd):
    url = f"https://{instance}/api/now/table/incident/{sys_id}"
    return requests.get(url, auth=(user, pwd)).json()


def resolve_incident(instance, sys_id, notes, user, pwd):
    url = f"https://{instance}/api/now/table/incident/{sys_id}"
    payload = {
        "state": "6",
        "close_notes": notes
    }
    return requests.patch(url, json=payload, auth=(user, pwd))


if __name__ == '__main__':
    print('Sample ServiceNow Resolution Bot')
