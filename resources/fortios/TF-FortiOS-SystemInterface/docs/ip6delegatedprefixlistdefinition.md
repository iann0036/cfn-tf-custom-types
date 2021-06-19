# TF::FortiOS::SystemInterface Ip6DelegatedPrefixListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autonomousflag" title="AutonomousFlag">AutonomousFlag</a>" : <i>String</i>,
    "<a href="#onlinkflag" title="OnlinkFlag">OnlinkFlag</a>" : <i>String</i>,
    "<a href="#prefixid" title="PrefixId">PrefixId</a>" : <i>Double</i>,
    "<a href="#rdnss" title="Rdnss">Rdnss</a>" : <i>String</i>,
    "<a href="#rdnssservice" title="RdnssService">RdnssService</a>" : <i>String</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
    "<a href="#upstreaminterface" title="UpstreamInterface">UpstreamInterface</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autonomousflag" title="AutonomousFlag">AutonomousFlag</a>: <i>String</i>
<a href="#onlinkflag" title="OnlinkFlag">OnlinkFlag</a>: <i>String</i>
<a href="#prefixid" title="PrefixId">PrefixId</a>: <i>Double</i>
<a href="#rdnss" title="Rdnss">Rdnss</a>: <i>String</i>
<a href="#rdnssservice" title="RdnssService">RdnssService</a>: <i>String</i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
<a href="#upstreaminterface" title="UpstreamInterface">UpstreamInterface</a>: <i>String</i>
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

#### PrefixId

Prefix ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rdnss

Recursive DNS server option.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdnssService

Recursive DNS service option. Valid values: `delegated`, `default`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

Add subnet ID to routing prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamInterface

Name of the interface that provides delegated information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

