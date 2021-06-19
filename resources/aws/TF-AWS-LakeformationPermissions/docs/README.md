# TF::AWS::LakeformationPermissions

Grants permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3. Permissions are granted to a principal, in a Data Catalog, relative to a Lake Formation resource, which includes the Data Catalog, databases, and tables. For more information, see [Security and Access Control to Metadata and Data in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html).

~> **NOTE:** Lake Formation grants implicit permissions to data lake administrators, database creators, and table creators. These implicit permissions cannot be revoked _per se_. If this resource reads implicit permissions, it will attempt to revoke them, which causes an error when the resource is destroyed. There are two ways to avoid these errors. First, grant explicit permissions (and `permissions_with_grant_option`) to "overwrite" a principal's implicit permissions, which you can then revoke with this resource. Second, avoid using this res...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LakeformationPermissions",
    "Properties" : {
        "<a href="#catalogid" title="CatalogId">CatalogId</a>" : <i>String</i>,
        "<a href="#catalogresource" title="CatalogResource">CatalogResource</a>" : <i>Boolean</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#permissionswithgrantoption" title="PermissionsWithGrantOption">PermissionsWithGrantOption</a>" : <i>[ String, ... ]</i>,
        "<a href="#principal" title="Principal">Principal</a>" : <i>String</i>,
        "<a href="#datalocation" title="DataLocation">DataLocation</a>" : <i>[ <a href="datalocationdefinition.md">DataLocationDefinition</a>, ... ]</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ <a href="databasedefinition.md">DatabaseDefinition</a>, ... ]</i>,
        "<a href="#table" title="Table">Table</a>" : <i>[ <a href="tabledefinition.md">TableDefinition</a>, ... ]</i>,
        "<a href="#tablewithcolumns" title="TableWithColumns">TableWithColumns</a>" : <i>[ <a href="tablewithcolumnsdefinition.md">TableWithColumnsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LakeformationPermissions
Properties:
    <a href="#catalogid" title="CatalogId">CatalogId</a>: <i>String</i>
    <a href="#catalogresource" title="CatalogResource">CatalogResource</a>: <i>Boolean</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - String</i>
    <a href="#permissionswithgrantoption" title="PermissionsWithGrantOption">PermissionsWithGrantOption</a>: <i>
      - String</i>
    <a href="#principal" title="Principal">Principal</a>: <i>String</i>
    <a href="#datalocation" title="DataLocation">DataLocation</a>: <i>
      - <a href="datalocationdefinition.md">DataLocationDefinition</a></i>
    <a href="#database" title="Database">Database</a>: <i>
      - <a href="databasedefinition.md">DatabaseDefinition</a></i>
    <a href="#table" title="Table">Table</a>: <i>
      - <a href="tabledefinition.md">TableDefinition</a></i>
    <a href="#tablewithcolumns" title="TableWithColumns">TableWithColumns</a>: <i>
      - <a href="tablewithcolumnsdefinition.md">TableWithColumnsDefinition</a></i>
</pre>

## Properties

#### CatalogId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogResource

Whether the permissions are to be granted for the Data Catalog. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionsWithGrantOption

Subset of `permissions` which the principal can pass.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Principal

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataLocation

_Required_: No

_Type_: List of <a href="datalocationdefinition.md">DataLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="databasedefinition.md">DatabaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Table

_Required_: No

_Type_: List of <a href="tabledefinition.md">TableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableWithColumns

_Required_: No

_Type_: List of <a href="tablewithcolumnsdefinition.md">TableWithColumnsDefinition</a>

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

