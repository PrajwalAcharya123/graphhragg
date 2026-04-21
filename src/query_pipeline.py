# src/query_pipeline.py
from query_to_cypher import question_to_cypher
from neo4j_handler import Neo4jHandler
from answer_generator import generate_answer

def ask_question(question):

    print(f"\n❓ Question: {question}")

    # Step 1: Convert to Cypher
    cypher = question_to_cypher(question)
    print(f"\n🧠 Generated Cypher:\n{cypher}")

    # Step 2: Run query
    neo4j = Neo4jHandler()
    result = neo4j.run_query(cypher)
    neo4j.close()

    print(f"\n📊 DB Result:\n{result}")

    # Step 3: Generate answer
    answer = generate_answer(question, result)

    print(f"\n✅ Answer:\n{answer}")

    return answer