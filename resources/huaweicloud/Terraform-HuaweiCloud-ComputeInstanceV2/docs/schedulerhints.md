# Terraform::HuaweiCloud::ComputeInstanceV2 SchedulerHints

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#buildnearhostip" title="BuildNearHostIp">BuildNearHostIp</a>" : <i>String</i>,
    "<a href="#dehid" title="DehId">DehId</a>" : <i>String</i>,
    "<a href="#differenthost" title="DifferentHost">DifferentHost</a>" : <i>[ String, ... ]</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ String, ... ]</i>,
    "<a href="#samehost" title="SameHost">SameHost</a>" : <i>[ String, ... ]</i>,
    "<a href="#targetcell" title="TargetCell">TargetCell</a>" : <i>String</i>,
    "<a href="#tenancy" title="Tenancy">Tenancy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#buildnearhostip" title="BuildNearHostIp">BuildNearHostIp</a>: <i>String</i>
<a href="#dehid" title="DehId">DehId</a>: <i>String</i>
<a href="#differenthost" title="DifferentHost">DifferentHost</a>: <i>
      - String</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>
      - String</i>
<a href="#samehost" title="SameHost">SameHost</a>: <i>
      - String</i>
<a href="#targetcell" title="TargetCell">TargetCell</a>: <i>String</i>
<a href="#tenancy" title="Tenancy">Tenancy</a>: <i>String</i>
</pre>

## Properties

#### BuildNearHostIp

An IP Address in CIDR form. The instance
will be placed on a compute node that is in the same subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DehId

The ID of DeH. This parameter takes effect only when the value
of tenancy is dedicated.

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
order to host an instance.

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

#### Tenancy

The tenancy specifies whether the ECS is to be created on a Dedicated Host
(DeH) or in a shared pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

