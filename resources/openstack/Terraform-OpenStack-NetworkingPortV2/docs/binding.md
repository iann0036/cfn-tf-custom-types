# Terraform::OpenStack::NetworkingPortV2 Binding

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostid" title="HostId">HostId</a>" : <i>String</i>,
    "<a href="#profile" title="Profile">Profile</a>" : <i>String</i>,
    "<a href="#vnictype" title="VnicType">VnicType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hostid" title="HostId">HostId</a>: <i>String</i>
<a href="#profile" title="Profile">Profile</a>: <i>String</i>
<a href="#vnictype" title="VnicType">VnicType</a>: <i>String</i>
</pre>

## Properties

#### HostId

The ID of the host to allocate port on.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

Custom data to be passed as `binding:profile`. Data
must be passed as JSON.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicType

VNIC type for the port. Can either be `direct`,
`direct-physical`, `macvtap`, `normal`, `baremetal` or `virtio-forwarder`.
Default value is `normal`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

