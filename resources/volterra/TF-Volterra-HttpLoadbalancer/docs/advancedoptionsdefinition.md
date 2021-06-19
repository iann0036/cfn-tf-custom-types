# TF::Volterra::HttpLoadbalancer AdvancedOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commonbuffering" title="CommonBuffering">CommonBuffering</a>" : <i>Boolean</i>,
    "<a href="#commonhashpolicy" title="CommonHashPolicy">CommonHashPolicy</a>" : <i>Boolean</i>,
    "<a href="#defaultretrypolicy" title="DefaultRetryPolicy">DefaultRetryPolicy</a>" : <i>Boolean</i>,
    "<a href="#disablelocationadd" title="DisableLocationAdd">DisableLocationAdd</a>" : <i>Boolean</i>,
    "<a href="#disablemirroring" title="DisableMirroring">DisableMirroring</a>" : <i>Boolean</i>,
    "<a href="#disableprefixrewrite" title="DisablePrefixRewrite">DisablePrefixRewrite</a>" : <i>Boolean</i>,
    "<a href="#disablespdy" title="DisableSpdy">DisableSpdy</a>" : <i>Boolean</i>,
    "<a href="#disablewaf" title="DisableWaf">DisableWaf</a>" : <i>Boolean</i>,
    "<a href="#disablewebsocketconfig" title="DisableWebSocketConfig">DisableWebSocketConfig</a>" : <i>Boolean</i>,
    "<a href="#donotretractcluster" title="DoNotRetractCluster">DoNotRetractCluster</a>" : <i>Boolean</i>,
    "<a href="#enablespdy" title="EnableSpdy">EnableSpdy</a>" : <i>Boolean</i>,
    "<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>" : <i>[ <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>, ... ]</i>,
    "<a href="#prefixrewrite" title="PrefixRewrite">PrefixRewrite</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
    "<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#retractcluster" title="RetractCluster">RetractCluster</a>" : <i>Boolean</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#bufferpolicy" title="BufferPolicy">BufferPolicy</a>" : <i>[ <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a>, ... ]</i>,
    "<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>" : <i>[ <a href="corspolicydefinition.md">CorsPolicyDefinition</a>, ... ]</i>,
    "<a href="#mirrorpolicy" title="MirrorPolicy">MirrorPolicy</a>" : <i>[ <a href="mirrorpolicydefinition.md">MirrorPolicyDefinition</a>, ... ]</i>,
    "<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>" : <i>[ <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a>, ... ]</i>,
    "<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>" : <i>[ <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a>, ... ]</i>,
    "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>, ... ]</i>,
    "<a href="#specifichashpolicy" title="SpecificHashPolicy">SpecificHashPolicy</a>" : <i>[ <a href="specifichashpolicydefinition.md">SpecificHashPolicyDefinition</a>, ... ]</i>,
    "<a href="#waf" title="Waf">Waf</a>" : <i>[ <a href="wafdefinition.md">WafDefinition</a>, ... ]</i>,
    "<a href="#wafrule" title="WafRule">WafRule</a>" : <i>[ <a href="wafruledefinition.md">WafRuleDefinition</a>, ... ]</i>,
    "<a href="#websocketconfig" title="WebSocketConfig">WebSocketConfig</a>" : <i>[ <a href="websocketconfigdefinition.md">WebSocketConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commonbuffering" title="CommonBuffering">CommonBuffering</a>: <i>Boolean</i>
<a href="#commonhashpolicy" title="CommonHashPolicy">CommonHashPolicy</a>: <i>Boolean</i>
<a href="#defaultretrypolicy" title="DefaultRetryPolicy">DefaultRetryPolicy</a>: <i>Boolean</i>
<a href="#disablelocationadd" title="DisableLocationAdd">DisableLocationAdd</a>: <i>Boolean</i>
<a href="#disablemirroring" title="DisableMirroring">DisableMirroring</a>: <i>Boolean</i>
<a href="#disableprefixrewrite" title="DisablePrefixRewrite">DisablePrefixRewrite</a>: <i>Boolean</i>
<a href="#disablespdy" title="DisableSpdy">DisableSpdy</a>: <i>Boolean</i>
<a href="#disablewaf" title="DisableWaf">DisableWaf</a>: <i>Boolean</i>
<a href="#disablewebsocketconfig" title="DisableWebSocketConfig">DisableWebSocketConfig</a>: <i>Boolean</i>
<a href="#donotretractcluster" title="DoNotRetractCluster">DoNotRetractCluster</a>: <i>Boolean</i>
<a href="#enablespdy" title="EnableSpdy">EnableSpdy</a>: <i>Boolean</i>
<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>: <i>
      - <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a></i>
<a href="#prefixrewrite" title="PrefixRewrite">PrefixRewrite</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>String</i>
<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>: <i>
      - String</i>
<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>: <i>
      - String</i>
<a href="#retractcluster" title="RetractCluster">RetractCluster</a>: <i>Boolean</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#bufferpolicy" title="BufferPolicy">BufferPolicy</a>: <i>
      - <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a></i>
<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>: <i>
      - <a href="corspolicydefinition.md">CorsPolicyDefinition</a></i>
<a href="#mirrorpolicy" title="MirrorPolicy">MirrorPolicy</a>: <i>
      - <a href="mirrorpolicydefinition.md">MirrorPolicyDefinition</a></i>
<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>: <i>
      - <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a></i>
<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>: <i>
      - <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a></i>
<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicydefinition.md">RetryPolicyDefinition</a></i>
<a href="#specifichashpolicy" title="SpecificHashPolicy">SpecificHashPolicy</a>: <i>
      - <a href="specifichashpolicydefinition.md">SpecificHashPolicyDefinition</a></i>
<a href="#waf" title="Waf">Waf</a>: <i>
      - <a href="wafdefinition.md">WafDefinition</a></i>
<a href="#wafrule" title="WafRule">WafRule</a>: <i>
      - <a href="wafruledefinition.md">WafRuleDefinition</a></i>
<a href="#websocketconfig" title="WebSocketConfig">WebSocketConfig</a>: <i>
      - <a href="websocketconfigdefinition.md">WebSocketConfigDefinition</a></i>
</pre>

## Properties

#### CommonBuffering

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommonHashPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRetryPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableLocationAdd

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableMirroring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisablePrefixRewrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSpdy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableWaf

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableWebSocketConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoNotRetractCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSpdy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointSubsets

_Required_: No

_Type_: List of <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixRewrite

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToRemove

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToRemove

_Required_: No

_Type_: List of String

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

#### MirrorPolicy

_Required_: No

_Type_: List of <a href="mirrorpolicydefinition.md">MirrorPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToAdd

_Required_: No

_Type_: List of <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToAdd

_Required_: No

_Type_: List of <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecificHashPolicy

_Required_: No

_Type_: List of <a href="specifichashpolicydefinition.md">SpecificHashPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Waf

_Required_: No

_Type_: List of <a href="wafdefinition.md">WafDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafRule

_Required_: No

_Type_: List of <a href="wafruledefinition.md">WafRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebSocketConfig

_Required_: No

_Type_: List of <a href="websocketconfigdefinition.md">WebSocketConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

