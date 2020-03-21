# Terraform::VCD::NsxvFirewallRule

Provides a vCloud Director firewall rule resource for advanced edge gateways (NSX-V). This can be
used to create, modify, and delete firewall rules. Replaces
[`vcd_firewall_rules`](/docs/providers/vcd/r/firewall_rules.html) resource.

~> **Note:** This resource requires advanced edge gateway (NSX-V). For non-advanced edge gateways please
use the [`vcd_firewall_rules`](/docs/providers/vcd/r/firewall_rules.html) resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::NsxvFirewallRule",
    "Properties" : {
        "<a href="#aboveruleid" title="AboveRuleId">AboveRuleId</a>" : <i>String</i>,
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#loggingenabled" title="LoggingEnabled">LoggingEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#ruletag" title="RuleTag">RuleTag</a>" : <i>Double</i>,
        "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destination.md">Destination</a>, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ <a href="service.md">Service</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="source.md">Source</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::NsxvFirewallRule
Properties:
    <a href="#aboveruleid" title="AboveRuleId">AboveRuleId</a>: <i>String</i>
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#edgegateway" title="EdgeGateway">EdgeGateway</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#loggingenabled" title="LoggingEnabled">LoggingEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#ruletag" title="RuleTag">RuleTag</a>: <i>Double</i>
    <a href="#ruletype" title="RuleType">RuleType</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destination.md">Destination</a></i>
    <a href="#service" title="Service">Service</a>: <i>
      - <a href="service.md">Service</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="source.md">Source</a></i>
</pre>

## Properties

#### AboveRuleId

This can be used to alter default rule placement order. By default
every rule is appended to the end of firewall rule list. When a value of another rule is set - this
rule will be placed above the specified rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

Defines if the rule is set to `accept` or `deny` traffic. Default `accept`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeGateway

The name of the edge gateway on which to apply the firewall rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Defines if the rule is enabaled. Default `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingEnabled

Defines if the logging for this rule is enabaled. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Free text name. Can be duplicate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful
when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleTag

This can be used to specify user-controlled rule tag. If not specified,
it will report rule ID after creation. Must be between 65537-131072.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="service.md">Service</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="source.md">Source</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

