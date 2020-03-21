# Terraform::Google::FolderIamBinding

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform folder.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_folder_iam_policy` or they will fight over what your policy
   should be.

~> **Note:** On create, this resource will overwrite members of any existing roles.
    Use `terraform import` and inspect the `terraform plan` output to ensure
    your existing members are preserved.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::FolderIamBinding",
    "Properties" : {
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#members" title="Members">Members</a>" : <i>[ String, ... ]</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::FolderIamBinding
Properties:
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#members" title="Members">Members</a>: <i>
      - String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
</pre>

## Properties

#### Folder

The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The role that should be applied. Only one
`google_folder_iam_binding` can be used per role. Note that custom roles must be of the format
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

