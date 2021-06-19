# TF::AVI::Dnspolicy ClientIpAddressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#useednsclientsubnetip" title="UseEdnsClientSubnetIp">UseEdnsClientSubnetIp</a>" : <i>Boolean</i>,
    "<a href="#clientip" title="ClientIp">ClientIp</a>" : <i>[ <a href="clientipdefinition.md">ClientIpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#useednsclientsubnetip" title="UseEdnsClientSubnetIp">UseEdnsClientSubnetIp</a>: <i>Boolean</i>
<a href="#clientip" title="ClientIp">ClientIp</a>: <i>
      - <a href="clientipdefinition.md">ClientIpDefinition</a></i>
</pre>

## Properties

#### UseEdnsClientSubnetIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIp

_Required_: No

_Type_: List of <a href="clientipdefinition.md">ClientIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

