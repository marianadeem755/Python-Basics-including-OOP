import argparse
import requests
parser=argparse.ArgumentParser()

def DownloadFile(url, local_filename):
    if local_filename is None:
      local_filename = url.split('/')[-1]
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
          f.write(chunk)
    # f.close()
    return 
parser.add_argument("url", help="url of the file", nargs='?', default="https://imagej.net/images/Fibroblast_Cell_Nucleus.jpg")
# parser.add_argument("output", help="The output of given file", nargs='?', default="output.jpg")
parser.add_argument("-O", "--output", help="The output of given file", nargs='?', default="myfile.jpg")
args=parser.parse_args()
print(args.url)
print(args.output)
# Calling the download function
DownloadFile(args.url, args.output)

print(f"Downloaded file from {args.url} to {args.output}")