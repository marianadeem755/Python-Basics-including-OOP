import re 
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern='\d{10}|\(\d{3}\)-\d{3}-\d{4}'
matches=re.findall(pattern, text)
print(matches)


text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern='Note \d - ([^\n]+)'
matches=re.findall(pattern, text)
print(matches)


text='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''

pattern='FY\d{4} Q\d{1}'
matches=re.findall(pattern, text)
print(matches)

pattern='\$\d.+'
matches=re.findall(pattern, text)
print(matches)

pattern='\$\d\.\d{2}'
matches=re.findall(pattern, text)
print(matches)

pattern='\$([\d\.]+)'
matches=re.findall(pattern, text)
print(matches)


text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 ljh lsj a 123 was $4.85 billion. Same number for FY2020 Q4 was $8 billion
'''
pattern='FY\d{4} Q[1-4]|\$[\d\.]+'
matches=re.findall(pattern, text)
print(matches)


text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''

pattern='https:\/\/[a-z]+[\.]com\/[a-z]+'
matches=re.findall(pattern, text)
print(matches)


pattern='https:\/\/[a-z]+[\.]com\/[a-z]+_[a-z]+|https:\/\/[a-z]+[\.]com\/[a-z]+_\d_[a-z]+|https:\/\/www\.[a-z]+\.com\/\.|https:\/\/[a-z]+[\.]com\/[a-z]+'
matches=re.findall(pattern, text)
print(matches)


text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern='Concentration of Risk:( [A-Za-z]+ [A-Za-z]+)'
matches=re.findall(pattern, text)
print(matches)

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern='FY[\d]+ [A-Za-z]\d|\$[\d\.]+'
matches=re.findall(pattern, text)
print(matches)