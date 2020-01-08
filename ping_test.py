#!/usr/bin/env python3
import subprocess
import os
import iperf3

def main():


    ipadd = "8.8.8.8"

    response = subprocess.run(["ping", "-c", "12", ipadd], stdout=subprocess.PIPE)
    answer = response.returncode

    if answer == 1:
        ping_results = "Lost Connection \n"
        print("Lost Connection")
    elif answer == 0:
        ping_results = "Ping Successful \n"
        print("Ping Successful")

    with open("results_test.txt", "a+") as f:
        f.write(ping_results)

def run_iperf():
    client = iperf3.Client()
    client.duration = 1
    client.server_hostname ='81.52.142.209'
    client.port = 5201
    result = client.run()
    if result.error:
        print(result.error)
    else:
        with open("results_iperf3.txt", "a+") as f:
            f.write('Average transmitted data \n')
            f.write(' Megabits per second {0}'.format(result.Mbps),'\n')


if __name__=="__main__":
    main()
    run_iperf()
