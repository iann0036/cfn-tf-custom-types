# CloudFormation Custom Types for Terraform

[![Resource Count](https://img.shields.io/badge/resource%20count-6984-blue.svg)](docs/README.md)

> Deploy over 6,000 new resource types with CloudFormation custom types.

<img src="https://github.com/iann0036/cfn-tf-custom-types/raw/master/assets/screen1.png" width="536" height="417">

:exclamation: **CAUTION:** This project is currently in beta stages. Some resources may not work as expected. Please [report these](https://github.com/iann0036/cfn-tf-custom-types/issues) if you find them.


This project registers the CloudFormation equivalent of any official or verified Terraform provider resources and allows you to manage the lifecycle of these types using CloudFormation.

## Installation

To use the types, you must first deploy the Execution Infrastructure (which is responsible for running Terraform within your account) then perform the resource registration step for each type you intend to use.

### Execution Infrastructure

[![Launch Stack](https://cdn.rawgit.com/buildkite/cloudformation-launch-stack-button-svg/master/launch-stack.svg)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=tfcfn-custom-type-resources&templateURL=https://s3.amazonaws.com/ianmckay-us-east-1/cfn-tf-custom-types/template.yml)

Click the above link to deploy the stack to your environment. This stack creates a single bucket in your account for the storage of state data, as well as a Lambda function that is used to execute the Terraform actions.

If you prefer, you can also manually upsert the [template.yml](https://github.com/iann0036/cfn-tf-custom-types/blob/master/template.yml) stack from source.

### Resource Registration

Resources may be registered from the AWS CloudFormation Public Registry. At the time of writing, only a small set of resources are supported due to limitations with service limits.

To register the type, click the "Activate" button from the Registry: Public Extensions area. You may override the default type if you wish. For the "Execution role ARN" field, the outputs of the Execution Infrastructure stack has an ARN you may use. Logging config may be left blank and automatic updates is recommended to be enabled.

If your desired type is not yet available, you can generate the type privately yourself using the instructions in the below expandable section:

<details>
  <summary>Click here for resource generation instructions:</summary>

### Resource Generation

#### Requirements

The below requirements must be installed and be available in PATH:

* Python 3
* Git
* Docker
* Terraform 0.15+
* CloudFormation CLI with Python Provider

#### Generation

To generate the custom type source files, run:

```
python3 generate.py <providername>
# For example:
python3 generate.py aws
```

Note that generating all files may take several minutes depending upon the amount of resources the provider has.

You can also use `all` as the provider name to generate resources for all providers. Note this can take some hours to complete.

#### Submission

Once you have generated the required resource files, you can submit the type to the CloudFormation registry by running the following:

```
python3 submit.py <resourcename>
# For example:
python3 submit.py TF::AWS::Instance
```

Note that resource submission will also generally take several minutes.

</details>

## Resource Usage

Most providers will require you to store credentials and/or other provider-specific settings within AWS Secrets Manager in order to access their services, generally in the secret name format **terraform/_provider-name-lowercase_**. For the AWS provider only, the resources permissions will suffice, however you may choose to override those values in the secret.

A full list of documentation can be found [here](docs/README.md).

You can use a submitted resource like any other CloudFormation native resource, provided you follow the appropriate documentation. Check out some of the [examples](https://github.com/iann0036/cfn-tf-custom-types/tree/master/examples) to get started.

## How It Works

![Architecture Diagram](assets/arch.png)

## Acknowledgements

This project would not be possible without the work from the contributors to Terraform providers and the Terraform core product.
