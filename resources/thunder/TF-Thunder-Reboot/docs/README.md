# TF::Thunder::Reboot

`thunder_reboot` Provides details about thunder reboot

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::Reboot",
    "Properties" : {
        "<a href="#all" title="All">All</a>" : <i>Double</i>,
        "<a href="#at" title="At">At</a>" : <i>Double</i>,
        "<a href="#cancel" title="Cancel">Cancel</a>" : <i>Double</i>,
        "<a href="#dayofmonth" title="DayOfMonth">DayOfMonth</a>" : <i>Double</i>,
        "<a href="#dayofmonth2" title="DayOfMonth2">DayOfMonth2</a>" : <i>Double</i>,
        "<a href="#device" title="Device">Device</a>" : <i>Double</i>,
        "<a href="#in" title="In">In</a>" : <i>String</i>,
        "<a href="#month" title="Month">Month</a>" : <i>String</i>,
        "<a href="#month2" title="Month2">Month2</a>" : <i>String</i>,
        "<a href="#reason" title="Reason">Reason</a>" : <i>String</i>,
        "<a href="#reason2" title="Reason2">Reason2</a>" : <i>String</i>,
        "<a href="#reason3" title="Reason3">Reason3</a>" : <i>String</i>,
        "<a href="#time" title="Time">Time</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::Reboot
Properties:
    <a href="#all" title="All">All</a>: <i>Double</i>
    <a href="#at" title="At">At</a>: <i>Double</i>
    <a href="#cancel" title="Cancel">Cancel</a>: <i>Double</i>
    <a href="#dayofmonth" title="DayOfMonth">DayOfMonth</a>: <i>Double</i>
    <a href="#dayofmonth2" title="DayOfMonth2">DayOfMonth2</a>: <i>Double</i>
    <a href="#device" title="Device">Device</a>: <i>Double</i>
    <a href="#in" title="In">In</a>: <i>String</i>
    <a href="#month" title="Month">Month</a>: <i>String</i>
    <a href="#month2" title="Month2">Month2</a>: <i>String</i>
    <a href="#reason" title="Reason">Reason</a>: <i>String</i>
    <a href="#reason2" title="Reason2">Reason2</a>: <i>String</i>
    <a href="#reason3" title="Reason3">Reason3</a>: <i>String</i>
    <a href="#time" title="Time">Time</a>: <i>String</i>
</pre>

## Properties

#### All

Reboot all devices when VCS is enabled, or only this device itself if VCS is not enabled.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### At

Reboot at a Specific time/date.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cancel

Cancel Pending Reboot.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfMonth

Day of the Month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfMonth2

Day of the Month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Device

Reboot a specific device when VCS is enabled (device id).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### In

Reboot after a time interval (Time in hours and minutes).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Month

‘January’: Month of the year; ‘February’: Month of the year; ‘March’: Month of the year; ‘April’: Month of the year; ‘May’: Month of the year; ‘June’: Month of the year; ‘July’: Month of the year; ‘August’: Month of the year; ‘September’: Month of the year; ‘October’: Month of the year; ‘November’: Month of the year; ‘December’: Month of the year;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Month2

‘January’: Month of the year; ‘February’: Month of the year; ‘March’: Month of the year; ‘April’: Month of the year; ‘May’: Month of the year; ‘June’: Month of the year; ‘July’: Month of the r; ‘August’: Month of the year; ‘September’: Month of the year; ‘October’: Month of the year; ‘November’: Month of the year; ‘December’: Month of the year;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reason

Reason for Reboot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reason2

Reason for Reboot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reason3

Reason for Reboot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

Time to Reboot (hh:mm).

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

#### Id

Returns the <code>Id</code> value.

