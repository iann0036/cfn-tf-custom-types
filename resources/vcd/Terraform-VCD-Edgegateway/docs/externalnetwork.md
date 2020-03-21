# Terraform::VCD::Edgegateway ExternalNetwork

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableratelimit" title="EnableRateLimit">EnableRateLimit</a>" : <i>Boolean</i>,
    "<a href="#incomingratelimit" title="IncomingRateLimit">IncomingRateLimit</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#outgoingratelimit" title="OutgoingRateLimit">OutgoingRateLimit</a>" : <i>Double</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="externalnetwork-subnet.md">Subnet</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableratelimit" title="EnableRateLimit">EnableRateLimit</a>: <i>Boolean</i>
<a href="#incomingratelimit" title="IncomingRateLimit">IncomingRateLimit</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#outgoingratelimit" title="OutgoingRateLimit">OutgoingRateLimit</a>: <i>Double</i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="externalnetwork-subnet.md">Subnet</a></i>
</pre>

## Properties

#### EnableRateLimit

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncomingRateLimit

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutgoingRateLimit

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No
_Type_: List of <a href="externalnetwork-subnet.md">Subnet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

