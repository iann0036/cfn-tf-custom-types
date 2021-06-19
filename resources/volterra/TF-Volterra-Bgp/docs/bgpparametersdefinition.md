# TF::Volterra::Bgp BgpParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#bgprouteridkey" title="BgpRouterIdKey">BgpRouterIdKey</a>" : <i>String</i>,
    "<a href="#bgprouteridtype" title="BgpRouterIdType">BgpRouterIdType</a>" : <i>String</i>,
    "<a href="#fromsite" title="FromSite">FromSite</a>" : <i>Boolean</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#localaddress" title="LocalAddress">LocalAddress</a>" : <i>Boolean</i>,
    "<a href="#bgprouterid" title="BgpRouterId">BgpRouterId</a>" : <i>[ <a href="bgprouteriddefinition.md">BgpRouterIdDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#bgprouteridkey" title="BgpRouterIdKey">BgpRouterIdKey</a>: <i>String</i>
<a href="#bgprouteridtype" title="BgpRouterIdType">BgpRouterIdType</a>: <i>String</i>
<a href="#fromsite" title="FromSite">FromSite</a>: <i>Boolean</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#localaddress" title="LocalAddress">LocalAddress</a>: <i>Boolean</i>
<a href="#bgprouterid" title="BgpRouterId">BgpRouterId</a>: <i>
      - <a href="bgprouteriddefinition.md">BgpRouterIdDefinition</a></i>
</pre>

## Properties

#### Asn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpRouterIdKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpRouterIdType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromSite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAddress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpRouterId

_Required_: No

_Type_: List of <a href="bgprouteriddefinition.md">BgpRouterIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

