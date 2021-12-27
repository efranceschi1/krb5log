# Kerberos Log Analyzer

## About the project
This is a python script for parsing KDC logs and displaying relevant statistics and information about authentication and ticket validations.

This project was also inspired by the [Stanford::Metrics log analysis system](https://git.eyrie.org/?p=system/metrics.git;a=summary)

## Motivation
In some troubleshooting situations it is necessary to analyze KDC MIT logs to identify bottlenecks and malfunctions in Kerberos environments. This script aims to facilitate this analysis through reports containing access statistics in certain scenarios.

## Sample input
```
Dec 06 03:31:01 sample00377pl krb5kdc[2130](info): TGS_REQ (4 etypes {18 17 16 23}) 10.238.126.145: ISSUE: authtime 1638705804, etypes {rep=18 tkt=18 ses=18}, hbase/sample00673sl.example.com@EXAMPLE.COM for HTTP/sample01715co.example.com@EXAMPLE.COM
Dec 06 03:31:01 sample00377pl krb5kdc[2130](info): TGS_REQ (4 etypes {18 17 16 23}) 10.238.126.145: ISSUE: authtime 1638705804, etypes {rep=18 tkt=18 ses=18}, hbase/sample00673sl.example.com@EXAMPLE.COM for HTTP/sample01715co.example.com@EXAMPLE.COM
Dec 06 03:31:01 sample00377pl krb5kdc[2130](info): TGS_REQ (4 etypes {18 17 16 23}) 10.238.125.181: ISSUE: authtime 1638742011, etypes {rep=18 tkt=18 ses=18}, hbase/sample01769co.example.com@EXAMPLE.COM for HTTP/sample01732co.example.com@EXAMPLE.COM
Dec 06 03:31:01 sample00377pl krb5kdc[2130](info): TGS_REQ (4 etypes {18 17 16 23}) 10.238.127.78: ISSUE: authtime 1638742028, etypes {rep=18 tkt=18 ses=18}, hbase/sample01837co.example.com@EXAMPLE.COM for HTTP/sample01732co.example.com@EXAMPLE.COM
Dec 06 03:31:01 sample00377pl krb5kdc[2130](info): TGS_REQ (4 etypes {18 17 16 23}) 10.238.124.14: ISSUE: authtime 1638736182, etypes {rep=18 tkt=17 ses=18}, hbase/sample00643co.example.com@EXAMPLE.COM for HTTP/sample00802co.example.com@EXAMPLE.COM
Dec 06 03:31:01 sample00377pl krb5kdc[2130](info): TGS_REQ (4 etypes {18 17 16 23}) 10.238.127.85: ISSUE: authtime 1638742022, etypes {rep=18 tkt=18 ses=18}, hbase/sample02114co.example.com@EXAMPLE.COM for HTTP/sample01732co.example.com@EXAMPLE.COM
```

## Running
```
krb5log.py < krb5kdc.out
```
OR
```
cat krb5kdc.out | krb5log.py
```
OR
```
zcat *.gz | krb5log.py
```

## Sample Report Output
```
                      REQUESTS PER USER
+-----------------------------------------------+------------+
| USER                                          |        QTY |
+-----------------------------------------------+------------+
| rm/sample00787co.example.com@EXAMPLE.COM      |         19 |
| hive/sample00791co.example.com@EXAMPLE.COM    |          8 |
| hive/sample00788co.example.com@EXAMPLE.COM    |          7 |
| hive/sample01727co.example.com@EXAMPLE.COM    |          5 |
| hive/sample02048co.example.com@EXAMPLE.COM    |          5 |
| hive/sample01744co.example.com@EXAMPLE.COM    |          4 |
| hive/sample00787co.example.com@EXAMPLE.COM    |          4 |
| knox/sample01715co.example.com@EXAMPLE.COM    |          3 |
+-----------------------------------------------+------------+

                  REQUESTS PER PRINCIPAL
+-----------------------------------------------+------------+
| PRINCIPAL                                     |        QTY |
+-----------------------------------------------+------------+
| HTTP/sample01732co.example.com@EXAMPLE.COM    |         45 |
| HTTP/sample00789co.example.com@EXAMPLE.COM    |         26 |
| HTTP/sample01733co.example.com@EXAMPLE.COM    |         19 |
| HTTP/sample00802co.example.com@EXAMPLE.COM    |         17 |
| hdfs/sample01721co.example.com@EXAMPLE.COM    |         11 |
| krbtgt/EXAMPLE.COM@EXAMPLE.COM                |         10 |
| hive/sample01727co.example.com@EXAMPLE.COM    |          9 |
| nn/sample00786co.example.com@EXAMPLE.COM      |          8 |
| nn/sample00785co.example.com@EXAMPLE.COM      |          7 |
| HTTP/sample01715co.example.com@EXAMPLE.COM    |          6 |
| HTTP/sample00262co.example.com@EXAMPLE.COM    |          5 |
| rm/sample00787co.example.com@EXAMPLE.COM      |          3 |
| hive/sample01728co.example.com@EXAMPLE.COM    |          2 |
| hive/sample02048co.example.com@EXAMPLE.COM    |          2 |
| kafka/sample00810co.example.com@EXAMPLE.COM   |          1 |
| kafka/sample00809co.example.com@EXAMPLE.COM   |          1 |
| hdfs/sample01751co.example.com@EXAMPLE.COM    |          1 |
| HTTP/sample01779co.example.com@EXAMPLE.COM    |          1 |
| HTTP/sample01725co.example.com@EXAMPLE.COM    |          1 |
| HTTP/sample01773co.example.com@EXAMPLE.COM    |          1 |
| hive/sample00789co.example.com@EXAMPLE.COM    |          1 |
| hive/sample02050co.example.com@EXAMPLE.COM    |          1 |
| hdfs/sample01710co.example.com@EXAMPLE.COM    |          1 |
+-----------------------------------------------+------------+

                     REQUESTS PER HOST
+-----------------------------------------------+------------+
| HOST                                          |        QTY |
+-----------------------------------------------+------------+
| 10.238.124.57                                 |         23 |
| 10.238.124.58                                 |          8 |
| 10.238.124.61                                 |          8 |
| 10.238.127.37                                 |          6 |
| 10.238.124.59                                 |          6 |
| 10.238.125.159                                |          5 |
| 10.238.125.239                                |          5 |
| 10.238.127.48                                 |          5 |
| 10.238.125.162                                |          4 |
| 10.238.125.181                                |          3 |
| 10.238.125.151                                |          3 |

+-----------------------------------------------+------------+

                                                  REQUESTS PER OPERATION
+-----------------------------------------------+------------+
| OPERATION                                     |        QTY |
+-----------------------------------------------+------------+
| Service Ticket                                |        169 |
| Initial Authentication                        |         10 |
+-----------------------------------------------+------------+
```

## Contributing
This project is at a very early stage of development and certainly still needs a lot of improvement.

So please, report any bugs or feature requests using the Github Issues here. Better yet, send pull requests!
