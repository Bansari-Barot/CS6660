
# Assignment-4
1)
File Name: queries_allread.js
Without Index: Avg time - 115562.863ms
With Index: Avg time - 8953.638ms
43 find query with status
57 find query with  post date


2)
File Name: queries_mixreadwrite.js
Without Index: Avg time - 61331.12ms
With Index: Avg time - 5518.637ms
51 find query (Status: 20 query, Postdate:31)
49 Update Query

3)
File Name: queries__allAgg.js
Without Index avg run time: 25865.3529
After Index on email ids: 21755.6325
200 Aggregate Query


4)
File Name: queries__MixWriteAggRead.js
Without Index: Avg time - 55322.54ms
With Index: Avg time - 8485.474ms
59 find query( Status:31, Postdate: 28)
41 aggregate query
53 Update Query


Discussion:

In the queries_allread.js file, we’re reading all the posts posted by users after one specified date or fetching all the statuses of users.
As we can see in the results, after indexing on post_date, average time decreased. After indexing it scanned a portion of data from database compared to queries without indexes.

In the queries_mixreadwrite.js, we have mixed read and write queries for searching a document and the adding a post to it. It took less time than all read queries because it might have encountered the document to update before reaching to the last document in database. All read queries have to read all the values which is large in number and hence took longer.

In the queries_allAgg.js file, we have queries for finding all users of particular status and in how many workspaces and how many channels a user have and another queries slecting any email id of user(its taking random email ids and the js file to get all the email ids from database is uploaded as get_emails.js) and finding that user with that email id giving how many workspaces and how many channels a user have. With index on email, we got all the users in a little less time than without index. This file has 50(25%) queries which is matching particular status while other 150(75%) queries which is matching with particular emails. We guess the queries with looking for status with all users are taking more time in input output while the query who is looking for particular email id is taking more in searching before applying index while after applying index its taking less time. So index on email is very helpful while performing these kind of queries(Where you are looking for particular user with that email id as email id will be unique only). 

In the queries_MixWriteAggRead.js file, we have queries for all the three operations mentioned above. As we can see these queries took longer compared to Aggregate read because I guess write queries in this file takes more time. Here indexing on post and statuses increased the average time maybe because indexing didn’t go well with all queries. For example, index on post_date doesn’t help with “finding user with a given status” query.
