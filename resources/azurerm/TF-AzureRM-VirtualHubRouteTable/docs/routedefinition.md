# TF::AzureRM::VirtualHubRouteTable RouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinations" title="Destinations">Destinations</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationstype" title="DestinationsType">DestinationsType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nexthop" title="NextHop">NextHop</a>" : <i>String</i>,
    "<a href="#nexthoptype" title="NextHopType">NextHopType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#destinations" title="Destinations">Destinations</a>: <i>
      - String</i>
<a href="#destinationstype" title="DestinationsType">DestinationsType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nexthop" title="NextHop">NextHop</a>: <i>String</i>
<a href="#nexthoptype" title="NextHopType">NextHopType</a>: <i>String</i>
</pre>

## Properties

#### Destinations

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationsType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHop

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

