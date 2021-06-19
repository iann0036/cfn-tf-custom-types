# TF::Gitlab::ProjectFreezePeriod

This resource allows you to create and manage freeze periods. For further information on freeze periods, consult the [gitlab documentation](https://docs.gitlab.com/ee/api/freeze_periods.html#create-a-freeze-period).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::ProjectFreezePeriod",
    "Properties" : {
        "<a href="#crontimezone" title="CronTimezone">CronTimezone</a>" : <i>String</i>,
        "<a href="#freezeend" title="FreezeEnd">FreezeEnd</a>" : <i>String</i>,
        "<a href="#freezestart" title="FreezeStart">FreezeStart</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::ProjectFreezePeriod
Properties:
    <a href="#crontimezone" title="CronTimezone">CronTimezone</a>: <i>String</i>
    <a href="#freezeend" title="FreezeEnd">FreezeEnd</a>: <i>String</i>
    <a href="#freezestart" title="FreezeStart">FreezeStart</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
</pre>

## Properties

#### CronTimezone

The timezone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreezeEnd

End of the Freeze Period in cron format (e.g. `0 2 * * *`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreezeStart

Start of the Freeze Period in cron format (e.g. `0 1 * * *`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The id of the project to add the schedule to.

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

