# ⚖️ CaseBrief Backend: Core API Server (Node.js)

This is the **core backend service** for the CaseBrief application.
Built with **Node.js** and **Express**, it provides a robust REST API to handle **user authentication**, **data management**, and **core application logic**.

---

## ✨ Core Responsibilities

* **User Authentication**
  Securely manages user registration, login, and sessions using **JWT (JSON Web Tokens)**.

* **Database Management**
  Handles CRUD operations for:

  * User Accounts
  * Uploaded Documents
  * Chat Histories
  * Notebook Entries

* **Web Scraping**
  Scrapes legal case information from **public sources** like *indiankanoon.org*.

* **API Gateway**
  Acts as the **primary interface** for the frontend, ensuring data is served efficiently and securely.

---

## 🚀 Technology Stack

* **Framework:** Express.js
* **Database:** MongoDB with Mongoose
* **Authentication:** JSON Web Tokens (JWT)
* **Web Scraping:** Axios & Cheerio

---

## ⚙️ Getting Started

### 🔑 Prerequisites

* [Node.js](https://nodejs.org/) & npm installed
* A running **MongoDB instance** (local or cloud, e.g., MongoDB Atlas)

---

### 📥 Installation & Setup

1. **Navigate to the Backend Directory**

   ```bash
   cd sihbackend/NodejsBackend
   ```

2. **Install Dependencies**

   ```bash
   npm install
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the root of the project:

   ```env
   # MongoDB connection string
   MONGO_URI=your_mongodb_connection_string

   # Secret key for signing JWT tokens
   JWT_SECRET=your_super_secret_jwt_key

   # Port for the server
   PORT=4000
   ```

---

### ▶️ Running the Server

Start the Node.js server:

```bash
npm start
```

The backend will now be running at:
👉 [http://localhost:4000](http://localhost:4000)

If successful, you’ll see a **confirmation message** in your terminal indicating a successful MongoDB connection and server startup.

---

## 📌 Notes

* Ensure MongoDB is running before starting the backend.
* The **frontend** and **Django AI backend** should be configured to connect to this API server.
* Keep your `.env` file **private** and never commit secrets to GitHub.

---

## 📜 License

This project is licensed under the **MIT License**.
