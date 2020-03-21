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

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdministratorLoginPassword

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationMode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageKey

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageKeyType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageUri

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

