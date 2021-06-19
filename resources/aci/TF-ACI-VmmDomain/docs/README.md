# TF::ACI::VmmDomain

CloudFormation equivalent of aci_vmm_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::VmmDomain",
    "Properties" : {
        "<a href="#accessmode" title="AccessMode">AccessMode</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#arplearning" title="ArpLearning">ArpLearning</a>" : <i>String</i>,
        "<a href="#avetimeout" title="AveTimeOut">AveTimeOut</a>" : <i>String</i>,
        "<a href="#configinfrapg" title="ConfigInfraPg">ConfigInfraPg</a>" : <i>String</i>,
        "<a href="#ctrlknob" title="CtrlKnob">CtrlKnob</a>" : <i>String</i>,
        "<a href="#delimiter" title="Delimiter">Delimiter</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableave" title="EnableAve">EnableAve</a>" : <i>String</i>,
        "<a href="#enabletag" title="EnableTag">EnableTag</a>" : <i>String</i>,
        "<a href="#encapmode" title="EncapMode">EncapMode</a>" : <i>String</i>,
        "<a href="#enfpref" title="EnfPref">EnfPref</a>" : <i>String</i>,
        "<a href="#epinventorytype" title="EpInventoryType">EpInventoryType</a>" : <i>String</i>,
        "<a href="#eprettime" title="EpRetTime">EpRetTime</a>" : <i>String</i>,
        "<a href="#hvavailmonitor" title="HvAvailMonitor">HvAvailMonitor</a>" : <i>String</i>,
        "<a href="#mcastaddr" title="McastAddr">McastAddr</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#prefencapmode" title="PrefEncapMode">PrefEncapMode</a>" : <i>String</i>,
        "<a href="#providerprofiledn" title="ProviderProfileDn">ProviderProfileDn</a>" : <i>String</i>,
        "<a href="#relationinfrarsdomvxlannsdef" title="RelationInfraRsDomVxlanNsDef">RelationInfraRsDomVxlanNsDef</a>" : <i>String</i>,
        "<a href="#relationinfrarsvipaddrns" title="RelationInfraRsVipAddrNs">RelationInfraRsVipAddrNs</a>" : <i>String</i>,
        "<a href="#relationinfrarsvlanns" title="RelationInfraRsVlanNs">RelationInfraRsVlanNs</a>" : <i>String</i>,
        "<a href="#relationinfrarsvlannsdef" title="RelationInfraRsVlanNsDef">RelationInfraRsVlanNsDef</a>" : <i>String</i>,
        "<a href="#relationvmmrsdefaultcdpifpol" title="RelationVmmRsDefaultCdpIfPol">RelationVmmRsDefaultCdpIfPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsdefaultfwpol" title="RelationVmmRsDefaultFwPol">RelationVmmRsDefaultFwPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsdefaultl2instpol" title="RelationVmmRsDefaultL2InstPol">RelationVmmRsDefaultL2InstPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsdefaultlacplagpol" title="RelationVmmRsDefaultLacpLagPol">RelationVmmRsDefaultLacpLagPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsdefaultlldpifpol" title="RelationVmmRsDefaultLldpIfPol">RelationVmmRsDefaultLldpIfPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsdefaultstpifpol" title="RelationVmmRsDefaultStpIfPol">RelationVmmRsDefaultStpIfPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsdommcastaddrns" title="RelationVmmRsDomMcastAddrNs">RelationVmmRsDomMcastAddrNs</a>" : <i>String</i>,
        "<a href="#relationvmmrsprefenhancedlagpol" title="RelationVmmRsPrefEnhancedLagPol">RelationVmmRsPrefEnhancedLagPol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::VmmDomain
Properties:
    <a href="#accessmode" title="AccessMode">AccessMode</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#arplearning" title="ArpLearning">ArpLearning</a>: <i>String</i>
    <a href="#avetimeout" title="AveTimeOut">AveTimeOut</a>: <i>String</i>
    <a href="#configinfrapg" title="ConfigInfraPg">ConfigInfraPg</a>: <i>String</i>
    <a href="#ctrlknob" title="CtrlKnob">CtrlKnob</a>: <i>String</i>
    <a href="#delimiter" title="Delimiter">Delimiter</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableave" title="EnableAve">EnableAve</a>: <i>String</i>
    <a href="#enabletag" title="EnableTag">EnableTag</a>: <i>String</i>
    <a href="#encapmode" title="EncapMode">EncapMode</a>: <i>String</i>
    <a href="#enfpref" title="EnfPref">EnfPref</a>: <i>String</i>
    <a href="#epinventorytype" title="EpInventoryType">EpInventoryType</a>: <i>String</i>
    <a href="#eprettime" title="EpRetTime">EpRetTime</a>: <i>String</i>
    <a href="#hvavailmonitor" title="HvAvailMonitor">HvAvailMonitor</a>: <i>String</i>
    <a href="#mcastaddr" title="McastAddr">McastAddr</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#prefencapmode" title="PrefEncapMode">PrefEncapMode</a>: <i>String</i>
    <a href="#providerprofiledn" title="ProviderProfileDn">ProviderProfileDn</a>: <i>String</i>
    <a href="#relationinfrarsdomvxlannsdef" title="RelationInfraRsDomVxlanNsDef">RelationInfraRsDomVxlanNsDef</a>: <i>String</i>
    <a href="#relationinfrarsvipaddrns" title="RelationInfraRsVipAddrNs">RelationInfraRsVipAddrNs</a>: <i>String</i>
    <a href="#relationinfrarsvlanns" title="RelationInfraRsVlanNs">RelationInfraRsVlanNs</a>: <i>String</i>
    <a href="#relationinfrarsvlannsdef" title="RelationInfraRsVlanNsDef">RelationInfraRsVlanNsDef</a>: <i>String</i>
    <a href="#relationvmmrsdefaultcdpifpol" title="RelationVmmRsDefaultCdpIfPol">RelationVmmRsDefaultCdpIfPol</a>: <i>String</i>
    <a href="#relationvmmrsdefaultfwpol" title="RelationVmmRsDefaultFwPol">RelationVmmRsDefaultFwPol</a>: <i>String</i>
    <a href="#relationvmmrsdefaultl2instpol" title="RelationVmmRsDefaultL2InstPol">RelationVmmRsDefaultL2InstPol</a>: <i>String</i>
    <a href="#relationvmmrsdefaultlacplagpol" title="RelationVmmRsDefaultLacpLagPol">RelationVmmRsDefaultLacpLagPol</a>: <i>String</i>
    <a href="#relationvmmrsdefaultlldpifpol" title="RelationVmmRsDefaultLldpIfPol">RelationVmmRsDefaultLldpIfPol</a>: <i>String</i>
    <a href="#relationvmmrsdefaultstpifpol" title="RelationVmmRsDefaultStpIfPol">RelationVmmRsDefaultStpIfPol</a>: <i>String</i>
    <a href="#relationvmmrsdommcastaddrns" title="RelationVmmRsDomMcastAddrNs">RelationVmmRsDomMcastAddrNs</a>: <i>String</i>
    <a href="#relationvmmrsprefenhancedlagpol" title="RelationVmmRsPrefEnhancedLagPol">RelationVmmRsPrefEnhancedLagPol</a>: <i>String</i>
</pre>

## Properties

#### AccessMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpLearning

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AveTimeOut

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigInfraPg

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CtrlKnob

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delimiter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAve

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncapMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnfPref

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpInventoryType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpRetTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HvAvailMonitor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McastAddr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

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

#### PrefEncapMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderProfileDn

_Required_: Yes

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

#### RelationVmmRsDefaultCdpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsDefaultFwPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsDefaultL2InstPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsDefaultLacpLagPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsDefaultLldpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsDefaultStpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsDomMcastAddrNs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsPrefEnhancedLagPol

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

