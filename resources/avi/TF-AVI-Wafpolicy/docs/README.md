# TF::AVI::Wafpolicy

The WafPolicy resource allows the creation and management of Avi WafPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Wafpolicy",
    "Properties" : {
        "<a href="#allowmodedelegation" title="AllowModeDelegation">AllowModeDelegation</a>" : <i>Boolean</i>,
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableapplearning" title="EnableAppLearning">EnableAppLearning</a>" : <i>Boolean</i>,
        "<a href="#enableautoruleupdates" title="EnableAutoRuleUpdates">EnableAutoRuleUpdates</a>" : <i>Boolean</i>,
        "<a href="#enableregexlearning" title="EnableRegexLearning">EnableRegexLearning</a>" : <i>Boolean</i>,
        "<a href="#failuremode" title="FailureMode">FailureMode</a>" : <i>String</i>,
        "<a href="#minconfidence" title="MinConfidence">MinConfidence</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#paranoialevel" title="ParanoiaLevel">ParanoiaLevel</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#wafcrsref" title="WafCrsRef">WafCrsRef</a>" : <i>String</i>,
        "<a href="#wafprofileref" title="WafProfileRef">WafProfileRef</a>" : <i>String</i>,
        "<a href="#allowlist" title="Allowlist">Allowlist</a>" : <i>[ <a href="allowlistdefinition.md">AllowlistDefinition</a>, ... ]</i>,
        "<a href="#applicationsignatures" title="ApplicationSignatures">ApplicationSignatures</a>" : <i>[ <a href="applicationsignaturesdefinition.md">ApplicationSignaturesDefinition</a>, ... ]</i>,
        "<a href="#confidenceoverride" title="ConfidenceOverride">ConfidenceOverride</a>" : <i>[ <a href="confidenceoverridedefinition.md">ConfidenceOverrideDefinition</a>, ... ]</i>,
        "<a href="#crsoverrides" title="CrsOverrides">CrsOverrides</a>" : <i>[ <a href="crsoverridesdefinition.md">CrsOverridesDefinition</a>, ... ]</i>,
        "<a href="#learningparams" title="LearningParams">LearningParams</a>" : <i>[ <a href="learningparamsdefinition.md">LearningParamsDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#positivesecuritymodel" title="PositiveSecurityModel">PositiveSecurityModel</a>" : <i>[ <a href="positivesecuritymodeldefinition.md">PositiveSecurityModelDefinition</a>, ... ]</i>,
        "<a href="#postcrsgroups" title="PostCrsGroups">PostCrsGroups</a>" : <i>[ <a href="postcrsgroupsdefinition.md">PostCrsGroupsDefinition</a>, ... ]</i>,
        "<a href="#precrsgroups" title="PreCrsGroups">PreCrsGroups</a>" : <i>[ <a href="precrsgroupsdefinition.md">PreCrsGroupsDefinition</a>, ... ]</i>,
        "<a href="#resolvedcrsgroups" title="ResolvedCrsGroups">ResolvedCrsGroups</a>" : <i>[ <a href="resolvedcrsgroupsdefinition.md">ResolvedCrsGroupsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Wafpolicy
Properties:
    <a href="#allowmodedelegation" title="AllowModeDelegation">AllowModeDelegation</a>: <i>Boolean</i>
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableapplearning" title="EnableAppLearning">EnableAppLearning</a>: <i>Boolean</i>
    <a href="#enableautoruleupdates" title="EnableAutoRuleUpdates">EnableAutoRuleUpdates</a>: <i>Boolean</i>
    <a href="#enableregexlearning" title="EnableRegexLearning">EnableRegexLearning</a>: <i>Boolean</i>
    <a href="#failuremode" title="FailureMode">FailureMode</a>: <i>String</i>
    <a href="#minconfidence" title="MinConfidence">MinConfidence</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#paranoialevel" title="ParanoiaLevel">ParanoiaLevel</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#wafcrsref" title="WafCrsRef">WafCrsRef</a>: <i>String</i>
    <a href="#wafprofileref" title="WafProfileRef">WafProfileRef</a>: <i>String</i>
    <a href="#allowlist" title="Allowlist">Allowlist</a>: <i>
      - <a href="allowlistdefinition.md">AllowlistDefinition</a></i>
    <a href="#applicationsignatures" title="ApplicationSignatures">ApplicationSignatures</a>: <i>
      - <a href="applicationsignaturesdefinition.md">ApplicationSignaturesDefinition</a></i>
    <a href="#confidenceoverride" title="ConfidenceOverride">ConfidenceOverride</a>: <i>
      - <a href="confidenceoverridedefinition.md">ConfidenceOverrideDefinition</a></i>
    <a href="#crsoverrides" title="CrsOverrides">CrsOverrides</a>: <i>
      - <a href="crsoverridesdefinition.md">CrsOverridesDefinition</a></i>
    <a href="#learningparams" title="LearningParams">LearningParams</a>: <i>
      - <a href="learningparamsdefinition.md">LearningParamsDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#positivesecuritymodel" title="PositiveSecurityModel">PositiveSecurityModel</a>: <i>
      - <a href="positivesecuritymodeldefinition.md">PositiveSecurityModelDefinition</a></i>
    <a href="#postcrsgroups" title="PostCrsGroups">PostCrsGroups</a>: <i>
      - <a href="postcrsgroupsdefinition.md">PostCrsGroupsDefinition</a></i>
    <a href="#precrsgroups" title="PreCrsGroups">PreCrsGroups</a>: <i>
      - <a href="precrsgroupsdefinition.md">PreCrsGroupsDefinition</a></i>
    <a href="#resolvedcrsgroups" title="ResolvedCrsGroups">ResolvedCrsGroups</a>: <i>
      - <a href="resolvedcrsgroupsdefinition.md">ResolvedCrsGroupsDefinition</a></i>
</pre>

## Properties

#### AllowModeDelegation

Allow rules to overwrite the policy mode. This must be set if the policy mode is set to enforcement. Field introduced in 18.1.5, 18.2.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBy

Creator name. Field introduced in 17.2.4.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Field introduced in 17.2.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAppLearning

Enable application learning for this waf policy. Field introduced in 18.2.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoRuleUpdates

Enable application learning based rule updates on the waf profile. Rules will be programmed in dedicated waf learning group. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRegexLearning

Enable dynamic regex generation for positive security model rules. This is an experimental feature and shouldn't be used in production. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureMode

Waf policy failure mode. This can be 'open' or 'closed'. Enum options - WAF_FAILURE_MODE_OPEN, WAF_FAILURE_MODE_CLOSED. Field introduced in 18.1.2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinConfidence

Minimum confidence label required for auto rule updates. Enum options - CONFIDENCE_VERY_HIGH, CONFIDENCE_HIGH, CONFIDENCE_PROBABLE, CONFIDENCE_LOW, CONFIDENCE_NONE. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Waf policy mode. This can be detection or enforcement. It can be overwritten by rules if allow_mode_delegation is set. Enum options - WAF_MODE_DETECTION_ONLY, WAF_MODE_ENFORCEMENT. Field introduced in 17.2.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Field introduced in 17.2.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParanoiaLevel

Waf ruleset paranoia  mode. This is used to select rules based on the paranoia-level tag. Enum options - WAF_PARANOIA_LEVEL_LOW, WAF_PARANOIA_LEVEL_MEDIUM, WAF_PARANOIA_LEVEL_HIGH, WAF_PARANOIA_LEVEL_EXTREME. Field introduced in 17.2.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant. Field introduced in 17.2.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafCrsRef

Waf core ruleset used for the crs part of this policy. It is a reference to an object of type wafcrs. Field introduced in 18.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafProfileRef

Waf profile for waf policy. It is a reference to an object of type wafprofile. Field introduced in 17.2.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Allowlist

_Required_: No

_Type_: List of <a href="allowlistdefinition.md">AllowlistDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSignatures

_Required_: No

_Type_: List of <a href="applicationsignaturesdefinition.md">ApplicationSignaturesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidenceOverride

_Required_: No

_Type_: List of <a href="confidenceoverridedefinition.md">ConfidenceOverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrsOverrides

_Required_: No

_Type_: List of <a href="crsoverridesdefinition.md">CrsOverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LearningParams

_Required_: No

_Type_: List of <a href="learningparamsdefinition.md">LearningParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositiveSecurityModel

_Required_: No

_Type_: List of <a href="positivesecuritymodeldefinition.md">PositiveSecurityModelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostCrsGroups

_Required_: No

_Type_: List of <a href="postcrsgroupsdefinition.md">PostCrsGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreCrsGroups

_Required_: No

_Type_: List of <a href="precrsgroupsdefinition.md">PreCrsGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolvedCrsGroups

_Required_: No

_Type_: List of <a href="resolvedcrsgroupsdefinition.md">ResolvedCrsGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

