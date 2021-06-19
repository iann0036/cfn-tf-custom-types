# TF::ACI::L3ExtSubnet

CloudFormation equivalent of aci_l3_ext_subnet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3ExtSubnet",
    "Properties" : {
        "<a href="#aggregate" title="Aggregate">Aggregate</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#externalnetworkinstanceprofiledn" title="ExternalNetworkInstanceProfileDn">ExternalNetworkInstanceProfileDn</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationl3extrssubnettortsumm" title="RelationL3extRsSubnetToRtSumm">RelationL3extRsSubnetToRtSumm</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationl3extrssubnettoprofile" title="RelationL3extRsSubnetToProfile">RelationL3extRsSubnetToProfile</a>" : <i>[ <a href="relationl3extrssubnettoprofiledefinition.md">RelationL3extRsSubnetToProfileDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3ExtSubnet
Properties:
    <a href="#aggregate" title="Aggregate">Aggregate</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#externalnetworkinstanceprofiledn" title="ExternalNetworkInstanceProfileDn">ExternalNetworkInstanceProfileDn</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationl3extrssubnettortsumm" title="RelationL3extRsSubnetToRtSumm">RelationL3extRsSubnetToRtSumm</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>
      - String</i>
    <a href="#relationl3extrssubnettoprofile" title="RelationL3extRsSubnetToProfile">RelationL3extRsSubnetToProfile</a>: <i>
      - <a href="relationl3extrssubnettoprofiledefinition.md">RelationL3extRsSubnetToProfileDefinition</a></i>
</pre>

## Properties

#### Aggregate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNetworkInstanceProfileDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL3extRsSubnetToRtSumm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL3extRsSubnetToProfile

_Required_: No

_Type_: List of <a href="relationl3extrssubnettoprofiledefinition.md">RelationL3extRsSubnetToProfileDefinition</a>

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

