from hdn import *

app = HDNWorker("example-token-0")


@app.task(info="Main Task", main=True)
def main_t(args):
    print("Hello, world!", args)
