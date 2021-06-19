# TF::Vultr::SnapshotFromUrl

Provides a Vultr Snapshots from URL resource. This can be used to create, read, modify, and delete Snapshots from URL.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::SnapshotFromUrl",
    "Properties" : {
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::SnapshotFromUrl
Properties:
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### Url

URL of the given resource you want to create a snapshot from.

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

#### AppId

Returns the <code>AppId</code> value.

#### DateCreated

Returns the <code>DateCreated</code> value.

#### Description

Returns the <code>Description</code> value.

#### Id

Returns the <code>Id</code> value.

#### OsId

Returns the <code>OsId</code> value.

#### Size

Returns the <code>Size</code> value.

#### Status

Returns the <code>Status</code> value.

