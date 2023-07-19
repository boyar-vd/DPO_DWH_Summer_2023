import schedule
import subprocess as sp


# Create function which do necessary job
def job():
    """
    Run ```echo "Test text"``` in a terminal
    """
    command = ['echo', 'Test text']
    sp.run(command)


# Specify to run job every minute
schedule.every().minute.do(job)


# Run job
while True:
    schedule.run_pending()
