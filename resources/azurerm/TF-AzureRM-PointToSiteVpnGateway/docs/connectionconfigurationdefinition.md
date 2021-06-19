# TF::AzureRM::PointToSiteVpnGateway ConnectionConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#route" title="Route">Route</a>" : <i>[ <a href="routedefinition.md">RouteDefinition</a>, ... ]</i>,
    "<a href="#vpnclientaddresspool" title="VpnClientAddressPool">VpnClientAddressPool</a>" : <i>[ <a href="vpnclientaddresspooldefinition.md">VpnClientAddressPoolDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#route" title="Route">Route</a>: <i>
      - <a href="routedefinition.md">RouteDefinition</a></i>
<a href="#vpnclientaddresspool" title="VpnClientAddressPool">VpnClientAddressPool</a>: <i>
      - <a href="vpnclientaddresspooldefinition.md">VpnClientAddressPoolDefinition</a></i>
</pre>

## Properties

#### Name

The Name which should be used for this Connection Configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

_Required_: No

_Type_: List of <a href="routedefinition.md">RouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnClientAddressPool

_Required_: No

_Type_: List of <a href="vpnclientaddresspooldefinition.md">VpnClientAddressPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

