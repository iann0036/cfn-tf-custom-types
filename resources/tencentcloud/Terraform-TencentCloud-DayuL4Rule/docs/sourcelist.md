# Terraform::TencentCloud::DayuL4Rule SourceList

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### Source

Source ip or domain, valid format of ip is like `1.1.1.1` and valid format of host source is like `abc.com`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Weight of the source, the valid value ranges from 0 to 100.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

