# TF::FortiOS::ReportLayout

Report layout configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::ReportLayout",
    "Properties" : {
        "<a href="#cutoffoption" title="CutoffOption">CutoffOption</a>" : <i>String</i>,
        "<a href="#cutofftime" title="CutoffTime">CutoffTime</a>" : <i>String</i>,
        "<a href="#day" title="Day">Day</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#emailrecipients" title="EmailRecipients">EmailRecipients</a>" : <i>String</i>,
        "<a href="#emailsend" title="EmailSend">EmailSend</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#maxpdfreport" title="MaxPdfReport">MaxPdfReport</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>String</i>,
        "<a href="#scheduletype" title="ScheduleType">ScheduleType</a>" : <i>String</i>,
        "<a href="#styletheme" title="StyleTheme">StyleTheme</a>" : <i>String</i>,
        "<a href="#subtitle" title="Subtitle">Subtitle</a>" : <i>String</i>,
        "<a href="#time" title="Time">Time</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#bodyitem" title="BodyItem">BodyItem</a>" : <i>[ <a href="bodyitemdefinition.md">BodyItemDefinition</a>, ... ]</i>,
        "<a href="#page" title="Page">Page</a>" : <i>[ <a href="pagedefinition.md">PageDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::ReportLayout
Properties:
    <a href="#cutoffoption" title="CutoffOption">CutoffOption</a>: <i>String</i>
    <a href="#cutofftime" title="CutoffTime">CutoffTime</a>: <i>String</i>
    <a href="#day" title="Day">Day</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#emailrecipients" title="EmailRecipients">EmailRecipients</a>: <i>String</i>
    <a href="#emailsend" title="EmailSend">EmailSend</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#maxpdfreport" title="MaxPdfReport">MaxPdfReport</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>String</i>
    <a href="#scheduletype" title="ScheduleType">ScheduleType</a>: <i>String</i>
    <a href="#styletheme" title="StyleTheme">StyleTheme</a>: <i>String</i>
    <a href="#subtitle" title="Subtitle">Subtitle</a>: <i>String</i>
    <a href="#time" title="Time">Time</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#bodyitem" title="BodyItem">BodyItem</a>: <i>
      - <a href="bodyitemdefinition.md">BodyItemDefinition</a></i>
    <a href="#page" title="Page">Page</a>: <i>
      - <a href="pagedefinition.md">PageDefinition</a></i>
</pre>

## Properties

#### CutoffOption

Cutoff-option is either run-time or custom. Valid values: `run-time`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CutoffTime

Custom cutoff time to generate report [hh:mm].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Day

Schedule days of week to generate report. Valid values: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailRecipients

Email recipients for generated reports.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailSend

Enable/disable sending emails after reports are generated. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Report format. Valid values: `pdf`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPdfReport

Maximum number of PDF reports to keep at one time (oldest report is overwritten).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Report layout name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Report layout options. Valid values: `include-table-of-content`, `auto-numbering-heading`, `view-chart-as-heading`, `show-html-navbar-before-heading`, `dummy-option`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleType

Report schedule type. Valid values: `demand`, `daily`, `weekly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StyleTheme

Report style theme.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subtitle

Report subtitle.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

Schedule time to generate report [hh:mm].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Report title.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BodyItem

_Required_: No

_Type_: List of <a href="bodyitemdefinition.md">BodyItemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Page

_Required_: No

_Type_: List of <a href="pagedefinition.md">PageDefinition</a>

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

