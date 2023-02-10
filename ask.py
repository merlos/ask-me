import sys
from answers import df, answer_question

# Main ####

# At least more than one argument.
if len(sys.argv) == 1: 
    print("""
    Usage:
       python ask.py "question related with the knowledge base"

    Example:
       python ask.py "Who is Juan?"
        
    """)
    exit(1)

# The question is the second argument onwards concatenate it with spaces
question = " ".join(sys.argv[1:])
print(answer_question(df, question=question))

