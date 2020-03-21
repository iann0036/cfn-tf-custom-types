# Terraform::DigitalOcean::Firewall OutboundRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationdropletids" title="DestinationDropletIds">DestinationDropletIds</a>" : <i>[ Double, ... ]</i>,
    "<a href="#destinationloadbalanceruids" title="DestinationLoadBalancerUids">DestinationLoadBalancerUids</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationtags" title="DestinationTags">DestinationTags</a>" : <i>[ String, ... ]</i>,
    "<a href="#portrange" title="PortRange">PortRange</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>: <i>
      - String</i>
<a href="#destinationdropletids" title="DestinationDropletIds">DestinationDropletIds</a>: <i>
      - Double</i>
<a href="#destinationloadbalanceruids" title="DestinationLoadBalancerUids">DestinationLoadBalancerUids</a>: <i>
      - String</i>
<a href="#destinationtags" title="DestinationTags">DestinationTags</a>: <i>
      - String</i>
<a href="#portrange" title="PortRange">PortRange</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### DestinationAddresses

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationDropletIds

_Required_: No
_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationLoadBalancerUids

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationTags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRange

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

