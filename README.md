# Terraform Custom Types

> Deploy over 2,000 new resource types with CloudFormation custom types.

<img src="https://github.com/iann0036/cfn-tf-custom-types/raw/master/assets/screen1.png" width="558" height="491">

:exclamation: **CAUTION:** This project is currently in beta stages. Some resources may not work as expected. Please [report these](https://github.com/iann0036/cfn-tf-custom-types/issues) if you find them.


## Requirements

* Python 3
* Git
* Terraform
* CloudFormation CLI
* CloudFormation CLI Python Provider (currently expects slot 4)

## Installation

### State Bucket

[![Launch Stack](https://cdn.rawgit.com/buildkite/cloudformation-launch-stack-button-svg/master/launch-stack.svg)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=terraform-cloudformation-state-bucket&templateURL=https://s3.amazonaws.com/ianmckay-us-east-1/cf-tf-custom-types/template.yml)

Click the above link to deploy the stack to your environment. This stack creates a single bucket in your account for the storage of state data.

If you prefer, you can also manually upsert the [template.yml](https://github.com/iann0036/cf-tf-custom-types/blob/master/template.yml) stack from source.

### Resource Generation

To generate the custom type source files, run:

```
python3 generate.py <providername>
# For example:
python3 generate.py aws
```

Note that generating all files may take several minutes depending upon the amount of resources the provider has.

Once you have generated the required resource files, you can submit the type by running the following:

```
python3 upload.py <resourcename>
# For example:
python3 upload.py Terraform::AWS::Instance
```

Note that resource submission will also generally take several minutes.

### Resource Usage

*TBC*