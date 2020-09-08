import collections as col
Instrument = col.namedtuple('Instrument', ['exchange', 'token', 'symbol',
                                      'name','expiry', 'lot_size'])

tuple_list=[Instrument(exchange='NSE', token=1594, symbol='INFY', name='INFOSYS LIMITED', expiry=None, lot_size=None), 
Instrument(exchange='NSE', token=4963, symbol='ICICIBANK', name='ICICI BANK LTD.', expiry=None, lot_size=None), 
Instrument(exchange='NSE', token=2885, symbol='RELIANCE', name='RELIANCE INDUSTRIES LTD', expiry=None, lot_size=None), 
Instrument(exchange='NSE', token=10604, symbol='BHARTIARTL', name='BHARTI AIRTEL LIMITED', expiry=None, lot_size=None)]

ins_script="RELIANCE"
for tup in tuple_list:
 print(tup[2]==ins_script)
 ##
