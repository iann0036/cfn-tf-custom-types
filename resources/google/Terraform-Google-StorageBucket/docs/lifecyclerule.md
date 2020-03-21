# Terraform::Google::StorageBucket LifecycleRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="lifecyclerule-action.md">Action</a>, ... ]</i>,
    "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="lifecyclerule-condition.md">Condition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="lifecyclerule-action.md">Action</a></i>
<a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="lifecyclerule-condition.md">Condition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: List of <a href="lifecyclerule-action.md">Action</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="lifecyclerule-condition.md">Condition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

