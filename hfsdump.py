#!/usr/bin/python2
# coding: utf-8
# HTTPFileServer mirror script
# Used for mirroring HFS servers
# often used by chinese malware
# ~skyhighatrist
from clint.textui import progress
import requests
import argparse
import urlparse
import sys

def do_list(listfile):
    print "{+} Using list: %s" %(listfile)
    # mirrors a list of servers
    try:
        f = open(listfile, "r")
    except Exception, e:
        sys.exit("{!} Abort: Could not read listfile")
    urls = f.readlines()
    for url in urls:
        mirror_url(url.strip())

def mirror_url(url):
    # mirrors a server
    print "{+} Mirroring %s" %(url)
    mirror_url = url + "/?mode=archive&recursive"
    host = urlparse.urlparse(url).netloc
    if ":" in host:
        host = host.replace(":", "_")
    outfile = "output/mirror-%s.tar" %(host) # mirror- prefix and s/:/_/g because fuck gnu-tar
    print "{*} Saving to %s" %(outfile)
    try:
        r = requests.get(url=mirror_url, stream=True)
        with open(outfile, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()
    except Exception, e:
        print "{!} Mirroring failed."
        return False
    print "{*} Done!"
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="url or list of urls (if list, use -l flag)")
    parser.add_argument("-l", action="store_true", help="Use listfile")
    args = parser.parse_args()
    if args.l:
        do_list(args.target)
    else:
        mirror_url(args.target)

if __name__ == "__main__":
    main()
