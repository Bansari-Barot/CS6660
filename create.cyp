CREATE  (general:CHANNEL{name: 'general'}),
		(random:CHANNEL{name:'random'}),
        (project1:CHANNEL{name:'project 1'}),
        (bansri:USER{name:'Bansri', phone_no:'0123456', email_id:'bb@xyz.com', status:'active'}),
        (bhavik:USER{name:'Bhavik', phone_no:'1783456', email_id:'bt@xyz.com', status:'In a meeting'}),
        (sophie:USER{name:'Sophie', phone_no:'5679000', email_id:'ly@xyz.com', status:'Outside'}),
        (renee:USER{name:'Renee', phone_no:'0993456', email_id:'rr@xyz.com', status:'active'}),
        (john:USER{name:'John', phone_no:'5229000', email_id:'hn@xyz.com', status:'active'}),
        (dropbox:APP{name:'DropBox'}),
        (twitter:APP{name:'Twitter'}),
        (vote:APP{name:'Vote'}),
        (tasks:POST{title:'Task list', body:'1 analyze 2 design 3 develop 4 test', date:'01-04-2018', time:'5pm'}),
        (meeting:POST{title:'Meeting time', body:'Meeting is on 4th may 2018',date:3,month:1,year:2018}),
        (results:POST{title:'Results', body:'project 1 is successfully tested and is ready for deployment.' ,date:13,month:4,year:2018}),
        (discussion:POST{title:'Discussion', body:'We will use imdb dataset for project 1' , date:3,month:2,year:2018}),
        (cs6660:WORKSPACE{name:'Database Systems'}),
        (cs6820:WORKSPACE{name:'Machine learning'}),

        (bansri)-[:ACCESSES]->(cs6660),
        (bhavik)-[:ACCESSES]->(cs6660),
        (bhavik)-[:ACCESSES]->(cs6820),
        (bansri)-[:ACCESSES]->(cs6820),
        (sophie)-[:ACCESSES]->(cs6820),
        (renee)-[:ACCESSES]->(cs6820),
        (john)-[:ACCESSES]->(cs6820),
        (cs6660)-[:HAS]->(general),
        (cs6820)-[:HAS]->(random),
        (cs6820)-[:HAS]->(project1),
        (bansri)-[:POSTED]->(tasks),
        (bhavik)-[:POSTED]->(meeting),
        (sophie)-[:POSTED]->(discussion),
        (john)-[:POSTED]->(results),
        (cs6660)-[:INCLUDES]->(twitter),
        (cs6820)-[:INCLUDES]->(dropbox),
        (cs6820)-[:INCLUDES]->(vote),
        (general)-[:HAS_A_POST]->(tasks),
        (project1)-[:HAS_A_POST]->(discussion),
        (random)-[:HAS_A_POST]->(meeting),
        (project1)-[:HAS_A_POST]->(results),
        (bansri)-[:USES]->(dropbox),
        (bhavik)-[:USES]->(vote),
        (john)-[:USES]->(twitter),
        (sophie)-[:USES]->(vote);


// Adding a review to help test histogram query
MATCH (u:USER {name:'Bansri'})
MATCH (c:CHANNEL {name:'general'})
CREATE (p:POST {title:'To-DO', body:'Check ypur gmail for more information'})
CREATE (c)-[:HAS_A_POST]->(p);


       




