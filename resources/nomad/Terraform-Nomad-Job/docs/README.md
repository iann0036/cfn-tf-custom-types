# Terraform::Nomad::Job

CloudFormation equivalent of nomad_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Nomad::Job",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#allocationids" title="AllocationIds">AllocationIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#datacenters" title="Datacenters">Datacenters</a>" : <i>[ String, ... ]</i>,
        "<a href="#deploymentid" title="DeploymentId">DeploymentId</a>" : <i>String</i>,
        "<a href="#deploymentstatus" title="DeploymentStatus">DeploymentStatus</a>" : <i>String</i>,
        "<a href="#deregisterondestroy" title="DeregisterOnDestroy">DeregisterOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#deregisteronidchange" title="DeregisterOnIdChange">DeregisterOnIdChange</a>" : <i>Boolean</i>,
        "<a href="#detach" title="Detach">Detach</a>" : <i>Boolean</i>,
        "<a href="#jobspec" title="Jobspec">Jobspec</a>" : <i>String</i>,
        "<a href="#json" title="Json">Json</a>" : <i>Boolean</i>,
        "<a href="#modifyindex" title="ModifyIndex">ModifyIndex</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#policyoverride" title="PolicyOverride">PolicyOverride</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#taskgroups" title="TaskGroups">TaskGroups</a>" : <i>[ &lt;a href=&#34;taskgroups.md&#34;&gt;TaskGroups&lt;/a&gt;, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Nomad::Job
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#allocationids" title="AllocationIds">AllocationIds</a>: <i>
      - String</i>
    <a href="#datacenters" title="Datacenters">Datacenters</a>: <i>
      - String</i>
    <a href="#deploymentid" title="DeploymentId">DeploymentId</a>: <i>String</i>
    <a href="#deploymentstatus" title="DeploymentStatus">DeploymentStatus</a>: <i>String</i>
    <a href="#deregisterondestroy" title="DeregisterOnDestroy">DeregisterOnDestroy</a>: <i>Boolean</i>
    <a href="#deregisteronidchange" title="DeregisterOnIdChange">DeregisterOnIdChange</a>: <i>Boolean</i>
    <a href="#detach" title="Detach">Detach</a>: <i>Boolean</i>
    <a href="#jobspec" title="Jobspec">Jobspec</a>: <i>String</i>
    <a href="#json" title="Json">Json</a>: <i>Boolean</i>
    <a href="#modifyindex" title="ModifyIndex">ModifyIndex</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#policyoverride" title="PolicyOverride">PolicyOverride</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#taskgroups" title="TaskGroups">TaskGroups</a>: <i>
      - &lt;a href=&#34;taskgroups.md&#34;&gt;TaskGroups&lt;/a&gt;</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllocationIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenters

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### ModifyIndex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyOverride

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskGroups

_Required_: No

_Type_: List of &lt;a href=&#34;taskgroups.md&#34;&gt;TaskGroups&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

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

Returns the &lt;code&gt;AllocationIds&lt;/code&gt; value.

#### Datacenters

Returns the &lt;code&gt;Datacenters&lt;/code&gt; value.

#### DeploymentId

Returns the &lt;code&gt;DeploymentId&lt;/code&gt; value.

#### DeploymentStatus

Returns the &lt;code&gt;DeploymentStatus&lt;/code&gt; value.

#### ModifyIndex

Returns the &lt;code&gt;ModifyIndex&lt;/code&gt; value.

#### Name

Returns the &lt;code&gt;Name&lt;/code&gt; value.

#### Namespace

Returns the &lt;code&gt;Namespace&lt;/code&gt; value.

#### Region

Returns the &lt;code&gt;Region&lt;/code&gt; value.

#### TaskGroups

Returns the &lt;code&gt;TaskGroups&lt;/code&gt; value.

#### Type

Returns the &lt;code&gt;Type&lt;/code&gt; value.

