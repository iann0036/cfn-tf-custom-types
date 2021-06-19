# TF::ACI::ConfigurationExportPolicy

Manages ACI Configuration Export Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::ConfigurationExportPolicy",
    "Properties" : {
        "<a href="#adminst" title="AdminSt">AdminSt</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#includesecurefields" title="IncludeSecureFields">IncludeSecureFields</a>" : <i>String</i>,
        "<a href="#maxsnapshotcount" title="MaxSnapshotCount">MaxSnapshotCount</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationconfigrsexportdestination" title="RelationConfigRsExportDestination">RelationConfigRsExportDestination</a>" : <i>String</i>,
        "<a href="#relationconfigrsexportscheduler" title="RelationConfigRsExportScheduler">RelationConfigRsExportScheduler</a>" : <i>String</i>,
        "<a href="#relationconfigrsremotepath" title="RelationConfigRsRemotePath">RelationConfigRsRemotePath</a>" : <i>String</i>,
        "<a href="#relationtrigrstriggerable" title="RelationTrigRsTriggerable">RelationTrigRsTriggerable</a>" : <i>String</i>,
        "<a href="#snapshot" title="Snapshot">Snapshot</a>" : <i>String</i>,
        "<a href="#targetdn" title="TargetDn">TargetDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::ConfigurationExportPolicy
Properties:
    <a href="#adminst" title="AdminSt">AdminSt</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#includesecurefields" title="IncludeSecureFields">IncludeSecureFields</a>: <i>String</i>
    <a href="#maxsnapshotcount" title="MaxSnapshotCount">MaxSnapshotCount</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationconfigrsexportdestination" title="RelationConfigRsExportDestination">RelationConfigRsExportDestination</a>: <i>String</i>
    <a href="#relationconfigrsexportscheduler" title="RelationConfigRsExportScheduler">RelationConfigRsExportScheduler</a>: <i>String</i>
    <a href="#relationconfigrsremotepath" title="RelationConfigRsRemotePath">RelationConfigRsRemotePath</a>: <i>String</i>
    <a href="#relationtrigrstriggerable" title="RelationTrigRsTriggerable">RelationTrigRsTriggerable</a>: <i>String</i>
    <a href="#snapshot" title="Snapshot">Snapshot</a>: <i>String</i>
    <a href="#targetdn" title="TargetDn">TargetDn</a>: <i>String</i>
</pre>

## Properties

#### AdminSt

admin state of the export policy
Allowed values: "untriggered", "triggered"
- `annotation` - (Optional) annotation for object configuration_export_policy.
- `description` - (Optional) Description for object configuration_export_policy.
- `format` - (Optional) export data format
Allowed values: "xml", "json"
- `include_secure_fields` - (Optional) include_secure_fields for object configuration_export_policy.
Allowed values: "no", "yes"
- `max_snapshot_count` - (Optional) max_snapshot_count for object configuration_export_policy.
- `name_alias` - (Optional) name_alias for object configuration_export_policy.
- `snapshot` - (Optional) snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

annotation for object configuration_export_policy.
- `description` - (Optional) Description for object configuration_export_policy.
- `format` - (Optional) export data format
Allowed values: "xml", "json"
- `include_secure_fields` - (Optional) include_secure_fields for object configuration_export_policy.
Allowed values: "no", "yes"
- `max_snapshot_count` - (Optional) max_snapshot_count for object configuration_export_policy.
- `name_alias` - (Optional) name_alias for object configuration_export_policy.
- `snapshot` - (Optional) snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object configuration_export_policy.
- `format` - (Optional) export data format
Allowed values: "xml", "json"
- `include_secure_fields` - (Optional) include_secure_fields for object configuration_export_policy.
Allowed values: "no", "yes"
- `max_snapshot_count` - (Optional) max_snapshot_count for object configuration_export_policy.
- `name_alias` - (Optional) name_alias for object configuration_export_policy.
- `snapshot` - (Optional) snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

export data format
Allowed values: "xml", "json"
- `include_secure_fields` - (Optional) include_secure_fields for object configuration_export_policy.
Allowed values: "no", "yes"
- `max_snapshot_count` - (Optional) max_snapshot_count for object configuration_export_policy.
- `name_alias` - (Optional) name_alias for object configuration_export_policy.
- `snapshot` - (Optional) snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeSecureFields

include_secure_fields for object configuration_export_policy.
Allowed values: "no", "yes"
- `max_snapshot_count` - (Optional) max_snapshot_count for object configuration_export_policy.
- `name_alias` - (Optional) name_alias for object configuration_export_policy.
- `snapshot` - (Optional) snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSnapshotCount

max_snapshot_count for object configuration_export_policy.
- `name_alias` - (Optional) name_alias for object configuration_export_policy.
- `snapshot` - (Optional) snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

name of Object configuration_export_policy.
- `admin_st` - (Optional) admin state of the export policy
Allowed values: "untriggered", "triggered"
- `annotation` - (Optional) annotation for object configuration_export_policy.
- `description` - (Optional) Description for object configuration_export_policy.
- `format` - (Optional) export data format
Allowed values: "xml", "json"
- `include_secure_fields` - (Optional) include_secure_fields for object configuration_export_policy.
Allowed values: "no", "yes"
- `max_snapshot_count` - (Optional) max_snapshot_count for object configuration_export_policy.
- `name_alias` - (Optional) name_alias for object configuration_export_policy.
- `snapshot` - (Optional) snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

name_alias for object configuration_export_policy.
- `snapshot` - (Optional) snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationConfigRsExportDestination

Relation to class fileRemotePath. Cardinality - ONE_TO_ONE. Type - String.
- `relation_trig_rs_triggerable` - (Optional) Relation to class trigTriggerable. Cardinality - ONE_TO_ONE. Type - String.
- `relation_config_rs_remote_path` - (Optional) Relation to class fileRemotePath. Cardinality - N_TO_ONE. Type - String.
- `relation_config_rs_export_scheduler` - (Optional) Relation to class trigSchedP. Cardinality - ONE_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationConfigRsExportScheduler

Relation to class trigSchedP. Cardinality - ONE_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationConfigRsRemotePath

Relation to class fileRemotePath. Cardinality - N_TO_ONE. Type - String.
- `relation_config_rs_export_scheduler` - (Optional) Relation to class trigSchedP. Cardinality - ONE_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationTrigRsTriggerable

Relation to class trigTriggerable. Cardinality - ONE_TO_ONE. Type - String.
- `relation_config_rs_remote_path` - (Optional) Relation to class fileRemotePath. Cardinality - N_TO_ONE. Type - String.
- `relation_config_rs_export_scheduler` - (Optional) Relation to class trigSchedP. Cardinality - ONE_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshot

snapshot for object configuration_export_policy.
Allowed values: "no", "yes"
- `target_dn` - (Optional) target export object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDn

target export object.

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

