# TF::ECL::BaremetalServerV2 FilesystemsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fstype" title="FsType">FsType</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#mountpoint" title="MountPoint">MountPoint</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#fstype" title="FsType">FsType</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#mountpoint" title="MountPoint">MountPoint</a>: <i>String</i>
</pre>

## Properties

#### FsType

Filesystem type. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

Filesystem label. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountPoint

Mount point. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

