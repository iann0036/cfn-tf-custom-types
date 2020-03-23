# Terraform::AWS::KinesisFirehoseDeliveryStream Parameters

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#parametername" title="ParameterName">ParameterName</a>" : <i>String</i>,
    "<a href="#parametervalue" title="ParameterValue">ParameterValue</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#parametername" title="ParameterName">ParameterName</a>: <i>String</i>
<a href="#parametervalue" title="ParameterValue">ParameterValue</a>: <i>String</i>
</pre>

## Properties

#### ParameterName

Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterValue

Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

