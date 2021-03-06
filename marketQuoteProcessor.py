import re
import sys
import csv 

if __name__ == '__main__':
    with open(sys.argv[1], 'rt') as file:
        readFile = file.read()
    
    line = readFile.splitlines()
    
 
    
    message_type = ''
    symbol = ''
    ask_quote_flag = ''
    bid_quote_flag = ''
    best_ask = '0'
    best_bid = '0'
    best_ask_value = 0
    best_bid_value = 0
    time = ''
    csvHeader = ['MESSAGE TYPE','SYMBOL','TIME','ASK QUOTE FLAG','BID QUOTE FLAG','BEST ASK','BEST BID']
    
    req_file = 'processedmarketdata.csv'
    fo = open(req_file,'w', newline ="")
    csv_writer = csv.writer(fo, delimiter = ',')
    csv_writer.writerow(csvHeader)
    
    for each_line in line:
        if 'MSGTYPE = QUOTE' not in each_line:
            continue
        
        marketData = each_line.split(',')
        
        for each_marketData in marketData:
            tag = each_marketData.split('=')[0].strip()
            value = each_marketData.split('=')[1].strip()
            
            if 'MSGTYPE' in tag:
                message_type = value
            if 'SYMBOL' in tag:
                symbol = value
            if 'BEST_ASK_QUOTE_FLAG' in tag:
                ask_quote_flag = value
            if 'BEST_BID_QUOTE_FLAG' in tag:
                bid_quote_flag = value
            if 'BEST_BID' in tag:
                best_bid = int(value) / 10000000
            if 'BEST_ASK' in tag:
                best_ask = int(value) / 10000000
            if 'TIME' in tag:
                time = value
        csv_writer.writerow([message_type,symbol,time,ask_quote_flag,bid_quote_flag,best_ask,best_bid])
    fo.close()
    