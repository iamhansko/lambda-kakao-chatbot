# ✊✌️🖐️ Rock Scissors Paper

## Deployment
```
cd rock-scissors-paper

# 1st Deployment
sam build & sam deploy --guided --capabilities CAPABILITY_NAMED_IAM

# Update
sam build & sam deploy --no-confirm-changeset --no-disable-rollback --capabilities CAPABILITY_NAMED_IAM

# Register Command
pip install requests -t helpers && python helpers/register_commands.py
```

## Packages
```
# cd rock-scissors-paper
# mkdir -p layer/python
# pip install requests -t ./layer/python
# Zip layer/ -> layer.zip

requests
```