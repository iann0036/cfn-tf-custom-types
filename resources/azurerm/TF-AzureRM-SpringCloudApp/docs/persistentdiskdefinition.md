# TF::AzureRM::SpringCloudApp PersistentDiskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mountpath" title="MountPath">MountPath</a>" : <i>String</i>,
    "<a href="#sizeingb" title="SizeInGb">SizeInGb</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#mountpath" title="MountPath">MountPath</a>: <i>String</i>
<a href="#sizeingb" title="SizeInGb">SizeInGb</a>: <i>Double</i>
</pre>

## Properties

#### MountPath

Specifies the mount path of the persistent disk. Defaults to `/persistent`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeInGb

Specifies the size of the persistent disk in GB. Possible values are between `0` and `50`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

