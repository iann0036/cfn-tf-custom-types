# TF::FortiOS::SwitchcontrollerqosIpdscpmap MapDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cosqueue" title="CosQueue">CosQueue</a>" : <i>Double</i>,
    "<a href="#diffserv" title="Diffserv">Diffserv</a>" : <i>String</i>,
    "<a href="#ipprecedence" title="IpPrecedence">IpPrecedence</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cosqueue" title="CosQueue">CosQueue</a>: <i>Double</i>
<a href="#diffserv" title="Diffserv">Diffserv</a>: <i>String</i>
<a href="#ipprecedence" title="IpPrecedence">IpPrecedence</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### CosQueue

COS queue number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diffserv

Differentiated service. Valid values: `CS0`, `CS1`, `AF11`, `AF12`, `AF13`, `CS2`, `AF21`, `AF22`, `AF23`, `CS3`, `AF31`, `AF32`, `AF33`, `CS4`, `AF41`, `AF42`, `AF43`, `CS5`, `EF`, `CS6`, `CS7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrecedence

IP Precedence. Valid values: `network-control`, `internetwork-control`, `critic-ecp`, `flashoverride`, `flash`, `immediate`, `priority`, `routine`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Dscp mapping entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

Raw values of DSCP (0 - 63).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

