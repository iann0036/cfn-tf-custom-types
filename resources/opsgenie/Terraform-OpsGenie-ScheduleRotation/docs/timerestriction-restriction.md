# Terraform::OpsGenie::ScheduleRotation TimeRestriction Restriction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endhour" title="EndHour">EndHour</a>" : <i>Double</i>,
    "<a href="#endmin" title="EndMin">EndMin</a>" : <i>Double</i>,
    "<a href="#starthour" title="StartHour">StartHour</a>" : <i>Double</i>,
    "<a href="#startmin" title="StartMin">StartMin</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#endhour" title="EndHour">EndHour</a>: <i>Double</i>
<a href="#endmin" title="EndMin">EndMin</a>: <i>Double</i>
<a href="#starthour" title="StartHour">StartHour</a>: <i>Double</i>
<a href="#startmin" title="StartMin">StartMin</a>: <i>Double</i>
</pre>

## Properties

#### EndHour

Value of the hour that frame will end.
* `end_min` - (Required) Value of the minute that frame will end. Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndMin

Value of the minute that frame will end. Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartHour

Value of the hour that frame will start
* `start_min` - (Required) Value of the minute that frame will start. Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically.
* `end_hour` - (Required) Value of the hour that frame will end.
* `end_min` - (Required) Value of the minute that frame will end. Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartMin

Value of the minute that frame will start. Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically.
* `end_hour` - (Required) Value of the hour that frame will end.
* `end_min` - (Required) Value of the minute that frame will end. Minutes may take 0 or 30 as value. Otherwise they will be converted to nearest 0 or 30 automatically.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

