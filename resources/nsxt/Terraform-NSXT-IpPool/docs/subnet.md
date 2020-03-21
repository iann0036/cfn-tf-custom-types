# Terraform::NSXT::IpPool Subnet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allocationranges" title="AllocationRanges">AllocationRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
    "<a href="#dnsnameservers" title="DnsNameservers">DnsNameservers</a>" : <i>[ String, ... ]</i>,
    "<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>" : <i>String</i>,
    "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allocationranges" title="AllocationRanges">AllocationRanges</a>: <i>
      - String</i>
<a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
<a href="#dnsnameservers" title="DnsNameservers">DnsNameservers</a>: <i>
      - String</i>
<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>: <i>String</i>
<a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>String</i>
</pre>

## Properties

#### AllocationRanges

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cidr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsNameservers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSuffix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

