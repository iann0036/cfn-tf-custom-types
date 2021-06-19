# TF::ACI::L3outBfdInterfaceProfile

Manages ACI L3out BFD Interface Profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outBfdInterfaceProfile",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#interfaceprofiletype" title="InterfaceProfileType">InterfaceProfileType</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#logicalinterfaceprofiledn" title="LogicalInterfaceProfileDn">LogicalInterfaceProfileDn</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationbfdrsifpol" title="RelationBfdRsIfPol">RelationBfdRsIfPol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outBfdInterfaceProfile
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#interfaceprofiletype" title="InterfaceProfileType">InterfaceProfileType</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#logicalinterfaceprofiledn" title="LogicalInterfaceProfileDn">LogicalInterfaceProfileDn</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationbfdrsifpol" title="RelationBfdRsIfPol">RelationBfdRsIfPol</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for L3out BFD interface profile object.
- `name_alias` - (Optional) Name alias for L3out BFD interface profile object.
- `description` - (Optional) Description for L3out BFD interface profile object.
- `key` - (Optional) Password to identify this L3out BFD interface profile object.
- `key_id` - (Optional) Authentication key id for L3out BFD interface profile object. Default value is "1".
- `interface_profile_type` - (Optional) Component type for L3out BFD interface profile object. Allowed values are "none" and "sha1". Default value is "none".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for L3out BFD interface profile object.
- `key` - (Optional) Password to identify this L3out BFD interface profile object.
- `key_id` - (Optional) Authentication key id for L3out BFD interface profile object. Default value is "1".
- `interface_profile_type` - (Optional) Component type for L3out BFD interface profile object. Allowed values are "none" and "sha1". Default value is "none".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceProfileType

Component type for L3out BFD interface profile object. Allowed values are "none" and "sha1". Default value is "none".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

Password to identify this L3out BFD interface profile object.
- `key_id` - (Optional) Authentication key id for L3out BFD interface profile object. Default value is "1".
- `interface_profile_type` - (Optional) Component type for L3out BFD interface profile object. Allowed values are "none" and "sha1". Default value is "none".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

Authentication key id for L3out BFD interface profile object. Default value is "1".
- `interface_profile_type` - (Optional) Component type for L3out BFD interface profile object. Allowed values are "none" and "sha1". Default value is "none".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalInterfaceProfileDn

Distinguished name of parent logical interface profile object.
- `annotation` - (Optional) Annotation for L3out BFD interface profile object.
- `name_alias` - (Optional) Name alias for L3out BFD interface profile object.
- `description` - (Optional) Description for L3out BFD interface profile object.
- `key` - (Optional) Password to identify this L3out BFD interface profile object.
- `key_id` - (Optional) Authentication key id for L3out BFD interface profile object. Default value is "1".
- `interface_profile_type` - (Optional) Component type for L3out BFD interface profile object. Allowed values are "none" and "sha1". Default value is "none".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for L3out BFD interface profile object.
- `description` - (Optional) Description for L3out BFD interface profile object.
- `key` - (Optional) Password to identify this L3out BFD interface profile object.
- `key_id` - (Optional) Authentication key id for L3out BFD interface profile object. Default value is "1".
- `interface_profile_type` - (Optional) Component type for L3out BFD interface profile object. Allowed values are "none" and "sha1". Default value is "none".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationBfdRsIfPol

Relation to class bfdIfPol. Cardinality - N_TO_ONE. Type - String.

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

