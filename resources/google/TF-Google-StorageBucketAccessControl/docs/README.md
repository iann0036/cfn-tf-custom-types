# TF::Google::StorageBucketAccessControl

Bucket ACLs can be managed authoritatively using the
[`storage_bucket_acl`](https://www.terraform.io/docs/providers/google/r/storage_bucket_acl.html)
resource. Do not use these two resources in conjunction to manage the same bucket.

The BucketAccessControls resource manages the Access Control List
(ACLs) for a single entity/role pairing on a bucket. ACLs let you specify who
has access to your data and to what extent.

There are three roles that can be assigned to an entity:

READERs can get the bucket, though no acl property will be returned, and
list the bucket's objects.  WRITERs are READERs, and they can insert
objects into the bucket and delete the bucket's objects.  OWNERs are
WRITERs, and they can get the acl property of a bucket, update a bucket,
and call all BucketAccessControls methods on the bucket.  For more
information, see Access Control, with the caveat that this API uses
READER, WRITER, and OWNER instead of READ, WRITE, and FULL_CONTROL.


To get more information about BucketAccessControl,...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::StorageBucketAccessControl",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#entity" title="Entity">Entity</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::StorageBucketAccessControl
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#entity" title="Entity">Entity</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Domain

Returns the <code>Domain</code> value.

#### Email

Returns the <code>Email</code> value.

#### Id

Returns the <code>Id</code> value.

