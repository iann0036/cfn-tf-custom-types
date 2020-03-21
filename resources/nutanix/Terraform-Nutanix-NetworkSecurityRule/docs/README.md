# Terraform::Nutanix::NetworkSecurityRule

CloudFormation equivalent of nutanix_network_security_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Nutanix::NetworkSecurityRule",
    "Properties" : {
        "<a href="#appruleaction" title="AppRuleAction">AppRuleAction</a>" : <i>String</i>,
        "<a href="#appruletargetgroupdefaultinternalpolicy" title="AppRuleTargetGroupDefaultInternalPolicy">AppRuleTargetGroupDefaultInternalPolicy</a>" : <i>String</i>,
        "<a href="#appruletargetgroupfilterkindlist" title="AppRuleTargetGroupFilterKindList">AppRuleTargetGroupFilterKindList</a>" : <i>[ String, ... ]</i>,
        "<a href="#appruletargetgroupfiltertype" title="AppRuleTargetGroupFilterType">AppRuleTargetGroupFilterType</a>" : <i>String</i>,
        "<a href="#appruletargetgrouppeerspecificationtype" title="AppRuleTargetGroupPeerSpecificationType">AppRuleTargetGroupPeerSpecificationType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isolationruleaction" title="IsolationRuleAction">IsolationRuleAction</a>" : <i>String</i>,
        "<a href="#isolationrulefirstentityfilterkindlist" title="IsolationRuleFirstEntityFilterKindList">IsolationRuleFirstEntityFilterKindList</a>" : <i>[ String, ... ]</i>,
        "<a href="#isolationrulefirstentityfiltertype" title="IsolationRuleFirstEntityFilterType">IsolationRuleFirstEntityFilterType</a>" : <i>String</i>,
        "<a href="#isolationrulesecondentityfilterkindlist" title="IsolationRuleSecondEntityFilterKindList">IsolationRuleSecondEntityFilterKindList</a>" : <i>[ String, ... ]</i>,
        "<a href="#isolationrulesecondentityfiltertype" title="IsolationRuleSecondEntityFilterType">IsolationRuleSecondEntityFilterType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreference.md">OwnerReference</a>, ... ]</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreference.md">ProjectReference</a>, ... ]</i>,
        "<a href="#appruleinboundallowlist" title="AppRuleInboundAllowList">AppRuleInboundAllowList</a>" : <i>[ <a href="appruleinboundallowlist.md">AppRuleInboundAllowList</a>, ... ]</i>,
        "<a href="#appruleoutboundallowlist" title="AppRuleOutboundAllowList">AppRuleOutboundAllowList</a>" : <i>[ <a href="appruleoutboundallowlist.md">AppRuleOutboundAllowList</a>, ... ]</i>,
        "<a href="#appruletargetgroupfilterparams" title="AppRuleTargetGroupFilterParams">AppRuleTargetGroupFilterParams</a>" : <i>[ <a href="appruletargetgroupfilterparams.md">AppRuleTargetGroupFilterParams</a>, ... ]</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categories.md">Categories</a>, ... ]</i>,
        "<a href="#isolationrulefirstentityfilterparams" title="IsolationRuleFirstEntityFilterParams">IsolationRuleFirstEntityFilterParams</a>" : <i>[ <a href="isolationrulefirstentityfilterparams.md">IsolationRuleFirstEntityFilterParams</a>, ... ]</i>,
        "<a href="#isolationrulesecondentityfilterparams" title="IsolationRuleSecondEntityFilterParams">IsolationRuleSecondEntityFilterParams</a>" : <i>[ <a href="isolationrulesecondentityfilterparams.md">IsolationRuleSecondEntityFilterParams</a>, ... ]</i>,
        "<a href="#filterparams" title="FilterParams">FilterParams</a>" : <i>[ <a href="filterparams.md">FilterParams</a>, ... ]</i>,
        "<a href="#icmptypecodelist" title="IcmpTypeCodeList">IcmpTypeCodeList</a>" : <i>[ <a href="icmptypecodelist.md">IcmpTypeCodeList</a>, ... ]</i>,
        "<a href="#tcpportrangelist" title="TcpPortRangeList">TcpPortRangeList</a>" : <i>[ <a href="tcpportrangelist.md">TcpPortRangeList</a>, ... ]</i>,
        "<a href="#udpportrangelist" title="UdpPortRangeList">UdpPortRangeList</a>" : <i>[ <a href="udpportrangelist.md">UdpPortRangeList</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Nutanix::NetworkSecurityRule
Properties:
    <a href="#appruleaction" title="AppRuleAction">AppRuleAction</a>: <i>String</i>
    <a href="#appruletargetgroupdefaultinternalpolicy" title="AppRuleTargetGroupDefaultInternalPolicy">AppRuleTargetGroupDefaultInternalPolicy</a>: <i>String</i>
    <a href="#appruletargetgroupfilterkindlist" title="AppRuleTargetGroupFilterKindList">AppRuleTargetGroupFilterKindList</a>: <i>
      - String</i>
    <a href="#appruletargetgroupfiltertype" title="AppRuleTargetGroupFilterType">AppRuleTargetGroupFilterType</a>: <i>String</i>
    <a href="#appruletargetgrouppeerspecificationtype" title="AppRuleTargetGroupPeerSpecificationType">AppRuleTargetGroupPeerSpecificationType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isolationruleaction" title="IsolationRuleAction">IsolationRuleAction</a>: <i>String</i>
    <a href="#isolationrulefirstentityfilterkindlist" title="IsolationRuleFirstEntityFilterKindList">IsolationRuleFirstEntityFilterKindList</a>: <i>
      - String</i>
    <a href="#isolationrulefirstentityfiltertype" title="IsolationRuleFirstEntityFilterType">IsolationRuleFirstEntityFilterType</a>: <i>String</i>
    <a href="#isolationrulesecondentityfilterkindlist" title="IsolationRuleSecondEntityFilterKindList">IsolationRuleSecondEntityFilterKindList</a>: <i>
      - String</i>
    <a href="#isolationrulesecondentityfiltertype" title="IsolationRuleSecondEntityFilterType">IsolationRuleSecondEntityFilterType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreference.md">OwnerReference</a></i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreference.md">ProjectReference</a></i>
    <a href="#appruleinboundallowlist" title="AppRuleInboundAllowList">AppRuleInboundAllowList</a>: <i>
      - <a href="appruleinboundallowlist.md">AppRuleInboundAllowList</a></i>
    <a href="#appruleoutboundallowlist" title="AppRuleOutboundAllowList">AppRuleOutboundAllowList</a>: <i>
      - <a href="appruleoutboundallowlist.md">AppRuleOutboundAllowList</a></i>
    <a href="#appruletargetgroupfilterparams" title="AppRuleTargetGroupFilterParams">AppRuleTargetGroupFilterParams</a>: <i>
      - <a href="appruletargetgroupfilterparams.md">AppRuleTargetGroupFilterParams</a></i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categories.md">Categories</a></i>
    <a href="#isolationrulefirstentityfilterparams" title="IsolationRuleFirstEntityFilterParams">IsolationRuleFirstEntityFilterParams</a>: <i>
      - <a href="isolationrulefirstentityfilterparams.md">IsolationRuleFirstEntityFilterParams</a></i>
    <a href="#isolationrulesecondentityfilterparams" title="IsolationRuleSecondEntityFilterParams">IsolationRuleSecondEntityFilterParams</a>: <i>
      - <a href="isolationrulesecondentityfilterparams.md">IsolationRuleSecondEntityFilterParams</a></i>
    <a href="#filterparams" title="FilterParams">FilterParams</a>: <i>
      - <a href="filterparams.md">FilterParams</a></i>
    <a href="#icmptypecodelist" title="IcmpTypeCodeList">IcmpTypeCodeList</a>: <i>
      - <a href="icmptypecodelist.md">IcmpTypeCodeList</a></i>
    <a href="#tcpportrangelist" title="TcpPortRangeList">TcpPortRangeList</a>: <i>
      - <a href="tcpportrangelist.md">TcpPortRangeList</a></i>
    <a href="#udpportrangelist" title="UdpPortRangeList">UdpPortRangeList</a>: <i>
      - <a href="udpportrangelist.md">UdpPortRangeList</a></i>
</pre>

## Properties

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

_Type_: List of <a href="ownerreference.md">OwnerReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreference.md">ProjectReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleInboundAllowList

_Required_: No

_Type_: List of <a href="appruleinboundallowlist.md">AppRuleInboundAllowList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleOutboundAllowList

_Required_: No

_Type_: List of <a href="appruleoutboundallowlist.md">AppRuleOutboundAllowList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRuleTargetGroupFilterParams

_Required_: No

_Type_: List of <a href="appruletargetgroupfilterparams.md">AppRuleTargetGroupFilterParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categories.md">Categories</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleFirstEntityFilterParams

_Required_: No

_Type_: List of <a href="isolationrulefirstentityfilterparams.md">IsolationRuleFirstEntityFilterParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationRuleSecondEntityFilterParams

_Required_: No

_Type_: List of <a href="isolationrulesecondentityfilterparams.md">IsolationRuleSecondEntityFilterParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterParams

_Required_: No

_Type_: List of <a href="filterparams.md">FilterParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpTypeCodeList

_Required_: No

_Type_: List of <a href="icmptypecodelist.md">IcmpTypeCodeList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpPortRangeList

_Required_: No

_Type_: List of <a href="tcpportrangelist.md">TcpPortRangeList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpPortRangeList

_Required_: No

_Type_: List of <a href="udpportrangelist.md">UdpPortRangeList</a>

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

#### Metadata

Returns the <code>Metadata</code> value.

