from neo4j import GraphDatabase

class Neo4jUserIngestor:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def ingest_user(self, username):
        
        with self.driver.session() as session:
            session.run(
                "MERGE (u:User {name: $name})",
                name=username,
            )

    def close(self):
       
        self.driver.close()
