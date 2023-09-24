# Define a list of available functions with their descriptions
functions = [
    {
        "name": "total_donations",
        "description": "Get the total donations",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "donations_list",
        "description": "Get the list of donations for a month and year if given",
        "parameters": {
            "type": "object",
            "properties": {
                "month": {
                    "type": "string",
                    "description": "Month of the donations",
                    "enum": [
                        "1",
                        "2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                        "10",
                        "11",
                        "12",
                    ],
                },
                "year": {
                    "type": "string",
                    "description": "Year of the donations",
                },
            },
            "required": [],
        },
    }
]