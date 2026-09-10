import requests

url = "https://api.luma.com/event/register"

n = 6
x = '''
data = {"name":"John Doe",
            "first_name":"",
            "last_name":"",
            "email":f"lolnicetryezjohn{n}@gmail.com",
            "event_api_id":"evt-BRY5KUn2LY8kScI",
            "registration_answers":[{"label":"What is your LinkedIn profile?",
                                      "question_id":"50n83n2d",
                                      "value":f"https://www.linkedin.com/in/example{n}",
                                      "question_type":"linkedin"}],
                                      "phone_number":f"+91900000000{n}",
                                      "expected_amount_cents":0,
                                      "expected_amount_tax":0,
                                      "ticket_type_to_selection":{"evtticktyp-qrzW9HwxQDYtSw5":{"count":1,
                                                                                                    "amount":0}}}
'''

data = {"name":"John Doe",
            "first_name":"",
            "last_name":"",
            "email":"lolnicetryezjohn0@gmail.com",
            "event_api_id":"evt-BRY5KUn2LY8kScI",
            "for_waitlist":False,
            "payment_method":None,
            "payment_currency":None,
            "registration_answers":[{"label":"What is your LinkedIn profile?",
                                      "question_id":"50n83n2d",
                                      "value":"https://www.linkedin.com/in/example0",
                                      "question_type":"linkedin"}],
                                      "coupon_code":None,
                                      "token_gate_info":None,
                                      "eth_address_info":None,
                                      "phone_number":"+919000000000",
                                      "solana_address_info":None,
                                      "expected_amount_cents":0,
                                      "expected_amount_tax":0,
                                      "currency":None,
                                      "event_invite_api_id":None,
                                      "ticket_type_to_selection":{"evtticktyp-qrzW9HwxQDYtSw5":{"count":1,
                                                                                                    "amount":0}}}
response = requests.post(url, json=data)
print(response.status_code)
print(response.text)