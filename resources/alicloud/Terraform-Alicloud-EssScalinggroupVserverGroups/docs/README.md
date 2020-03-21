# Terraform::Alicloud::EssScalinggroupVserverGroups

Attaches/Detaches vserver groups to a specified scaling group.

-> **NOTE:** The load balancer of which vserver groups belongs to must be in `active` status.

-> **NOTE:** If scaling group's network type is `VPC`, the vserver groups must be in the same `VPC`.
 
-> **NOTE:** A scaling group can have at most 5 vserver groups attached by default.

-> **NOTE:** Vserver groups and the default group of loadbalancer share the same backend server quota.

-> **NOTE:** When attach vserver groups to scaling group, existing ECS instances will be added to vserver groups; Instead, ECS instances will be removed from vserver group when detach.

-> **NOTE:** Detach action will be executed before attach action.

-> **NOTE:** Vserver group is defined uniquely by `loadbalancer_id`, `vserver_group_id`, `port`.

-> **NOTE:** Modifing `weight` attribute means detach vserver group first and then, attach with new weight parameter.

-> **NOTE:** Resource `alicloud_ess_scalinggroup_vserver_groups` is available in 1.53.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::EssScalinggroupVserverGroups",
    "Properties" : {
        "<a href="#force" title="Force">Force</a>" : <i>Boolean</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>,
        "<a href="#vservergroups" title="VserverGroups">VserverGroups</a>" : <i>[ <a href="vservergroups.md">VserverGroups</a>, ... ]</i>,
        "<a href="#vserverattributes" title="VserverAttributes">VserverAttributes</a>" : <i>[ <a href="vserverattributes.md">VserverAttributes</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::EssScalinggroupVserverGroups
Properties:
    <a href="#force" title="Force">Force</a>: <i>Boolean</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
    <a href="#vservergroups" title="VserverGroups">VserverGroups</a>: <i>
      - <a href="vservergroups.md">VserverGroups</a></i>
    <a href="#vserverattributes" title="VserverAttributes">VserverAttributes</a>: <i>
      - <a href="vserverattributes.md">VserverAttributes</a></i>
</pre>

## Properties

#### Force

If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

ID of the scaling group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VserverGroups

_Required_: No

_Type_: List of <a href="vservergroups.md">VserverGroups</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VserverAttributes

_Required_: No

_Type_: List of <a href="vserverattributes.md">VserverAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

