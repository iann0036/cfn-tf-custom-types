# TF::OCI::CoreInstancePoolInstance

This resource provides the Instance Pool Instance resource in Oracle Cloud Infrastructure Core service.

Attaches an instance to an instance pool. For information about the prerequisites
that an instance must meet before you can attach it to a pool, see
[Attaching an Instance to an Instance Pool](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/updatinginstancepool.htm#attach-instance).

Using this resource will impact the size of the instance pool, attach will increment the size of the pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreInstancePoolInstance",
    "Properties" : {
        "<a href="#autoterminateinstanceondelete" title="AutoTerminateInstanceOnDelete">AutoTerminateInstanceOnDelete</a>" : <i>Boolean</i>,
        "<a href="#decrementsizeondelete" title="DecrementSizeOnDelete">DecrementSizeOnDelete</a>" : <i>Boolean</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#instancepoolid" title="InstancePoolId">InstancePoolId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreInstancePoolInstance
Properties:
    <a href="#autoterminateinstanceondelete" title="AutoTerminateInstanceOnDelete">AutoTerminateInstanceOnDelete</a>: <i>Boolean</i>
    <a href="#decrementsizeondelete" title="DecrementSizeOnDelete">DecrementSizeOnDelete</a>: <i>Boolean</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#instancepoolid" title="InstancePoolId">InstancePoolId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutoTerminateInstanceOnDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DecrementSizeOnDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePoolId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance pool.

_Required_: Yes

_Type_: String

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

#### AvailabilityDomain

Returns the <code>AvailabilityDomain</code> value.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### DisplayName

Returns the <code>DisplayName</code> value.

#### FaultDomain

Returns the <code>FaultDomain</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceConfigurationId

Returns the <code>InstanceConfigurationId</code> value.

#### LoadBalancerBackends

Returns the <code>LoadBalancerBackends</code> value.

#### Region

Returns the <code>Region</code> value.

#### Shape

Returns the <code>Shape</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

