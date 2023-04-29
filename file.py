from azure.identity import DefaultAzureCredential
from azure.mgmt.billing import BillingManagementClient
from azure.mgmt.billing.models import Address

credential = DefaultAzureCredential()
client = BillingManagementClient(credential=credential, subscription_id='9366fe78-fc69-43dd-b594-b10bff70d0f8')

address = Address(
    address_line1='ADDRESS_LINE_1_HERE',
    address_line2='ADDRESS_LINE_2_HERE',
    city='CITY_HERE',
    country='COUNTRY_HERE',
    postal_code='POSTAL_CODE_HERE',
    region='REGION_HERE'
)

response = client.address.validate(address=address)

if response.status == "Invalid":
    print("Address validation failed:")
    print(response.reasons)
else:
    validated_address = response.address
    print("Validated address:")
    print(f"\tAddress line 1: {validated_address.address_line1}")
    print(f"\tAddress line 2: {validated_address.address_line2}")
    print(f"\tCity: {validated_address.city}")
    print(f"\tCountry: {validated_address.country}")
    print(f"\tPostal code: {validated_address.postal_code}")
    print(f"\tRegion: {validated_address.region}")
