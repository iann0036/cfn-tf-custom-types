# Terraform::Google::Folder

Allows management of a Google Cloud Platform folder. For more information see 
[the official documentation](https://cloud.google.com/resource-manager/docs/creating-managing-folders)
and 
[API](https://cloud.google.com/resource-manager/reference/rest/v2/folders).

A folder can contain projects, other folders, or a combination of both. You can use folders to group projects under an organization in a hierarchy. For example, your organization might contain multiple departments, each with its own set of Cloud Platform resources. Folders allows you to group these resources on a per-department basis. Folders are used to group resources that share common IAM policies.

Folders created live inside an Organization. See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.

The service account used to run Terraform when creating a `google_folder`
resource must have `roles/resourcemanager.folderCreator`. See the
[Access Control for Folders Using IAM](https://cloud.google.com/resource-manager/docs/access-control-folders)
doc for more information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::Folder",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::Folder
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DisplayName

The folder’s display name.
A folder’s display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

The resource name of the parent Folder or Organization.
Must be of the form `folders/{folder_id}` or `organizations/{org_id}`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### LifecycleState

Returns the <code>LifecycleState</code> value.

#### Name

Returns the <code>Name</code> value.

