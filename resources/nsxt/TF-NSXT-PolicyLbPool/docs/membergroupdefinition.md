# TF::NSXT::PolicyLbPool MemberGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowipv4" title="AllowIpv4">AllowIpv4</a>" : <i>Boolean</i>,
    "<a href="#allowipv6" title="AllowIpv6">AllowIpv6</a>" : <i>Boolean</i>,
    "<a href="#grouppath" title="GroupPath">GroupPath</a>" : <i>String</i>,
    "<a href="#maxiplistsize" title="MaxIpListSize">MaxIpListSize</a>" : <i>Double</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowipv4" title="AllowIpv4">AllowIpv4</a>: <i>Boolean</i>
<a href="#allowipv6" title="AllowIpv6">AllowIpv6</a>: <i>Boolean</i>
<a href="#grouppath" title="GroupPath">GroupPath</a>: <i>String</i>
<a href="#maxiplistsize" title="MaxIpListSize">MaxIpListSize</a>: <i>Double</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
</pre>

## Properties

#### AllowIpv4

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIpv6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIpListSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

