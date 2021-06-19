# TF::OCI::DatabaseExternalNonContainerDatabaseManagement

This resource provides the External Non Container Database Management resource in Oracle Cloud Infrastructure Database service.

Enable Database Management Service for the external non-container database.
For more information about the Database Management Service, see
[Database Management Service](https://docs.cloud.oracle.com/iaas/Content/ExternalDatabase/Concepts/databasemanagementservice.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseExternalNonContainerDatabaseManagement",
    "Properties" : {
        "<a href="#enablemanagement" title="EnableManagement">EnableManagement</a>" : <i>Boolean</i>,
        "<a href="#externaldatabaseconnectorid" title="ExternalDatabaseConnectorId">ExternalDatabaseConnectorId</a>" : <i>String</i>,
        "<a href="#externalnoncontainerdatabaseid" title="ExternalNonContainerDatabaseId">ExternalNonContainerDatabaseId</a>" : <i>String</i>,
        "<a href="#licensemodel" title="LicenseModel">LicenseModel</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseExternalNonContainerDatabaseManagement
Properties:
    <a href="#enablemanagement" title="EnableManagement">EnableManagement</a>: <i>Boolean</i>
    <a href="#externaldatabaseconnectorid" title="ExternalDatabaseConnectorId">ExternalDatabaseConnectorId</a>: <i>String</i>
    <a href="#externalnoncontainerdatabaseid" title="ExternalNonContainerDatabaseId">ExternalNonContainerDatabaseId</a>: <i>String</i>
    <a href="#licensemodel" title="LicenseModel">LicenseModel</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### EnableManagement

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalDatabaseConnectorId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the [external database connector](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNonContainerDatabaseId

The external non-container database [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseModel

The Oracle license model that applies to the external database. Required only for enabling database management.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

