# Terraform::AzureRM::SqlDatabase Import

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#administratorlogin" title="AdministratorLogin">AdministratorLogin</a>" : <i>String</i>,
    "<a href="#administratorloginpassword" title="AdministratorLoginPassword">AdministratorLoginPassword</a>" : <i>String</i>,
    "<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>" : <i>String</i>,
    "<a href="#operationmode" title="OperationMode">OperationMode</a>" : <i>String</i>,
    "<a href="#storagekey" title="StorageKey">StorageKey</a>" : <i>String</i>,
    "<a href="#storagekeytype" title="StorageKeyType">StorageKeyType</a>" : <i>String</i>,
    "<a href="#storageuri" title="StorageUri">StorageUri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#administratorlogin" title="AdministratorLogin">AdministratorLogin</a>: <i>String</i>
<a href="#administratorloginpassword" title="AdministratorLoginPassword">AdministratorLoginPassword</a>: <i>String</i>
<a href="#authenticationtype" title="AuthenticationType">AuthenticationType</a>: <i>String</i>
<a href="#operationmode" title="OperationMode">OperationMode</a>: <i>String</i>
<a href="#storagekey" title="StorageKey">StorageKey</a>: <i>String</i>
<a href="#storagekeytype" title="StorageKeyType">StorageKeyType</a>: <i>String</i>
<a href="#storageuri" title="StorageUri">StorageUri</a>: <i>String</i>
</pre>

## Properties

#### AdministratorLogin

Specifies the name of the SQL administrator.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdministratorLoginPassword

Specifies the password of the SQL administrator.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationType

Specifies the type of authentication used to access the server. Valid values are `SQL` or `ADPassword`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationMode

Specifies the type of import operation being performed. The only allowable value is `Import`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageKey

Specifies the access key for the storage account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageKeyType

Specifies the type of access key for the storage account. Valid values are `StorageAccessKey` or `SharedAccessKey`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageUri

Specifies the blob URI of the .bacpac file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

