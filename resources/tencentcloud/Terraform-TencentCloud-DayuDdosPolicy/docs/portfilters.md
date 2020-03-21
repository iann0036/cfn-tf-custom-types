# Terraform::TencentCloud::DayuDdosPolicy PortFilters

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#endport" title="EndPort">EndPort</a>" : <i>Double</i>,
    "<a href="#kind" title="Kind">Kind</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#startport" title="StartPort">StartPort</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#endport" title="EndPort">EndPort</a>: <i>Double</i>
<a href="#kind" title="Kind">Kind</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#startport" title="StartPort">StartPort</a>: <i>Double</i>
</pre>

## Properties

#### Action

Action of port to take, valid values area `drop`, `transmit`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndPort

End port, valid value is range from 0 to 65535. It must be greater than `start_port`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

The type of forbidden port, and valid values are 0, 1, 2. 0 for destination ports make effect, 1 for source ports make effect. 2 for both destination and source ports.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol, valid values are `tcp`, `udp`, `icmp`, `all`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartPort

Start port, valid value is range from 0 to 65535.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

