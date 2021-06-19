# TF::NSXT::PolicyGatewayRedistributionConfig

This resource provides a method for the management of a Tier-0 Gateway Route Redistribution config. Note that this configuration can be defined only for Active-Standby Tier0 gateway.

This resource is applicable to NSX Global Manager and NSX Policy Manager.

# Example Usage

```hcl
resource "nsxt_policy_gateway_redistribution_config" "test" {
  gateway_path = data.nsxt_policy_tier0_gateway.gw1.path
  bgp_enabled  = true
  ospf_enabled = true

  rule {
    name  = "test-rule-1"
    types = ["TIER1_CONNECTED", "TIER1_LB_VIP"]
  }

  rule {
    name           = "test-rule-2"
    types          = ["TIER0_EVPN_TEP_IP"]
    route_map_path = nsxt_policy_gateway_route_map.map1.path
  }
}
```

# Global Manager Example Usage

```hcl
resource "nsxt_policy_gateway_redistribution_config" "test" {
  gateway_path = data.nsxt_policy_tier0_gateway.gw1.path
  site_path    = nsxt_policy_site.paris.path

  bgp_enabled = true

  rule {
    name  = "test-rule-1"
    types = ["TIER1_CONNECTED", "TIER1_LB_VIP"]
  }
}
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyGatewayRedistributionConfig",
    "Properties" : {
        "<a href="#bgpenabled" title="BgpEnabled">BgpEnabled</a>" : <i>Boolean</i>,
        "<a href="#gatewaypath" title="GatewayPath">GatewayPath</a>" : <i>String</i>,
        "<a href="#ospfenabled" title="OspfEnabled">OspfEnabled</a>" : <i>Boolean</i>,
        "<a href="#sitepath" title="SitePath">SitePath</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyGatewayRedistributionConfig
Properties:
    <a href="#bgpenabled" title="BgpEnabled">BgpEnabled</a>: <i>Boolean</i>
    <a href="#gatewaypath" title="GatewayPath">GatewayPath</a>: <i>String</i>
    <a href="#ospfenabled" title="OspfEnabled">OspfEnabled</a>: <i>Boolean</i>
    <a href="#sitepath" title="SitePath">SitePath</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
</pre>

## Properties

#### BgpEnabled

Enable route redistribution for BGP. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayPath

Policy path to Tier0 Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfEnabled

Enable route redistribution for OSPF. Defaults to `false`. Applicable from NSX 3.1.0 onwards.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SitePath

Policy path to Global Manager site (domain). This attribute is required for NSX Global Manager and not applicable otherwise.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### GatewayId

Returns the <code>GatewayId</code> value.

#### Id

Returns the <code>Id</code> value.

#### LocaleServiceId

Returns the <code>LocaleServiceId</code> value.

