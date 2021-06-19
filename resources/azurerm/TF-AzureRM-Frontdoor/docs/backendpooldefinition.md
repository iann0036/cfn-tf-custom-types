# TF::AzureRM::Frontdoor BackendPoolDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthprobename" title="HealthProbeName">HealthProbeName</a>" : <i>String</i>,
    "<a href="#loadbalancingname" title="LoadBalancingName">LoadBalancingName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backenddefinition.md">BackendDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#healthprobename" title="HealthProbeName">HealthProbeName</a>: <i>String</i>
<a href="#loadbalancingname" title="LoadBalancingName">LoadBalancingName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backenddefinition.md">BackendDefinition</a></i>
</pre>

## Properties

#### HealthProbeName

Specifies the name of the `backend_pool_health_probe` block within this resource to use for this `Backend Pool`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingName

Specifies the name of the `backend_pool_load_balancing` block within this resource to use for this `Backend Pool`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Backend Pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of <a href="backenddefinition.md">BackendDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

