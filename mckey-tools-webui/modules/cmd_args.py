#
import os
import argparse

#
parser = argparse.ArgumentParser()

parser.add_argument("--share", action='store_true', help="use share=True for gradio and make the UI accessible through their site")
parser.add_argument("--use-cpu", nargs='+', help="use CPU as torch device for specified modules", default=[], type=str.lower)
parser.add_argument("--server-name", type=str, help="Sets hostname of server", default=None)
parser.add_argument("--port", type=int, help="launch gradio with given server port, you need root/admin rights for ports < 1024, defaults to 7860 if available", default=None)
parser.add_argument("--gradio-queue", action='store_true', help="does not do anything", default=True)
parser.add_argument("--no-gradio-queue", action='store_true', help="Disables gradio queue; causes the webpage to use http requests instead of websockets; was the default in earlier versions")
