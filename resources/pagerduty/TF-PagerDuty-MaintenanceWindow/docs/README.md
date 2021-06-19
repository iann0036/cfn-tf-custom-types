# TF::PagerDuty::MaintenanceWindow

A [maintenance window](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Maintenance_Windows/get_maintenance_windows) is used to temporarily disable one or more services for a set period of time. No incidents will be triggered and no notifications will be received while a service is disabled by a maintenance window.

Maintenance windows are specified to start at a certain time and end after they have begun. Once started, a maintenance window cannot be deleted; it can only be ended immediately to re-enable the service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PagerDuty::MaintenanceWindow",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PagerDuty::MaintenanceWindow
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
    <a href="#services" title="Services">Services</a>: <i>
      - String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
</pre>

## Properties

#### Description

A description for the maintenance window.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

The maintenance window's end time. This is when the services will start creating incidents again. This date must be in the future and after the `start_time`.
* `services`    - (Required) A list of service IDs to include in the maintenance window.
* `description` - (Optional) A description for the maintenance window.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

A list of service IDs to include in the maintenance window.
* `description` - (Optional) A description for the maintenance window.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

The maintenance window's start time. This is when the services will stop creating incidents. If this date is in the past, it will be updated to be the current time.
* `end_time`    - (Required) The maintenance window's end time. This is when the services will start creating incidents again. This date must be in the future and after the `start_time`.
* `services`    - (Required) A list of service IDs to include in the maintenance window.
* `description` - (Optional) A description for the maintenance window.

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

