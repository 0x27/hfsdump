## hfsdump - Dump/Backup a "HFS" (HTTPFileServer) Server with no auth

This is a quick script I wrote for quickly making dumps/backups of [HFS (HTTPFileServer)](http://www.rejetto.com/hfs/) hosts that had no auth that might be serving malware for science reasons.

This is an early version of the script, I had written a better one that integrated Virustotal scanning of dumped files, but cannot find it right now. Releasing this to remind myself to do this later.

The [Shodan Query](https://www.shodan.io/search?query=%22Server%3A+HFS%22) of "Server: HFS" will find you a lot of these servers.

It is not recommended to go "dumping" or making "backups" of HFS boxes without authorization, but given how fucking many of them are used to serve shitty Chinese DDoS malware...

### Usage  
To use, just run it with the URL of the target server, or a listfile of target hosts. You will need to "mkdir output" in the directory you are running it from as I forgot to make that automatic.

### Requirements  
Written for python2.7, the non-stdlib components are "clint" and "requests". Install them with "pip" or via the requirements.txt file thing.

### Licence  
Dual licenced under the [WTFPL](http://www.wtfpl.net/) and the Snitches Get Stitches Public Licence.

### Todo  
* Fix up and improve exception handling stuff, which is a bit rubbish at the moment.
* Add an automatic shodan scanning component
* Fix and integrate the Virustotal scanning and alerting of hosts serving malware
* Enable authentication handling for servers using the auth built into HFS.

### Beer  
[Donations of beer money gladly accepted](https://www.coinbase.com/infodox/)
