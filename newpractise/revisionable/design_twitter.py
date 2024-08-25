'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
'''
import heapq as hq

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.time = 0 # for maxheap
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        tmp = self.tweets.get(userId, [])
        tmp = [[-self.time, tweetId]] + tmp # this will maintain the order
        self.tweets[userId] = tmp
        

    def getNewsFeed(self, userId: int) -> List[int]:
        q = []

        friends = self.followers.get(userId, [])
        for i in range(len(friends)):
            fid = friends[i]
            other_tweets = self.tweets.get(fid, [])
            if len(other_tweets) > 0:
                q.append([other_tweets[0], 0, other_tweets])
        
        if len(self.tweets.get(userId, [])) > 0:
            userTweet = self.tweets[userId]
            print(userTweet)
            q.append([userTweet[0], 0, userTweet])
            # [first tweet , current index, full array]
        hq.heapify(q)

        cnt = 0
        res = []
        while cnt < 10 and q:
            tw, ind, twarr = hq.heappop(q)
            res.append(tw[1])
            ind += 1

            if ind < len(twarr):
                hq.heappush(q, [twarr[ind], ind, twarr])

            cnt += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        tmp = self.followers.get(followerId, [])
        if followeeId not in tmp:
            tmp.append(followeeId)
        self.followers[followerId] = tmp

    def unfollow(self, followerId: int, followeeId: int) -> None:
        tmp = self.followers.get(followerId, [])
        for i in range(len(tmp)):
            if tmp[i] == followeeId:
                tmp = tmp[:i] + tmp[i+1:]
                break
        self.followers[followerId] = tmp


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)