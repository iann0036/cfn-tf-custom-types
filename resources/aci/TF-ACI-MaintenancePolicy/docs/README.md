# TF::ACI::MaintenancePolicy

CloudFormation equivalent of aci_maintenance_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::MaintenancePolicy",
    "Properties" : {
        "<a href="#adminst" title="AdminSt">AdminSt</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#graceful" title="Graceful">Graceful</a>" : <i>String</i>,
        "<a href="#ignorecompat" title="IgnoreCompat">IgnoreCompat</a>" : <i>String</i>,
        "<a href="#internallabel" title="InternalLabel">InternalLabel</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#notifcond" title="NotifCond">NotifCond</a>" : <i>String</i>,
        "<a href="#relationmaintrspolnotif" title="RelationMaintRsPolNotif">RelationMaintRsPolNotif</a>" : <i>String</i>,
        "<a href="#relationmaintrspolscheduler" title="RelationMaintRsPolScheduler">RelationMaintRsPolScheduler</a>" : <i>String</i>,
        "<a href="#relationtrigrstriggerable" title="RelationTrigRsTriggerable">RelationTrigRsTriggerable</a>" : <i>String</i>,
        "<a href="#runmode" title="RunMode">RunMode</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#versioncheckoverride" title="VersionCheckOverride">VersionCheckOverride</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::MaintenancePolicy
Properties:
    <a href="#adminst" title="AdminSt">AdminSt</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#graceful" title="Graceful">Graceful</a>: <i>String</i>
    <a href="#ignorecompat" title="IgnoreCompat">IgnoreCompat</a>: <i>String</i>
    <a href="#internallabel" title="InternalLabel">InternalLabel</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#notifcond" title="NotifCond">NotifCond</a>: <i>String</i>
    <a href="#relationmaintrspolnotif" title="RelationMaintRsPolNotif">RelationMaintRsPolNotif</a>: <i>String</i>
    <a href="#relationmaintrspolscheduler" title="RelationMaintRsPolScheduler">RelationMaintRsPolScheduler</a>: <i>String</i>
    <a href="#relationtrigrstriggerable" title="RelationTrigRsTriggerable">RelationTrigRsTriggerable</a>: <i>String</i>
    <a href="#runmode" title="RunMode">RunMode</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#versioncheckoverride" title="VersionCheckOverride">VersionCheckOverride</a>: <i>String</i>
</pre>

## Properties

#### AdminSt

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

#### Graceful

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreCompat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalLabel

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

#### NotifCond

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationMaintRsPolNotif

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationMaintRsPolScheduler

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationTrigRsTriggerable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionCheckOverride

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

