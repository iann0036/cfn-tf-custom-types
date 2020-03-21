# Terraform::Google::ComputeInstanceGroupManager Version

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancetemplate" title="InstanceTemplate">InstanceTemplate</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#targetsize" title="TargetSize">TargetSize</a>" : <i>[ <a href="version-targetsize.md">TargetSize</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#instancetemplate" title="InstanceTemplate">InstanceTemplate</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#targetsize" title="TargetSize">TargetSize</a>: <i>
      - <a href="version-targetsize.md">TargetSize</a></i>
</pre>

## Properties

#### InstanceTemplate

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSize

_Required_: No
_Type_: List of <a href="version-targetsize.md">TargetSize</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

