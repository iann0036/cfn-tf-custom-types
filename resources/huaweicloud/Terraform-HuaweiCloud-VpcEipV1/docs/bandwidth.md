# Terraform::HuaweiCloud::VpcEipV1 Bandwidth

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#chargemode" title="ChargeMode">ChargeMode</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sharetype" title="ShareType">ShareType</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#chargemode" title="ChargeMode">ChargeMode</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sharetype" title="ShareType">ShareType</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
</pre>

## Properties

#### ChargeMode

This is a reserved field. If the system supports charging
by traffic and this field is specified, then you are charged by traffic for elastic
IP addresses. Changing this creates a new eip.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

The share bandwidth id. Changing this creates a new eip.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The bandwidth name, which is a string of 1 to 64 characters
that contain letters, digits, underscores (_), and hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareType

Whether the bandwidth is shared or exclusive. Changing
this creates a new eip.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The bandwidth size. The value ranges from 1 to 300 Mbit/s.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

