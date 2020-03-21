# Terraform::Alicloud::EssScalinggroupVserverGroups

CloudFormation equivalent of alicloud_ess_scalinggroup_vserver_groups

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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

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

