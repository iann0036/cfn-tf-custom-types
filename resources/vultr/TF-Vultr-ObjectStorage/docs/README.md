# TF::Vultr::ObjectStorage

Provides a Vultr private object storage resource. This can be used to create, read, update and delete object storage resources on your Vultr account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::ObjectStorage",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>Double</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::ObjectStorage
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>Double</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
</pre>

## Properties

#### ClusterId

The region ID that you want the network to be created in.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The description you want to give your network.

_Required_: No

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

#### Id

Returns the <code>Id</code> value.

#### Location

Returns the <code>Location</code> value.

#### Region

Returns the <code>Region</code> value.

#### S3AccessKey

Returns the <code>S3AccessKey</code> value.

#### S3Hostname

Returns the <code>S3Hostname</code> value.

#### S3SecretKey

Returns the <code>S3SecretKey</code> value.

#### Status

Returns the <code>Status</code> value.

