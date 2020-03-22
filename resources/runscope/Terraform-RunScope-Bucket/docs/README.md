# Terraform::RunScope::Bucket

A [bucket](https://www.runscope.com/docs/api/buckets) resource.
[Buckets](https://www.runscope.com/docs/buckets) are a simple way to
organize your requests and tests.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::RunScope::Bucket",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#teamuuid" title="TeamUuid">TeamUuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::RunScope::Bucket
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#teamuuid" title="TeamUuid">TeamUuid</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of this bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamUuid

Unique identifier for the team this bucket
is being created for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

