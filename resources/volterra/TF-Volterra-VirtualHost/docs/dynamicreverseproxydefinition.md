# TF::Volterra::VirtualHost DynamicReverseProxyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>" : <i>Double</i>,
    "<a href="#resolutionnetworktype" title="ResolutionNetworkType">ResolutionNetworkType</a>" : <i>String</i>,
    "<a href="#resolveendpointdynamically" title="ResolveEndpointDynamically">ResolveEndpointDynamically</a>" : <i>Boolean</i>,
    "<a href="#resolutionnetwork" title="ResolutionNetwork">ResolutionNetwork</a>" : <i>[ <a href="resolutionnetworkdefinition.md">ResolutionNetworkDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>: <i>Double</i>
<a href="#resolutionnetworktype" title="ResolutionNetworkType">ResolutionNetworkType</a>: <i>String</i>
<a href="#resolveendpointdynamically" title="ResolveEndpointDynamically">ResolveEndpointDynamically</a>: <i>Boolean</i>
<a href="#resolutionnetwork" title="ResolutionNetwork">ResolutionNetwork</a>: <i>
      - <a href="resolutionnetworkdefinition.md">ResolutionNetworkDefinition</a></i>
</pre>

## Properties

#### ConnectionTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolutionNetworkType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveEndpointDynamically

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolutionNetwork

_Required_: No

_Type_: List of <a href="resolutionnetworkdefinition.md">ResolutionNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

