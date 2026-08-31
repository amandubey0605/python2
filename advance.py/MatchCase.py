'''it is introduced in python 3.10 which is  similar to the switch statement found in 
other programing languages.
Syntex-'''

def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "Internal server Error"
        case _:
            return "Unknown status"

print(http_status(200))  #output : OK
print(http_status(404))  #output : not found
print(http_status(500))  #output : Internal server Error
print(http_status(403))  #output : Unknown status
