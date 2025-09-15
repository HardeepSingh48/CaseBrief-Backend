CaseBrief Backend: Core API Server (Node.js)
This is the core backend service for the CaseBrief application. Built with Node.js and Express, it provides a robust REST API to handle user authentication, data management, and core application logic.

✨ Core Responsibilities
User Authentication: Securely manages user registration, login, and session management using JSON Web Tokens (JWT).

Database Management: Performs all CRUD (Create, Read, Update, Delete) operations for:

User Accounts

Uploaded Documents

Chat Histories

Notebook Entries

Web Scraping: Includes a service to scrape legal case information from public sources like indiankanoon.org.

API Gateway: Acts as the primary interface for the frontend application, ensuring data is handled efficiently and securely.

🚀 Technology Stack
Framework: Express.js

Database: MongoDB with Mongoose

Authentication: JSON Web Tokens (JWT)

Web Scraping: Axios & Cheerio

⚙️ Getting Started
Prerequisites
Node.js and npm

A running MongoDB instance (either local or on a cloud service like MongoDB Atlas).

Installation & Setup
Navigate to the Directory:

cd sihbackend/NodejsBackend

Install Dependencies:

npm install

Configure Environment Variables:
Create a .env file in the root of the NodejsBackend directory. This is crucial for security and configuration.

# Your MongoDB connection string
MONGO_URI=your_mongodb_connection_string

# A strong, secret key for signing JWT tokens
JWT_SECRET=your_super_secret_jwt_key

# The port for the server to run on
PORT=4000

Running the Server
Once the dependencies are installed and the environment variables are configured, you can start the server.

npm start

The server will connect to your MongoDB database and start listening for requests, typically on http://localhost:4000. You should see a confirmation message in your terminal.