def http_status(status):
    match status:
        case 'pizza':
            return "OK"
        case 'momo':
            return "Not Found"
        case 'chowmin':
            return "Internal Server Error"
        case _:
            return "Unknown status"
        
print(http_status('momo'))
