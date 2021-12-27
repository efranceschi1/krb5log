#!/usr/bin/env python

from collections import defaultdict
import os, sys, re, logging, fileinput

# Logging
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format="[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s")
log = logging.getLogger(__name__)

# Generic Functions
def print_table(title, subj, rpt):
   template = "| {0:109} | {1:>10} |"
   print('{:^123s}'.format(title))
   print('+{:-^111s}+{:-^12s}+'.format("", ""))
   print(template.format(subj, "QTY"))
   print('+{:-^111s}+{:-^12s}+'.format("", ""))
   for key in dict(sorted(rpt.items(), key = lambda x: x[1], reverse = True)):
      print(template.format(key, rpt[key]))
   print('+{:-^111s}+{:-^12s}+'.format("", ""))
   print()

# Kerberos
krb_operations = {
   "TGS_REQ": "Service Ticket",
   "AS_REQ": "Initial Authentication"
}

# Reports
rpt_principals = defaultdict(int)
rpt_hosts = defaultdict(int)
rpt_users = defaultdict(int)
rpt_operation = defaultdict(int)

def report():
   print_table("REQUESTS PER USER", "USER", rpt_users)
   print_table("REQUESTS PER PRINCIPAL", "PRINCIPAL", rpt_principals)
   print_table("REQUESTS PER HOST", "HOST", rpt_hosts)
   print_table("REQUESTS PER OPERATION", "OPERATION", rpt_operation)

# Line processing
def process_line(line):
   r = re.search(r"^(\w+) (\d+) (\d+:\d+:\d+) (\w+) (\w+)\[(\d+)\]\((\w+)\): (\w+) \((.+)\) (\d+\.\d+\.\d+\.\d+): (\w+): (\w+) (\d+), (.+), (.+) for (.+)$", line)
   if r:
      user = r.group(15)
      principal = r.group(16)
      host = r.group(10)
      operation = krb_operations.get(r.group(8), r.group(8))

      rpt_principals[principal] += 1
      rpt_users[user] += 1
      rpt_hosts[host] += 1
      rpt_operation[operation] += 1

# Log processing
def process() -> int:
   with fileinput.input() as infile:
      line_count = 0
      for line in infile:
         line_count += 1
         process_line(line)
   return line_count

# Usage
def usage():
   print("Usage: krb5log.py < krb5kdc.out", file=sys.stderr)
   exit(1)

# Main
def main() -> int:
   args = sys.argv[1:]
   if len(args) != 0:
      usage()
   line_count = process()
   log.info("Processed %s lines", line_count)
   report()
   return 0

if __name__ == "__main__":
   exit(main())
