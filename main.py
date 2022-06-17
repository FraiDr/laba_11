import re
from datetime import datetime

file_name = 'access_log_Jul95.txt'
logs_file = open(file_name, "r")
logs_lines = logs_file.readlines()

DATE = ".*(\\[08/Jul/1995:(05:10:2[7-9]|0[6-9]:[0-5][0-9]|1[0-9]:[0-5][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]:[0-5][0-9])|" \
     "(\\[09/Jul/1995:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])|" \
     "(\\[1[0-1]/Jul/1995:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])|" \
     "(\\[12/Jul/1995:(0[0-9]:[0-5][0-9]:[0-5][0-9]|1[0-5]:[0-5][0-9]:[0-5][0-9]|" \
     "16:([0-1][0-9]:[0-5][0-9]|20:[0-5][0-9]|21:[0-4]:[0-9]|21:50)))).*git\"\\s"

pattern_for_200 = re.compile(DATE + "200 .*")
pattern_for_400 = re.compile(DATE + "[4]\\d{2} .*")
pattern_for_500 = re.compile(DATE + "[5]\\d{2} .*")


date_format = '%d/%b/%Y:%H:%M:%S'
date_from = datetime.strptime('09/Mar/1995:21:10:44', date_format)
date_to = datetime.strptime('11/Mar/1995:19:29:28', date_format)

result_dict = {}
for line in logs_lines:
    success_request_matches = re.match(pattern_for_200, line)
    not_found_request_matches = re.match(pattern_for_400, line)
    error_request_matches = re.match(pattern_for_500, line)
    if success_request_matches:
        result_dict["200 requests:"] = result_dict.get("200 requests:", 0) + 1
    if not_found_request_matches:
        result_dict["400-499 requests:"] = result_dict.get("400-499 requests:", 0) + 1
    if error_request_matches:
        result_dict["500-599 requests:"] = result_dict.get("500-599 requests:", 0) + 1

for keys, values in result_dict.items():
    print(f"{keys} - {values}")
