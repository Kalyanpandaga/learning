

REQUEST_BODY_JSON = """
{
    "sort_by": "ASC",
    "filter": {
        "applied_status": "APPLIED"
    },
    "from_location": "string",
    "to_location": "string",
    "datetime": "string"
}
"""


RESPONSE_200_JSON = """
{
    "Requester_details": {
        "user_id": "string",
        "user_name": "string"
    },
    "from_location": "string",
    "to_location": "string",
    "start_date": "string",
    "end_date": "string",
    "assets_quantity": 1,
    "asset_type": "LAPTOP",
    "asset_sensitivity": "HIGHLY_SENSITIVE",
    "whom_to_deliver": "string",
    "applied_status": "APPLIED"
}
"""

