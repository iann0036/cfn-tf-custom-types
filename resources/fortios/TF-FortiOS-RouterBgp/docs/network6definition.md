# TF::FortiOS::RouterBgp Network6Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backdoor" title="Backdoor">Backdoor</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#prefix6" title="Prefix6">Prefix6</a>" : <i>String</i>,
    "<a href="#routemap" title="RouteMap">RouteMap</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backdoor" title="Backdoor">Backdoor</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#prefix6" title="Prefix6">Prefix6</a>: <i>String</i>
<a href="#routemap" title="RouteMap">RouteMap</a>: <i>String</i>
</pre>

## Properties

#### Backdoor

Enable/disable route as backdoor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix6

Network IPv6 prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMap

Route map to modify generated route.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

