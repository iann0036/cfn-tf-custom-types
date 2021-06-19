# TF::Alicloud::ResourceManagerFolder

Provides a Resource Manager Folder resource. A folder is an organizational unit in a resource directory. You can use folders to build an organizational structure for resources.
For information about Resource Manager Foler and how to use it, see [What is Resource Manager Folder](https://www.alibabacloud.com/help/en/doc-detail/111221.htm).

-> **NOTE:** Available in v1.82.0+.

-> **NOTE:** A maximum of five levels of folders can be created under the root folder.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::ResourceManagerFolder",
    "Properties" : {
        "<a href="#foldername" title="FolderName">FolderName</a>" : <i>String</i>,
        "<a href="#parentfolderid" title="ParentFolderId">ParentFolderId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::ResourceManagerFolder
Properties:
    <a href="#foldername" title="FolderName">FolderName</a>: <i>String</i>
    <a href="#parentfolderid" title="ParentFolderId">ParentFolderId</a>: <i>String</i>
</pre>

## Properties

#### FolderName

The name of the folder. The name must be 1 to 24 characters in length and can contain letters, digits, underscores (_), periods (.), and hyphens (-).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentFolderId

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

#### Id

Returns the <code>Id</code> value.

