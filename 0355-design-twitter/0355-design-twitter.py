class Twitter:

    def __init__(self):
        self.followers = {}
        self.write = [None,None,None]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.write=[userId,tweetId,self.write]

    def getNewsFeed(self, userId: int) -> List[int]:
        rt = []
        if userId not in self.followers:
            self.followers[userId]={userId}
        tg=self.followers[userId]
        nw = self.write
        while(len(rt)<10):
            uid,tid,n = nw
            if uid==None:
                break
            if uid in tg:
                rt.append(tid)
            nw = n
        return rt


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId]={followerId}
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId]={followerId}
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)