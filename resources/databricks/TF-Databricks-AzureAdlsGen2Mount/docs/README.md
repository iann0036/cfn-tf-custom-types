# TF::Databricks::AzureAdlsGen2Mount

CloudFormation equivalent of databricks_azure_adls_gen2_mount

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::AzureAdlsGen2Mount",
    "Properties" : {
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#clientsecretkey" title="ClientSecretKey">ClientSecretKey</a>" : <i>String</i>,
        "<a href="#clientsecretscope" title="ClientSecretScope">ClientSecretScope</a>" : <i>String</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#containername" title="ContainerName">ContainerName</a>" : <i>String</i>,
        "<a href="#directory" title="Directory">Directory</a>" : <i>String</i>,
        "<a href="#initializefilesystem" title="InitializeFileSystem">InitializeFileSystem</a>" : <i>Boolean</i>,
        "<a href="#mountname" title="MountName">MountName</a>" : <i>String</i>,
        "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::AzureAdlsGen2Mount
Properties:
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#clientsecretkey" title="ClientSecretKey">ClientSecretKey</a>: <i>String</i>
    <a href="#clientsecretscope" title="ClientSecretScope">ClientSecretScope</a>: <i>String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#containername" title="ContainerName">ContainerName</a>: <i>String</i>
    <a href="#directory" title="Directory">Directory</a>: <i>String</i>
    <a href="#initializefilesystem" title="InitializeFileSystem">InitializeFileSystem</a>: <i>Boolean</i>
    <a href="#mountname" title="MountName">MountName</a>: <i>String</i>
    <a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
</pre>

## Properties

#### ClientId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecretKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecretScope

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Directory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializeFileSystem

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: Yes

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

#### Source

Returns the <code>Source</code> value.

