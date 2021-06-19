# TF::AWS::CloudfrontDistribution DefaultCacheBehaviorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#cachepolicyid" title="CachePolicyId">CachePolicyId</a>" : <i>String</i>,
    "<a href="#cachedmethods" title="CachedMethods">CachedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#compress" title="Compress">Compress</a>" : <i>Boolean</i>,
    "<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>" : <i>Double</i>,
    "<a href="#fieldlevelencryptionid" title="FieldLevelEncryptionId">FieldLevelEncryptionId</a>" : <i>String</i>,
    "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>Double</i>,
    "<a href="#minttl" title="MinTtl">MinTtl</a>" : <i>Double</i>,
    "<a href="#originrequestpolicyid" title="OriginRequestPolicyId">OriginRequestPolicyId</a>" : <i>String</i>,
    "<a href="#realtimelogconfigarn" title="RealtimeLogConfigArn">RealtimeLogConfigArn</a>" : <i>String</i>,
    "<a href="#smoothstreaming" title="SmoothStreaming">SmoothStreaming</a>" : <i>Boolean</i>,
    "<a href="#targetoriginid" title="TargetOriginId">TargetOriginId</a>" : <i>String</i>,
    "<a href="#trustedkeygroups" title="TrustedKeyGroups">TrustedKeyGroups</a>" : <i>[ <a href="trustedkeygroupsdefinition2.md">TrustedKeyGroupsDefinition2</a>, ... ]</i>,
    "<a href="#trustedsigners" title="TrustedSigners">TrustedSigners</a>" : <i>[ <a href="trustedsignersdefinition2.md">TrustedSignersDefinition2</a>, ... ]</i>,
    "<a href="#viewerprotocolpolicy" title="ViewerProtocolPolicy">ViewerProtocolPolicy</a>" : <i>String</i>,
    "<a href="#forwardedvalues" title="ForwardedValues">ForwardedValues</a>" : <i>[ <a href="forwardedvaluesdefinition.md">ForwardedValuesDefinition</a>, ... ]</i>,
    "<a href="#functionassociation" title="FunctionAssociation">FunctionAssociation</a>" : <i>[ <a href="functionassociationdefinition.md">FunctionAssociationDefinition</a>, ... ]</i>,
    "<a href="#lambdafunctionassociation" title="LambdaFunctionAssociation">LambdaFunctionAssociation</a>" : <i>[ <a href="lambdafunctionassociationdefinition.md">LambdaFunctionAssociationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>: <i>
      - String</i>
<a href="#cachepolicyid" title="CachePolicyId">CachePolicyId</a>: <i>String</i>
<a href="#cachedmethods" title="CachedMethods">CachedMethods</a>: <i>
      - String</i>
<a href="#compress" title="Compress">Compress</a>: <i>Boolean</i>
<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>: <i>Double</i>
<a href="#fieldlevelencryptionid" title="FieldLevelEncryptionId">FieldLevelEncryptionId</a>: <i>String</i>
<a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>Double</i>
<a href="#minttl" title="MinTtl">MinTtl</a>: <i>Double</i>
<a href="#originrequestpolicyid" title="OriginRequestPolicyId">OriginRequestPolicyId</a>: <i>String</i>
<a href="#realtimelogconfigarn" title="RealtimeLogConfigArn">RealtimeLogConfigArn</a>: <i>String</i>
<a href="#smoothstreaming" title="SmoothStreaming">SmoothStreaming</a>: <i>Boolean</i>
<a href="#targetoriginid" title="TargetOriginId">TargetOriginId</a>: <i>String</i>
<a href="#trustedkeygroups" title="TrustedKeyGroups">TrustedKeyGroups</a>: <i>
      - <a href="trustedkeygroupsdefinition2.md">TrustedKeyGroupsDefinition2</a></i>
<a href="#trustedsigners" title="TrustedSigners">TrustedSigners</a>: <i>
      - <a href="trustedsignersdefinition2.md">TrustedSignersDefinition2</a></i>
<a href="#viewerprotocolpolicy" title="ViewerProtocolPolicy">ViewerProtocolPolicy</a>: <i>String</i>
<a href="#forwardedvalues" title="ForwardedValues">ForwardedValues</a>: <i>
      - <a href="forwardedvaluesdefinition.md">ForwardedValuesDefinition</a></i>
<a href="#functionassociation" title="FunctionAssociation">FunctionAssociation</a>: <i>
      - <a href="functionassociationdefinition.md">FunctionAssociationDefinition</a></i>
<a href="#lambdafunctionassociation" title="LambdaFunctionAssociation">LambdaFunctionAssociation</a>: <i>
      - <a href="lambdafunctionassociationdefinition.md">LambdaFunctionAssociationDefinition</a></i>
</pre>

## Properties

#### AllowedMethods

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachePolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachedMethods

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldLevelEncryptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginRequestPolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealtimeLogConfigArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmoothStreaming

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetOriginId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedKeyGroups

_Required_: No

_Type_: List of <a href="trustedkeygroupsdefinition2.md">TrustedKeyGroupsDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedSigners

_Required_: No

_Type_: List of <a href="trustedsignersdefinition2.md">TrustedSignersDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewerProtocolPolicy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardedValues

_Required_: No

_Type_: List of <a href="forwardedvaluesdefinition.md">ForwardedValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionAssociation

_Required_: No

_Type_: List of <a href="functionassociationdefinition.md">FunctionAssociationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFunctionAssociation

_Required_: No

_Type_: List of <a href="lambdafunctionassociationdefinition.md">LambdaFunctionAssociationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

