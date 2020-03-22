# Terraform::NSXT::LogicalTier1Router

This resource provides a method for the management of a tier 1 logical router. A tier 1 logical router is often used for tenants, users and applications. There can be many tier 1 logical routers connected to a common tier 0 provider router.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LogicalTier1Router",
    "Properties" : {
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
        "<a href="#firewallsections" title="FirewallSections">FirewallSections</a>" : <i>[ <a href="firewallsections.md">FirewallSections</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LogicalTier1Router
Properties:
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
    <a href="#firewallsections" title="FirewallSections">FirewallSections</a>: <i>
      - <a href="firewallsections.md">FirewallSections</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### AdvertiseConnectedRoutes

Enable the router advertisement for all NSX connected routes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseLbSnatIpRoutes

Enable the router advertisement for LB SNAT IP routes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseLbVipRoutes

Enable the router advertisement for LB VIP routes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseNatRoutes

Enable the router advertisement for NAT routes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseStaticRoutes

Enable the router advertisement for static routes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name, defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeClusterId

Edge Cluster ID for the logical Tier1 router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRouterAdvertisement

Enable the router advertisement.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverMode

This failover mode determines, whether the preferred service router instance for given logical router will preempt the peer. Note - It can be specified if and only if logical router is ACTIVE_STANDBY and NON_PREEMPTIVE mode is supported only for a Tier1 logical router. For ACTIVE_ACTIVE logical routers, this field must not be populated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallSections

_Required_: No

_Type_: List of <a href="firewallsections.md">FirewallSections</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AdvertiseConfigRevision

Returns the <code>AdvertiseConfigRevision</code> value.

#### Id

Returns the <code>Id</code> value.

#### Revision

Returns the <code>Revision</code> value.

