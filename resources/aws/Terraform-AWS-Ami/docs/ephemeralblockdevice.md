# Terraform::AWS::Ami EphemeralBlockDevice

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#virtualname" title="VirtualName">VirtualName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#virtualname" title="VirtualName">VirtualName</a>: <i>String</i>
</pre>

## Properties

#### DeviceName

The path at which the device is exposed to created instances.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualName

A name for the ephemeral device, of the form "ephemeralN" where
*N* is a volume number starting from zero.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

