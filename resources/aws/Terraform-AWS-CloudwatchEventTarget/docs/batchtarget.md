# Terraform::AWS::CloudwatchEventTarget BatchTarget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arraysize" title="ArraySize">ArraySize</a>" : <i>Double</i>,
    "<a href="#jobattempts" title="JobAttempts">JobAttempts</a>" : <i>Double</i>,
    "<a href="#jobdefinition" title="JobDefinition">JobDefinition</a>" : <i>String</i>,
    "<a href="#jobname" title="JobName">JobName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#arraysize" title="ArraySize">ArraySize</a>: <i>Double</i>
<a href="#jobattempts" title="JobAttempts">JobAttempts</a>: <i>Double</i>
<a href="#jobdefinition" title="JobDefinition">JobDefinition</a>: <i>String</i>
<a href="#jobname" title="JobName">JobName</a>: <i>String</i>
</pre>

## Properties

#### ArraySize

The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobAttempts

The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobDefinition

The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobName

The name to use for this execution of the job, if the target is an AWS Batch job.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

