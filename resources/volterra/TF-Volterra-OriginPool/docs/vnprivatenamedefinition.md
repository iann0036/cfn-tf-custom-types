# TF::Volterra::OriginPool VnPrivateNameDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsname" title="DnsName">DnsName</a>" : <i>String</i>,
    "<a href="#privatenetwork" title="PrivateNetwork">PrivateNetwork</a>" : <i>[ <a href="privatenetworkdefinition.md">PrivateNetworkDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsname" title="DnsName">DnsName</a>: <i>String</i>
<a href="#privatenetwork" title="PrivateNetwork">PrivateNetwork</a>: <i>
      - <a href="privatenetworkdefinition.md">PrivateNetworkDefinition</a></i>
</pre>

## Properties

#### DnsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateNetwork

_Required_: No

_Type_: List of <a href="privatenetworkdefinition.md">PrivateNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

