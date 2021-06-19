# TF::Volterra::GcpVpcSite NexthopAddressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipv4" title="Ipv4">Ipv4</a>" : <i>[ <a href="ipv4definition.md">Ipv4Definition</a>, ... ]</i>,
    "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>[ <a href="ipv6definition.md">Ipv6Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipv4" title="Ipv4">Ipv4</a>: <i>
      - <a href="ipv4definition.md">Ipv4Definition</a></i>
<a href="#ipv6" title="Ipv6">Ipv6</a>: <i>
      - <a href="ipv6definition.md">Ipv6Definition</a></i>
</pre>

## Properties

#### Ipv4

_Required_: No

_Type_: List of <a href="ipv4definition.md">Ipv4Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: List of <a href="ipv6definition.md">Ipv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

