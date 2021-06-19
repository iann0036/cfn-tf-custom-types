# TF::AVI::Vrfcontext StaticRoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablegatewaymonitor" title="DisableGatewayMonitor">DisableGatewayMonitor</a>" : <i>Boolean</i>,
    "<a href="#ifname" title="IfName">IfName</a>" : <i>String</i>,
    "<a href="#routeid" title="RouteId">RouteId</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#nexthop" title="NextHop">NextHop</a>" : <i>[ <a href="nexthopdefinition.md">NextHopDefinition</a>, ... ]</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>[ <a href="prefixdefinition.md">PrefixDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablegatewaymonitor" title="DisableGatewayMonitor">DisableGatewayMonitor</a>: <i>Boolean</i>
<a href="#ifname" title="IfName">IfName</a>: <i>String</i>
<a href="#routeid" title="RouteId">RouteId</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#nexthop" title="NextHop">NextHop</a>: <i>
      - <a href="nexthopdefinition.md">NextHopDefinition</a></i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>
      - <a href="prefixdefinition.md">PrefixDefinition</a></i>
</pre>

## Properties

#### DisableGatewayMonitor

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IfName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHop

_Required_: No

_Type_: List of <a href="nexthopdefinition.md">NextHopDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

_Required_: No

_Type_: List of <a href="prefixdefinition.md">PrefixDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

