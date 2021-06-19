# TF::FortiOS::SystemSdwan NeighborDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthCheckDefinition</a>, ... ]</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#member" title="Member">Member</a>" : <i>Double</i>,
    "<a href="#role" title="Role">Role</a>" : <i>String</i>,
    "<a href="#slaid" title="SlaId">SlaId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthCheckDefinition</a></i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#member" title="Member">Member</a>: <i>Double</i>
<a href="#role" title="Role">Role</a>: <i>String</i>
<a href="#slaid" title="SlaId">SlaId</a>: <i>Double</i>
</pre>

## Properties

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP/IPv6 address of neighbor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

Member sequence number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

Role of neighbor. Valid values: `standalone`, `primary`, `secondary`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaId

SLA ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

