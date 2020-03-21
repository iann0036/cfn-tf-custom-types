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

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobAttempts

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobDefinition

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

