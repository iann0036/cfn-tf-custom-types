# TF::Volterra::OriginPool PrivateIpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#insidenetwork" title="InsideNetwork">InsideNetwork</a>" : <i>Boolean</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#outsidenetwork" title="OutsideNetwork">OutsideNetwork</a>" : <i>Boolean</i>,
    "<a href="#sitelocator" title="SiteLocator">SiteLocator</a>" : <i>[ <a href="sitelocatordefinition.md">SiteLocatorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#insidenetwork" title="InsideNetwork">InsideNetwork</a>: <i>Boolean</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#outsidenetwork" title="OutsideNetwork">OutsideNetwork</a>: <i>Boolean</i>
<a href="#sitelocator" title="SiteLocator">SiteLocator</a>: <i>
      - <a href="sitelocatordefinition.md">SiteLocatorDefinition</a></i>
</pre>

## Properties

#### InsideNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteLocator

_Required_: No

_Type_: List of <a href="sitelocatordefinition.md">SiteLocatorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

