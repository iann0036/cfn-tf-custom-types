# TF::UpCloud::Network IpNetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#dhcp" title="Dhcp">Dhcp</a>" : <i>Boolean</i>,
    "<a href="#dhcpdefaultroute" title="DhcpDefaultRoute">DhcpDefaultRoute</a>" : <i>Boolean</i>,
    "<a href="#dhcpdns" title="DhcpDns">DhcpDns</a>" : <i>[ String, ... ]</i>,
    "<a href="#family" title="Family">Family</a>" : <i>String</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#dhcp" title="Dhcp">Dhcp</a>: <i>Boolean</i>
<a href="#dhcpdefaultroute" title="DhcpDefaultRoute">DhcpDefaultRoute</a>: <i>Boolean</i>
<a href="#dhcpdns" title="DhcpDns">DhcpDns</a>: <i>
      - String</i>
<a href="#family" title="Family">Family</a>: <i>String</i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
</pre>

## Properties

#### Address

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpDefaultRoute

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpDns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Family

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

