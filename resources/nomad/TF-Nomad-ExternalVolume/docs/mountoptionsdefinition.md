# TF::Nomad::ExternalVolume MountOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fstype" title="FsType">FsType</a>" : <i>String</i>,
    "<a href="#mountflags" title="MountFlags">MountFlags</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fstype" title="FsType">FsType</a>: <i>String</i>
<a href="#mountflags" title="MountFlags">MountFlags</a>: <i>
      - String</i>
</pre>

## Properties

#### FsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountFlags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
