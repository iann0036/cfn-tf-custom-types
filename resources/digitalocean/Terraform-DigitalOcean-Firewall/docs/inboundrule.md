# Terraform::DigitalOcean::Firewall InboundRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#portrange" title="PortRange">PortRange</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcedropletids" title="SourceDropletIds">SourceDropletIds</a>" : <i>[ Double, ... ]</i>,
    "<a href="#sourceloadbalanceruids" title="SourceLoadBalancerUids">SourceLoadBalancerUids</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcetags" title="SourceTags">SourceTags</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#portrange" title="PortRange">PortRange</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
<a href="#sourcedropletids" title="SourceDropletIds">SourceDropletIds</a>: <i>
      - Double</i>
<a href="#sourceloadbalanceruids" title="SourceLoadBalancerUids">SourceLoadBalancerUids</a>: <i>
      - String</i>
<a href="#sourcetags" title="SourceTags">SourceTags</a>: <i>
      - String</i>
</pre>

## Properties

#### PortRange

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDropletIds

_Required_: No
_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceLoadBalancerUids

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceTags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

