// Getting apps of a workspace
MATCH (ws:WORKSPACE {name:'Machine learning'})
MATCH (app:APP)
MATCH (ws)-[:INCLUDES]-(app)
RETURN ws.name, app.name;

// Getting channels of a workspace
MATCH (ws:WORKSPACE {name:'Database Systems'})
MATCH (channel:CHANNEL)
MATCH (ws)-[:HAS]-(channel)
RETURN ws.name, channel.name;

// Get the names of user and the app in the Machine learning workspace
MATCH (ws:WORKSPACE{name:'Machine learning'})
MATCH (app:APP)
MATCH (u:USER)
MATCH (ws)-[:INCLUDES]-(app)
MATCH (u)-[:USES]-(app)
RETURN ws.name, u.name, app.name;

// Get the names of user who poted in channel=random
MATCH (u:USER)
MATCH (c:CHANNEL{name:'random'})
MATCH (post:POST)
MATCH (post)-[:POSTED]-(u)
MATCH (c)-[:HAS_A_POST]-(post)
WHERE not exists(()-[:POSTED]-(c))
RETURN c.name, post.title,u.name;

//Get all the posts posted in february month in project 1 channel
MATCH (ws:WORKSPACE)
MATCH (c:CHANNEL{ name:'project 1'})
MATCH (post:POST)
MATCH (ws)-[:HAS]-(c)
MATCH (c)-[:HAS_A_POST]-(post)
WHERE post.month=2
RETURN ws.name, c.name, post.title, post.body;

// For a particular user,
// list all the posts and apps used by user and number of apps used by user

UNWIND [1,2,3,4,5] AS value
MATCH (u:USER {name:'Bansri'})
MATCH (post:POST)
MATCH (u)-[:POSTED]-(post)
MATCH (u)-[:USES]-(app)
RETURN u, post, app, count(app);
