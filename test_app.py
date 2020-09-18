import json

def test_api_post_form(api):
    # Stub out response data, turn into json using json.dumps
    mock_data = json.dumps({ 'form' : 
    {
        'customer': 'YassineBoo',
        'dealer': 'Ibrahim',
        'rating': 8,
        'comments': 'Love my new car, Ibrahim was great.',
        'submitted': False
    }})
    mock_headers = {'Content-Type': 'application/json'}
    
    res = api.post('/submit', data=mock_data, headers=mock_headers)
    assert res.json['submitted'] == 'Yes'