# run.py
from src.app import create_app

# WSGI application expected by IIS/wfastcgi:
application = create_app()

if __name__ == "__main__":
    # apenas para teste local
    application.run(host="0.0.0.0", port=5000, debug=True)
