# TF::ACI::EndpointSecurityGroup

CloudFormation equivalent of aci_endpoint_security_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::EndpointSecurityGroup",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#applicationprofiledn" title="ApplicationProfileDn">ApplicationProfileDn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#floodonencap" title="FloodOnEncap">FloodOnEncap</a>" : <i>String</i>,
        "<a href="#matcht" title="MatchT">MatchT</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#pcenfpref" title="PcEnfPref">PcEnfPref</a>" : <i>String</i>,
        "<a href="#prefgrmemb" title="PrefGrMemb">PrefGrMemb</a>" : <i>String</i>,
        "<a href="#prio" title="Prio">Prio</a>" : <i>String</i>,
        "<a href="#relationfvrscustqospol" title="RelationFvRsCustQosPol">RelationFvRsCustQosPol</a>" : <i>String</i>,
        "<a href="#relationfvrsintraepg" title="RelationFvRsIntraEpg">RelationFvRsIntraEpg</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrsprotby" title="RelationFvRsProtBy">RelationFvRsProtBy</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrsscope" title="RelationFvRsScope">RelationFvRsScope</a>" : <i>String</i>,
        "<a href="#relationfvrssecinherited" title="RelationFvRsSecInherited">RelationFvRsSecInherited</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrscons" title="RelationFvRsCons">RelationFvRsCons</a>" : <i>[ <a href="relationfvrsconsdefinition.md">RelationFvRsConsDefinition</a>, ... ]</i>,
        "<a href="#relationfvrsconsif" title="RelationFvRsConsIf">RelationFvRsConsIf</a>" : <i>[ <a href="relationfvrsconsifdefinition.md">RelationFvRsConsIfDefinition</a>, ... ]</i>,
        "<a href="#relationfvrsprov" title="RelationFvRsProv">RelationFvRsProv</a>" : <i>[ <a href="relationfvrsprovdefinition.md">RelationFvRsProvDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::EndpointSecurityGroup
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#applicationprofiledn" title="ApplicationProfileDn">ApplicationProfileDn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#floodonencap" title="FloodOnEncap">FloodOnEncap</a>: <i>String</i>
    <a href="#matcht" title="MatchT">MatchT</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#pcenfpref" title="PcEnfPref">PcEnfPref</a>: <i>String</i>
    <a href="#prefgrmemb" title="PrefGrMemb">PrefGrMemb</a>: <i>String</i>
    <a href="#prio" title="Prio">Prio</a>: <i>String</i>
    <a href="#relationfvrscustqospol" title="RelationFvRsCustQosPol">RelationFvRsCustQosPol</a>: <i>String</i>
    <a href="#relationfvrsintraepg" title="RelationFvRsIntraEpg">RelationFvRsIntraEpg</a>: <i>
      - String</i>
    <a href="#relationfvrsprotby" title="RelationFvRsProtBy">RelationFvRsProtBy</a>: <i>
      - String</i>
    <a href="#relationfvrsscope" title="RelationFvRsScope">RelationFvRsScope</a>: <i>String</i>
    <a href="#relationfvrssecinherited" title="RelationFvRsSecInherited">RelationFvRsSecInherited</a>: <i>
      - String</i>
    <a href="#relationfvrscons" title="RelationFvRsCons">RelationFvRsCons</a>: <i>
      - <a href="relationfvrsconsdefinition.md">RelationFvRsConsDefinition</a></i>
    <a href="#relationfvrsconsif" title="RelationFvRsConsIf">RelationFvRsConsIf</a>: <i>
      - <a href="relationfvrsconsifdefinition.md">RelationFvRsConsIfDefinition</a></i>
    <a href="#relationfvrsprov" title="RelationFvRsProv">RelationFvRsProv</a>: <i>
      - <a href="relationfvrsprovdefinition.md">RelationFvRsProvDefinition</a></i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationProfileDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloodOnEncap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchT

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

#### PcEnfPref

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefGrMemb

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prio

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCustQosPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsIntraEpg

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsProtBy

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsSecInherited

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCons

_Required_: No

_Type_: List of <a href="relationfvrsconsdefinition.md">RelationFvRsConsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsConsIf

_Required_: No

_Type_: List of <a href="relationfvrsconsifdefinition.md">RelationFvRsConsIfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsProv

_Required_: No

_Type_: List of <a href="relationfvrsprovdefinition.md">RelationFvRsProvDefinition</a>

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

