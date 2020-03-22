# Terraform::Linode::ObjectStorageBucket

Provides a Linode Object Storage Bucket resource. This can be used to create, modify, and delete Linodes Object Storage Buckets.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Linode::ObjectStorageBucket",
    "Properties" : {
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Linode::ObjectStorageBucket
Properties:
    <a href="#cluster" title="Cluster">Cluster</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
</pre>

## Properties

#### Cluster

The cluster of the Linode Object Storage Bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The label of the Linode Object Storage Bucket.

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

#### Id

Returns the <code>Id</code> value.

