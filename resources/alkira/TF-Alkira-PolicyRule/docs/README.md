# TF::Alkira::PolicyRule

CloudFormation equivalent of alkira_policy_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alkira::PolicyRule",
    "Properties" : {
        "<a href="#applicationfamilylist" title="ApplicationFamilyList">ApplicationFamilyList</a>" : <i>[ String, ... ]</i>,
        "<a href="#applicationlist" title="ApplicationList">ApplicationList</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dscp" title="Dscp">Dscp</a>" : <i>String</i>,
        "<a href="#dstip" title="DstIp">DstIp</a>" : <i>String</i>,
        "<a href="#dstportlist" title="DstPortList">DstPortList</a>" : <i>[ String, ... ]</i>,
        "<a href="#internetapplicationid" title="InternetApplicationId">InternetApplicationId</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#ruleaction" title="RuleAction">RuleAction</a>" : <i>String</i>,
        "<a href="#ruleactionservicetypelist" title="RuleActionServiceTypeList">RuleActionServiceTypeList</a>" : <i>[ String, ... ]</i>,
        "<a href="#srcip" title="SrcIp">SrcIp</a>" : <i>String</i>,
        "<a href="#srcportlist" title="SrcPortList">SrcPortList</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alkira::PolicyRule
Properties:
    <a href="#applicationfamilylist" title="ApplicationFamilyList">ApplicationFamilyList</a>: <i>
      - String</i>
    <a href="#applicationlist" title="ApplicationList">ApplicationList</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dscp" title="Dscp">Dscp</a>: <i>String</i>
    <a href="#dstip" title="DstIp">DstIp</a>: <i>String</i>
    <a href="#dstportlist" title="DstPortList">DstPortList</a>: <i>
      - String</i>
    <a href="#internetapplicationid" title="InternetApplicationId">InternetApplicationId</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#ruleaction" title="RuleAction">RuleAction</a>: <i>String</i>
    <a href="#ruleactionservicetypelist" title="RuleActionServiceTypeList">RuleActionServiceTypeList</a>: <i>
      - String</i>
    <a href="#srcip" title="SrcIp">SrcIp</a>: <i>String</i>
    <a href="#srcportlist" title="SrcPortList">SrcPortList</a>: <i>
      - String</i>
</pre>

## Properties

#### ApplicationFamilyList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dscp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstPortList

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetApplicationId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleActionServiceTypeList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcPortList

_Required_: Yes

_Type_: List of String

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

#### RuleId

Returns the <code>RuleId</code> value.

