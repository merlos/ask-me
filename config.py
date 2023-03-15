# Ask me
#
# Configuration file
#
CONFIG={}

#
# Source folder for
#
CONFIG['texts_folder'] = './text/'


#
# File where embeddings are stored
#
CONFIG['embeddings_csv'] = './processed/embeddings.csv'

#
# This file contains the scrapped csv file that is used as knowledge base. It is the compilation of
# all the files in text/
# 
CONFIG['corpus_csv'] = './processed/corpus.csv'

#
# This file contains the scrapped csv file that is used as knowledge base. It is the compilation of
# all the files in text/
# 
CONFIG['tokenized_corpus_csv'] = './processed/.tokenized_corpus.csv'

#
# Max tokens
#
CONFIG['max_tokens'] = 500

#
# Time between calls to OpenAPI 
# In seconds (float)
#
CONFIG['idle_time'] = 6000/1000 

#
# Batch size
#
CONFIG['batch_size'] = 10


# Web App

CONFIG['log_answers'] = True
#
# Q&A Save
#
CONFIG['answers_log_file'] = '/home/answers.log'