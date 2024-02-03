from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class ReqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        self.send_response(200)
        self.send_header("Content-Type", params.get('accept')[0]) # Noncompliant
        self.end_headers()
        self.wfile.write(bytes("Hello World!", "utf-8"))

class Too_Much_Access:
    from aws_cdk.aws_iam import Effect, PolicyDocument, PolicyStatement

    PolicyDocument(
        statements=[
            PolicyStatement(
                effect=Effect.ALLOW,
                actions="iam:CreatePolicyVersion",
                resources=["*"] # Sensitive
            )
        ]
    )

class Hard_Coding:
    username = 'admin'
    password = 'admin' # Sensitive
    usernamePassword = 'user=admin&password=admin' # Sensitive

class Weak_Hashing:
    import hashlib
    m = hashlib.md5() 

class SQL_Injection:
    from flask import request, render_template_string, Flask
    app = Flask(__name__)
    @app.route('/example')

    def example():
        username = request.args.get('username')
        template = f"<p>Hello {username}</p>"
        return render_template_string(template) 

class Bad_Stack_Trace:
    from flask import Flask, render_template
    import traceback
    app = Flask(__name__)

    @app.errorhandler(500)
    def internal_server_error(error):
        error_message = traceback.format_stack()
        return render_template('error.html', error_message=error_message), 500