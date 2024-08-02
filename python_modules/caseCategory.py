####################################
# @file         - caseCategory.py
# @contributors -  
# @Usage        - 
# @Notes        - 
####################################
from datetime import datetime
import time
def main(obj):
    print (obj)
    time.sleep(1)
    
    if obj.total_delay:
        obj.total_delay = datetime.strptime(obj.total_delay, "%H:%M")
        
    if obj.flight_date:
        obj.flight_date = datetime.strptime(obj.flight_date, "%Y-%m-%d")
    
    #Total Delay less than 3 hours. Others are specific which has t be identified manually or to add those columns if possible
    if obj.total_delay and obj.total_delay.hour < 3:
        return "Full defense-MTD", "No", ""
    
    #If "Do we have the CAS ID?" (CAS number available is "No"), primary reason political, secondary reason weather , amount is below 1500
    if obj.cas_id_yes_no.lower() == "no" and obj.primary_reason.lower() == "political" and obj.secondary_reason.lower() == "weather":
        return "Summary - Defence Others", "No", ""
        
    #If "Do we have the CAS ID?" (CAS number available is "No"), then Affidavit Required? (Affidavit required)  should be "Yes".
    if obj.cas_id_yes_no.lower() == "no":
        return "MRA Affidavit Needed", "Yes", "MRA-Affidavit"
    
    #Is Duplicate Case =Yes
    if obj.duplicate_case_yes_no.lower() == "yes":
        return "Full defense/Summary defense-Dupe", "No", ""
        
    #Reason Claim or Primary Reason = Denied boarding
    if obj.reason_claim.lower() == "denied boarding" or obj.primary_reason.lower() == "denied boarding":
        return "Full defense-DBC", "No", ""
    
    #If primary or secondary reason - Crew/ Manpower and Flight Date has dates falling between May/lune/July 2022, amount above 1500
    if  (
         obj.flight_date and ( obj.primary_reason.lower() in ['crew', 'manpower'] or obj.secondary_reason.lower() in ['crew', 'manpower'] ) and
         (obj.flight_date.year == 2022 and int(obj.flight_date.month) in [5,6,7]) and
         (int(obj.claim_amount) >= 1500)
        ):
        return "Full defense-COVID", "Yes", "Crew Affidavit"
        
    #If primary reason is Crew, secondary reason is Maintenance and Flight Date has dates falling between May/June/July 2022, amount above 1500
    if  (
         obj.flight_date and ( obj.primary_reason.lower() == 'crew' and obj.secondary_reason.lower() == 'maintenance' ) and
         (obj.flight_date.year == 2022 and obj.flight_date.month in [5,6,7]) and
         (int(obj.claim_amount) >= 1500)
        ):
        return "Full defense-COVID", "Yes", "Maintenance+Crew Affidavit"
    
    #If primary reason is Maintenance, secondary reason is Crew and Flight Date, amount above 1500
    if  (
         ( obj.primary_reason.lower() == 'maintenance' and obj.secondary_reason.lower() == 'crew' ) and (int(obj.claim_amount) >= 1500)
        ):
        return "Full defense - Maintenance+Crew above 1500", "Yes", "Maintenance+Crew Affidavit"

    '''
    If Primary reason OR Secondary reason is "Crew" AND secondary reason (Flight date) falls during:
          Aug 7, 2021 to Sept 22, 2021
          Dec'21, Jan'22 , Feb'22
          May'22, Jun'22, Jul'22
    then Row 25 (Affidavit required) should be "Yes". Type is Crew Affidavit.
    '''
    if  (
         obj.flight_date and ( obj.primary_reason.lower() == 'crew' or obj.secondary_reason.lower() == 'crew') and
          ( 
            (obj.flight_date.year == 2022 and obj.flight_date.month in [1,2,5,6,7]) or 
            (obj.flight_date.year == 2021 and obj.flight_date.month in [12]) or 
            (datetime(2021, 8, 7, 0, 0) <= obj.flight_date <= datetime(2021, 9, 22, 0, 0))
          )
        ):
        return "Full defense-COVID", "Yes", "Crew Affidavit"


    #primary reason Political secondary reason weather , value below 1500
    if (obj.primary_reason.lower() == "political" and obj.secondary_reason.lower() == "weather" and int(obj.claim_amount) < 1500):
        return "Summary- Defence Others", "No", ""
        
    #primary reason medical emergency, secondary reason is Maintenance , value below 1500, time is below 3 hours 
    if (obj.primary_reason.lower() == "medical emergency" and obj.secondary_reason.lower() == "weather" and int(obj.claim_amount) < 1500 and obj.total_delay.hour < 3):
        return "Summary- Full Defence MTD", "No", ""
        
    #Row 14- Baggage or any combination with baggage
    if 'baggage' in obj.reason_claim.lower():
        return "Baggage", "No", ""
        
    # CTA case ID Single or multiple - Multiple and Do we have CAS ID = Yes
    if obj.cta_case_single_multiple.lower() == "multiple" and obj.cas_id_yes_no.lower() == "yes":
        return "Joinder-see comments", "No", ""

    if int(obj.claim_amount) >= 1500:
        
        #primary reason= weather and secondary reason-Crew and Claim Amount equal to or more than 1500. (Or) primary reason-Crew and secondary reason- weather and Claim Amount equal to or more than 1500
        if (
            ( obj.primary_reason.lower() == "weather" and obj.secondary_reason == "crew" ) or 
            ( obj.primary_reason.lower() == "crew" and obj.secondary_reason == "weather" )
           ):
            return "Full defense- Weather+Crew above 1500", "No", ""
            
        #primary reason= Maintenance and secondary reason-Crew and Claim Amount equal to or more than 1500. (0r) primary reason- Crew and secondary reason- Maintenance and Claim Amount equal to or more than 1500
        if (
            ( obj.primary_reason.lower() == "maintenance" and obj.secondary_reason == "crew" ) or 
            ( obj.primary_reason.lower() == "crew" and obj.secondary_reason == "maintenance" )
           ):
            return "Full defense- Maintenance+Crew above 1500", "Yes", "Maintenance+Crew Affidavit"
            
        #primary reason= weather and Claim Amount equal to or more than 1500
        if obj.primary_reason.lower() == "weather":
            return "Summary- weather above 1500", "No", ""
        
        #primary reason= Maintenance and Claim Amount equal to or more than 1500
        if obj.primary_reason.lower() == "maintenance":
            return "Summary-Maintenance above 1500", "Yes", "Maintenance Affidavit"
        
        #primary reason= ATC and Claim Amount equal to or more than 1500
        if obj.primary_reason.lower() == "atc":  
            return "Full defense-airport facilities above 1500", "No", ""
        
        #primary reason Crew and Claim Amount equal to or more than 1500
        if obj.primary_reason.lower() == "crew":    
            return "Full defense- Crew above 1500", "Yes", "Crew Affidavit"
          
        #primary reason= labour strike and Claim Amount equal to or more than 1500
        if obj.primary_reason.lower() == "labour strike":
            return "Full defense- labour strike", "No", ""

        #primary reason= schedule change and Claim Amount equal to or more than 1500
        if obj.primary_reason.lower() == "schedule change":
            return "Full defense- Schedule change", "No", ""
    
        #primary reason= political, medical emergency and Claim Amount equal to or more than 1500
        if obj.primary_reason.lower() == "political, medical emergency":
            return "Full defense- Other (political, medical emergency)", "No", ""
    
    if int(obj.claim_amount) < 1500:
        
        #primary reason= Weather and Claim Amount less than 1500
        if obj.primary_reason.lower() == "weather":
            return "Summary - Weather below 1500", "No", ""
        
        #primary reason= Maintenance and Claim Amount less than 1500
        if obj.primary_reason.lower() == "maintenance":
            return "Summary - Maintenance below 1500", "No", ""
        
        #primary reason= ATC and Claim Amount less than 1500
        if obj.primary_reason.lower() == "atc": 
            return "Summary- ATC below 1500", "No", ""

        #primary reason- Crew and Claim Amount less than 1500
        if obj.primary_reason.lower() == "crew": 
            return "Summary crew below 1500", "No", ""

        #primary reason= political, medical emergency and Row less than 1500
        if obj.primary_reason.lower() == "political, medical emergency":
            return "Summary- other (political, medical emergency)", "No", ""
    
    return "", "No", ""