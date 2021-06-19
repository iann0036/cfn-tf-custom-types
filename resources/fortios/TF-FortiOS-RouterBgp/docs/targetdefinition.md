# TF::FortiOS::RouterBgp TargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
    "<a href="#routemap" title="RouteMap">RouteMap</a>" : <i>String</i>,
    "<a href="#vrf" title="Vrf">Vrf</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#interface" title="Interface">Interface</a>: <i>String</i>
<a href="#routemap" title="RouteMap">RouteMap</a>: <i>String</i>
<a href="#vrf" title="Vrf">Vrf</a>: <i>String</i>
</pre>

## Properties

#### Interface

Interface which is used to leak routes to target VRF.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMap

Route map of VRF leaking.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrf

Target VRF ID <0 - 31>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

