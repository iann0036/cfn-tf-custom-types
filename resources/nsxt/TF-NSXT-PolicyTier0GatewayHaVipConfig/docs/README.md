# TF::NSXT::PolicyTier0GatewayHaVipConfig

This resource provides a method for the management of a Tier-0 gateway HA Vip config. Note that this configuration can be defined only for Active-Standby Tier0 gateway.

# Example Usage

```hcl
data "nsxt_policy_tier0_gateway" "gw1" {
  display_name = "gw1"
}

resource "nsxt_policy_tier0_gateway_interface" "if1" {
  display_name = "segment0_interface"
  description  = "connection to segment1"
  type         = "EXTERNAL"
  gateway_path = data.nsxt_policy_tier0_gateway.gw1.path
  segment_path = nsxt_policy_vlan_segment.segment1.path
  subnets      = ["12.12.2.1/24"]
}

resource "nsxt_policy_tier0_gateway_interface" "if2" {
  display_name = "segment0_interface"
  description  = "connection to segment2"
  type         = "EXTERNAL"
  gateway_path = data.nsxt_policy_tier0_gateway.gw1.path
  segment_path = nsxt_policy_vlan_segment.segment2.path
  subnets      = ["12.12.2.2/24"]
}

resource "nsxt_policy_tier0_gateway_ha_vip_config" "ha-vip" {
  config {
    enabled                  = true
    external_interface_p...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyTier0GatewayHaVipConfig",
    "Properties" : {
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="configdefinition.md">ConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyTier0GatewayHaVipConfig
Properties:
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="configdefinition.md">ConfigDefinition</a></i>
</pre>

## Properties

#### Config

_Required_: No

_Type_: List of <a href="configdefinition.md">ConfigDefinition</a>

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

#### LocaleServiceId

Returns the <code>LocaleServiceId</code> value.

#### Tier0Id

Returns the <code>Tier0Id</code> value.

