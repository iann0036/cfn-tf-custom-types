# TF::ACI::ConfigurationImportPolicy

Manages ACI Configuration Import Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::ConfigurationImportPolicy",
    "Properties" : {
        "<a href="#adminst" title="AdminSt">AdminSt</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#failondecrypterrors" title="FailOnDecryptErrors">FailOnDecryptErrors</a>" : <i>String</i>,
        "<a href="#filename" title="FileName">FileName</a>" : <i>String</i>,
        "<a href="#importmode" title="ImportMode">ImportMode</a>" : <i>String</i>,
        "<a href="#importtype" title="ImportType">ImportType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationconfigrsimportsource" title="RelationConfigRsImportSource">RelationConfigRsImportSource</a>" : <i>String</i>,
        "<a href="#relationconfigrsremotepath" title="RelationConfigRsRemotePath">RelationConfigRsRemotePath</a>" : <i>String</i>,
        "<a href="#relationtrigrstriggerable" title="RelationTrigRsTriggerable">RelationTrigRsTriggerable</a>" : <i>String</i>,
        "<a href="#snapshot" title="Snapshot">Snapshot</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::ConfigurationImportPolicy
Properties:
    <a href="#adminst" title="AdminSt">AdminSt</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#failondecrypterrors" title="FailOnDecryptErrors">FailOnDecryptErrors</a>: <i>String</i>
    <a href="#filename" title="FileName">FileName</a>: <i>String</i>
    <a href="#importmode" title="ImportMode">ImportMode</a>: <i>String</i>
    <a href="#importtype" title="ImportType">ImportType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationconfigrsimportsource" title="RelationConfigRsImportSource">RelationConfigRsImportSource</a>: <i>String</i>
    <a href="#relationconfigrsremotepath" title="RelationConfigRsRemotePath">RelationConfigRsRemotePath</a>: <i>String</i>
    <a href="#relationtrigrstriggerable" title="RelationTrigRsTriggerable">RelationTrigRsTriggerable</a>: <i>String</i>
    <a href="#snapshot" title="Snapshot">Snapshot</a>: <i>String</i>
</pre>

## Properties

#### AdminSt

admin state of the import
Allowed values: "untriggered", "triggered"
- `annotation` - (Optional) annotation for object configuration_import_policy.
- `description` - (Optional) Description for object configuration_import_policy.
- `fail_on_decrypt_errors` - (Optional) fail_on_decrypt_errors for object configuration_import_policy.
Allowed values: "no", "yes"
- `file_name` - (Optional) import file name
- `import_mode` - (Optional) data import mode.
Allowed values: "atomic", "best-effort"
- `import_type` - (Optional) data import type.
Allowed values: "merge", "replace"
- `name_alias` - (Optional) name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

annotation for object configuration_import_policy.
- `description` - (Optional) Description for object configuration_import_policy.
- `fail_on_decrypt_errors` - (Optional) fail_on_decrypt_errors for object configuration_import_policy.
Allowed values: "no", "yes"
- `file_name` - (Optional) import file name
- `import_mode` - (Optional) data import mode.
Allowed values: "atomic", "best-effort"
- `import_type` - (Optional) data import type.
Allowed values: "merge", "replace"
- `name_alias` - (Optional) name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object configuration_import_policy.
- `fail_on_decrypt_errors` - (Optional) fail_on_decrypt_errors for object configuration_import_policy.
Allowed values: "no", "yes"
- `file_name` - (Optional) import file name
- `import_mode` - (Optional) data import mode.
Allowed values: "atomic", "best-effort"
- `import_type` - (Optional) data import type.
Allowed values: "merge", "replace"
- `name_alias` - (Optional) name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailOnDecryptErrors

fail_on_decrypt_errors for object configuration_import_policy.
Allowed values: "no", "yes"
- `file_name` - (Optional) import file name
- `import_mode` - (Optional) data import mode.
Allowed values: "atomic", "best-effort"
- `import_type` - (Optional) data import type.
Allowed values: "merge", "replace"
- `name_alias` - (Optional) name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileName

import file name
- `import_mode` - (Optional) data import mode.
Allowed values: "atomic", "best-effort"
- `import_type` - (Optional) data import type.
Allowed values: "merge", "replace"
- `name_alias` - (Optional) name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportMode

data import mode.
Allowed values: "atomic", "best-effort"
- `import_type` - (Optional) data import type.
Allowed values: "merge", "replace"
- `name_alias` - (Optional) name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportType

data import type.
Allowed values: "merge", "replace"
- `name_alias` - (Optional) name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

name of Object configuration_import_policy.
- `admin_st` - (Optional) admin state of the import
Allowed values: "untriggered", "triggered"
- `annotation` - (Optional) annotation for object configuration_import_policy.
- `description` - (Optional) Description for object configuration_import_policy.
- `fail_on_decrypt_errors` - (Optional) fail_on_decrypt_errors for object configuration_import_policy.
Allowed values: "no", "yes"
- `file_name` - (Optional) import file name
- `import_mode` - (Optional) data import mode.
Allowed values: "atomic", "best-effort"
- `import_type` - (Optional) data import type.
Allowed values: "merge", "replace"
- `name_alias` - (Optional) name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

name_alias for object configuration_import_policy.
- `snapshot` - (Optional) snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationConfigRsImportSource

Relation to class fileRemotePath. Cardinality - ONE_TO_ONE. Type - String.
- `relation_trig_rs_triggerable` - (Optional) Relation to class trigTriggerable. Cardinality - ONE_TO_ONE. Type - String.
- `relation_config_rs_remote_path` - (Optional) Relation to class fileRemotePath. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationConfigRsRemotePath

Relation to class fileRemotePath. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationTrigRsTriggerable

Relation to class trigTriggerable. Cardinality - ONE_TO_ONE. Type - String.
- `relation_config_rs_remote_path` - (Optional) Relation to class fileRemotePath. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshot

snapshot for object configuration_import_policy.
Allowed values: "no", "yes".

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

