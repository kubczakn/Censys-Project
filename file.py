import censys.certificates
import os
import csv

f = open("data.csv", "a", newline="")
writer = csv.writer(f)


certificates = censys.certificates.CensysCertificates(os.environ['UID'], os.environ['SECRET'])
fields = ["parsed.fingerprint_sha256", "parsed.validity.start", "parsed.validity.end"]
for c in certificates.search("parsed.names: censys.io AND tags: trusted", fields):
    tup = (c["parsed.fingerprint_sha256"],c["parsed.validity.start"], c["parsed.validity.end"])
    writer.writerow(tup)

f.close()