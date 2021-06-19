# TF::ACI::Vrf

CloudFormation equivalent of aci_vrf

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::Vrf",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#bdenforcedenable" title="BdEnforcedEnable">BdEnforcedEnable</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipdataplanelearning" title="IpDataPlaneLearning">IpDataPlaneLearning</a>" : <i>String</i>,
        "<a href="#knwmcastact" title="KnwMcastAct">KnwMcastAct</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#pcenfdir" title="PcEnfDir">PcEnfDir</a>" : <i>String</i>,
        "<a href="#pcenfpref" title="PcEnfPref">PcEnfPref</a>" : <i>String</i>,
        "<a href="#relationfvrsbgpctxpol" title="RelationFvRsBgpCtxPol">RelationFvRsBgpCtxPol</a>" : <i>String</i>,
        "<a href="#relationfvrsctxmcastto" title="RelationFvRsCtxMcastTo">RelationFvRsCtxMcastTo</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrsctxmonpol" title="RelationFvRsCtxMonPol">RelationFvRsCtxMonPol</a>" : <i>String</i>,
        "<a href="#relationfvrsctxtoepret" title="RelationFvRsCtxToEpRet">RelationFvRsCtxToEpRet</a>" : <i>String</i>,
        "<a href="#relationfvrsctxtoextroutetagpol" title="RelationFvRsCtxToExtRouteTagPol">RelationFvRsCtxToExtRouteTagPol</a>" : <i>String</i>,
        "<a href="#relationfvrsospfctxpol" title="RelationFvRsOspfCtxPol">RelationFvRsOspfCtxPol</a>" : <i>String</i>,
        "<a href="#relationfvrsvrfvalidationpol" title="RelationFvRsVrfValidationPol">RelationFvRsVrfValidationPol</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>,
        "<a href="#relationfvrsctxtobgpctxafpol" title="RelationFvRsCtxToBgpCtxAfPol">RelationFvRsCtxToBgpCtxAfPol</a>" : <i>[ <a href="relationfvrsctxtobgpctxafpoldefinition.md">RelationFvRsCtxToBgpCtxAfPolDefinition</a>, ... ]</i>,
        "<a href="#relationfvrsctxtoeigrpctxafpol" title="RelationFvRsCtxToEigrpCtxAfPol">RelationFvRsCtxToEigrpCtxAfPol</a>" : <i>[ <a href="relationfvrsctxtoeigrpctxafpoldefinition.md">RelationFvRsCtxToEigrpCtxAfPolDefinition</a>, ... ]</i>,
        "<a href="#relationfvrsctxtoospfctxpol" title="RelationFvRsCtxToOspfCtxPol">RelationFvRsCtxToOspfCtxPol</a>" : <i>[ <a href="relationfvrsctxtoospfctxpoldefinition.md">RelationFvRsCtxToOspfCtxPolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::Vrf
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#bdenforcedenable" title="BdEnforcedEnable">BdEnforcedEnable</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipdataplanelearning" title="IpDataPlaneLearning">IpDataPlaneLearning</a>: <i>String</i>
    <a href="#knwmcastact" title="KnwMcastAct">KnwMcastAct</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#pcenfdir" title="PcEnfDir">PcEnfDir</a>: <i>String</i>
    <a href="#pcenfpref" title="PcEnfPref">PcEnfPref</a>: <i>String</i>
    <a href="#relationfvrsbgpctxpol" title="RelationFvRsBgpCtxPol">RelationFvRsBgpCtxPol</a>: <i>String</i>
    <a href="#relationfvrsctxmcastto" title="RelationFvRsCtxMcastTo">RelationFvRsCtxMcastTo</a>: <i>
      - String</i>
    <a href="#relationfvrsctxmonpol" title="RelationFvRsCtxMonPol">RelationFvRsCtxMonPol</a>: <i>String</i>
    <a href="#relationfvrsctxtoepret" title="RelationFvRsCtxToEpRet">RelationFvRsCtxToEpRet</a>: <i>String</i>
    <a href="#relationfvrsctxtoextroutetagpol" title="RelationFvRsCtxToExtRouteTagPol">RelationFvRsCtxToExtRouteTagPol</a>: <i>String</i>
    <a href="#relationfvrsospfctxpol" title="RelationFvRsOspfCtxPol">RelationFvRsOspfCtxPol</a>: <i>String</i>
    <a href="#relationfvrsvrfvalidationpol" title="RelationFvRsVrfValidationPol">RelationFvRsVrfValidationPol</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
    <a href="#relationfvrsctxtobgpctxafpol" title="RelationFvRsCtxToBgpCtxAfPol">RelationFvRsCtxToBgpCtxAfPol</a>: <i>
      - <a href="relationfvrsctxtobgpctxafpoldefinition.md">RelationFvRsCtxToBgpCtxAfPolDefinition</a></i>
    <a href="#relationfvrsctxtoeigrpctxafpol" title="RelationFvRsCtxToEigrpCtxAfPol">RelationFvRsCtxToEigrpCtxAfPol</a>: <i>
      - <a href="relationfvrsctxtoeigrpctxafpoldefinition.md">RelationFvRsCtxToEigrpCtxAfPolDefinition</a></i>
    <a href="#relationfvrsctxtoospfctxpol" title="RelationFvRsCtxToOspfCtxPol">RelationFvRsCtxToOspfCtxPol</a>: <i>
      - <a href="relationfvrsctxtoospfctxpoldefinition.md">RelationFvRsCtxToOspfCtxPolDefinition</a></i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BdEnforcedEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpDataPlaneLearning

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KnwMcastAct

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

#### PcEnfDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcEnfPref

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsBgpCtxPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCtxMcastTo

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCtxMonPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCtxToEpRet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCtxToExtRouteTagPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsOspfCtxPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsVrfValidationPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCtxToBgpCtxAfPol

_Required_: No

_Type_: List of <a href="relationfvrsctxtobgpctxafpoldefinition.md">RelationFvRsCtxToBgpCtxAfPolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCtxToEigrpCtxAfPol

_Required_: No

_Type_: List of <a href="relationfvrsctxtoeigrpctxafpoldefinition.md">RelationFvRsCtxToEigrpCtxAfPolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCtxToOspfCtxPol

_Required_: No

_Type_: List of <a href="relationfvrsctxtoospfctxpoldefinition.md">RelationFvRsCtxToOspfCtxPolDefinition</a>

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

