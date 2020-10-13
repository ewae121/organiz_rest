import connexion
from flask_cors import CORS

# Create the application instance
app = connexion.App(__name__, specification_dir='../swaggers')

app.add_api("swagger.yml")
CORS(app.app)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

