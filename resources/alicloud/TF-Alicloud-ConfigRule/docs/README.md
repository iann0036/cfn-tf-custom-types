# TF::Alicloud::ConfigRule

CloudFormation equivalent of alicloud_config_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ConfigRule",
    "Properties" : {
        "<a href="#configruletriggertypes" title="ConfigRuleTriggerTypes">ConfigRuleTriggerTypes</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#excluderesourceidsscope" title="ExcludeResourceIdsScope">ExcludeResourceIdsScope</a>" : <i>String</i>,
        "<a href="#inputparameters" title="InputParameters">InputParameters</a>" : <i>[ <a href="inputparametersdefinition.md">InputParametersDefinition</a>, ... ]</i>,
        "<a href="#maximumexecutionfrequency" title="MaximumExecutionFrequency">MaximumExecutionFrequency</a>" : <i>String</i>,
        "<a href="#memberid" title="MemberId">MemberId</a>" : <i>Double</i>,
        "<a href="#multiaccount" title="MultiAccount">MultiAccount</a>" : <i>Boolean</i>,
        "<a href="#regionidsscope" title="RegionIdsScope">RegionIdsScope</a>" : <i>String</i>,
        "<a href="#resourcegroupidsscope" title="ResourceGroupIdsScope">ResourceGroupIdsScope</a>" : <i>String</i>,
        "<a href="#resourcetypesscope" title="ResourceTypesScope">ResourceTypesScope</a>" : <i>[ String, ... ]</i>,
        "<a href="#risklevel" title="RiskLevel">RiskLevel</a>" : <i>Double</i>,
        "<a href="#rulename" title="RuleName">RuleName</a>" : <i>String</i>,
        "<a href="#scopecomplianceresourceid" title="ScopeComplianceResourceId">ScopeComplianceResourceId</a>" : <i>String</i>,
        "<a href="#scopecomplianceresourcetypes" title="ScopeComplianceResourceTypes">ScopeComplianceResourceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcedetailmessagetype" title="SourceDetailMessageType">SourceDetailMessageType</a>" : <i>String</i>,
        "<a href="#sourceidentifier" title="SourceIdentifier">SourceIdentifier</a>" : <i>String</i>,
        "<a href="#sourcemaximumexecutionfrequency" title="SourceMaximumExecutionFrequency">SourceMaximumExecutionFrequency</a>" : <i>String</i>,
        "<a href="#sourceowner" title="SourceOwner">SourceOwner</a>" : <i>String</i>,
        "<a href="#tagkeyscope" title="TagKeyScope">TagKeyScope</a>" : <i>String</i>,
        "<a href="#tagvaluescope" title="TagValueScope">TagValueScope</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ConfigRule
Properties:
    <a href="#configruletriggertypes" title="ConfigRuleTriggerTypes">ConfigRuleTriggerTypes</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#excluderesourceidsscope" title="ExcludeResourceIdsScope">ExcludeResourceIdsScope</a>: <i>String</i>
    <a href="#inputparameters" title="InputParameters">InputParameters</a>: <i>
      - <a href="inputparametersdefinition.md">InputParametersDefinition</a></i>
    <a href="#maximumexecutionfrequency" title="MaximumExecutionFrequency">MaximumExecutionFrequency</a>: <i>String</i>
    <a href="#memberid" title="MemberId">MemberId</a>: <i>Double</i>
    <a href="#multiaccount" title="MultiAccount">MultiAccount</a>: <i>Boolean</i>
    <a href="#regionidsscope" title="RegionIdsScope">RegionIdsScope</a>: <i>String</i>
    <a href="#resourcegroupidsscope" title="ResourceGroupIdsScope">ResourceGroupIdsScope</a>: <i>String</i>
    <a href="#resourcetypesscope" title="ResourceTypesScope">ResourceTypesScope</a>: <i>
      - String</i>
    <a href="#risklevel" title="RiskLevel">RiskLevel</a>: <i>Double</i>
    <a href="#rulename" title="RuleName">RuleName</a>: <i>String</i>
    <a href="#scopecomplianceresourceid" title="ScopeComplianceResourceId">ScopeComplianceResourceId</a>: <i>String</i>
    <a href="#scopecomplianceresourcetypes" title="ScopeComplianceResourceTypes">ScopeComplianceResourceTypes</a>: <i>
      - String</i>
    <a href="#sourcedetailmessagetype" title="SourceDetailMessageType">SourceDetailMessageType</a>: <i>String</i>
    <a href="#sourceidentifier" title="SourceIdentifier">SourceIdentifier</a>: <i>String</i>
    <a href="#sourcemaximumexecutionfrequency" title="SourceMaximumExecutionFrequency">SourceMaximumExecutionFrequency</a>: <i>String</i>
    <a href="#sourceowner" title="SourceOwner">SourceOwner</a>: <i>String</i>
    <a href="#tagkeyscope" title="TagKeyScope">TagKeyScope</a>: <i>String</i>
    <a href="#tagvaluescope" title="TagValueScope">TagValueScope</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ConfigRuleTriggerTypes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeResourceIdsScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputParameters

_Required_: No

_Type_: List of <a href="inputparametersdefinition.md">InputParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumExecutionFrequency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiAccount

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionIdsScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupIdsScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceTypesScope

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RiskLevel

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScopeComplianceResourceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScopeComplianceResourceTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDetailMessageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceMaximumExecutionFrequency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceOwner

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagKeyScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagValueScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Status

Returns the <code>Status</code> value.

