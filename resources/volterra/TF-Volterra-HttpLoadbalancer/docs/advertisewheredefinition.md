# TF::Volterra::HttpLoadbalancer AdvertiseWhereDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#usedefaultport" title="UseDefaultPort">UseDefaultPort</a>" : <i>Boolean</i>,
    "<a href="#site" title="Site">Site</a>" : <i>[ <a href="sitedefinition.md">SiteDefinition</a>, ... ]</i>,
    "<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>" : <i>[ <a href="virtualnetworkdefinition.md">VirtualNetworkDefinition</a>, ... ]</i>,
    "<a href="#virtualsite" title="VirtualSite">VirtualSite</a>" : <i>[ <a href="virtualsitedefinition.md">VirtualSiteDefinition</a>, ... ]</i>,
    "<a href="#vk8sservice" title="Vk8sService">Vk8sService</a>" : <i>[ <a href="vk8sservicedefinition.md">Vk8sServiceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#usedefaultport" title="UseDefaultPort">UseDefaultPort</a>: <i>Boolean</i>
<a href="#site" title="Site">Site</a>: <i>
      - <a href="sitedefinition.md">SiteDefinition</a></i>
<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>: <i>
      - <a href="virtualnetworkdefinition.md">VirtualNetworkDefinition</a></i>
<a href="#virtualsite" title="VirtualSite">VirtualSite</a>: <i>
      - <a href="virtualsitedefinition.md">VirtualSiteDefinition</a></i>
<a href="#vk8sservice" title="Vk8sService">Vk8sService</a>: <i>
      - <a href="vk8sservicedefinition.md">Vk8sServiceDefinition</a></i>
</pre>

## Properties

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Vk8sService

_Required_: No

_Type_: List of <a href="vk8sservicedefinition.md">Vk8sServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

