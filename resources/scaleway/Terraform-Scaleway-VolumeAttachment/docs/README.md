# Terraform::Scaleway::VolumeAttachment

**DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
Please use `scaleway_instance_server.additional_volumes` instead.

This allows volumes to be attached to servers.

~> **Warning:** Attaching volumes requires the servers to be powered off. This will lead to downtime if the server is already in use.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::VolumeAttachment",
    "Properties" : {
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::VolumeAttachment
Properties:
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#volume" title="Volume">Volume</a>: <i>String</i>
</pre>

## Properties

#### Server

id of the server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

id of the volume to be attached.

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

