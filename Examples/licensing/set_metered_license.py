from groupdocs.redaction import Metered

def set_metered_license():
    # Replace these placeholders with your real metered public/private keys
    public_key = "*****"
    private_key = "*****"

    # Skip the call until real keys are supplied (placeholder keys are rejected)
    if "*" in public_key or "*" in private_key:
        print("Provide real metered keys to enable metered licensing.")
        return

    # Apply the metered keys before using any redaction features
    Metered().set_metered_key(public_key, private_key)

    # Query the current metered consumption
    quantity = Metered().get_consumption_quantity()
    credit = Metered().get_consumption_credit()
    print(f"Consumption quantity: {quantity}, credit: {credit}")

if __name__ == "__main__":
    set_metered_license()