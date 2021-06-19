# TF::OCI::AutoscalingAutoScalingConfiguration

This resource provides the Auto Scaling Configuration resource in Oracle Cloud Infrastructure Auto Scaling service.

Creates an autoscaling configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::AutoscalingAutoScalingConfiguration",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#cooldowninseconds" title="CoolDownInSeconds">CoolDownInSeconds</a>" : <i>Double</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#autoscalingresources" title="AutoScalingResources">AutoScalingResources</a>" : <i>[ <a href="autoscalingresourcesdefinition.md">AutoScalingResourcesDefinition</a>, ... ]</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ <a href="policiesdefinition.md">PoliciesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::AutoscalingAutoScalingConfiguration
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#cooldowninseconds" title="CoolDownInSeconds">CoolDownInSeconds</a>: <i>Double</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#autoscalingresources" title="AutoScalingResources">AutoScalingResources</a>: <i>
      - <a href="autoscalingresourcesdefinition.md">AutoScalingResourcesDefinition</a></i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - <a href="policiesdefinition.md">PoliciesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the autoscaling configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoolDownInSeconds

(Updatable) For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which is also the default. The cooldown period starts when the instance pool reaches the running state.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

A user-friendly name. Does not have to be unique. Avoid entering confidential information. This value is not changeable through Terraform.
* `metric` - (Required when policy_type=threshold) Metric and threshold details for triggering an autoscaling action.
* `metric_type` - (Required when policy_type=threshold)
* `threshold` - (Required when policy_type=threshold)
* `operator` - (Required when policy_type=threshold) The comparison operator to use. Options are greater than (`GT`), greater than or equal to (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
* `value` - (Required when policy_type=threshold).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

Whether the autoscaling policy is enabled.
* `policy_type` - (Required) The type of autoscaling policy.
* `resource_action` - (Applicable when policy_type=scheduled) An action that can be executed against a resource.
* `action` - (Required)
* `action_type` - (Required) The type of resource action.
* `rules` - (Required when policy_type=threshold)
* `action` - (Required when policy_type=threshold) The action to take when autoscaling is triggered.
* `type` - (Required when policy_type=threshold) The type of action to take.
* `value` - (Required when policy_type=threshold) To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of instances), provide a negative value.
* `display_name` - (Required when policy_type=threshold) A user-friendly name. Does not have to be unique. Avoid entering confidential information. This value is not changeable through Terraform.
* `metric` - (Required when policy_type=threshold) Metric and threshold details for triggering an autoscaling action.
* `metric_type` - (Required when policy_type=threshold)
* `threshold` - (Required when policy_type=threshold)
* `operator` - (Required when policy_type=threshold) The comparison operator to use. Options are greater than (`GT`), greater than or equal to (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
* `value` - (Required when policy_type=threshold).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingResources

_Required_: No

_Type_: List of <a href="autoscalingresourcesdefinition.md">AutoScalingResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of <a href="policiesdefinition.md">PoliciesDefinition</a>

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

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling configuration.
* `type` - (Required) The type of resource.

#### MaxResourceCount

Returns the <code>MaxResourceCount</code> value.

#### MinResourceCount

Returns the <code>MinResourceCount</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

