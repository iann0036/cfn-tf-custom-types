# TF::FortiOS::RouterOspf6 SummaryAddressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#advertise" title="Advertise">Advertise</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#prefix6" title="Prefix6">Prefix6</a>" : <i>String</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#advertise" title="Advertise">Advertise</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#prefix6" title="Prefix6">Prefix6</a>: <i>String</i>
<a href="#tag" title="Tag">Tag</a>: <i>Double</i>
</pre>

## Properties

#### Advertise

Enable/disable advertise status. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Summary address entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix6

IPv6 prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

Tag value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

