# Terraform::NSXT::LogicalTier1Router

CloudFormation equivalent of nsxt_logical_tier1_router

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LogicalTier1Router",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#advertiseconfigrevision" title="AdvertiseConfigRevision">AdvertiseConfigRevision</a>" : <i>Double</i>,
        "<a href="#advertiseconnectedroutes" title="AdvertiseConnectedRoutes">AdvertiseConnectedRoutes</a>" : <i>Boolean</i>,
        "<a href="#advertiselbsnatiproutes" title="AdvertiseLbSnatIpRoutes">AdvertiseLbSnatIpRoutes</a>" : <i>Boolean</i>,
        "<a href="#advertiselbviproutes" title="AdvertiseLbVipRoutes">AdvertiseLbVipRoutes</a>" : <i>Boolean</i>,
        "<a href="#advertisenatroutes" title="AdvertiseNatRoutes">AdvertiseNatRoutes</a>" : <i>Boolean</i>,
        "<a href="#advertisestaticroutes" title="AdvertiseStaticRoutes">AdvertiseStaticRoutes</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#edgeclusterid" title="EdgeClusterId">EdgeClusterId</a>" : <i>String</i>,
        "<a href="#enablerouteradvertisement" title="EnableRouterAdvertisement">EnableRouterAdvertisement</a>" : <i>Boolean</i>,
        "<a href="#failovermode" title="FailoverMode">FailoverMode</a>" : <i>String</i>,
        "<a href="#revision" title="Revision">Revision</a>" : <i>Double</i>,
        "<a href="#firewallsections" title="FirewallSections">FirewallSections</a>" : <i>[ &lt;a href=&#34;firewallsections.md&#34;&gt;FirewallSections&lt;/a&gt;, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LogicalTier1Router
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#advertiseconfigrevision" title="AdvertiseConfigRevision">AdvertiseConfigRevision</a>: <i>Double</i>
    <a href="#advertiseconnectedroutes" title="AdvertiseConnectedRoutes">AdvertiseConnectedRoutes</a>: <i>Boolean</i>
    <a href="#advertiselbsnatiproutes" title="AdvertiseLbSnatIpRoutes">AdvertiseLbSnatIpRoutes</a>: <i>Boolean</i>
    <a href="#advertiselbviproutes" title="AdvertiseLbVipRoutes">AdvertiseLbVipRoutes</a>: <i>Boolean</i>
    <a href="#advertisenatroutes" title="AdvertiseNatRoutes">AdvertiseNatRoutes</a>: <i>Boolean</i>
    <a href="#advertisestaticroutes" title="AdvertiseStaticRoutes">AdvertiseStaticRoutes</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#edgeclusterid" title="EdgeClusterId">EdgeClusterId</a>: <i>String</i>
    <a href="#enablerouteradvertisement" title="EnableRouterAdvertisement">EnableRouterAdvertisement</a>: <i>Boolean</i>
    <a href="#failovermode" title="FailoverMode">FailoverMode</a>: <i>String</i>
    <a href="#revision" title="Revision">Revision</a>: <i>Double</i>
    <a href="#firewallsections" title="FirewallSections">FirewallSections</a>: <i>
      - &lt;a href=&#34;firewallsections.md&#34;&gt;FirewallSections&lt;/a&gt;</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseConfigRevision

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseConnectedRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseLbSnatIpRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseLbVipRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseNatRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseStaticRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRouterAdvertisement

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Revision

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallSections

_Required_: No

_Type_: List of &lt;a href=&#34;firewallsections.md&#34;&gt;FirewallSections&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AdvertiseConfigRevision

Returns the &lt;code&gt;AdvertiseConfigRevision&lt;/code&gt; value.

#### Revision

Returns the &lt;code&gt;Revision&lt;/code&gt; value.

