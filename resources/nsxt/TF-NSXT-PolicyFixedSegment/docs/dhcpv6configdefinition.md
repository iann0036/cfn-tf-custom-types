# TF::NSXT::PolicyFixedSegment DhcpV6ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsservers" title="DnsServers">DnsServers</a>" : <i>[ String, ... ]</i>,
    "<a href="#domainnames" title="DomainNames">DomainNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#leasetime" title="LeaseTime">LeaseTime</a>" : <i>Double</i>,
    "<a href="#preferredtime" title="PreferredTime">PreferredTime</a>" : <i>Double</i>,
    "<a href="#serveraddress" title="ServerAddress">ServerAddress</a>" : <i>String</i>,
    "<a href="#sntpservers" title="SntpServers">SntpServers</a>" : <i>[ String, ... ]</i>,
    "<a href="#excludedrange" title="ExcludedRange">ExcludedRange</a>" : <i>[ <a href="excludedrangedefinition.md">ExcludedRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsservers" title="DnsServers">DnsServers</a>: <i>
      - String</i>
<a href="#domainnames" title="DomainNames">DomainNames</a>: <i>
      - String</i>
<a href="#leasetime" title="LeaseTime">LeaseTime</a>: <i>Double</i>
<a href="#preferredtime" title="PreferredTime">PreferredTime</a>: <i>Double</i>
<a href="#serveraddress" title="ServerAddress">ServerAddress</a>: <i>String</i>
<a href="#sntpservers" title="SntpServers">SntpServers</a>: <i>
      - String</i>
<a href="#excludedrange" title="ExcludedRange">ExcludedRange</a>: <i>
      - <a href="excludedrangedefinition.md">ExcludedRangeDefinition</a></i>
</pre>

## Properties

#### DnsServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SntpServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedRange

_Required_: No

_Type_: List of <a href="excludedrangedefinition.md">ExcludedRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

