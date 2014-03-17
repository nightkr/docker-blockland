import sys, subprocess, urllib2, os, hashlib, threading

ignored_prefixes = [
    "screenshots/",
    "shaders/",
    "saves/"
]

def ignored(path):
	return any((path.startswith(i) for i in ignored_prefixes))

def update(manifestPath):
	print "Downloading manifest " + manifestPath + "...",
	manifestRequest = urllib2.Request(manifestPath, headers={"User-Agent": "blocklandWIN/2.0"})
	manifestFile = urllib2.urlopen(manifestRequest)
	manifest = manifestFile.readlines(False)
	print "DONE"

	print "Processing manifest...",
	downloadPath = manifest[0].split("\t")[1].strip()
	files = {}
	ignoredFiles = open("ignored.txt").readlines(False)
	for i in manifest[1:]:
		i = i.strip()[1:].split("\t")
		digest = ""
		if os.path.exists(i[0]):
			digest = hashlib.sha1()
			digest.update(open(i[0], "rb").read())
			digest = digest.hexdigest()
		if not ignored(i[0]) and digest.lower() != i[1].lower():
			files[i[0]] = i[1]
	print "DONE"

	downloadedFiles = 0
	for i in files:
		downloadedFiles += 1
		print "Downloading " + i + " (file " + str(downloadedFiles)  + "/" + str(len(files)) + ")...",
		download = urllib2.urlopen(downloadPath + "/" + files[i])
		folders = i.split("/")[:-1]
		for j in range(len(folders)):
			path = "/".join(folders[:j + 1])
			if not os.path.exists(path):
				os.mkdir(path)
		open(i, "wb").write(download.read())
		print "DONE"

update("http://update.blockland.us/latestVersion.php")
