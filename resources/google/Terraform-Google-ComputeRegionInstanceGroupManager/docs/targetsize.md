# Terraform::Google::ComputeRegionInstanceGroupManager TargetSize

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fixed" title="Fixed">Fixed</a>" : <i>Double</i>,
    "<a href="#percent" title="Percent">Percent</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#fixed" title="Fixed">Fixed</a>: <i>Double</i>
<a href="#percent" title="Percent">Percent</a>: <i>Double</i>
</pre>

## Properties

#### Fixed

, The number of instances which are managed for this version. Conflicts with `percent`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Percent

, The number of instances (calculated as percentage) which are managed for this version. Conflicts with `fixed`.
Note that when using `percent`, rounding will be in favor of explicitly set `target_size` values; a managed instance group with 2 instances and 2 `version`s,
one of which has a `target_size.percent` of `60` will create 2 instances of that `version`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

