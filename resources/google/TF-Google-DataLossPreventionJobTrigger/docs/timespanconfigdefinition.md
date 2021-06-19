# TF::Google::DataLossPreventionJobTrigger TimespanConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableautopopulationoftimespanconfig" title="EnableAutoPopulationOfTimespanConfig">EnableAutoPopulationOfTimespanConfig</a>" : <i>Boolean</i>,
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#timestampfield" title="TimestampField">TimestampField</a>" : <i>[ <a href="timestampfielddefinition.md">TimestampFieldDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableautopopulationoftimespanconfig" title="EnableAutoPopulationOfTimespanConfig">EnableAutoPopulationOfTimespanConfig</a>: <i>Boolean</i>
<a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#timestampfield" title="TimestampField">TimestampField</a>: <i>
      - <a href="timestampfielddefinition.md">TimestampFieldDefinition</a></i>
</pre>

## Properties

#### EnableAutoPopulationOfTimespanConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimestampField

_Required_: No

_Type_: List of <a href="timestampfielddefinition.md">TimestampFieldDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

