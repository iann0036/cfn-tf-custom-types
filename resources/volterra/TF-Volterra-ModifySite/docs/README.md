# TF::Volterra::ModifySite

CloudFormation equivalent of volterra_modify_site

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::ModifySite",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#bgppeeraddress" title="BgpPeerAddress">BgpPeerAddress</a>" : <i>String</i>,
        "<a href="#bgprouterid" title="BgpRouterId">BgpRouterId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredpoolcount" title="DesiredPoolCount">DesiredPoolCount</a>" : <i>Double</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#insidenameserver" title="InsideNameserver">InsideNameserver</a>" : <i>String</i>,
        "<a href="#insidevip" title="InsideVip">InsideVip</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#operatingsystemversion" title="OperatingSystemVersion">OperatingSystemVersion</a>" : <i>String</i>,
        "<a href="#outsidenameserver" title="OutsideNameserver">OutsideNameserver</a>" : <i>String</i>,
        "<a href="#outsidevip" title="OutsideVip">OutsideVip</a>" : <i>String</i>,
        "<a href="#retry" title="Retry">Retry</a>" : <i>Double</i>,
        "<a href="#sitetositenetworktype" title="SiteToSiteNetworkType">SiteToSiteNetworkType</a>" : <i>String</i>,
        "<a href="#sitetositetunnelip" title="SiteToSiteTunnelIp">SiteToSiteTunnelIp</a>" : <i>String</i>,
        "<a href="#tunneldeadtimeout" title="TunnelDeadTimeout">TunnelDeadTimeout</a>" : <i>Double</i>,
        "<a href="#tunneltype" title="TunnelType">TunnelType</a>" : <i>String</i>,
        "<a href="#vipvrrpmode" title="VipVrrpMode">VipVrrpMode</a>" : <i>String</i>,
        "<a href="#volterrasoftwareoveride" title="VolterraSoftwareOveride">VolterraSoftwareOveride</a>" : <i>String</i>,
        "<a href="#volterrasoftwareversion" title="VolterraSoftwareVersion">VolterraSoftwareVersion</a>" : <i>String</i>,
        "<a href="#waittime" title="WaitTime">WaitTime</a>" : <i>Double</i>,
        "<a href="#coordinates" title="Coordinates">Coordinates</a>" : <i>[ <a href="coordinatesdefinition.md">CoordinatesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::ModifySite
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#bgppeeraddress" title="BgpPeerAddress">BgpPeerAddress</a>: <i>String</i>
    <a href="#bgprouterid" title="BgpRouterId">BgpRouterId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredpoolcount" title="DesiredPoolCount">DesiredPoolCount</a>: <i>Double</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#insidenameserver" title="InsideNameserver">InsideNameserver</a>: <i>String</i>
    <a href="#insidevip" title="InsideVip">InsideVip</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#operatingsystemversion" title="OperatingSystemVersion">OperatingSystemVersion</a>: <i>String</i>
    <a href="#outsidenameserver" title="OutsideNameserver">OutsideNameserver</a>: <i>String</i>
    <a href="#outsidevip" title="OutsideVip">OutsideVip</a>: <i>String</i>
    <a href="#retry" title="Retry">Retry</a>: <i>Double</i>
    <a href="#sitetositenetworktype" title="SiteToSiteNetworkType">SiteToSiteNetworkType</a>: <i>String</i>
    <a href="#sitetositetunnelip" title="SiteToSiteTunnelIp">SiteToSiteTunnelIp</a>: <i>String</i>
    <a href="#tunneldeadtimeout" title="TunnelDeadTimeout">TunnelDeadTimeout</a>: <i>Double</i>
    <a href="#tunneltype" title="TunnelType">TunnelType</a>: <i>String</i>
    <a href="#vipvrrpmode" title="VipVrrpMode">VipVrrpMode</a>: <i>String</i>
    <a href="#volterrasoftwareoveride" title="VolterraSoftwareOveride">VolterraSoftwareOveride</a>: <i>String</i>
    <a href="#volterrasoftwareversion" title="VolterraSoftwareVersion">VolterraSoftwareVersion</a>: <i>String</i>
    <a href="#waittime" title="WaitTime">WaitTime</a>: <i>Double</i>
    <a href="#coordinates" title="Coordinates">Coordinates</a>: <i>
      - <a href="coordinatesdefinition.md">CoordinatesDefinition</a></i>
</pre>

## Properties

#### Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpPeerAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpRouterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredPoolCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideNameserver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideVip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystemVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideNameserver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideVip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retry

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteToSiteNetworkType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteToSiteTunnelIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelDeadTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipVrrpMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolterraSoftwareOveride

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolterraSoftwareVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Coordinates

_Required_: No

_Type_: List of <a href="coordinatesdefinition.md">CoordinatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

