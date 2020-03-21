# Terraform::AzureRM::KeyVault AccessPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationid" title="ApplicationId">ApplicationId</a>" : <i>String</i>,
    "<a href="#certificatepermissions" title="CertificatePermissions">CertificatePermissions</a>" : <i>[ String, ... ]</i>,
    "<a href="#keypermissions" title="KeyPermissions">KeyPermissions</a>" : <i>[ String, ... ]</i>,
    "<a href="#objectid" title="ObjectId">ObjectId</a>" : <i>String</i>,
    "<a href="#secretpermissions" title="SecretPermissions">SecretPermissions</a>" : <i>[ String, ... ]</i>,
    "<a href="#storagepermissions" title="StoragePermissions">StoragePermissions</a>" : <i>[ String, ... ]</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#applicationid" title="ApplicationId">ApplicationId</a>: <i>String</i>
<a href="#certificatepermissions" title="CertificatePermissions">CertificatePermissions</a>: <i>
      - String</i>
<a href="#keypermissions" title="KeyPermissions">KeyPermissions</a>: <i>
      - String</i>
<a href="#objectid" title="ObjectId">ObjectId</a>: <i>String</i>
<a href="#secretpermissions" title="SecretPermissions">SecretPermissions</a>: <i>
      - String</i>
<a href="#storagepermissions" title="StoragePermissions">StoragePermissions</a>: <i>
      - String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
</pre>

## Properties

#### ApplicationId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePermissions

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPermissions

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretPermissions

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoragePermissions

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

