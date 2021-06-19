# TF::ProfitBricks::Server NicDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dhcp" title="Dhcp">Dhcp</a>" : <i>Boolean</i>,
    "<a href="#firewallactive" title="FirewallActive">FirewallActive</a>" : <i>Boolean</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#lan" title="Lan">Lan</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nat" title="Nat">Nat</a>" : <i>Boolean</i>,
    "<a href="#firewall" title="Firewall">Firewall</a>" : <i>[ <a href="firewalldefinition.md">FirewallDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dhcp" title="Dhcp">Dhcp</a>: <i>Boolean</i>
<a href="#firewallactive" title="FirewallActive">FirewallActive</a>: <i>Boolean</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#lan" title="Lan">Lan</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nat" title="Nat">Nat</a>: <i>Boolean</i>
<a href="#firewall" title="Firewall">Firewall</a>: <i>
      - <a href="firewalldefinition.md">FirewallDefinition</a></i>
</pre>

## Properties

#### Dhcp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallActive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lan

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nat

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firewall

_Required_: No

_Type_: List of <a href="firewalldefinition.md">FirewallDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

