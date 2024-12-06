from functools import wraps
from flask import after_this_request

def cache_response(max_age=3600, s_maxage=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            @after_this_request
            def set_cache_header(response):
                response.cache_control.public = True
                response.cache_control.max_age = max_age
                response.cache_control.s_maxage = s_maxage
                return response
            
            # Call the original function to generate the response
            response = func(*args, **kwargs)
            return response
        return wrapper
    return decorator
