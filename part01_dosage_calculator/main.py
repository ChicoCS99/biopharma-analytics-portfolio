
# Drug Dosage Calculator 
print("--- Clinical Dosage Calculator ---")
print("This tool calculates total medication dosage based on patient weight.\n")


patients_name = input("Enter the patient's name: ")
weight = float(input("Enter the patient's weight in kg: "))

# Calculate the drug dosage based on weight
# Assuming the dosage is 5 mg per kg of body weight

dose_per_kg = 5  # mg/kg
total_dosage = weight * dose_per_kg  # mg

#calculate the volume of the drug to be administered
# Assuming the drug concentration is 10 mg/ml
drug_concentration = 10  # mg/ml
volume_to_administer = total_dosage / drug_concentration  # ml

#check if the calculated dosage exceeds the maximum allowed dosage

max_dosage = 500  # mg

try:
    if total_dosage > max_dosage:
        raise ValueError(f"The calculated dosage of {total_dosage} mg exceeds the maximum allowed dosage of {max_dosage} mg.")
    else:    
        print(f"The calculated dosage for {patients_name} is {total_dosage} mg, which corresponds to {volume_to_administer} ml of the drug.")
except ValueError as error:
    print(f"Error: {error}")    

# Note: This is a simple drug dosage calculator and should not be used for actual medical purposes without consulting a healthcare professional. 
# Always verify dosages with a qualified medical practitioner.