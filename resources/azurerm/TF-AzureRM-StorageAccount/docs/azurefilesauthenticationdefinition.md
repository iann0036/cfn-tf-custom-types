# TF::AzureRM::StorageAccount AzureFilesAuthenticationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#directorytype" title="DirectoryType">DirectoryType</a>" : <i>String</i>,
    "<a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>" : <i>[ <a href="activedirectorydefinition.md">ActiveDirectoryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#directorytype" title="DirectoryType">DirectoryType</a>: <i>String</i>
<a href="#activedirectory" title="ActiveDirectory">ActiveDirectory</a>: <i>
      - <a href="activedirectorydefinition.md">ActiveDirectoryDefinition</a></i>
</pre>

## Properties

#### DirectoryType

Specifies the directory service used. Possible values are `AADDS` and `AD`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveDirectory

_Required_: No

_Type_: List of <a href="activedirectorydefinition.md">ActiveDirectoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

