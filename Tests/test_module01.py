import requests

base_url = "http://127.0.0.1:5000/api"
headers_test = {"Content-Type" : "application/json"}   

payload = {
    "name":"Waldo",
    "age":32,
    "sallary":"125000.00",
    "designation":"Something Else",
    "yow":"6"
}

headers_test = {"Content-Type" : "application/json"}   

def test_post_create():
    response =  requests.post(url = base_url + "/employee", headers=headers_test, json=payload)
    assert response.status_code == 201

def test_get():
    response =  requests.get(url = base_url + "/employee", headers=headers_test)
    assert response.status_code == 200

def test_get_one():
    base_url = "http://127.0.0.1:5000/api"

    headers_test = {"Content-Type" : "application/json"}    
    response =  requests.get(url = base_url + "/employee/1", headers=headers_test)
    assert response.status_code == 201

def test_post_update():
    headers_test = {"Content-Type" : "application/json"}    
    response =  requests.put(url = base_url + "/employee/1", headers=headers_test, json=payload)
    assert response.status_code == 200

def test_post_delete():
    headers_test = {"Content-Type" : "application/json"}    
    response =  requests.delete(url = base_url + "/employee/1", headers=headers_test)
    assert response.status_code == 200






