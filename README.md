# AWS IAM User Management with Neo4j

A Python application that fetches AWS IAM users and stores them in a Neo4j graph database.

## Using Docker Compose file 

### Commands to Execute
- Build and Start the Containers
- Navigate to the project directory and execute:


```
docker-compose up --build
```
- This command builds and starts the services defined in docker-compose.yml.
1. The neo4j container initializes the Neo4j database.
2. The app container fetches AWS IAM users and injects them into Neo4j.
3. The report container generates a report of injected users.

#### Note: If you wish to run the containers in detached mode, append ```-d:```
![alt text](<app/images/Screenshot 2024-12-07 144937.png>)
![alt text](<app/images/Screenshot 2024-12-07 145032.png>)

bash
Copy code
docker-compose up --build -d
Check the Logs for AWS IAM Fetcher
View the logs of the app container to verify user injection:

bash
Copy code
docker logs aws-iam-fetcher


##Using without Docker-Compose file 
## Prerequisites

- Docker
- Python 3.x
- AWS credentials configured
- Neo4j database

## Installation

1. Clone the repository
2. Install dependencies:
   ```pip install -r requirements.txt```  

## Configuration

1. Create a `.env` file with the following credentials:   ```env
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your_password   ```

## Setting Up Neo4j

1. Start Neo4j using Docker:   ```bash
   docker run -d --name neo4j \
       -p 7474:7474 -p 7687:7687 \
       -e NEO4J_AUTH=neo4j/your_password \
       neo4j   ```

2. Access Neo4j Browser at `http://localhost:7474`

## Usage

1. Run the application:   ```bash
   python main.py   ```

   ![alt text](<images/Screenshot 2024-12-07 110252.png>)

   - Neo4j Database

   ![alt text](<images/Screenshot 2024-12-07 110330.png>)

   - AWS IAM Users
   ![alt text](<images/Screenshot 2024-12-07 111847.png>)


The application will:
- Fetch users from AWS IAM
- Create nodes in Neo4j for each user
- Establish relationships between users and their permissions

## Project Structure

- `main.py`: Entry point of the application
- `aws_user_fetcher.py`: Handles AWS IAM user retrieval
- `neo4j_user_ingestor.py`: Manages Neo4j database operations
- `utils.py`: Utility functions
- `requirements.txt`: Project dependencies

## Troubleshooting

If you encounter connection issues:
1. Verify Neo4j is running: `docker ps`
2. Check correct ports (7474 for HTTP, 7687 for Bolt)
3. Ensure credentials in `.env` match Neo4j configuration

