# Terraform::AzureRM::ServiceFabricCluster NodeType

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capacities" title="Capacities">Capacities</a>" : <i>[ &lt;a href=&#34;nodetype-capacities.md&#34;&gt;Capacities&lt;/a&gt;, ... ]</i>,
    "<a href="#clientendpointport" title="ClientEndpointPort">ClientEndpointPort</a>" : <i>Double</i>,
    "<a href="#durabilitylevel" title="DurabilityLevel">DurabilityLevel</a>" : <i>String</i>,
    "<a href="#httpendpointport" title="HttpEndpointPort">HttpEndpointPort</a>" : <i>Double</i>,
    "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
    "<a href="#isprimary" title="IsPrimary">IsPrimary</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#placementproperties" title="PlacementProperties">PlacementProperties</a>" : <i>[ &lt;a href=&#34;nodetype-placementproperties.md&#34;&gt;PlacementProperties&lt;/a&gt;, ... ]</i>,
    "<a href="#reverseproxyendpointport" title="ReverseProxyEndpointPort">ReverseProxyEndpointPort</a>" : <i>Double</i>,
    "<a href="#applicationports" title="ApplicationPorts">ApplicationPorts</a>" : <i>[ &lt;a href=&#34;nodetype-applicationports.md&#34;&gt;ApplicationPorts&lt;/a&gt;, ... ]</i>,
    "<a href="#ephemeralports" title="EphemeralPorts">EphemeralPorts</a>" : <i>[ &lt;a href=&#34;nodetype-ephemeralports.md&#34;&gt;EphemeralPorts&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#capacities" title="Capacities">Capacities</a>: <i>
      - &lt;a href=&#34;nodetype-capacities.md&#34;&gt;Capacities&lt;/a&gt;</i>
<a href="#clientendpointport" title="ClientEndpointPort">ClientEndpointPort</a>: <i>Double</i>
<a href="#durabilitylevel" title="DurabilityLevel">DurabilityLevel</a>: <i>String</i>
<a href="#httpendpointport" title="HttpEndpointPort">HttpEndpointPort</a>: <i>Double</i>
<a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
<a href="#isprimary" title="IsPrimary">IsPrimary</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#placementproperties" title="PlacementProperties">PlacementProperties</a>: <i>
      - &lt;a href=&#34;nodetype-placementproperties.md&#34;&gt;PlacementProperties&lt;/a&gt;</i>
<a href="#reverseproxyendpointport" title="ReverseProxyEndpointPort">ReverseProxyEndpointPort</a>: <i>Double</i>
<a href="#applicationports" title="ApplicationPorts">ApplicationPorts</a>: <i>
      - &lt;a href=&#34;nodetype-applicationports.md&#34;&gt;ApplicationPorts&lt;/a&gt;</i>
<a href="#ephemeralports" title="EphemeralPorts">EphemeralPorts</a>: <i>
      - &lt;a href=&#34;nodetype-ephemeralports.md&#34;&gt;EphemeralPorts&lt;/a&gt;</i>
</pre>

## Properties

#### Capacities

_Required_: No
_Type_: List of &lt;a href=&#34;nodetype-capacities.md&#34;&gt;Capacities&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientEndpointPort

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DurabilityLevel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpEndpointPort

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPrimary

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementProperties

_Required_: No
_Type_: List of &lt;a href=&#34;nodetype-placementproperties.md&#34;&gt;PlacementProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseProxyEndpointPort

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationPorts

_Required_: No
_Type_: List of &lt;a href=&#34;nodetype-applicationports.md&#34;&gt;ApplicationPorts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralPorts

_Required_: No
_Type_: List of &lt;a href=&#34;nodetype-ephemeralports.md&#34;&gt;EphemeralPorts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

