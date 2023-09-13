def host_address(request):
    protocol = "https://" if request.is_secure() else "http://"
    return {"host_address": protocol + request.get_host()}
