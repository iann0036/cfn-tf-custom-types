# TF::MongoDBAtlas::MaintenanceWindow

`mongodbatlas_maintenance_window` provides a resource to schedule a maintenance window for your MongoDB Atlas Project and/or set to defer a scheduled maintenance up to two times.

-> **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::MaintenanceWindow",
    "Properties" : {
        "<a href="#dayofweek" title="DayOfWeek">DayOfWeek</a>" : <i>Double</i>,
        "<a href="#defer" title="Defer">Defer</a>" : <i>Boolean</i>,
        "<a href="#hourofday" title="HourOfDay">HourOfDay</a>" : <i>Double</i>,
        "<a href="#numberofdeferrals" title="NumberOfDeferrals">NumberOfDeferrals</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::MaintenanceWindow
Properties:
    <a href="#dayofweek" title="DayOfWeek">DayOfWeek</a>: <i>Double</i>
    <a href="#defer" title="Defer">Defer</a>: <i>Boolean</i>
    <a href="#hourofday" title="HourOfDay">HourOfDay</a>: <i>Double</i>
    <a href="#numberofdeferrals" title="NumberOfDeferrals">NumberOfDeferrals</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
</pre>

## Properties

#### DayOfWeek

Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Defer

Defer maintenance for the given project for one week.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourOfDay

Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfDeferrals

Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique identifier of the project for the Maintenance Window.

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

#### StartAsap

Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.

