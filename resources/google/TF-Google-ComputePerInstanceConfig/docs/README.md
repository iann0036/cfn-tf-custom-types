# TF::Google::ComputePerInstanceConfig

A config defined for a single managed instance that belongs to an instance group manager. It preserves the instance name
across instance group manager operations and can define stateful disks or metadata that are unique to the instance.


To get more information about PerInstanceConfig, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/compute/docs/instance-groups/stateful-migs#per-instance_configs)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ComputePerInstanceConfig",
    "Properties" : {
        "<a href="#instancegroupmanager" title="InstanceGroupManager">InstanceGroupManager</a>" : <i>String</i>,
        "<a href="#minimalaction" title="MinimalAction">MinimalAction</a>" : <i>String</i>,
        "<a href="#mostdisruptiveallowedaction" title="MostDisruptiveAllowedAction">MostDisruptiveAllowedAction</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#removeinstancestateondestroy" title="RemoveInstanceStateOnDestroy">RemoveInstanceStateOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#preservedstate" title="PreservedState">PreservedState</a>" : <i>[ <a href="preservedstatedefinition.md">PreservedStateDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::ComputePerInstanceConfig
Properties:
    <a href="#instancegroupmanager" title="InstanceGroupManager">InstanceGroupManager</a>: <i>String</i>
    <a href="#minimalaction" title="MinimalAction">MinimalAction</a>: <i>String</i>
    <a href="#mostdisruptiveallowedaction" title="MostDisruptiveAllowedAction">MostDisruptiveAllowedAction</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#removeinstancestateondestroy" title="RemoveInstanceStateOnDestroy">RemoveInstanceStateOnDestroy</a>: <i>Boolean</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#preservedstate" title="PreservedState">PreservedState</a>: <i>
      - <a href="preservedstatedefinition.md">PreservedStateDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### InstanceGroupManager

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimalAction

The minimal action to perform on the instance during an update.
Default is `NONE`. Possible values are:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MostDisruptiveAllowedAction

The most disruptive action to perform on the instance during an update.
Default is `REPLACE`. Possible values are:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveInstanceStateOnDestroy

When true, deleting this config will immediately remove any specified state from the underlying instance.
When false, deleting this config will *not* immediately remove any state from the underlying instance.
State will be removed on the next instance recreation or update.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreservedState

_Required_: No

_Type_: List of <a href="preservedstatedefinition.md">PreservedStateDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

