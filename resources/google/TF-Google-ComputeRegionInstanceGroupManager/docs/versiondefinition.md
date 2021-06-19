# TF::Google::ComputeRegionInstanceGroupManager VersionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancetemplate" title="InstanceTemplate">InstanceTemplate</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#targetsize" title="TargetSize">TargetSize</a>" : <i>[ <a href="targetsizedefinition.md">TargetSizeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#instancetemplate" title="InstanceTemplate">InstanceTemplate</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#targetsize" title="TargetSize">TargetSize</a>: <i>
      - <a href="targetsizedefinition.md">TargetSizeDefinition</a></i>
</pre>

## Properties

#### InstanceTemplate

- The full URL to an instance template from which all new instances of this version will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

- Version name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSize

_Required_: No

_Type_: List of <a href="targetsizedefinition.md">TargetSizeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

