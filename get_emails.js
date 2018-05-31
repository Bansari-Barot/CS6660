// A script to read from a collection of stores in the local database
conn = new Mongo();

// connect to the local database
db = conn.getDB("local");

// Queries
result = db.slack.find({},{_id:0,email:1})
while ( result.hasNext() ) {
   printjson( result.next());
}
