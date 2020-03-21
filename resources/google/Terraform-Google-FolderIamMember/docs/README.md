# Terraform::Google::FolderIamMember

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform folder.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_folder_iam_policy` or they will fight over what your policy
   should be. Similarly, roles controlled by `google_folder_iam_binding`
   should not be assigned to using `google_folder_iam_member`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::FolderIamMember",
    "Properties" : {
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#member" title="Member">Member</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::FolderIamMember
Properties:
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#member" title="Member">Member</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
</pre>

## Properties

#### Folder

The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

The identity that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
This field can have one of the following values:
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

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

#### Etag

Returns the <code>Etag</code> value.

