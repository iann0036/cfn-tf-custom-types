# Terraform::OCI::ObjectstoragePreauthrequest

This resource provides the Preauthenticated Request resource in Oracle Cloud Infrastructure Object Storage service.

Creates a pre-authenticated request specific to the bucket.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::ObjectstoragePreauthrequest",
    "Properties" : {
        "<a href="#accesstype" title="AccessType">AccessType</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#object" title="Object">Object</a>" : <i>String</i>,
        "<a href="#timeexpires" title="TimeExpires">TimeExpires</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::ObjectstoragePreauthrequest
Properties:
    <a href="#accesstype" title="AccessType">AccessType</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#object" title="Object">Object</a>: <i>String</i>
    <a href="#timeexpires" title="TimeExpires">TimeExpires</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AccessType

The operation that can be performed on this resource. Allowed Values: `ObjectRead`, `ObjectWrite`, `ObjectReadWrite`, or `AnyObjectWrite`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A user-specified name for the pre-authenticated request. Names can be helpful in managing pre-authenticated requests.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

The Object Storage namespace used for the request.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Object

The name of the object that is being granted access to by the pre-authenticated request. Avoid entering confidential information. The object name can be null and if so, the pre-authenticated request grants access to the entire bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeExpires

The expiration date for the pre-authenticated request as per [RFC 3339](https://tools.ietf.org/rfc/rfc3339). After this date the pre-authenticated request will no longer be valid.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessUri

Returns the <code>AccessUri</code> value.

#### Id

Returns the <code>Id</code> value.

#### ParId

Returns the <code>ParId</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

