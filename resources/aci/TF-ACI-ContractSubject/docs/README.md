# TF::ACI::ContractSubject

CloudFormation equivalent of aci_contract_subject

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::ContractSubject",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#consmatcht" title="ConsMatchT">ConsMatchT</a>" : <i>String</i>,
        "<a href="#contractdn" title="ContractDn">ContractDn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#prio" title="Prio">Prio</a>" : <i>String</i>,
        "<a href="#provmatcht" title="ProvMatchT">ProvMatchT</a>" : <i>String</i>,
        "<a href="#relationvzrssdwanpol" title="RelationVzRsSdwanPol">RelationVzRsSdwanPol</a>" : <i>String</i>,
        "<a href="#relationvzrssubjfiltatt" title="RelationVzRsSubjFiltAtt">RelationVzRsSubjFiltAtt</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationvzrssubjgraphatt" title="RelationVzRsSubjGraphAtt">RelationVzRsSubjGraphAtt</a>" : <i>String</i>,
        "<a href="#revfltports" title="RevFltPorts">RevFltPorts</a>" : <i>String</i>,
        "<a href="#targetdscp" title="TargetDscp">TargetDscp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::ContractSubject
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#consmatcht" title="ConsMatchT">ConsMatchT</a>: <i>String</i>
    <a href="#contractdn" title="ContractDn">ContractDn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#prio" title="Prio">Prio</a>: <i>String</i>
    <a href="#provmatcht" title="ProvMatchT">ProvMatchT</a>: <i>String</i>
    <a href="#relationvzrssdwanpol" title="RelationVzRsSdwanPol">RelationVzRsSdwanPol</a>: <i>String</i>
    <a href="#relationvzrssubjfiltatt" title="RelationVzRsSubjFiltAtt">RelationVzRsSubjFiltAtt</a>: <i>
      - String</i>
    <a href="#relationvzrssubjgraphatt" title="RelationVzRsSubjGraphAtt">RelationVzRsSubjGraphAtt</a>: <i>String</i>
    <a href="#revfltports" title="RevFltPorts">RevFltPorts</a>: <i>String</i>
    <a href="#targetdscp" title="TargetDscp">TargetDscp</a>: <i>String</i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsMatchT

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContractDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prio

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvMatchT

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVzRsSdwanPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVzRsSubjFiltAtt

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVzRsSubjGraphAtt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevFltPorts

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDscp

_Required_: No

_Type_: String

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

