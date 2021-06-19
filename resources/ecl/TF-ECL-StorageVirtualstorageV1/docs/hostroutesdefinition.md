# TF::ECL::StorageVirtualstorageV1 HostRoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
    "<a href="#nexthop" title="Nexthop">Nexthop</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#destination" title="Destination">Destination</a>: <i>String</i>
<a href="#nexthop" title="Nexthop">Nexthop</a>: <i>String</i>
</pre>

## Properties

#### Destination

Destination CIDR of this routing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nexthop

Nexthop IP address of this routing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

