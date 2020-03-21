# Terraform::AzureRM::StreamAnalyticsJob

Manages a Stream Analytics Job.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::StreamAnalyticsJob",
    "Properties" : {
        "<a href="#compatibilitylevel" title="CompatibilityLevel">CompatibilityLevel</a>" : <i>String</i>,
        "<a href="#datalocale" title="DataLocale">DataLocale</a>" : <i>String</i>,
        "<a href="#eventslatearrivalmaxdelayinseconds" title="EventsLateArrivalMaxDelayInSeconds">EventsLateArrivalMaxDelayInSeconds</a>" : <i>Double</i>,
        "<a href="#eventsoutofordermaxdelayinseconds" title="EventsOutOfOrderMaxDelayInSeconds">EventsOutOfOrderMaxDelayInSeconds</a>" : <i>Double</i>,
        "<a href="#eventsoutoforderpolicy" title="EventsOutOfOrderPolicy">EventsOutOfOrderPolicy</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outputerrorpolicy" title="OutputErrorPolicy">OutputErrorPolicy</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#streamingunits" title="StreamingUnits">StreamingUnits</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#transformationquery" title="TransformationQuery">TransformationQuery</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::StreamAnalyticsJob
Properties:
    <a href="#compatibilitylevel" title="CompatibilityLevel">CompatibilityLevel</a>: <i>String</i>
    <a href="#datalocale" title="DataLocale">DataLocale</a>: <i>String</i>
    <a href="#eventslatearrivalmaxdelayinseconds" title="EventsLateArrivalMaxDelayInSeconds">EventsLateArrivalMaxDelayInSeconds</a>: <i>Double</i>
    <a href="#eventsoutofordermaxdelayinseconds" title="EventsOutOfOrderMaxDelayInSeconds">EventsOutOfOrderMaxDelayInSeconds</a>: <i>Double</i>
    <a href="#eventsoutoforderpolicy" title="EventsOutOfOrderPolicy">EventsOutOfOrderPolicy</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outputerrorpolicy" title="OutputErrorPolicy">OutputErrorPolicy</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#streamingunits" title="StreamingUnits">StreamingUnits</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#transformationquery" title="TransformationQuery">TransformationQuery</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CompatibilityLevel

Specifies the compatibility level for this job - which controls certain runtime behaviors of the streaming job. Possible values are `1.0` and `1.1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataLocale

Specifies the Data Locale of the Job, which [should be a supported .NET Culture](https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventsLateArrivalMaxDelayInSeconds

Specifies the maximum tolerable delay in seconds where events arriving late could be included. Supported range is `-1` (indefinite) to `1814399` (20d 23h 59m 59s).  Default is `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventsOutOfOrderMaxDelayInSeconds

Specifies the maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. Supported range is `0` to `599` (9m 59s). Default is `5`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventsOutOfOrderPolicy

Specifies the policy which should be applied to events which arrive out of order in the input event stream. Possible values are `Adjust` and `Drop`.  Default is `Adjust`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The Azure Region in which the Resource Group exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Stream Analytics Job. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputErrorPolicy

Specifies the policy which should be applied to events which arrive at the output and cannot be written to the external storage due to being malformed (such as missing column values, column values of wrong type or size). Possible values are `Drop` and `Stop`.  Default is `Drop`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group where the Stream Analytics Job should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamingUnits

Specifies the number of streaming units that the streaming job uses. Supported values are `1`, `3`, `6` and multiples of `6` up to `120`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags assigned to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransformationQuery

Specifies the query that will be run in the streaming job, [written in Stream Analytics Query Language (SAQL)](https://msdn.microsoft.com/library/azure/dn834998).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### JobId

Returns the <code>JobId</code> value.

