# Terraform::Google::StorageObjectAcl

Authoritatively manages the access control list (ACL) for an object in a Google
Cloud Storage (GCS) bucket. Removing a `google_storage_object_acl` sets the
acl to the `private` [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl).

For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls).

-> Want fine-grained control over object ACLs? Use `google_storage_object_access_control` to control individual
role entity pairs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::StorageObjectAcl",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#object" title="Object">Object</a>" : <i>String</i>,
        "<a href="#predefinedacl" title="PredefinedAcl">PredefinedAcl</a>" : <i>String</i>,
        "<a href="#roleentity" title="RoleEntity">RoleEntity</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::StorageObjectAcl
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#object" title="Object">Object</a>: <i>String</i>
    <a href="#predefinedacl" title="PredefinedAcl">PredefinedAcl</a>: <i>String</i>
    <a href="#roleentity" title="RoleEntity">RoleEntity</a>: <i>
      - String</i>
</pre>

## Properties

#### Bucket

The name of the bucket the object is stored in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Object

The name of the object to apply the acl to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedAcl

The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `role_entity` is not.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleEntity

List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
Must be set if `predefined_acl` is not.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

