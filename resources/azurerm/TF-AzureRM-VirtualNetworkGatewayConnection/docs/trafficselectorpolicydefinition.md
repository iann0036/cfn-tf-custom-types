# TF::AzureRM::VirtualNetworkGatewayConnection TrafficSelectorPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#localaddresscidrs" title="LocalAddressCidrs">LocalAddressCidrs</a>" : <i>[ String, ... ]</i>,
    "<a href="#remoteaddresscidrs" title="RemoteAddressCidrs">RemoteAddressCidrs</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#localaddresscidrs" title="LocalAddressCidrs">LocalAddressCidrs</a>: <i>
      - String</i>
<a href="#remoteaddresscidrs" title="RemoteAddressCidrs">RemoteAddressCidrs</a>: <i>
      - String</i>
</pre>

## Properties

#### LocalAddressCidrs

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAddressCidrs

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

