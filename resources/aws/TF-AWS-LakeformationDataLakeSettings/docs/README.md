# TF::AWS::LakeformationDataLakeSettings

Manages Lake Formation principals designated as data lake administrators and lists of principal permission entries for default create database and default create table permissions.

~> **NOTE:** Lake Formation introduces fine-grained access control for data in your data lake. Part of the changes include the `IAMAllowedPrincipals` principal in order to make Lake Formation backwards compatible with existing IAM and Glue permissions. For more information, see [Changing the Default Security Settings for Your Data Lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html) and [Upgrading AWS Glue Data Permissions to the AWS Lake Formation Model](https://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LakeformationDataLakeSettings",
    "Properties" : {
        "<a href="#admins" title="Admins">Admins</a>" : <i>[ String, ... ]</i>,
        "<a href="#catalogid" title="CatalogId">CatalogId</a>" : <i>String</i>,
        "<a href="#trustedresourceowners" title="TrustedResourceOwners">TrustedResourceOwners</a>" : <i>[ String, ... ]</i>,
        "<a href="#createdatabasedefaultpermissions" title="CreateDatabaseDefaultPermissions">CreateDatabaseDefaultPermissions</a>" : <i>[ <a href="createdatabasedefaultpermissionsdefinition.md">CreateDatabaseDefaultPermissionsDefinition</a>, ... ]</i>,
        "<a href="#createtabledefaultpermissions" title="CreateTableDefaultPermissions">CreateTableDefaultPermissions</a>" : <i>[ <a href="createtabledefaultpermissionsdefinition.md">CreateTableDefaultPermissionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LakeformationDataLakeSettings
Properties:
    <a href="#admins" title="Admins">Admins</a>: <i>
      - String</i>
    <a href="#catalogid" title="CatalogId">CatalogId</a>: <i>String</i>
    <a href="#trustedresourceowners" title="TrustedResourceOwners">TrustedResourceOwners</a>: <i>
      - String</i>
    <a href="#createdatabasedefaultpermissions" title="CreateDatabaseDefaultPermissions">CreateDatabaseDefaultPermissions</a>: <i>
      - <a href="createdatabasedefaultpermissionsdefinition.md">CreateDatabaseDefaultPermissionsDefinition</a></i>
    <a href="#createtabledefaultpermissions" title="CreateTableDefaultPermissions">CreateTableDefaultPermissions</a>: <i>
      - <a href="createtabledefaultpermissionsdefinition.md">CreateTableDefaultPermissionsDefinition</a></i>
</pre>

## Properties

#### Admins

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedResourceOwners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDatabaseDefaultPermissions

_Required_: No

_Type_: List of <a href="createdatabasedefaultpermissionsdefinition.md">CreateDatabaseDefaultPermissionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTableDefaultPermissions

_Required_: No

_Type_: List of <a href="createtabledefaultpermissionsdefinition.md">CreateTableDefaultPermissionsDefinition</a>

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

