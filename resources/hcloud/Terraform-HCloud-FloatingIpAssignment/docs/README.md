# Terraform::HCloud::FloatingIpAssignment

Provides a Hetzner Cloud Floating IP Assignment to assign a Floating IP to a Hetzner Cloud Server. Deleting a Floating IP Assignment will unassign the Floating IP from the Server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HCloud::FloatingIpAssignment",
    "Properties" : {
        "<a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>" : <i>Double</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HCloud::FloatingIpAssignment
Properties:
    <a href="#floatingipid" title="FloatingIpId">FloatingIpId</a>: <i>Double</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>Double</i>
</pre>

## Properties

#### FloatingIpId

ID of the Floating IP.
- `server_id` - (Required, int) Server to assign the Floating IP to.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

Server to assign the Floating IP to.

_Required_: Yes

_Type_: Double

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

