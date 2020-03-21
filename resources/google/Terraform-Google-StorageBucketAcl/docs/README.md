# Terraform::Google::StorageBucketAcl

Authoritatively manages a bucket's ACLs in Google cloud storage service (GCS). For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls).

Bucket ACLs can be managed non authoritatively using the [`storage_bucket_access_control`](https://www.terraform.io/docs/providers/google/r/storage_bucket_access_control.html) resource. Do not use these two resources in conjunction to manage the same bucket.

Permissions can be granted either by ACLs or Cloud IAM policies. In general, permissions granted by Cloud IAM policies do not appear in ACLs, and permissions granted by ACLs do not appear in Cloud IAM policies. The only exception is for ACLs applied directly on a bucket and certain bucket-level Cloud IAM policies, as described in [Cloud IAM relation to ACLs](https://cloud.google.com/storage/docs/access-control/iam#acls).

**NOTE** This resource will not remove the `project-owners-<project_id>` entity from the `OWNER` role.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::StorageBucketAcl",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#defaultacl" title="DefaultAcl">DefaultAcl</a>" : <i>String</i>,
        "<a href="#predefinedacl" title="PredefinedAcl">PredefinedAcl</a>" : <i>String</i>,
        "<a href="#roleentity" title="RoleEntity">RoleEntity</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::StorageBucketAcl
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#defaultacl" title="DefaultAcl">DefaultAcl</a>: <i>String</i>
    <a href="#predefinedacl" title="PredefinedAcl">PredefinedAcl</a>: <i>String</i>
    <a href="#roleentity" title="RoleEntity">RoleEntity</a>: <i>
      - String</i>
</pre>

## Properties

#### Bucket

The name of the bucket it applies to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAcl

Configure this ACL to be the default ACL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedAcl

The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleEntity

List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.

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

