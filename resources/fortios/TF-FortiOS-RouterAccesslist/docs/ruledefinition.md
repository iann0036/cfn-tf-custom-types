# TF::FortiOS::RouterAccesslist RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#exactmatch" title="ExactMatch">ExactMatch</a>" : <i>String</i>,
    "<a href="#flags" title="Flags">Flags</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#wildcard" title="Wildcard">Wildcard</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#exactmatch" title="ExactMatch">ExactMatch</a>: <i>String</i>
<a href="#flags" title="Flags">Flags</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#wildcard" title="Wildcard">Wildcard</a>: <i>String</i>
</pre>

## Properties

#### Action

Permit or deny this IP address and netmask prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExactMatch

Enable/disable exact match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flags

Flags.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Rule ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

IPv4 prefix to define regular filter criteria, such as "any" or subnets.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wildcard

Wildcard to define Cisco-style wildcard filter criteria.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
