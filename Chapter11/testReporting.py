import re
import subprocess
result_file = open("result_file.txt", "w")
run_test_process = subprocess.run("routeToRunTestsFile", stdout=result_file)
file_object = open("result_file.txt", "r")
failed_number = re.findall("Failed: .", file_object.read())
if len(failed_number) >0:
    failed_tests = failed_number[0][8:]
    subprocess.run(["routeToSendEmail", failed_tests])