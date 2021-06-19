# TF::FortiOS::SystemInterface Ip6PrefixListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autonomousflag" title="AutonomousFlag">AutonomousFlag</a>" : <i>String</i>,
    "<a href="#onlinkflag" title="OnlinkFlag">OnlinkFlag</a>" : <i>String</i>,
    "<a href="#preferredlifetime" title="PreferredLifeTime">PreferredLifeTime</a>" : <i>Double</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#rdnss" title="Rdnss">Rdnss</a>" : <i>String</i>,
    "<a href="#validlifetime" title="ValidLifeTime">ValidLifeTime</a>" : <i>Double</i>,
    "<a href="#dnssl" title="Dnssl">Dnssl</a>" : <i>[ <a href="dnssldefinition.md">DnsslDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autonomousflag" title="AutonomousFlag">AutonomousFlag</a>: <i>String</i>
<a href="#onlinkflag" title="OnlinkFlag">OnlinkFlag</a>: <i>String</i>
<a href="#preferredlifetime" title="PreferredLifeTime">PreferredLifeTime</a>: <i>Double</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#rdnss" title="Rdnss">Rdnss</a>: <i>String</i>
<a href="#validlifetime" title="ValidLifeTime">ValidLifeTime</a>: <i>Double</i>
<a href="#dnssl" title="Dnssl">Dnssl</a>: <i>
      - <a href="dnssldefinition.md">DnsslDefinition</a></i>
</pre>

## Properties

#### AutonomousFlag

Enable/disable the autonomous flag. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlinkFlag

Enable/disable the onlink flag. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredLifeTime

Preferred life time (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

IPv6 prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rdnss

Recursive DNS server option.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidLifeTime

Valid life time (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dnssl

_Required_: No

_Type_: List of <a href="dnssldefinition.md">DnsslDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

