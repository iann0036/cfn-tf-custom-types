# TF::AVI::Serverautoscalepolicy

The ServerAutoScalePolicy resource allows the creation and management of Avi ServerAutoScalePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Serverautoscalepolicy",
    "Properties" : {
        "<a href="#delayforservergarbagecollection" title="DelayForServerGarbageCollection">DelayForServerGarbageCollection</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#intelligentautoscale" title="IntelligentAutoscale">IntelligentAutoscale</a>" : <i>Boolean</i>,
        "<a href="#intelligentscaleinmargin" title="IntelligentScaleinMargin">IntelligentScaleinMargin</a>" : <i>Double</i>,
        "<a href="#intelligentscaleoutmargin" title="IntelligentScaleoutMargin">IntelligentScaleoutMargin</a>" : <i>Double</i>,
        "<a href="#maxscaleinadjustmentstep" title="MaxScaleinAdjustmentStep">MaxScaleinAdjustmentStep</a>" : <i>Double</i>,
        "<a href="#maxscaleoutadjustmentstep" title="MaxScaleoutAdjustmentStep">MaxScaleoutAdjustmentStep</a>" : <i>Double</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scaleinalertconfigrefs" title="ScaleinAlertconfigRefs">ScaleinAlertconfigRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#scaleincooldown" title="ScaleinCooldown">ScaleinCooldown</a>" : <i>Double</i>,
        "<a href="#scaleoutalertconfigrefs" title="ScaleoutAlertconfigRefs">ScaleoutAlertconfigRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#scaleoutcooldown" title="ScaleoutCooldown">ScaleoutCooldown</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#usepredictedload" title="UsePredictedLoad">UsePredictedLoad</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Serverautoscalepolicy
Properties:
    <a href="#delayforservergarbagecollection" title="DelayForServerGarbageCollection">DelayForServerGarbageCollection</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#intelligentautoscale" title="IntelligentAutoscale">IntelligentAutoscale</a>: <i>Boolean</i>
    <a href="#intelligentscaleinmargin" title="IntelligentScaleinMargin">IntelligentScaleinMargin</a>: <i>Double</i>
    <a href="#intelligentscaleoutmargin" title="IntelligentScaleoutMargin">IntelligentScaleoutMargin</a>: <i>Double</i>
    <a href="#maxscaleinadjustmentstep" title="MaxScaleinAdjustmentStep">MaxScaleinAdjustmentStep</a>: <i>Double</i>
    <a href="#maxscaleoutadjustmentstep" title="MaxScaleoutAdjustmentStep">MaxScaleoutAdjustmentStep</a>: <i>Double</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scaleinalertconfigrefs" title="ScaleinAlertconfigRefs">ScaleinAlertconfigRefs</a>: <i>
      - String</i>
    <a href="#scaleincooldown" title="ScaleinCooldown">ScaleinCooldown</a>: <i>Double</i>
    <a href="#scaleoutalertconfigrefs" title="ScaleoutAlertconfigRefs">ScaleoutAlertconfigRefs</a>: <i>
      - String</i>
    <a href="#scaleoutcooldown" title="ScaleoutCooldown">ScaleoutCooldown</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#usepredictedload" title="UsePredictedLoad">UsePredictedLoad</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
</pre>

## Properties

#### DelayForServerGarbageCollection

Delay in minutes after which a down server will be removed from pool. Value 0 disables this functionality. Field introduced in 20.1.3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelligentAutoscale

Use avi intelligent autoscale algorithm where autoscale is performed by comparing load on the pool against estimated capacity of all the servers.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelligentScaleinMargin

Maximum extra capacity as percentage of load used by the intelligent scheme. Scale-in is triggered when available capacity is more than this margin. Allowed values are 1-99.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelligentScaleoutMargin

Minimum extra capacity as percentage of load used by the intelligent scheme. Scale-out is triggered when available capacity is less than this margin. Allowed values are 1-99.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxScaleinAdjustmentStep

Maximum number of servers to scale-in simultaneously. The actual number of servers to scale-in is chosen such that target number of servers is always more than or equal to the min_size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxScaleoutAdjustmentStep

Maximum number of servers to scale-out simultaneously. The actual number of servers to scale-out is chosen such that target number of servers is always less than or equal to the max_size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

Maximum number of servers after scale-out. Allowed values are 0-400.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

No scale-in happens once number of operationally up servers reach min_servers. Allowed values are 0-400.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleinAlertconfigRefs

Trigger scale-in when alerts due to any of these alert configurations are raised. It is a reference to an object of type alertconfig.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleinCooldown

Cooldown period during which no new scale-in is triggered to allow previous scale-in to successfully complete. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutAlertconfigRefs

Trigger scale-out when alerts due to any of these alert configurations are raised. It is a reference to an object of type alertconfig.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleoutCooldown

Cooldown period during which no new scale-out is triggered to allow previous scale-out to successfully complete. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePredictedLoad

Use predicted load rather than current load.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

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

