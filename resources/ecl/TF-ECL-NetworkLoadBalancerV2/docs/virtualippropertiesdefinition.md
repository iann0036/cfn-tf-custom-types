# TF::ECL::NetworkLoadBalancerV2 VirtualIpPropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#vrid" title="Vrid">Vrid</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#vrid" title="Vrid">Vrid</a>: <i>Double</i>
</pre>

## Properties

#### Protocol

Redundancy Protocol. Must be "vrrp".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrid

VRRP group identifier. This value is integer,
no less than 1 and no more than 255.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

