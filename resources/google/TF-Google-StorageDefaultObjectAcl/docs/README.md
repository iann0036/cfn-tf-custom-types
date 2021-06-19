# TF::Google::StorageDefaultObjectAcl

Authoritatively manages the default object ACLs for a Google Cloud Storage bucket
without managing the bucket itself.

-> Note that for each object, its creator will have the `"OWNER"` role in addition
to the default ACL that has been defined.

For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls).

-> Want fine-grained control over default object ACLs? Use `google_storage_default_object_access_control`
to control individual role entity pairs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::StorageDefaultObjectAcl",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#roleentity" title="RoleEntity">RoleEntity</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::StorageDefaultObjectAcl
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#roleentity" title="RoleEntity">RoleEntity</a>: <i>
      - String</i>
</pre>

## Properties

#### Bucket

The name of the bucket it applies to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleEntity

List of role/entity pairs in the form `ROLE:entity`.
See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
Omitting the field is the same as providing an empty list.

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

#### Id

Returns the <code>Id</code> value.

