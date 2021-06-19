# TF::DME::FolderRecord

CloudFormation equivalent of dme_folder_record

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DME::FolderRecord",
    "Properties" : {
        "<a href="#defaultfolder" title="DefaultFolder">DefaultFolder</a>" : <i>Boolean</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#secondaries" title="Secondaries">Secondaries</a>" : <i>[ String, ... ]</i>,
        "<a href="#folderpermissions" title="FolderPermissions">FolderPermissions</a>" : <i>[ <a href="folderpermissionsdefinition.md">FolderPermissionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DME::FolderRecord
Properties:
    <a href="#defaultfolder" title="DefaultFolder">DefaultFolder</a>: <i>Boolean</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#secondaries" title="Secondaries">Secondaries</a>: <i>
      - String</i>
    <a href="#folderpermissions" title="FolderPermissions">FolderPermissions</a>: <i>
      - <a href="folderpermissionsdefinition.md">FolderPermissionsDefinition</a></i>
</pre>

## Properties

#### DefaultFolder

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secondaries

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FolderPermissions

_Required_: No

_Type_: List of <a href="folderpermissionsdefinition.md">FolderPermissionsDefinition</a>

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

