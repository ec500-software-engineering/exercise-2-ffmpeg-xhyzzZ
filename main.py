import os
import subprocess
import queue
## asyncio is a library to write concurrent code using the async/await syntax.
import asyncio
import time

def tranfer_video(inputPath):
    files = os.listdir(inputPath)
    q = queue.Queue()
    j = 1
    for file in files:
        q.put(file)
    while not q.empty():
        video = q.get()

        ## transfer to 480p video
        async def transfer_video_for_480p():
            print('start to transfer')
            subprocess.call('ffmpeg -i /Users/kobale/exercise2/Input/'
                            + video + ' -b 1M -r 30 -s 720x480 -c:a copy'
                            + ' /Users/kobale/exercise2/Output/480p_video'
                            + str(j) + '.mp4', shell = True)
            return '480p videos have been all transformed'

        ## transfer to 720p video
        async def transfer_video_for_720p():
            print('start to transfer')
            subprocess.call('ffmpeg -i /Users/kobale/exercise2/Input/'
                            + video + ' -b 2M -r 30 -s 1280x720 -c:a copy'
                            + ' /Users/kobale/exercise2/Output/720p_video'
                            + str(j) + '.mp4', shell = True)
            return '720p videos have been all transformed'

        ## queue
        threadings = [asyncio.ensure_future(transfer_video_for_480p()), asyncio.ensure_future(transfer_video_for_720p()),]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(threadings))

        for threading in threadings:
            print('Task: ', threading.result())
        j += 1
        q.task_done()

    print(str(j - 1) + ' videos have been transferred into 720p and 480p type')

def main():

    startTime = time.process_time()

    tranfer_video('/Users/kobale/exercise2/Input')

    consumedTime = time.process_time() - startTime

    print("The consumed time is :", consumedTime)

if __name__=='__main__':
    main()