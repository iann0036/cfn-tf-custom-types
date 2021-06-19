# TF::FortiOS::WebfilterProfile FiltersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#category" title="Category">Category</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#log" title="Log">Log</a>" : <i>String</i>,
    "<a href="#overridereplacemsg" title="OverrideReplacemsg">OverrideReplacemsg</a>" : <i>String</i>,
    "<a href="#warnduration" title="WarnDuration">WarnDuration</a>" : <i>String</i>,
    "<a href="#warningdurationtype" title="WarningDurationType">WarningDurationType</a>" : <i>String</i>,
    "<a href="#warningprompt" title="WarningPrompt">WarningPrompt</a>" : <i>String</i>,
    "<a href="#authusrgrp" title="AuthUsrGrp">AuthUsrGrp</a>" : <i>[ <a href="authusrgrpdefinition.md">AuthUsrGrpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#category" title="Category">Category</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#log" title="Log">Log</a>: <i>String</i>
<a href="#overridereplacemsg" title="OverrideReplacemsg">OverrideReplacemsg</a>: <i>String</i>
<a href="#warnduration" title="WarnDuration">WarnDuration</a>: <i>String</i>
<a href="#warningdurationtype" title="WarningDurationType">WarningDurationType</a>: <i>String</i>
<a href="#warningprompt" title="WarningPrompt">WarningPrompt</a>: <i>String</i>
<a href="#authusrgrp" title="AuthUsrGrp">AuthUsrGrp</a>: <i>
      - <a href="authusrgrpdefinition.md">AuthUsrGrpDefinition</a></i>
</pre>

## Properties

#### Action

Action to take for matches. Valid values: `block`, `authenticate`, `monitor`, `warning`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

Categories and groups the filter examines.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

Enable/disable logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideReplacemsg

Override replacement message.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarnDuration

Duration of warnings.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarningDurationType

Re-display warning after closing browser or after a timeout. Valid values: `session`, `timeout`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarningPrompt

Warning prompts in each category or each domain. Valid values: `per-domain`, `per-category`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthUsrGrp

_Required_: No

_Type_: List of <a href="authusrgrpdefinition.md">AuthUsrGrpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

