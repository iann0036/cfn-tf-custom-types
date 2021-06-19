# TF::Nomad::Job

Manages a job registered in Nomad.

This can be used to initialize your cluster with system jobs, common services,
and more. In day to day Nomad use it is common for developers to submit jobs to
Nomad directly, such as for general app deployment. In addition to these apps, a
Nomad cluster often runs core system services that are ideally setup during
infrastructure creation. This resource is ideal for the latter type of job, but
can be used to manage any job within Nomad.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nomad::Job",
    "Properties" : {
        "<a href="#deregisterondestroy" title="DeregisterOnDestroy">DeregisterOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#deregisteronidchange" title="DeregisterOnIdChange">DeregisterOnIdChange</a>" : <i>Boolean</i>,
        "<a href="#detach" title="Detach">Detach</a>" : <i>Boolean</i>,
        "<a href="#jobspec" title="Jobspec">Jobspec</a>" : <i>String</i>,
        "<a href="#json" title="Json">Json</a>" : <i>Boolean</i>,
        "<a href="#policyoverride" title="PolicyOverride">PolicyOverride</a>" : <i>Boolean</i>,
        "<a href="#purgeondestroy" title="PurgeOnDestroy">PurgeOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#hcl2" title="Hcl2">Hcl2</a>" : <i>[ <a href="hcl2definition.md">Hcl2Definition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nomad::Job
Properties:
    <a href="#deregisterondestroy" title="DeregisterOnDestroy">DeregisterOnDestroy</a>: <i>Boolean</i>
    <a href="#deregisteronidchange" title="DeregisterOnIdChange">DeregisterOnIdChange</a>: <i>Boolean</i>
    <a href="#detach" title="Detach">Detach</a>: <i>Boolean</i>
    <a href="#jobspec" title="Jobspec">Jobspec</a>: <i>String</i>
    <a href="#json" title="Json">Json</a>: <i>Boolean</i>
    <a href="#policyoverride" title="PolicyOverride">PolicyOverride</a>: <i>Boolean</i>
    <a href="#purgeondestroy" title="PurgeOnDestroy">PurgeOnDestroy</a>: <i>Boolean</i>
    <a href="#hcl2" title="Hcl2">Hcl2</a>: <i>
      - <a href="hcl2definition.md">Hcl2Definition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DeregisterOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeregisterOnIdChange

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Detach

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jobspec

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Json

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyOverride

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PurgeOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hcl2

_Required_: No

_Type_: List of <a href="hcl2definition.md">Hcl2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllocationIds

Returns the <code>AllocationIds</code> value.

#### Datacenters

Returns the <code>Datacenters</code> value.

#### DeploymentId

Returns the <code>DeploymentId</code> value.

#### DeploymentStatus

Returns the <code>DeploymentStatus</code> value.

#### Id

Returns the <code>Id</code> value.

#### ModifyIndex

Returns the <code>ModifyIndex</code> value.

#### Name

Returns the <code>Name</code> value.

#### Namespace

Returns the <code>Namespace</code> value.

#### Region

Returns the <code>Region</code> value.

#### TaskGroups

Returns the <code>TaskGroups</code> value.

#### Type

Returns the <code>Type</code> value.

