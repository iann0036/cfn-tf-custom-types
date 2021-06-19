# TF::ACI::FcDomain

CloudFormation equivalent of aci_fc_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::FcDomain",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationfcrsvsanattr" title="RelationFcRsVsanAttr">RelationFcRsVsanAttr</a>" : <i>String</i>,
        "<a href="#relationfcrsvsanattrdef" title="RelationFcRsVsanAttrDef">RelationFcRsVsanAttrDef</a>" : <i>String</i>,
        "<a href="#relationfcrsvsanns" title="RelationFcRsVsanNs">RelationFcRsVsanNs</a>" : <i>String</i>,
        "<a href="#relationfcrsvsannsdef" title="RelationFcRsVsanNsDef">RelationFcRsVsanNsDef</a>" : <i>String</i>,
        "<a href="#relationinfrarsdomvxlannsdef" title="RelationInfraRsDomVxlanNsDef">RelationInfraRsDomVxlanNsDef</a>" : <i>String</i>,
        "<a href="#relationinfrarsvipaddrns" title="RelationInfraRsVipAddrNs">RelationInfraRsVipAddrNs</a>" : <i>String</i>,
        "<a href="#relationinfrarsvlanns" title="RelationInfraRsVlanNs">RelationInfraRsVlanNs</a>" : <i>String</i>,
        "<a href="#relationinfrarsvlannsdef" title="RelationInfraRsVlanNsDef">RelationInfraRsVlanNsDef</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::FcDomain
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationfcrsvsanattr" title="RelationFcRsVsanAttr">RelationFcRsVsanAttr</a>: <i>String</i>
    <a href="#relationfcrsvsanattrdef" title="RelationFcRsVsanAttrDef">RelationFcRsVsanAttrDef</a>: <i>String</i>
    <a href="#relationfcrsvsanns" title="RelationFcRsVsanNs">RelationFcRsVsanNs</a>: <i>String</i>
    <a href="#relationfcrsvsannsdef" title="RelationFcRsVsanNsDef">RelationFcRsVsanNsDef</a>: <i>String</i>
    <a href="#relationinfrarsdomvxlannsdef" title="RelationInfraRsDomVxlanNsDef">RelationInfraRsDomVxlanNsDef</a>: <i>String</i>
    <a href="#relationinfrarsvipaddrns" title="RelationInfraRsVipAddrNs">RelationInfraRsVipAddrNs</a>: <i>String</i>
    <a href="#relationinfrarsvlanns" title="RelationInfraRsVlanNs">RelationInfraRsVlanNs</a>: <i>String</i>
    <a href="#relationinfrarsvlannsdef" title="RelationInfraRsVlanNsDef">RelationInfraRsVlanNsDef</a>: <i>String</i>
</pre>

## Properties

#### Annotation

_Required_: No

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

#### RelationFcRsVsanAttr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFcRsVsanAttrDef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFcRsVsanNs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFcRsVsanNsDef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsDomVxlanNsDef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsVipAddrNs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsVlanNs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsVlanNsDef

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

