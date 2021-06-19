# TF::Nutanix::NetworkSecurityRule

Provides a Nutanix network security rule resource to Create a network security rule.

> NOTE: The use of network_security_rule is only applicable in AHV clusters and requires Microsegmentation to be enabled. This feature is a function of the Flow product and requires a Flow license. For more information on Flow and Microsegmentation please visit https://www.nutanix.com/products/flow

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nutanix::NetworkSecurityRule",
    "Properties" : {
        "<a href="#adruleaction" title="AdRuleAction">AdRuleAction</a>" : <i>String</i>,
        "<a href="#adruletargetgroupdefaultinternalpolicy" title="AdRuleTargetGroupDefaultInternalPolicy">AdRuleTargetGroupDefaultInternalPolicy</a>" : <i>String</i>,
        "<a href="#adruletargetgroupfilterkindlist" title="AdRuleTargetGroupFilterKindList">AdRuleTargetGroupFilterKindList</a>" : <i>[ String, ... ]</i>,
        "<a href="#adruletargetgroupfiltertype" title="AdRuleTargetGroupFilterType">AdRuleTargetGroupFilterType</a>" : <i>String</i>,
        "<a href="#adruletargetgrouppeerspecificationtype" title="AdRuleTargetGroupPeerSpecificationType">AdRuleTargetGroupPeerSpecificationType</a>" : <i>String</i>,
        "<a href="#allowipv6traffic" title="AllowIpv6Traffic">AllowIpv6Traffic</a>" : <i>Boolean</i>,
        "<a href="#appruleaction" title="AppRuleAction">AppRuleAction</a>" : <i>String</i>,
        "<a href="#appruletargetgroupdefaultinternalpolicy" title="AppRuleTargetGroupDefaultInternalPolicy">AppRuleTargetGroupDefaultInternalPolicy</a>" : <i>String</i>,
        "<a href="#appruletargetgroupfilterkindlist" title="AppRuleTargetGroupFilterKindList">AppRuleTargetGroupFilterKindList</a>" : <i>[ String, ... ]</i>,
        "<a href="#appruletargetgroupfiltertype" title="AppRuleTargetGroupFilterType">AppRuleTargetGroupFilterType</a>" : <i>String</i>,
        "<a href="#appruletargetgrouppeerspecificationtype" title="AppRuleTargetGroupPeerSpecificationType">AppRuleTargetGroupPeerSpecificationType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ispolicyhitlogenabled" title="IsPolicyHitlogEnabled">IsPolicyHitlogEnabled</a>" : <i>Boolean</i>,
        "<a href="#isolationruleaction" title="IsolationRuleAction">IsolationRuleAction</a>" : <i>String</i>,
        "<a href="#isolationrulefirstentityfilterkindlist" title="IsolationRuleFirstEntityFilterKindList">IsolationRuleFirstEntityFilterKindList</a>" : <i>[ String, ... ]</i>,
        "<a href="#isolationrulefirstentityfiltertype" title="IsolationRuleFirstEntityFilterType">IsolationRuleFirstEntityFilterType</a>" : <i>String</i>,
        "<a href="#isolationrulesecondentityfilterkindlist" title="IsolationRuleSecondEntityFilterKindList">IsolationRuleSecondEntityFilterKindList</a>" : <i>[ String, ... ]</i>,
        "<a href="#isolationrulesecondentityfiltertype" title="IsolationRuleSecondEntityFilterType">IsolationRuleSecondEntityFilterType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>, ... ]</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>, ... ]</i>,
        "<a href="#adruleinboundallowlist" title="AdRuleInboundAllowList">AdRuleInboundAllowList</a>" : <i>[ <a href="adruleinboundallowlistdefinition.md">AdRuleInboundAllowListDefinition</a>, ... ]</i>,
        "<a href="#adruleoutboundallowlist" title="AdRuleOutboundAllowList">AdRuleOutboundAllowList</a>" : <i>[ <a href="adruleoutboundallowlistdefinition.md">AdRuleOutboundAllowListDefinition</a>, ... ]</i>,
        "<a href="#adruletargetgroupfilterparams" title="AdRuleTargetGroupFilterParams">AdRuleTargetGroupFilterParams</a>" : <i>[ <a href="adruletargetgroupfilterparamsdefinition.md">AdRuleTargetGroupFilterParamsDefinition</a>, ... ]</i>,
        "<a href="#appruleinboundallowlist" title="AppRuleInboundAllowList">AppRuleInboundAllowList</a>" : <i>[ <a href="appruleinboundallowlistdefinition.md">AppRuleInboundAllowListDefinition</a>, ... ]</i>,
        "<a href="#appruleoutboundallowlist" title="AppRuleOutboundAllowList">AppRuleOutboundAllowList</a>" : <i>[ <a href="appruleoutboundallowlistdefinition.md">AppRuleOutboundAllowListDefinition</a>, ... ]</i>,
        "<a href="#appruletargetgroupfilterparams" title="AppRuleTargetGroupFilterParams">AppRuleTargetGroupFilterParams</a>" : <i>[ <a href="appruletargetgroupfilterparamsdefinition.md">AppRuleTargetGroupFilterParamsDefinition</a>, ... ]</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>,
        "<a href="#isolationrulefirstentityfilterparams" title="IsolationRuleFirstEntityFilterParams">IsolationRuleFirstEntityFilterParams</a>" : <i>[ <a href="isolationrulefirstentityfilterparamsdefinition.md">IsolationRuleFirstEntityFilterParamsDefinition</a>, ... ]</i>,
        "<a href="#isolationrulesecondentityfilterparams" title="IsolationRuleSecondEntityFilterParams">IsolationRuleSecondEntityFilterParams</a>" : <i>[ <a href="isolationrulesecondentityfilterparamsdefinition.md">IsolationRuleSecondEntityFilterParamsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nutanix::NetworkSecurityRule
Properties:
    <a href="#adruleaction" title="AdRuleAction">AdRuleAction</a>: <i>String</i>
    <a href="#adruletargetgroupdefaultinternalpolicy" title="AdRuleTargetGroupDefaultInternalPolicy">AdRuleTargetGroupDefaultInternalPolicy</a>: <i>String</i>
    <a href="#adruletargetgroupfilterkindlist" title="AdRuleTargetGroupFilterKindList">AdRuleTargetGroupFilterKindList</a>: <i>
      - String</i>
    <a href="#adruletargetgroupfiltertype" title="AdRuleTargetGroupFilterType">AdRuleTargetGroupFilterType</a>: <i>String</i>
    <a href="#adruletargetgrouppeerspecificationtype" title="AdRuleTargetGroupPeerSpecificationType">AdRuleTargetGroupPeerSpecificationType</a>: <i>String</i>
    <a href="#allowipv6traffic" title="AllowIpv6Traffic">AllowIpv6Traffic</a>: <i>Boolean</i>
    <a href="#appruleaction" title="AppRuleAction">AppRuleAction</a>: <i>String</i>
    <a href="#appruletargetgroupdefaultinternalpolicy" title="AppRuleTargetGroupDefaultInternalPolicy">AppRuleTargetGroupDefaultInternalPolicy</a>: <i>String</i>
    <a href="#appruletargetgroupfilterkindlist" title="AppRuleTargetGroupFilterKindList">AppRuleTargetGroupFilterKindList</a>: <i>
      - String</i>
    <a href="#appruletargetgroupfiltertype" title="AppRuleTargetGroupFilterType">AppRuleTargetGroupFilterType</a>: <i>String</i>
    <a href="#appruletargetgrouppeerspecificationtype" title="AppRuleTargetGroupPeerSpecificationType">AppRuleTargetGroupPeerSpecificationType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ispolicyhitlogenabled" title="IsPolicyHitlogEnabled">IsPolicyHitlogEnabled</a>: <i>Boolean</i>
    <a href="#isolationruleaction" title="IsolationRuleAction">IsolationRuleAction</a>: <i>String</i>
    <a href="#isolationrulefirstentityfilterkindlist" title="IsolationRuleFirstEntityFilterKindList">IsolationRuleFirstEntityFilterKindList</a>: <i>
      - String</i>
    <a href="#isolationrulefirstentityfiltertype" title="IsolationRuleFirstEntityFilterType">IsolationRuleFirstEntityFilterType</a>: <i>String</i>
    <a href="#isolationrulesecondentityfilterkindlist" title="IsolationRuleSecondEntityFilterKindList">IsolationRuleSecondEntityFilterKindList</a>: <i>
      - String</i>
    <a href="#isolationrulesecondentityfiltertype" title="IsolationRuleSecondEntityFilterType">IsolationRuleSecondEntityFilterType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a></i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a></i>
    <a href="#adruleinboundallowlist" title="AdRuleInboundAllowList">AdRuleInboundAllowList</a>: <i>
      - <a href="adruleinboundallowlistdefinition.md">AdRuleInboundAllowListDefinition</a></i>
    <a href="#adruleoutboundallowlist" title="AdRuleOutboundAllowList">AdRuleOutboundAllowList</a>: <i>
      - <a href="adruleoutboundallowlistdefinition.md">AdRuleOutboundAllowListDefinition</a></i>
    <a href="#adruletargetgroupfilterparams" title="AdRuleTargetGroupFilterParams">AdRuleTargetGroupFilterParams</a>: <i>
      - <a href="adruletargetgroupfilterparamsdefinition.md">AdRuleTargetGroupFilterParamsDefinition</a></i>
    <a href="#appruleinboundallowlist" title="AppRuleInboundAllowList">AppRuleInboundAllowList</a>: <i>
      - <a href="appruleinboundallowlistdefinition.md">AppRuleInboundAllowListDefinition</a></i>
    <a href="#appruleoutboundallowlist" title="AppRuleOutboundAllowList">AppRuleOutboundAllowList</a>: <i>
      - <a href="appruleoutboundallowlistdefinition.md">AppRuleOutboundAllowListDefinition</a></i>
    <a href="#appruletargetgroupfilterparams" title="AppRuleTargetGroupFilterParams">AppRuleTargetGroupFilterParams</a>: <i>
      - <a href="appruletargetgroupfilterparamsdefinition.md">AppRuleTargetGroupFilterParamsDefinition</a></i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
    <a href="#isolationrulefirstentityfilterparams" title="IsolationRuleFirstEntityFilterParams">IsolationRuleFirstEntityFilterParams</a>: <i>
      - <a href="isolationrulefirstentityfilterparamsdefinition.md">IsolationRuleFirstEntityFilterParamsDefinition</a></i>
    <a href="#isolationrulesecondentityfilterparams" title="IsolationRuleSecondEntityFilterParams">IsolationRuleSecondEntityFilterParams</a>: <i>
      - <a href="isolationrulesecondentityfilterparamsdefinition.md">IsolationRuleSecondEntityFilterParamsDefinition</a></i>
</pre>

## Properties

#### AdRuleAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdRuleTargetGroupDefaultInternalPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdRuleTargetGroupFilterKindList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdRuleTargetGroupFilterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdRuleTargetGroupPeerSpecificationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIpv6Traffic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleTargetGroupDefaultInternalPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleTargetGroupFilterKindList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleTargetGroupFilterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleTargetGroupPeerSpecificationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPolicyHitlogEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleFirstEntityFilterKindList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleFirstEntityFilterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleSecondEntityFilterKindList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleSecondEntityFilterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdRuleInboundAllowList

_Required_: No

_Type_: List of <a href="adruleinboundallowlistdefinition.md">AdRuleInboundAllowListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdRuleOutboundAllowList

_Required_: No

_Type_: List of <a href="adruleoutboundallowlistdefinition.md">AdRuleOutboundAllowListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdRuleTargetGroupFilterParams

_Required_: No

_Type_: List of <a href="adruletargetgroupfilterparamsdefinition.md">AdRuleTargetGroupFilterParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleInboundAllowList

_Required_: No

_Type_: List of <a href="appruleinboundallowlistdefinition.md">AppRuleInboundAllowListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleOutboundAllowList

_Required_: No

_Type_: List of <a href="appruleoutboundallowlistdefinition.md">AppRuleOutboundAllowListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleTargetGroupFilterParams

_Required_: No

_Type_: List of <a href="appruletargetgroupfilterparamsdefinition.md">AppRuleTargetGroupFilterParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleFirstEntityFilterParams

_Required_: No

_Type_: List of <a href="isolationrulefirstentityfilterparamsdefinition.md">IsolationRuleFirstEntityFilterParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleSecondEntityFilterParams

_Required_: No

_Type_: List of <a href="isolationrulesecondentityfilterparamsdefinition.md">IsolationRuleSecondEntityFilterParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiVersion

Returns the <code>ApiVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

