users = {
    "user1": {
        "name": "Nick",
        "user_location": {
            "country": "United Kingdom",
            "state_province": "England",
            "city": "London"
        },
        "parents_location": {
            "country": "Canada",
            "state_province": "British Columbia",
            "city": "Vancouver"
        },
        "parents_have_will": True,
        "is_executor": False,
        "estate": {
            "total_value": 1000000,  # $1M
            "assets": {
                "primary_residence": {
                    "value": 700000,
                    "purchase_date": "2010-01-01",
                    "purchase_price": 500000
                },
                "investments": {
                    "value": 300000,
                    "type": "stocks",
                    "purchase_date": "2015-01-01",
                    "purchase_price": 200000
                }
            },
            "liabilities": {
                "mortgage": 200000
            }
        }
    },
    "user2": {
        "name": "Allison",
        "user_location": {
            "country": "Canada",
            "state_province": "Ontario",
            "city": "Toronto"
        },
        "parents_location": {
            "country": "Canada",
            "state_province": "Ontario",
            "city": "Hamilton"
        },
        "parents_have_will": True,
        "is_executor": True,
        "estate": {
            "total_value": 1500000,  # $1.5M
            "assets": {
                "primary_residence": {
                    "value": 1000000,
                    "purchase_date": "2005-01-01",
                    "purchase_price": 600000
                },
                "investments": {
                    "value": 500000,
                    "type": "stocks",
                    "purchase_date": "2010-01-01",
                    "purchase_price": 300000
                }
            },
            "liabilities": {
                "mortgage": 300000
            }
        }
    },
    "user3": {
        "name": "Cole",
        "user_location": {
            "country": "United States",
            "state_province": "Massachusetts",
            "city": "Boston"
        },
        "parents_location": {
            "country": "United States",
            "state_province": "Massachusetts",
            "city": "Boston"
        },
        "parents_have_will": False,
        "is_executor": True
    },
    "user4": {
        "name": "Emma",
        "user_location": {
            "country": "Australia",
            "state_province": "New South Wales",
            "city": "Sydney"
        },
        "parents_location": {
            "country": "United States",
            "state_province": "Florida",
            "city": "Miami"
        },
        "parents_have_will": True,
        "is_executor": False
    },
    "user5": {
        "name": "David",
        "user_location": {
            "country": "Canada",
            "state_province": "Ontario",
            "city": "Toronto"
        },
        "parents_location": {
            "country": "United States",
            "state_province": "Washington",
            "city": "Seattle"
        },
        "parents_have_will": False,
        "is_executor": True
    }
}

# To test the data structure, you can print it
if __name__ == "__main__":
    import json
    print(json.dumps(users, indent=4))

