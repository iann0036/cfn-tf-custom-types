# TF::Vultr::IsoPrivate

Provides a Vultr ISO file resource. This can be used to create, read, and delete ISO files on your Vultr account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::IsoPrivate",
    "Properties" : {
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::IsoPrivate
Properties:
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### Url

URL pointing to the ISO file.

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

#### DateCreated

Returns the <code>DateCreated</code> value.

#### Filename

Returns the <code>Filename</code> value.

#### Id

Returns the <code>Id</code> value.

#### Md5sum

Returns the <code>Md5sum</code> value.

#### Sha512sum

Returns the <code>Sha512sum</code> value.

#### Size

Returns the <code>Size</code> value.

#### Status

Returns the <code>Status</code> value.

