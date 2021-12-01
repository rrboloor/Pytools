# Pytools
This is a quick firewall port or path testing tool. When you are deploying services,you need to check those applications are accessible from Users desktop.Sometimes its tedious when you have many office locations from where you need to check this. This tool checks TCP ports only. One way is to use "tcptrace" command. Tcptrace is comprehensive tool and gives hop-by hop status. But it could be time consuming. So I wrote this tool to quickly scan for IP/Port combinations quickly. The idea is tool tried to create a tcp socket . If its successful its assumed that path is complete from firewall/acl per se.
To run this
1. Clone the repository.
2. Create a testFile containing IP address and port.(check sample test file).
3. run "FirewallPortCheck.py path_to_testfile"
4. The results will be provided in the same directory as testfile.log.
