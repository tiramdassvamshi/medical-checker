# Medicine Drug-Drug Interactions Database
# This file contains all known medicine interactions

MEDICINE_INTERACTIONS = {
    "Aspirin": {
        "Warfarin": {
            "severity": "High",
            "description": "Increased risk of bleeding. Aspirin enhances anticoagulant effect.",
            "recommendation": "Avoid combination or monitor closely for bleeding signs"
        },
        "Ibuprofen": {
            "severity": "High",
            "description": "Both are NSAIDs - increased risk of GI bleeding and ulcers",
            "recommendation": "Do not combine. Use only one NSAID"
        },
        "Methotrexate": {
            "severity": "Medium",
            "description": "Aspirin may reduce methotrexate clearance",
            "recommendation": "Monitor kidney function and methotrexate levels"
        }
    },
    "Warfarin": {
        "Ibuprofen": {
            "severity": "High",
            "description": "NSAIDs increase bleeding risk with anticoagulants",
            "recommendation": "Use acetaminophen instead of NSAIDs"
        },
        "Aspirin": {
            "severity": "High",
            "description": "Increased risk of bleeding",
            "recommendation": "Avoid combination or monitor closely"
        },
        "Amoxicillin": {
            "severity": "Medium",
            "description": "Antibiotics may enhance warfarin effect",
            "recommendation": "Monitor INR closely"
        }
    },
    "Metformin": {
        "Alcohol": {
            "severity": "Medium",
            "description": "Increased risk of lactic acidosis",
            "recommendation": "Limit alcohol consumption"
        },
        "Contrast dye": {
            "severity": "High",
            "description": "Risk of acute kidney injury",
            "recommendation": "Temporarily discontinue before imaging procedures"
        }
    },
    "Lisinopril": {
        "Potassium": {
            "severity": "High",
            "description": "Both increase potassium levels - hyperkalemia risk",
            "recommendation": "Monitor potassium levels regularly"
        },
        "NSAIDs": {
            "severity": "Medium",
            "description": "Reduced blood pressure control and kidney function",
            "recommendation": "Use with caution, monitor kidney function"
        }
    },
    "Atorvastatin": {
        "Erythromycin": {
            "severity": "High",
            "description": "Increased statin levels - myopathy risk",
            "recommendation": "Avoid combination or use alternative antibiotic"
        },
        "Grapefruit": {
            "severity": "Medium",
            "description": "Grapefruit inhibits statin metabolism",
            "recommendation": "Avoid grapefruit juice"
        }
    },
    "Amoxicillin": {
        "Warfarin": {
            "severity": "Medium",
            "description": "Antibiotic may enhance warfarin effect",
            "recommendation": "Monitor INR"
        }
    },
    "Ibuprofen": {
        "Aspirin": {
            "severity": "High",
            "description": "Duplicate NSAID therapy",
            "recommendation": "Use only one NSAID"
        },
        "Warfarin": {
            "severity": "High",
            "description": "Increased bleeding risk",
            "recommendation": "Use acetaminophen instead"
        }
    }
}

def check_medicine_interactions(medicine_list):
    """
    Check for interactions between medicines in the list
    
    Args:
        medicine_list: List of medicine names
    
    Returns:
        Dictionary with interaction results
    """
    interactions_found = []
    warnings = []
    
    # Check each pair of medicines
    for i in range(len(medicine_list)):
        for j in range(i + 1, len(medicine_list)):
            med1 = medicine_list[i].strip()
            med2 = medicine_list[j].strip()
            
            # Check for interaction in both directions
            if med1 in MEDICINE_INTERACTIONS:
                if med2 in MEDICINE_INTERACTIONS[med1]:
                    interaction = MEDICINE_INTERACTIONS[med1][med2]
                    interactions_found.append({
                        "medicine1": med1,
                        "medicine2": med2,
                        "severity": interaction["severity"],
                        "description": interaction["description"],
                        "recommendation": interaction["recommendation"]
                    })
                    warnings.append(interaction["severity"])
            
            elif med2 in MEDICINE_INTERACTIONS:
                if med1 in MEDICINE_INTERACTIONS[med2]:
                    interaction = MEDICINE_INTERACTIONS[med2][med1]
                    interactions_found.append({
                        "medicine1": med2,
                        "medicine2": med1,
                        "severity": interaction["severity"],
                        "description": interaction["description"],
                        "recommendation": interaction["recommendation"]
                    })
                    warnings.append(interaction["severity"])
    
    # Determine overall risk level
    overall_risk = "Low"
    if "High" in warnings:
        overall_risk = "High"
    elif "Medium" in warnings:
        overall_risk = "Medium"
    
    return {
        "interactions": interactions_found,
        "overall_risk": overall_risk,
        "interaction_count": len(interactions_found)
    }