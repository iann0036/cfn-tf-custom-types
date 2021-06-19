# TF::UpCloud::Storage

CloudFormation equivalent of upcloud_storage

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::UpCloud::Storage",
    "Properties" : {
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#backuprule" title="BackupRule">BackupRule</a>" : <i>[ <a href="backupruledefinition.md">BackupRuleDefinition</a>, ... ]</i>,
        "<a href="#clone" title="Clone">Clone</a>" : <i>[ <a href="clonedefinition.md">CloneDefinition</a>, ... ]</i>,
        "<a href="#import" title="Import">Import</a>" : <i>[ <a href="importdefinition.md">ImportDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::UpCloud::Storage
Properties:
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#backuprule" title="BackupRule">BackupRule</a>: <i>
      - <a href="backupruledefinition.md">BackupRuleDefinition</a></i>
    <a href="#clone" title="Clone">Clone</a>: <i>
      - <a href="clonedefinition.md">CloneDefinition</a></i>
    <a href="#import" title="Import">Import</a>: <i>
      - <a href="importdefinition.md">ImportDefinition</a></i>
</pre>

## Properties

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRule

_Required_: No

_Type_: List of <a href="backupruledefinition.md">BackupRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Clone

_Required_: No

_Type_: List of <a href="clonedefinition.md">CloneDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Import

_Required_: No

_Type_: List of <a href="importdefinition.md">ImportDefinition</a>

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

