# TF::OCI::LoadBalancerLoadBalancer IpAddressDetailsDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#ispublic" title="IsPublic">IsPublic</a>" : <i>Boolean</i>,
    "<a href="#reservedip" title="ReservedIp">ReservedIp</a>" : <i>[ <a href="ipaddressdetailsdefinition.md">IpAddressDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#ispublic" title="IsPublic">IsPublic</a>: <i>Boolean</i>
<a href="#reservedip" title="ReservedIp">ReservedIp</a>: <i>
      - <a href="ipaddressdetailsdefinition.md">IpAddressDetailsDefinition</a></i>
</pre>

## Properties

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPublic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedIp

_Required_: No

_Type_: List of <a href="ipaddressdetailsdefinition.md">IpAddressDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

