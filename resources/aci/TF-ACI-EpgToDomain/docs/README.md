# TF::ACI::EpgToDomain

CloudFormation equivalent of aci_epg_to_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::EpgToDomain",
    "Properties" : {
        "<a href="#allowmicroseg" title="AllowMicroSeg">AllowMicroSeg</a>" : <i>Boolean</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#applicationepgdn" title="ApplicationEpgDn">ApplicationEpgDn</a>" : <i>String</i>,
        "<a href="#bindingtype" title="BindingType">BindingType</a>" : <i>String</i>,
        "<a href="#delimiter" title="Delimiter">Delimiter</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encap" title="Encap">Encap</a>" : <i>String</i>,
        "<a href="#encapmode" title="EncapMode">EncapMode</a>" : <i>String</i>,
        "<a href="#epgcos" title="EpgCos">EpgCos</a>" : <i>String</i>,
        "<a href="#epgcospref" title="EpgCosPref">EpgCosPref</a>" : <i>String</i>,
        "<a href="#instrimedcy" title="InstrImedcy">InstrImedcy</a>" : <i>String</i>,
        "<a href="#lagpolicyname" title="LagPolicyName">LagPolicyName</a>" : <i>String</i>,
        "<a href="#netflowdir" title="NetflowDir">NetflowDir</a>" : <i>String</i>,
        "<a href="#netflowpref" title="NetflowPref">NetflowPref</a>" : <i>String</i>,
        "<a href="#numports" title="NumPorts">NumPorts</a>" : <i>String</i>,
        "<a href="#portallocation" title="PortAllocation">PortAllocation</a>" : <i>String</i>,
        "<a href="#primaryencap" title="PrimaryEncap">PrimaryEncap</a>" : <i>String</i>,
        "<a href="#primaryencapinner" title="PrimaryEncapInner">PrimaryEncapInner</a>" : <i>String</i>,
        "<a href="#resimedcy" title="ResImedcy">ResImedcy</a>" : <i>String</i>,
        "<a href="#secondaryencapinner" title="SecondaryEncapInner">SecondaryEncapInner</a>" : <i>String</i>,
        "<a href="#switchingmode" title="SwitchingMode">SwitchingMode</a>" : <i>String</i>,
        "<a href="#tdn" title="Tdn">Tdn</a>" : <i>String</i>,
        "<a href="#vmmallowpromiscuous" title="VmmAllowPromiscuous">VmmAllowPromiscuous</a>" : <i>String</i>,
        "<a href="#vmmforgedtransmits" title="VmmForgedTransmits">VmmForgedTransmits</a>" : <i>String</i>,
        "<a href="#vmmmacchanges" title="VmmMacChanges">VmmMacChanges</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::EpgToDomain
Properties:
    <a href="#allowmicroseg" title="AllowMicroSeg">AllowMicroSeg</a>: <i>Boolean</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#applicationepgdn" title="ApplicationEpgDn">ApplicationEpgDn</a>: <i>String</i>
    <a href="#bindingtype" title="BindingType">BindingType</a>: <i>String</i>
    <a href="#delimiter" title="Delimiter">Delimiter</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encap" title="Encap">Encap</a>: <i>String</i>
    <a href="#encapmode" title="EncapMode">EncapMode</a>: <i>String</i>
    <a href="#epgcos" title="EpgCos">EpgCos</a>: <i>String</i>
    <a href="#epgcospref" title="EpgCosPref">EpgCosPref</a>: <i>String</i>
    <a href="#instrimedcy" title="InstrImedcy">InstrImedcy</a>: <i>String</i>
    <a href="#lagpolicyname" title="LagPolicyName">LagPolicyName</a>: <i>String</i>
    <a href="#netflowdir" title="NetflowDir">NetflowDir</a>: <i>String</i>
    <a href="#netflowpref" title="NetflowPref">NetflowPref</a>: <i>String</i>
    <a href="#numports" title="NumPorts">NumPorts</a>: <i>String</i>
    <a href="#portallocation" title="PortAllocation">PortAllocation</a>: <i>String</i>
    <a href="#primaryencap" title="PrimaryEncap">PrimaryEncap</a>: <i>String</i>
    <a href="#primaryencapinner" title="PrimaryEncapInner">PrimaryEncapInner</a>: <i>String</i>
    <a href="#resimedcy" title="ResImedcy">ResImedcy</a>: <i>String</i>
    <a href="#secondaryencapinner" title="SecondaryEncapInner">SecondaryEncapInner</a>: <i>String</i>
    <a href="#switchingmode" title="SwitchingMode">SwitchingMode</a>: <i>String</i>
    <a href="#tdn" title="Tdn">Tdn</a>: <i>String</i>
    <a href="#vmmallowpromiscuous" title="VmmAllowPromiscuous">VmmAllowPromiscuous</a>: <i>String</i>
    <a href="#vmmforgedtransmits" title="VmmForgedTransmits">VmmForgedTransmits</a>: <i>String</i>
    <a href="#vmmmacchanges" title="VmmMacChanges">VmmMacChanges</a>: <i>String</i>
</pre>

## Properties

#### AllowMicroSeg

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationEpgDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindingType

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

#### Encap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncapMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpgCos

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpgCosPref

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstrImedcy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LagPolicyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowPref

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumPorts

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortAllocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryEncap

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryEncapInner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResImedcy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryEncapInner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tdn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmmAllowPromiscuous

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmmForgedTransmits

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmmMacChanges

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

#### VmmId

Returns the <code>VmmId</code> value.

