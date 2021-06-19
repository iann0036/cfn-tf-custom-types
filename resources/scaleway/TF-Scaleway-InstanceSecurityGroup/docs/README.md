# TF::Scaleway::InstanceSecurityGroup

Creates and manages Scaleway Compute Instance security groups. For more information, see [the documentation](https://developers.scaleway.com/en/products/instance/api/#security-groups-8d7f89).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Scaleway::InstanceSecurityGroup",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabledefaultsecurity" title="EnableDefaultSecurity">EnableDefaultSecurity</a>" : <i>Boolean</i>,
        "<a href="#externalrules" title="ExternalRules">ExternalRules</a>" : <i>Boolean</i>,
        "<a href="#inbounddefaultpolicy" title="InboundDefaultPolicy">InboundDefaultPolicy</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outbounddefaultpolicy" title="OutboundDefaultPolicy">OutboundDefaultPolicy</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#stateful" title="Stateful">Stateful</a>" : <i>Boolean</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#inboundrule" title="InboundRule">InboundRule</a>" : <i>[ <a href="inboundruledefinition.md">InboundRuleDefinition</a>, ... ]</i>,
        "<a href="#outboundrule" title="OutboundRule">OutboundRule</a>" : <i>[ <a href="outboundruledefinition.md">OutboundRuleDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Scaleway::InstanceSecurityGroup
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabledefaultsecurity" title="EnableDefaultSecurity">EnableDefaultSecurity</a>: <i>Boolean</i>
    <a href="#externalrules" title="ExternalRules">ExternalRules</a>: <i>Boolean</i>
    <a href="#inbounddefaultpolicy" title="InboundDefaultPolicy">InboundDefaultPolicy</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outbounddefaultpolicy" title="OutboundDefaultPolicy">OutboundDefaultPolicy</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#stateful" title="Stateful">Stateful</a>: <i>Boolean</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#inboundrule" title="InboundRule">InboundRule</a>: <i>
      - <a href="inboundruledefinition.md">InboundRuleDefinition</a></i>
    <a href="#outboundrule" title="OutboundRule">OutboundRule</a>: <i>
      - <a href="outboundruledefinition.md">OutboundRuleDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDefaultSecurity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalRules

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundDefaultPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundDefaultPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateful

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundRule

_Required_: No

_Type_: List of <a href="inboundruledefinition.md">InboundRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundRule

_Required_: No

_Type_: List of <a href="outboundruledefinition.md">OutboundRuleDefinition</a>

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

#### OrganizationId

Returns the <code>OrganizationId</code> value.

