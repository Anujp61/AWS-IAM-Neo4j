from aws_user_fetcher import AWSUserFetcher
from neo4j_user_ingestor import Neo4jUserIngestor
from utils import load_env

def main():
    # Load environment variables
    config = load_env()

    # Fetch users from AWS IAM
    aws_fetcher = AWSUserFetcher(
        access_key=config["aws_access_key"],
        secret_key=config["aws_secret_key"],
        region=config["aws_region"],
    )
    users = aws_fetcher.fetch_users()
    print(f"Fetched {len(users)} users from AWS IAM.")

    # Ingest users into Neo4j
    neo4j_ingestor = Neo4jUserIngestor(
        uri=config["neo4j_uri"],
        username=config["neo4j_username"],
        password=config["neo4j_password"],
    )

    for user in users:
        neo4j_ingestor.ingest_user(user)
        print(f"Ingested user: {user}")

    neo4j_ingestor.close()
    print("All users have been successfully ingested into Neo4j.")

if __name__ == "__main__":
    main()
