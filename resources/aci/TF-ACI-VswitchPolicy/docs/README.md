# TF::ACI::VswitchPolicy

CloudFormation equivalent of aci_vswitch_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::VswitchPolicy",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationvmmrsvswitchoverridecdpifpol" title="RelationVmmRsVswitchOverrideCdpIfPol">RelationVmmRsVswitchOverrideCdpIfPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsvswitchoverridefwpol" title="RelationVmmRsVswitchOverrideFwPol">RelationVmmRsVswitchOverrideFwPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsvswitchoverridelacppol" title="RelationVmmRsVswitchOverrideLacpPol">RelationVmmRsVswitchOverrideLacpPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsvswitchoverridelldpifpol" title="RelationVmmRsVswitchOverrideLldpIfPol">RelationVmmRsVswitchOverrideLldpIfPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsvswitchoverridemcpifpol" title="RelationVmmRsVswitchOverrideMcpIfPol">RelationVmmRsVswitchOverrideMcpIfPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsvswitchoverridemtupol" title="RelationVmmRsVswitchOverrideMtuPol">RelationVmmRsVswitchOverrideMtuPol</a>" : <i>String</i>,
        "<a href="#relationvmmrsvswitchoverridestppol" title="RelationVmmRsVswitchOverrideStpPol">RelationVmmRsVswitchOverrideStpPol</a>" : <i>String</i>,
        "<a href="#vmmdomaindn" title="VmmDomainDn">VmmDomainDn</a>" : <i>String</i>,
        "<a href="#relationvmmrsvswitchexporterpol" title="RelationVmmRsVswitchExporterPol">RelationVmmRsVswitchExporterPol</a>" : <i>[ <a href="relationvmmrsvswitchexporterpoldefinition.md">RelationVmmRsVswitchExporterPolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::VswitchPolicy
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationvmmrsvswitchoverridecdpifpol" title="RelationVmmRsVswitchOverrideCdpIfPol">RelationVmmRsVswitchOverrideCdpIfPol</a>: <i>String</i>
    <a href="#relationvmmrsvswitchoverridefwpol" title="RelationVmmRsVswitchOverrideFwPol">RelationVmmRsVswitchOverrideFwPol</a>: <i>String</i>
    <a href="#relationvmmrsvswitchoverridelacppol" title="RelationVmmRsVswitchOverrideLacpPol">RelationVmmRsVswitchOverrideLacpPol</a>: <i>String</i>
    <a href="#relationvmmrsvswitchoverridelldpifpol" title="RelationVmmRsVswitchOverrideLldpIfPol">RelationVmmRsVswitchOverrideLldpIfPol</a>: <i>String</i>
    <a href="#relationvmmrsvswitchoverridemcpifpol" title="RelationVmmRsVswitchOverrideMcpIfPol">RelationVmmRsVswitchOverrideMcpIfPol</a>: <i>String</i>
    <a href="#relationvmmrsvswitchoverridemtupol" title="RelationVmmRsVswitchOverrideMtuPol">RelationVmmRsVswitchOverrideMtuPol</a>: <i>String</i>
    <a href="#relationvmmrsvswitchoverridestppol" title="RelationVmmRsVswitchOverrideStpPol">RelationVmmRsVswitchOverrideStpPol</a>: <i>String</i>
    <a href="#vmmdomaindn" title="VmmDomainDn">VmmDomainDn</a>: <i>String</i>
    <a href="#relationvmmrsvswitchexporterpol" title="RelationVmmRsVswitchExporterPol">RelationVmmRsVswitchExporterPol</a>: <i>
      - <a href="relationvmmrsvswitchexporterpoldefinition.md">RelationVmmRsVswitchExporterPolDefinition</a></i>
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

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVswitchOverrideCdpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVswitchOverrideFwPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVswitchOverrideLacpPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVswitchOverrideLldpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVswitchOverrideMcpIfPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVswitchOverrideMtuPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVswitchOverrideStpPol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmmDomainDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVmmRsVswitchExporterPol

_Required_: No

_Type_: List of <a href="relationvmmrsvswitchexporterpoldefinition.md">RelationVmmRsVswitchExporterPolDefinition</a>

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

