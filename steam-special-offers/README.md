# 🕹️ Steam Special Offers

## Deployment
```
cd steam-special-offers

# 1st Deployment
sam build & sam deploy --guided --capabilities CAPABILITY_NAMED_IAM

# Update
sam build & sam deploy --no-confirm-changeset --no-disable-rollback --capabilities CAPABILITY_NAMED_IAM

# Register Command
pip install requests -t helpers && python helpers/register_commands.py
```

## Packages
```
# cd steam-special-offers
# mkdir -p layer/python
# pip install requests -t ./layer/python
# Zip layer/ -> layer.zip

requests
```