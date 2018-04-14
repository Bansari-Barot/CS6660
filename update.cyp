// Move a user from one workspace to another
MATCH (u:USER {name:'sophie'})
MATCH(newws:WORKSPACE {name:'Database Systems'})
MATCH (u)-[oldfm:ACCESSES]-()
CREATE (u)-[newfm:ACCESSES]->(newws)
DELETE oldfm
RETURN u,newws.name;

// Change the phone number of one of the users
MATCH (u:USER {name:'Bhavik'})
SET u.phone_no = '3467888'
RETURN u;

//Delete one of the channel and all of it's posts
MATCH (c:CHANNEL {name:'random'})
MATCH (c)-[:HAS_A_POST]->(post:POST)
DETACH DELETE c,post;