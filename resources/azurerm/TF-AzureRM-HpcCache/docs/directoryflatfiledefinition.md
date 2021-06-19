# TF::AzureRM::HpcCache DirectoryFlatFileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#groupfileuri" title="GroupFileUri">GroupFileUri</a>" : <i>String</i>,
    "<a href="#passwordfileuri" title="PasswordFileUri">PasswordFileUri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#groupfileuri" title="GroupFileUri">GroupFileUri</a>: <i>String</i>
<a href="#passwordfileuri" title="PasswordFileUri">PasswordFileUri</a>: <i>String</i>
</pre>

## Properties

#### GroupFileUri

The URI of the file containing group information (`/etc/group` file format in Unix-like OS).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordFileUri

The URI of the file containing user information (`/etc/passwd` file format in Unix-like OS).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

