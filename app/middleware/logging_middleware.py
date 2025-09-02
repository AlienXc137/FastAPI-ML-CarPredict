import logging
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware): # Custom middleware for logging requests and responses
    async def dispatch(self, request, call_next): # Intercept each request
        logging.info(f'Request: {request.method} {request.url}') # Log request method and URL
        response = await call_next(request) # Process the request
        logging.info(f'Response: {response.status_code}') # Log response status code
        return response 
    
# The dispatch function in the LoggingMiddleware class is an asynchronous method that intercepts every HTTP request processed by your FastAPI app.
# It logs the incoming request's HTTP method (e.g., GET, POST) and URL using Python's logging module.
# It then calls call_next(request) to pass the request to the next middleware or route handler, and waits for the response.
# After receiving the response, it logs the response's status code (e.g., 200, 404).
# Finally, it returns the response to the client.
# This function helps you track all incoming requests and outgoing responses for debugging or monitoring purposes.