# Terraform::OpenStack::ComputeInstanceV2 SchedulerHints

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>[ <a href="schedulerhints-additionalproperties.md">AdditionalProperties</a>, ... ]</i>,
    "<a href="#buildnearhostip" title="BuildNearHostIp">BuildNearHostIp</a>" : <i>String</i>,
    "<a href="#differenthost" title="DifferentHost">DifferentHost</a>" : <i>[ String, ... ]</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ String, ... ]</i>,
    "<a href="#samehost" title="SameHost">SameHost</a>" : <i>[ String, ... ]</i>,
    "<a href="#targetcell" title="TargetCell">TargetCell</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>
      - <a href="schedulerhints-additionalproperties.md">AdditionalProperties</a></i>
<a href="#buildnearhostip" title="BuildNearHostIp">BuildNearHostIp</a>: <i>String</i>
<a href="#differenthost" title="DifferentHost">DifferentHost</a>: <i>
      - String</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>
      - String</i>
<a href="#samehost" title="SameHost">SameHost</a>: <i>
      - String</i>
<a href="#targetcell" title="TargetCell">TargetCell</a>: <i>String</i>
</pre>

## Properties

#### AdditionalProperties

Arbitrary key/value pairs of additional
properties to pass to the scheduler.

_Required_: No

_Type_: List of <a href="schedulerhints-additionalproperties.md">AdditionalProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildNearHostIp

An IP Address in CIDR form. The instance
will be placed on a compute node that is in the same subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DifferentHost

A list of instance UUIDs. The instance will
be scheduled on a different host than all other instances.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

A UUID of a Server Group. The instance will be placed
into that group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

A conditional query that a compute node must pass in
order to host an instance. The query must use the `JsonFilter` syntax
which is described
[here](https://docs.openstack.org/nova/latest/admin/configuration/schedulers.html#jsonfilter).
At this time, only simple queries are supported. Compound queries using
`and`, `or`, or `not` are not supported. An example of a simple query is:.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SameHost

A list of instance UUIDs. The instance will be
scheduled on the same host of those specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetCell

The name of a cell to host the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

