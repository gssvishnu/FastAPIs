import pydantic
from typing import Union

class newCase(pydantic.BaseModel):
    processingDate              : Union[str, None] = None
    cta_case_id                 : Union[str, None] = None
    cta_case_single_multiple    : Union[str, None] = ''
    additional_cta_ids          : Union[str, None] = None
    any_other_cta               : Union[str, None] = None
    applicant_name              : Union[str, None] = None
    cas_id_yes_no               : Union[str, None] = ''
    number_cas_ids              : Union[str, None] = None
    additional_cas_ids          : Union[str, None] = None
    initialDeadline             : Union[str, None] = None
    days_Left                   : Union[str, None] = None
    reason_claim                : Union[str, None] = None
    baggage_claim_number        : Union[str, None] = None
    primary_reason              : Union[str, None] = None
    secondary_reason            : Union[str, None] = None
    claim_amount                : Union[str, None] = None
    total_delay                 : Union[str, None] = None
    flight_date                 : Union[str, None] = None
    additional_docs             : Union[str, None] = None
    duplicate_case_yes_no       : Union[str, None] = ''
    
#This class extends newCase and gets additional values
class SubmitCase(newCase):
    verdict                     : Union[str, None] = None
    affidavit_required_yes_no   : Union[str, None] = None
    affidavit_type              : Union[str, None] = None
    evidenceMissing             : Union[str, None] = None
    
    
ViewCaseFields = [
    'Processing date', 
    'CTA Case ID', 
    'CTA case ID Single or multiple', 
    'Are there any other active/ inactive CTA cases with the same flight number, date and PNR?', 
    'Additional CTA IDs',
    'Applicant name', 
    'Do we have the CAS ID?', 
    'Number of CAS IDs',
    'Additional CAS IDs',
    'Initial deadline', 
    'Days left for delivery', 
    'Reason for Claim', 
    'Baggage claim number from CTA complaint', 
    'Primary reason for disruption', 
    'Secondary reasons for Disruptions', 
    'Claim amount', 
    'Total delay', 
    'Flight date', 
    'Is there any document that should be requested (Example: Crew details Missing)', 
    'Have u identified a duplicate CTA case', 
    'Verdict', 
    'Is Affidavit Needed?',
    'Affidavit Type',
    'Evidence Missing'
] 