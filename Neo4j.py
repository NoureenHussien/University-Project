from neo4j import GraphDatabase
import pandas as pd

# Neo4j connection details (modify these with your credentials)
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"  # Change to your actual password

def store_graph_in_neo4j(g, course_students):
    """Store the course conflict graph in Neo4j"""
    
    # Connect to Neo4j
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    
    # Clear existing data
    def clear_db(tx):
        tx.run("MATCH (n) DETACH DELETE n")
    
    # Add courses and relationships
    def add_courses_and_relationships(tx):
        # Create course nodes
        for course in g.nodes():
            tx.run("""
                MERGE (c:Course {code: $code})
                SET c.students = $students,
                    c.name = $name
            """, 
            code=course,
            students=g.nodes[course]['size'],
            name=course_names.get(course, ""))
        
        # Create conflict relationships
        for u, v, data in g.edges(data=True):
            tx.run("""
                MATCH (c1:Course {code: $course1})
                MATCH (c2:Course {code: $course2})
                MERGE (c1)-[r:CONFLICT]->(c2)
                SET r.weight = $weight
            """,
            course1=u,
            course2=v,
            weight=data['weight'])
    
    with driver.session() as session:
        print("Clearing existing data...")
        session.write_transaction(clear_db)
        
        print("Storing courses and relationships...")
        session.write_transaction(add_courses_and_relationships)
        
        print(f"Successfully stored {g.number_of_nodes()} courses and {g.number_of_edges()} conflicts in Neo4j")
    
    driver.close()

# Get course names (from your existing code)
course_names = {}
for _, row in combined_df.iterrows():
    code = str(row['رمز المقرر']).strip()
    name = str(row['اسم المقرر']).strip()
    if code and name:
        course_names[code] = name

# Store your graph in Neo4j
store_graph_in_neo4j(g, course_students)