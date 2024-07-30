#Entry point for starting the Flask development server.

# Import the create_app function from the app package
from app import create_app

# Create an instance of the Flask application using the create_app function
app = create_app()

if __name__ == '__main__':
    # Run the Flask development server in debug mode
    app.run(debug=True)

