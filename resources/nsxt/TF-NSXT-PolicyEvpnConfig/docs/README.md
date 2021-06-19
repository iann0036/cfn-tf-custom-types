# TF::NSXT::PolicyEvpnConfig

This resource provides a method to configure EVPN on T0 Gateway. A single resource should be configured per Gateway.

This resource is applicable to NSX Policy Manager only.
This resource is supported with NSX 3.1.0 onwards.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyEvpnConfig",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#evpntenantpath" title="EvpnTenantPath">EvpnTenantPath</a>" : <i>String</i>,
        "<a href="#gatewaypath" title="GatewayPath">GatewayPath</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#vnipoolpath" title="VniPoolPath">VniPoolPath</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyEvpnConfig
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#evpntenantpath" title="EvpnTenantPath">EvpnTenantPath</a>: <i>String</i>
    <a href="#gatewaypath" title="GatewayPath">GatewayPath</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#vnipoolpath" title="VniPoolPath">VniPoolPath</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Description

Description for the resource.
* `gateway_path` - (Required) Policy Path for Tier0 Gateway to configure EVPN on.
* `mode` - (Required) EVPN Mode, one of `INLINE` or `ROUTE_SERVER`. In `ROUTE_SERVER` mode, edge nodes participate in the BGP EVPN control plane route exchanges only and do not participate in the data forwarding
* `vni_pool_path` - (Optional) This setting is only applicable (and required) with `INLINE` mode.
* `tag` - (Optional) A list of scope + tag pairs to associate with this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name for the resource.
* `description` - (Optional) Description for the resource.
* `gateway_path` - (Required) Policy Path for Tier0 Gateway to configure EVPN on.
* `mode` - (Required) EVPN Mode, one of `INLINE` or `ROUTE_SERVER`. In `ROUTE_SERVER` mode, edge nodes participate in the BGP EVPN control plane route exchanges only and do not participate in the data forwarding
* `vni_pool_path` - (Optional) This setting is only applicable (and required) with `INLINE` mode.
* `tag` - (Optional) A list of scope + tag pairs to associate with this resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvpnTenantPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayPath

Policy Path for Tier0 Gateway to configure EVPN on.
* `mode` - (Required) EVPN Mode, one of `INLINE` or `ROUTE_SERVER`. In `ROUTE_SERVER` mode, edge nodes participate in the BGP EVPN control plane route exchanges only and do not participate in the data forwarding
* `vni_pool_path` - (Optional) This setting is only applicable (and required) with `INLINE` mode.
* `tag` - (Optional) A list of scope + tag pairs to associate with this resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

EVPN Mode, one of `INLINE` or `ROUTE_SERVER`. In `ROUTE_SERVER` mode, edge nodes participate in the BGP EVPN control plane route exchanges only and do not participate in the data forwarding
* `vni_pool_path` - (Optional) This setting is only applicable (and required) with `INLINE` mode.
* `tag` - (Optional) A list of scope + tag pairs to associate with this resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VniPoolPath

This setting is only applicable (and required) with `INLINE` mode.
* `tag` - (Optional) A list of scope + tag pairs to associate with this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

