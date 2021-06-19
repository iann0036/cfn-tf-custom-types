# TF::Databricks::SqlQuery ParameterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#date" title="Date">Date</a>" : <i>[ <a href="datedefinition.md">DateDefinition</a>, ... ]</i>,
    "<a href="#daterange" title="DateRange">DateRange</a>" : <i>[ <a href="daterangedefinition.md">DateRangeDefinition</a>, ... ]</i>,
    "<a href="#datetime" title="Datetime">Datetime</a>" : <i>[ <a href="datetimedefinition.md">DatetimeDefinition</a>, ... ]</i>,
    "<a href="#datetimerange" title="DatetimeRange">DatetimeRange</a>" : <i>[ <a href="datetimerangedefinition.md">DatetimeRangeDefinition</a>, ... ]</i>,
    "<a href="#datetimesec" title="Datetimesec">Datetimesec</a>" : <i>[ <a href="datetimesecdefinition.md">DatetimesecDefinition</a>, ... ]</i>,
    "<a href="#datetimesecrange" title="DatetimesecRange">DatetimesecRange</a>" : <i>[ <a href="datetimesecrangedefinition.md">DatetimesecRangeDefinition</a>, ... ]</i>,
    "<a href="#enum" title="Enum">Enum</a>" : <i>[ <a href="enumdefinition.md">EnumDefinition</a>, ... ]</i>,
    "<a href="#number" title="Number">Number</a>" : <i>[ <a href="numberdefinition.md">NumberDefinition</a>, ... ]</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="querydefinition.md">QueryDefinition</a>, ... ]</i>,
    "<a href="#text" title="Text">Text</a>" : <i>[ <a href="textdefinition.md">TextDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#date" title="Date">Date</a>: <i>
      - <a href="datedefinition.md">DateDefinition</a></i>
<a href="#daterange" title="DateRange">DateRange</a>: <i>
      - <a href="daterangedefinition.md">DateRangeDefinition</a></i>
<a href="#datetime" title="Datetime">Datetime</a>: <i>
      - <a href="datetimedefinition.md">DatetimeDefinition</a></i>
<a href="#datetimerange" title="DatetimeRange">DatetimeRange</a>: <i>
      - <a href="datetimerangedefinition.md">DatetimeRangeDefinition</a></i>
<a href="#datetimesec" title="Datetimesec">Datetimesec</a>: <i>
      - <a href="datetimesecdefinition.md">DatetimesecDefinition</a></i>
<a href="#datetimesecrange" title="DatetimesecRange">DatetimesecRange</a>: <i>
      - <a href="datetimesecrangedefinition.md">DatetimesecRangeDefinition</a></i>
<a href="#enum" title="Enum">Enum</a>: <i>
      - <a href="enumdefinition.md">EnumDefinition</a></i>
<a href="#number" title="Number">Number</a>: <i>
      - <a href="numberdefinition.md">NumberDefinition</a></i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="querydefinition.md">QueryDefinition</a></i>
<a href="#text" title="Text">Text</a>: <i>
      - <a href="textdefinition.md">TextDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Date

_Required_: No

_Type_: List of <a href="datedefinition.md">DateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateRange

_Required_: No

_Type_: List of <a href="daterangedefinition.md">DateRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datetime

_Required_: No

_Type_: List of <a href="datetimedefinition.md">DatetimeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatetimeRange

_Required_: No

_Type_: List of <a href="datetimerangedefinition.md">DatetimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datetimesec

_Required_: No

_Type_: List of <a href="datetimesecdefinition.md">DatetimesecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatetimesecRange

_Required_: No

_Type_: List of <a href="datetimesecrangedefinition.md">DatetimesecRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enum

_Required_: No

_Type_: List of <a href="enumdefinition.md">EnumDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Number

_Required_: No

_Type_: List of <a href="numberdefinition.md">NumberDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No

_Type_: List of <a href="querydefinition.md">QueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Text

_Required_: No

_Type_: List of <a href="textdefinition.md">TextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

