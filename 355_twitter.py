# https://leetcode.com/problems/design-twitter/description/
class Twitter:
    followMap = {} # followee: [follows1,follows2,...]
    tweets = {} # user: [tweetID1,...]

    def __init__(self):
        ...

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append(tweetId)
        else:
            self.tweets[userId] = [tweetId]
        
    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.followMap:
            self.followMap[userId] = []
        
        # Get last 10 tweets of everyone I follow including my own
        # pool = [self.tweets[user][:10] for user in self.followMap[userId]]
        pool = [tweet for user in self.followMap[userId] for tweet in self.tweets[user][:10]]
        pool.extend(self.tweets[userId][:10])
        pool.sort()

        feed = pool[-10:]
        feed.reverse()

        return feed
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].append(followeeId)
        else:
            self.followMap[followerId] = [followerId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followeeId:
            return 
        
        if followeeId in self.followMap:
            self.followMap[followeeId].remove(followerId)


# Your Twitter object will be instantiated and called as such:
twitter = Twitter()
print(twitter.postTweet(1, 10)) # User 1 posts a new tweet with id = 10.
print(twitter.postTweet(2, 20)) # User 2 posts a new tweet with id = 20.
print(twitter.getNewsFeed(1))   # User 1's news feed should only contain their own tweets -> [10].
print(twitter.getNewsFeed(2))   # User 2's news feed should only contain their own tweets -> [20].
print(twitter.follow(1, 2))     # User 1 follows user 2.
print(twitter.getNewsFeed(1))   # User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
print(twitter.getNewsFeed(2))   # User 2's news feed should still only contain their own tweets -> [20].
print(twitter.unfollow(1, 2))   # User 1 unfollows user 2.
print(twitter.getNewsFeed(1))   # User 1's news feed should only contain their own tweets -> [10].