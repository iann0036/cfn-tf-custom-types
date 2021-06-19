# TF::Volterra::AdvertisePolicy WhereDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#site" title="Site">Site</a>" : <i>[ <a href="sitedefinition.md">SiteDefinition</a>, ... ]</i>,
    "<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>" : <i>[ <a href="virtualnetworkdefinition.md">VirtualNetworkDefinition</a>, ... ]</i>,
    "<a href="#virtualsite" title="VirtualSite">VirtualSite</a>" : <i>[ <a href="virtualsitedefinition.md">VirtualSiteDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#site" title="Site">Site</a>: <i>
      - <a href="sitedefinition.md">SiteDefinition</a></i>
<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>: <i>
      - <a href="virtualnetworkdefinition.md">VirtualNetworkDefinition</a></i>
<a href="#virtualsite" title="VirtualSite">VirtualSite</a>: <i>
      - <a href="virtualsitedefinition.md">VirtualSiteDefinition</a></i>
</pre>

## Properties

#### Site

_Required_: No

_Type_: List of <a href="sitedefinition.md">SiteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetwork

_Required_: No

_Type_: List of <a href="virtualnetworkdefinition.md">VirtualNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualSite

_Required_: No

_Type_: List of <a href="virtualsitedefinition.md">VirtualSiteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

