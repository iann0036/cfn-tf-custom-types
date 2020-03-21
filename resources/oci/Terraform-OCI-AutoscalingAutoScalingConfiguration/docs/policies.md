# Terraform::OCI::AutoscalingAutoScalingConfiguration Policies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#policytype" title="PolicyType">PolicyType</a>" : <i>String</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ <a href="policies-capacity.md">Capacity</a>, ... ]</i>,
    "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="policies-rules.md">Rules</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#policytype" title="PolicyType">PolicyType</a>: <i>String</i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - <a href="policies-capacity.md">Capacity</a></i>
<a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="policies-rules.md">Rules</a></i>
</pre>

## Properties

#### DisplayName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No
_Type_: List of <a href="policies-capacity.md">Capacity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No
_Type_: List of <a href="policies-rules.md">Rules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

