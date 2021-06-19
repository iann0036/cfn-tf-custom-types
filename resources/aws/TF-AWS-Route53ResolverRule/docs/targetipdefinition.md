# TF::AWS::Route53ResolverRule TargetIpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
</pre>

## Properties

#### Ip

One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port at `ip` that you want to forward DNS queries to. Default value is `53`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

