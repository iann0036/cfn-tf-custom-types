# Terraform::OpenStack::ComputeInstanceV2 SchedulerHints

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>[ <a href="schedulerhints-additionalproperties.md">AdditionalProperties</a>, ... ]</i>,
    "<a href="#buildnearhostip" title="BuildNearHostIp">BuildNearHostIp</a>" : <i>String</i>,
    "<a href="#differenthost" title="DifferentHost">DifferentHost</a>" : <i>[ String, ... ]</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ String, ... ]</i>,
    "<a href="#samehost" title="SameHost">SameHost</a>" : <i>[ String, ... ]</i>,
    "<a href="#targetcell" title="TargetCell">TargetCell</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>
      - <a href="schedulerhints-additionalproperties.md">AdditionalProperties</a></i>
<a href="#buildnearhostip" title="BuildNearHostIp">BuildNearHostIp</a>: <i>String</i>
<a href="#differenthost" title="DifferentHost">DifferentHost</a>: <i>
      - String</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>
      - String</i>
<a href="#samehost" title="SameHost">SameHost</a>: <i>
      - String</i>
<a href="#targetcell" title="TargetCell">TargetCell</a>: <i>String</i>
</pre>

## Properties

#### AdditionalProperties

_Required_: No
_Type_: List of <a href="schedulerhints-additionalproperties.md">AdditionalProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildNearHostIp

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DifferentHost

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SameHost

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetCell

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

