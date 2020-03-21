# Terraform::OpenTelekomCloud::CesAlarmrule Dimensions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Name

Specifies the dimension name. The value can be a string
of 1 to 32 characters that must start with a letter and can consists of uppercase
letters, lowercase letters, numbers, underscores (_), or hyphens (-).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

Specifies the dimension value. The value can be a string
of 1 to 64 characters that must start with a letter or a number and can consists
of uppercase letters, lowercase letters, numbers, underscores (_), or hyphens
(-).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

