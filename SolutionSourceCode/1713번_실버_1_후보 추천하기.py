import sys


class Picture:
    def __init__(self, studentNumber):
        self.upvote = 0
        self.studentNumber = studentNumber
        self.step = 0

class PictureFrame:
    def __init__(self, pictureNumber):
        self.pictureFrame = []
        self.pictureNumber = pictureNumber

    def ReplacePictrueFrame(self, old, new):
        self.pictureFrame[self.pictureFrame.index(old)].upvote = 0
        self.pictureFrame[self.pictureFrame.index(old)].step = 0
        self.pictureFrame[self.pictureFrame.index(old)] = new
        self.pictureFrame = sorted(self.pictureFrame, key=lambda x: x.upvote, reverse=False)

    def FinalResultAscendingOrder(self):
        self.pictureFrame.sort(key=lambda x: x.upvote)
        return self.pictureFrame

    def CheckNeedReplacement(self, picture):
        if (len(self.pictureFrame) == self.pictureNumber and not (picture in self.pictureFrame)):
            self.pictureFrame = sorted(self.pictureFrame, key=lambda x: x.upvote, reverse=False)

            lowestUpVoteCandidates = [candidate for candidate in self.pictureFrame if candidate.upvote == self.pictureFrame[0].upvote]

            lowestUpVoteCandidates = sorted(lowestUpVoteCandidates, key=lambda x: x.step, reverse=True)

            self.ReplacePictrueFrame(lowestUpVoteCandidates[0], picture)
        elif not (picture in self.pictureFrame):
            self.pictureFrame.append(picture)
            # sorted(self.pictureFrame, key=lambda x: x.upvote, reverse=False)

        for i in range(len(self.pictureFrame)):
            self.pictureFrame[i].step += 1

def ActualCode(frameNumber, totalUpVoteNumber, upvoteTicketList):
    frames = PictureFrame(frameNumber)
    candidates = list()

    for i in range(1, totalUpVoteNumber + 1):
        candidates.append(Picture(i))

    for i in upvoteTicketList:
        candidates[i - 1].upvote += 1
        frames.CheckNeedReplacement(candidates[i - 1])

    result = frames.FinalResultAscendingOrder()
    result.sort(key=lambda x: x.studentNumber, reverse=False)

    for i in range(len(result)):
        if (i != len(result) - 1):
            sys.stdout.write(str(result[i].studentNumber) + ' ')
        else:
            sys.stdout.write(str(result[i].studentNumber))


if __name__ == '__main__':
    frameNumber = int(sys.stdin.readline())
    totalUpvoteNumber = int(sys.stdin.readline())
    upvoteTicketList = map(int, (sys.stdin.readline().split(' ')))

    ActualCode(frameNumber, totalUpvoteNumber, upvoteTicketList)
