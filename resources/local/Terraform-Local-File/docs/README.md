# Terraform::Local::File

Generates a local file with the given content.

~> **Note** When working with local files, Terraform will detect the resource
as having been deleted each time a configuration is applied on a new machine
where the file is not present and will generate a diff to re-create it. This
may cause "noise" in diffs in environments where configurations are routinely
applied by many different users or within automation systems.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Local::File",
    "Properties" : {
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#contentbase64" title="ContentBase64">ContentBase64</a>" : <i>String</i>,
        "<a href="#directorypermission" title="DirectoryPermission">DirectoryPermission</a>" : <i>String</i>,
        "<a href="#filepermission" title="FilePermission">FilePermission</a>" : <i>String</i>,
        "<a href="#filename" title="Filename">Filename</a>" : <i>String</i>,
        "<a href="#sensitivecontent" title="SensitiveContent">SensitiveContent</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Local::File
Properties:
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#contentbase64" title="ContentBase64">ContentBase64</a>: <i>String</i>
    <a href="#directorypermission" title="DirectoryPermission">DirectoryPermission</a>: <i>String</i>
    <a href="#filepermission" title="FilePermission">FilePermission</a>: <i>String</i>
    <a href="#filename" title="Filename">Filename</a>: <i>String</i>
    <a href="#sensitivecontent" title="SensitiveContent">SensitiveContent</a>: <i>String</i>
</pre>

## Properties

#### Content

The content of file to create. Conflicts with `sensitive_content` and `content_base64`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentBase64

The base64 encoded content of the file to create. Use this when dealing with binary data. Conflicts with `content` and `sensitive_content`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryPermission

The permission to set for any directories created. Expects a string. The default value is `"0777"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilePermission

The permission to set for the created file. Expects an a string. The default value is `"0777"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filename

The path of the file to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensitiveContent

The content of file to create. Will not be displayed in diffs. Conflicts with `content` and `content_base64`.

_Required_: No

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

