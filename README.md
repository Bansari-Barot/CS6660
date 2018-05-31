
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
100 Aggregate Query


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

In the queries_allAgg.js file, we have queries for finding all users of particular status and in how many workspaces and how many channels a user have. With index on status, we got all the users in a little less time than without index. Index didn’t optimize much. We guess it’s because of few different statuses(only 5 different statuses used).

In the queries_MixWriteAggRead.js file, we have queries for all the three operations mentioned above. As we can see these queries took longer compared to Aggregate read because I guess write queries in this file takes more time. Here indexing on post and statuses increased the average time maybe because indexing didn’t go well with all queries. For example, index on post_date doesn’t help with “finding user with a given status” query.
