# TF::Linode::ObjectStorageKey

Provides a Linode Object Storage Key resource. This can be used to create, modify, and delete Linodes Object Storage Keys.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Linode::ObjectStorageKey",
    "Properties" : {
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#bucketaccess" title="BucketAccess">BucketAccess</a>" : <i>[ <a href="bucketaccessdefinition.md">BucketAccessDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Linode::ObjectStorageKey
Properties:
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#bucketaccess" title="BucketAccess">BucketAccess</a>: <i>
      - <a href="bucketaccessdefinition.md">BucketAccessDefinition</a></i>
</pre>

## Properties

#### Label

The label given to this key. For display purposes only.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketAccess

_Required_: No

_Type_: List of <a href="bucketaccessdefinition.md">BucketAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessKey

Returns the <code>AccessKey</code> value.

#### Id

Returns the <code>Id</code> value.

#### Limited

Returns the <code>Limited</code> value.

#### SecretKey

Returns the <code>SecretKey</code> value.

