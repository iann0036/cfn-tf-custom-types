# TF::ACI::LeafAccessPortPolicyGroup

CloudFormation equivalent of aci_leaf_access_port_policy_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::LeafAccessPortPolicyGroup",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationinfrarsattentp" title="RelationInfraRsAttEntP">RelationInfraRsAttEntP</a>" : <i>String</i>,
        "<a href="#relationinfrarscdpifpol" title="RelationInfraRsCdpIfPol">RelationInfraRsCdpIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarscoppifpol" title="RelationInfraRsCoppIfPol">RelationInfraRsCoppIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsdwdmifpol" title="RelationInfraRsDwdmIfPol">RelationInfraRsDwdmIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsfcifpol" title="RelationInfraRsFcIfPol">RelationInfraRsFcIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarshifpol" title="RelationInfraRsHIfPol">RelationInfraRsHIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsl2ifpol" title="RelationInfraRsL2IfPol">RelationInfraRsL2IfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsl2instpol" title="RelationInfraRsL2InstPol">RelationInfraRsL2InstPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsl2portauthpol" title="RelationInfraRsL2PortAuthPol">RelationInfraRsL2PortAuthPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsl2portsecuritypol" title="RelationInfraRsL2PortSecurityPol">RelationInfraRsL2PortSecurityPol</a>" : <i>String</i>,
        "<a href="#relationinfrarslldpifpol" title="RelationInfraRsLldpIfPol">RelationInfraRsLldpIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsmacsecifpol" title="RelationInfraRsMacsecIfPol">RelationInfraRsMacsecIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsmcpifpol" title="RelationInfraRsMcpIfPol">RelationInfraRsMcpIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsmonifinfrapol" title="RelationInfraRsMonIfInfraPol">RelationInfraRsMonIfInfraPol</a>" : <i>String</i>,
        "<a href="#relationinfrarspoeifpol" title="RelationInfraRsPoeIfPol">RelationInfraRsPoeIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsqosdppifpol" title="RelationInfraRsQosDppIfPol">RelationInfraRsQosDppIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsqosegressdppifpol" title="RelationInfraRsQosEgressDppIfPol">RelationInfraRsQosEgressDppIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsqosingressdppifpol" title="RelationInfraRsQosIngressDppIfPol">RelationInfraRsQosIngressDppIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsqospfcifpol" title="RelationInfraRsQosPfcIfPol">RelationInfraRsQosPfcIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsqossdifpol" title="RelationInfraRsQosSdIfPol">RelationInfraRsQosSdIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsspanvdestgrp" title="RelationInfraRsSpanVDestGrp">RelationInfraRsSpanVDestGrp</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationinfrarsspanvsrcgrp" title="RelationInfraRsSpanVSrcGrp">RelationInfraRsSpanVSrcGrp</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationinfrarsstormctrlifpol" title="RelationInfraRsStormctrlIfPol">RelationInfraRsStormctrlIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsstpifpol" title="RelationInfraRsStpIfPol">RelationInfraRsStpIfPol</a>" : <i>String</i>,
        "<a href="#relationinfrarsnetflowmonitorpol" title="RelationInfraRsNetflowMonitorPol">RelationInfraRsNetflowMonitorPol</a>" : <i>[ <a href="relationinfrarsnetflowmonitorpoldefinition.md">RelationInfraRsNetflowMonitorPolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::LeafAccessPortPolicyGroup
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationinfrarsattentp" title="RelationInfraRsAttEntP">RelationInfraRsAttEntP</a>: <i>String</i>
    <a href="#relationinfrarscdpifpol" title="RelationInfraRsCdpIfPol">RelationInfraRsCdpIfPol</a>: <i>String</i>
    <a href="#relationinfrarscoppifpol" title="RelationInfraRsCoppIfPol">RelationInfraRsCoppIfPol</a>: <i>String</i>
    <a href="#relationinfrarsdwdmifpol" title="RelationInfraRsDwdmIfPol">RelationInfraRsDwdmIfPol</a>: <i>String</i>
    <a href="#relationinfrarsfcifpol" title="RelationInfraRsFcIfPol">RelationInfraRsFcIfPol</a>: <i>String</i>
    <a href="#relationinfrarshifpol" title="RelationInfraRsHIfPol">RelationInfraRsHIfPol</a>: <i>String</i>
    <a href="#relationinfrarsl2ifpol" title="RelationInfraRsL2IfPol">RelationInfraRsL2IfPol</a>: <i>String</i>
    <a href="#relationinfrarsl2instpol" title="RelationInfraRsL2InstPol">RelationInfraRsL2InstPol</a>: <i>String</i>
    <a href="#relationinfrarsl2portauthpol" title="RelationInfraRsL2PortAuthPol">RelationInfraRsL2PortAuthPol</a>: <i>String</i>
    <a href="#relationinfrarsl2portsecuritypol" title="RelationInfraRsL2PortSecurityPol">RelationInfraRsL2PortSecurityPol</a>: <i>String</i>
    <a href="#relationinfrarslldpifpol" title="RelationInfraRsLldpIfPol">RelationInfraRsLldpIfPol</a>: <i>String</i>
    <a href="#relationinfrarsmacsecifpol" title="RelationInfraRsMacsecIfPol">RelationInfraRsMacsecIfPol</a>: <i>String</i>
    <a href="#relationinfrarsmcpifpol" title="RelationInfraRsMcpIfPol">RelationInfraRsMcpIfPol</a>: <i>String</i>
    <a href="#relationinfrarsmonifinfrapol" title="RelationInfraRsMonIfInfraPol">RelationInfraRsMonIfInfraPol</a>: <i>String</i>
    <a href="#relationinfrarspoeifpol" title="RelationInfraRsPoeIfPol">RelationInfraRsPoeIfPol</a>: <i>String</i>
    <a href="#relationinfrarsqosdppifpol" title="RelationInfraRsQosDppIfPol">RelationInfraRsQosDppIfPol</a>: <i>String</i>
    <a href="#relationinfrarsqosegressdppifpol" title="RelationInfraRsQosEgressDppIfPol">RelationInfraRsQosEgressDppIfPol</a>: <i>String</i>
    <a href="#relationinfrarsqosingressdppifpol" title="RelationInfraRsQosIngressDppIfPol">RelationInfraRsQosIngressDppIfPol</a>: <i>String</i>
    <a href="#relationinfrarsqospfcifpol" title="RelationInfraRsQosPfcIfPol">RelationInfraRsQosPfcIfPol</a>: <i>String</i>
    <a href="#relationinfrarsqossdifpol" title="RelationInfraRsQosSdIfPol">RelationInfraRsQosSdIfPol</a>: <i>String</i>
    <a href="#relationinfrarsspanvdestgrp" title="RelationInfraRsSpanVDestGrp">RelationInfraRsSpanVDestGrp</a>: <i>
      - String</i>
    <a href="#relationinfrarsspanvsrcgrp" title="RelationInfraRsSpanVSrcGrp">RelationInfraRsSpanVSrcGrp</a>: <i>
      - String</i>
    <a href="#relationinfrarsstormctrlifpol" title="RelationInfraRsStormctrlIfPol">RelationInfraRsStormctrlIfPol</a>: <i>String</i>
    <a href="#relationinfrarsstpifpol" title="RelationInfraRsStpIfPol">RelationInfraRsStpIfPol</a>: <i>String</i>
    <a href="#relationinfrarsnetflowmonitorpol" title="RelationInfraRsNetflowMonitorPol">RelationInfraRsNetflowMonitorPol</a>: <i>
      - <a href="relationinfrarsnetflowmonitorpoldefinition.md">RelationInfraRsNetflowMonitorPolDefinition</a></i>
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

#### RelationInfraRsAttEntP

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsCdpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsCoppIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsDwdmIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsFcIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsHIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsL2IfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsL2InstPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsL2PortAuthPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsL2PortSecurityPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsLldpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsMacsecIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsMcpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsMonIfInfraPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsPoeIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsQosDppIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsQosEgressDppIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsQosIngressDppIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsQosPfcIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsQosSdIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsSpanVDestGrp

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsSpanVSrcGrp

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsStormctrlIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsStpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsNetflowMonitorPol

_Required_: No

_Type_: List of <a href="relationinfrarsnetflowmonitorpoldefinition.md">RelationInfraRsNetflowMonitorPolDefinition</a>

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

