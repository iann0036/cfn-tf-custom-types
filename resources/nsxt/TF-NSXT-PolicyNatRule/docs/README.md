# TF::NSXT::PolicyNatRule

This resource provides a method for the management of a NAT Rule.

This resource is applicable to NSX Global Manager, NSX Policy Manager and VMC.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyNatRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationnetworks" title="DestinationNetworks">DestinationNetworks</a>" : <i>[ String, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#firewallmatch" title="FirewallMatch">FirewallMatch</a>" : <i>String</i>,
        "<a href="#gatewaypath" title="GatewayPath">GatewayPath</a>" : <i>String</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>Boolean</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#rulepriority" title="RulePriority">RulePriority</a>" : <i>Double</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>[ String, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#sourcenetworks" title="SourceNetworks">SourceNetworks</a>" : <i>[ String, ... ]</i>,
        "<a href="#translatednetworks" title="TranslatedNetworks">TranslatedNetworks</a>" : <i>[ String, ... ]</i>,
        "<a href="#translatedports" title="TranslatedPorts">TranslatedPorts</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyNatRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationnetworks" title="DestinationNetworks">DestinationNetworks</a>: <i>
      - String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#firewallmatch" title="FirewallMatch">FirewallMatch</a>: <i>String</i>
    <a href="#gatewaypath" title="GatewayPath">GatewayPath</a>: <i>String</i>
    <a href="#logging" title="Logging">Logging</a>: <i>Boolean</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#rulepriority" title="RulePriority">RulePriority</a>: <i>Double</i>
    <a href="#scope" title="Scope">Scope</a>: <i>
      - String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#sourcenetworks" title="SourceNetworks">SourceNetworks</a>: <i>
      - String</i>
    <a href="#translatednetworks" title="TranslatedNetworks">TranslatedNetworks</a>: <i>
      - String</i>
    <a href="#translatedports" title="TranslatedPorts">TranslatedPorts</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Action

The action for the NAT Rule. One of `SNAT`, `DNAT`, `REFLEXIVE`, `NO_SNAT`, `NO_DNAT`, `NAT64`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationNetworks

A list of destination network IP addresses or CIDR.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enable/disable the Rule. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallMatch

Firewall match flag. One of `MATCH_EXTERNAL_ADDRESS`, `MATCH_INTERNAL_ADDRESS`, `BYPASS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayPath

The NSX Policy path to the Tier0 or Tier1 Gateway for this NAT Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

Enable/disable rule logging. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the policy resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulePriority

The priority of the rule. Valid values between 0 to 2147483647. Defaults to `100`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

A list of paths to interfaces and/or labels where the NAT Rule is enforced.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

Policy path of Service on which the NAT rule will be applied.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceNetworks

A list of source network IP addresses or CIDR.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedNetworks

A list of translated network IP addresses or CIDR.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedPorts

Port number or port range. For use with `DNAT` action only.

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

