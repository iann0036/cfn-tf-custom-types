# TF::Volterra::AzureVnetSite GlobalNetworkConnectionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disableforwardproxy" title="DisableForwardProxy">DisableForwardProxy</a>" : <i>Boolean</i>,
    "<a href="#enableforwardproxy" title="EnableForwardProxy">EnableForwardProxy</a>" : <i>[ <a href="enableforwardproxydefinition.md">EnableForwardProxyDefinition</a>, ... ]</i>,
    "<a href="#slitoglobaldr" title="SliToGlobalDr">SliToGlobalDr</a>" : <i>[ <a href="slitoglobaldrdefinition.md">SliToGlobalDrDefinition</a>, ... ]</i>,
    "<a href="#slotoglobaldr" title="SloToGlobalDr">SloToGlobalDr</a>" : <i>[ <a href="slotoglobaldrdefinition.md">SloToGlobalDrDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disableforwardproxy" title="DisableForwardProxy">DisableForwardProxy</a>: <i>Boolean</i>
<a href="#enableforwardproxy" title="EnableForwardProxy">EnableForwardProxy</a>: <i>
      - <a href="enableforwardproxydefinition.md">EnableForwardProxyDefinition</a></i>
<a href="#slitoglobaldr" title="SliToGlobalDr">SliToGlobalDr</a>: <i>
      - <a href="slitoglobaldrdefinition.md">SliToGlobalDrDefinition</a></i>
<a href="#slotoglobaldr" title="SloToGlobalDr">SloToGlobalDr</a>: <i>
      - <a href="slotoglobaldrdefinition.md">SloToGlobalDrDefinition</a></i>
</pre>

## Properties

#### DisableForwardProxy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableForwardProxy

_Required_: No

_Type_: List of <a href="enableforwardproxydefinition.md">EnableForwardProxyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SliToGlobalDr

_Required_: No

_Type_: List of <a href="slitoglobaldrdefinition.md">SliToGlobalDrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SloToGlobalDr

_Required_: No

_Type_: List of <a href="slotoglobaldrdefinition.md">SloToGlobalDrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

