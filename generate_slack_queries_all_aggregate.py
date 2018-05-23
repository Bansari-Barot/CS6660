from generate_slack import *
from random import choice, random, randint
from random import expovariate, normalvariate, choice, randint, random, shuffle

# to get first "page" of results
FIND_LIMIT = 5
REVIEW_PROB = 0.5
NOAVG_PROB = 0.5

def gen_status_query(key,value):
    '''
    Generate query to get for particular status all users, their email ids and number of workspaces, channels, apps that user is using
    '''
    query_file.write('''
result = db.slack.aggregate([
 { $project: {
   uname:1,
   email :1,
   status:1,
   _id:0,
   total_in_workspaces: { $size: "$workspaces"},
   total_in_channels : { $size: "$channels"},
 }},
 { $match: {status:'''
			+ value +
            '''}},
 { $limit:
 ''' + str(FIND_LIMIT) + '''}
 ]);
print('The list of all the users and count of their accessible workspaces and channels of slack whose status is '''+value+''':');

while ( result.hasNext() ) {

   printjson( result.next() );

}
''')

# Wrap some text with the chosen character on both ends
# (of course, could be any string)
def surround(text, quotes):
    return quotes + text + quotes
    
# Produce substring for MongoDB query of "categories" field
def gen_status_params():
    return ['status', surround(choice(STATUSES),'"')]


def gen_connection():
    '''
    Generate commands to initialize connection to database
    '''
    query_file.write('''
// A script to read from a collection of slack in the local database
conn = new Mongo();

// connect to the local database
db = conn.getDB("local");
'''
)

ids = []
                  
def read_ids():
    '''
    Get valid _id values from file, which is generated by get_ids.js
    '''
    ids_file = open('idsa.txt', 'r')
    for id_doc in ids_file:
        ids.append(id_doc.replace('\n',''))
    ids_file.close()
                     
def gen_id_doc():
    '''
    Return random id for document
    '''
    return choice(ids)
                          
# Generate the queries     
    
def generate_queries(to_generate):
    query_ct = 0
    while query_ct < to_generate:
        param_list = gen_status_params()
        gen_status_query(param_list[0],param_list[1])
        query_ct += 1
        
# To run:
# python generate_store_queries.py [num_queries [output_file
# 	[probability of no queries for average ratings
#         [probability of having reviews for a store]]]]
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        to_generate = 100
    else:
        to_generate = int(sys.argv[1])
    fname = 'queries_allAgg.js'
    if len(sys.argv) > 1:
        fname = sys.argv[2]
        if len(sys.argv) > 2:
            NOAVG_PROB = float(sys.argv[3])
            if len(sys.argv) > 3:
                REVIEW_PROB = float(sys.argv[4])
                
    query_file = open(fname,'w')
    read_ids()
    gen_connection()
    generate_queries(to_generate)
    query_file.close()