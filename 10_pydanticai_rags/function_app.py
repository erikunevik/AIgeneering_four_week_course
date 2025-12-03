import azure.functions as func
import api


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="{*route}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

