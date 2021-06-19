# TF::Volterra::Route RouteDestinationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autohostrewrite" title="AutoHostRewrite">AutoHostRewrite</a>" : <i>Boolean</i>,
    "<a href="#donotretractcluster" title="DoNotRetractCluster">DoNotRetractCluster</a>" : <i>Boolean</i>,
    "<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>" : <i>[ <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>, ... ]</i>,
    "<a href="#hostrewrite" title="HostRewrite">HostRewrite</a>" : <i>String</i>,
    "<a href="#prefixrewrite" title="PrefixRewrite">PrefixRewrite</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
    "<a href="#retractcluster" title="RetractCluster">RetractCluster</a>" : <i>Boolean</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#bufferpolicy" title="BufferPolicy">BufferPolicy</a>" : <i>[ <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a>, ... ]</i>,
    "<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>" : <i>[ <a href="corspolicydefinition.md">CorsPolicyDefinition</a>, ... ]</i>,
    "<a href="#destinations" title="Destinations">Destinations</a>" : <i>[ <a href="destinationsdefinition.md">DestinationsDefinition</a>, ... ]</i>,
    "<a href="#hashpolicy" title="HashPolicy">HashPolicy</a>" : <i>[ <a href="hashpolicydefinition.md">HashPolicyDefinition</a>, ... ]</i>,
    "<a href="#mirrorpolicy" title="MirrorPolicy">MirrorPolicy</a>" : <i>[ <a href="mirrorpolicydefinition.md">MirrorPolicyDefinition</a>, ... ]</i>,
    "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>, ... ]</i>,
    "<a href="#spdyconfig" title="SpdyConfig">SpdyConfig</a>" : <i>[ <a href="spdyconfigdefinition.md">SpdyConfigDefinition</a>, ... ]</i>,
    "<a href="#websocketconfig" title="WebSocketConfig">WebSocketConfig</a>" : <i>[ <a href="websocketconfigdefinition.md">WebSocketConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autohostrewrite" title="AutoHostRewrite">AutoHostRewrite</a>: <i>Boolean</i>
<a href="#donotretractcluster" title="DoNotRetractCluster">DoNotRetractCluster</a>: <i>Boolean</i>
<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>: <i>
      - <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a></i>
<a href="#hostrewrite" title="HostRewrite">HostRewrite</a>: <i>String</i>
<a href="#prefixrewrite" title="PrefixRewrite">PrefixRewrite</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>String</i>
<a href="#retractcluster" title="RetractCluster">RetractCluster</a>: <i>Boolean</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#bufferpolicy" title="BufferPolicy">BufferPolicy</a>: <i>
      - <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a></i>
<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>: <i>
      - <a href="corspolicydefinition.md">CorsPolicyDefinition</a></i>
<a href="#destinations" title="Destinations">Destinations</a>: <i>
      - <a href="destinationsdefinition.md">DestinationsDefinition</a></i>
<a href="#hashpolicy" title="HashPolicy">HashPolicy</a>: <i>
      - <a href="hashpolicydefinition.md">HashPolicyDefinition</a></i>
<a href="#mirrorpolicy" title="MirrorPolicy">MirrorPolicy</a>: <i>
      - <a href="mirrorpolicydefinition.md">MirrorPolicyDefinition</a></i>
<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicydefinition.md">RetryPolicyDefinition</a></i>
<a href="#spdyconfig" title="SpdyConfig">SpdyConfig</a>: <i>
      - <a href="spdyconfigdefinition.md">SpdyConfigDefinition</a></i>
<a href="#websocketconfig" title="WebSocketConfig">WebSocketConfig</a>: <i>
      - <a href="websocketconfigdefinition.md">WebSocketConfigDefinition</a></i>
</pre>

## Properties

#### AutoHostRewrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoNotRetractCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointSubsets

_Required_: No

_Type_: List of <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRewrite

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixRewrite

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetractCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferPolicy

_Required_: No

_Type_: List of <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsPolicy

_Required_: No

_Type_: List of <a href="corspolicydefinition.md">CorsPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destinations

_Required_: No

_Type_: List of <a href="destinationsdefinition.md">DestinationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashPolicy

_Required_: No

_Type_: List of <a href="hashpolicydefinition.md">HashPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MirrorPolicy

_Required_: No

_Type_: List of <a href="mirrorpolicydefinition.md">MirrorPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpdyConfig

_Required_: No

_Type_: List of <a href="spdyconfigdefinition.md">SpdyConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebSocketConfig

_Required_: No

_Type_: List of <a href="websocketconfigdefinition.md">WebSocketConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

