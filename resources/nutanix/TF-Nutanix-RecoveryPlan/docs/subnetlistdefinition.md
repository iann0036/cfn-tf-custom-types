# TF::Nutanix::RecoveryPlan SubnetListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#externalconnectivitystate" title="ExternalConnectivityState">ExternalConnectivityState</a>" : <i>String</i>,
    "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>String</i>,
    "<a href="#prefixlength" title="PrefixLength">PrefixLength</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#externalconnectivitystate" title="ExternalConnectivityState">ExternalConnectivityState</a>: <i>String</i>
<a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>String</i>
<a href="#prefixlength" title="PrefixLength">PrefixLength</a>: <i>Double</i>
</pre>

## Properties

#### ExternalConnectivityState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixLength

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

