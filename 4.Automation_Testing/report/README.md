# prepare Report

---
Generate HTML test report in runtime
### what is the fixture method?

1) how we can use fixture method in multiple test methods
2) how fixture method returns the data
3) how we use fixture data in test methods..
4) passing browser name as arguments through command line
```commandline
pytest -s -v .\day28\test_CommandLine.py --browser chrome
 pytest -s -v .\day28\test_CommandLine.py --browser edge
```
Generating HTML reports...
```commandline
pytest -s -v --html=day28\report.html .\day28\test_CommandLine2.py --browser chrome
```