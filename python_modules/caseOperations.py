####################################
# @file         - caseOperations.py
# @contributors -  
# @Usage        - 
# @Notes        - 
####################################
import database
import newCaseTemplate

db = database.OurDB()

def GetAllCases ():
    return db.GetAllCases()
    
def viewcase (cta):
    if cta:
        CaseDetails = db.viewcase(cta)
        if CaseDetails:
            Fields = newCaseTemplate.ViewCaseFields
            Values = list(CaseDetails[0].values())[1:]
            Output = list(zip(Fields, Values))
            print (Output)
            return Output
        else:
            return "Given CTA Case ID is not found in Database, search in Dashboard once...!!!"
    else:
        return ""
      

def SubmitNewCase (obj):
    query = f'''
            insert into `case` (
                `Processing date`,
                `CTA Case ID`, `CTA case ID Single or multiple`, 
                `any other active/ inactive CTA cases`, `additional CTA IDs`,
                `Applicant name`,
                `Do we have the CAS ID?`, `Number of CAS ID's`, `additional CAS IDs`,
                `Initial deadline`, `Days left for delivery`,
                `Reason for Claim`, `Baggage claim number from CTA complaint`,
                `Primary reason for disruption`, `Secondary reasons for Disruptions`,
                `Claim amount`, `Total delay`, `Flight date`,
                `Any document that should be requested`, `Have u identified a duplicate CTA case`,
                `Verdict`,
                `Affidavit Needed`, `Affidavit Type`,
                `Evidence Missing`
            )
            values (
                '{obj.processingDate}', 
                '{obj.cta_case_id}', '{obj.cta_case_single_multiple}', 
                '{obj.any_other_cta}', '{obj.additional_cta_ids}', 
                '{obj.applicant_name}', 
                '{obj.cas_id_yes_no}', '{obj.number_cas_ids}', '{obj.additional_cas_ids}', 
                '{obj.initialDeadline}', '{obj.days_Left}', 
                '{obj.reason_claim}', '{obj.baggage_claim_number}', 
                '{obj.primary_reason}', '{obj.secondary_reason}', 
                '{obj.claim_amount}', '{obj.total_delay}', '{obj.flight_date}', 
                '{obj.additional_docs}', '{obj.duplicate_case_yes_no}', 
                '{obj.verdict}', 
                '{obj.affidavit_required_yes_no}', '{obj.affidavit_type}', 
                '{obj.evidenceMissing}'
            )
            '''
    try:
        db.execute_insertUpdate_query (query)
        return "success"
    except:
        print ("Failed to insert Data into Database, check MySQL errors..!!")
        return "failure"


if __name__ == "__main__":
    viewcase("abcdefg")