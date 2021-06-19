# TF::Google::ComputeInstanceGroupManager AutoHealingPoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
    "<a href="#initialdelaysec" title="InitialDelaySec">InitialDelaySec</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
<a href="#initialdelaysec" title="InitialDelaySec">InitialDelaySec</a>: <i>Double</i>
</pre>

## Properties

#### HealthCheck

The health check resource that signals autohealing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialDelaySec

The number of seconds that the managed instance group waits before
it applies autohealing policies to new instances or recently recreated instances. Between 0 and 3600.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

