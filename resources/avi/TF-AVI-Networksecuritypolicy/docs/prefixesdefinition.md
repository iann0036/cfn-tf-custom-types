# TF::AVI::Networksecuritypolicy PrefixesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mask" title="Mask">Mask</a>" : <i>Double</i>,
    "<a href="#ipaddr" title="IpAddr">IpAddr</a>" : <i>[ <a href="ipaddrdefinition.md">IpAddrDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#mask" title="Mask">Mask</a>: <i>Double</i>
<a href="#ipaddr" title="IpAddr">IpAddr</a>: <i>
      - <a href="ipaddrdefinition.md">IpAddrDefinition</a></i>
</pre>

## Properties

#### Mask

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddr

_Required_: No

_Type_: List of <a href="ipaddrdefinition.md">IpAddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

