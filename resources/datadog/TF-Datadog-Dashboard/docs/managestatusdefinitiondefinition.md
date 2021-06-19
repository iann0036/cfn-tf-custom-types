# TF::Datadog::Dashboard ManageStatusDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#colorpreference" title="ColorPreference">ColorPreference</a>" : <i>String</i>,
    "<a href="#displayformat" title="DisplayFormat">DisplayFormat</a>" : <i>String</i>,
    "<a href="#hidezerocounts" title="HideZeroCounts">HideZeroCounts</a>" : <i>Boolean</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="querydefinition.md">QueryDefinition</a>, ... ]</i>,
    "<a href="#showlasttriggered" title="ShowLastTriggered">ShowLastTriggered</a>" : <i>Boolean</i>,
    "<a href="#sort" title="Sort">Sort</a>" : <i>[ <a href="sortdefinition.md">SortDefinition</a>, ... ]</i>,
    "<a href="#summarytype" title="SummaryType">SummaryType</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#colorpreference" title="ColorPreference">ColorPreference</a>: <i>String</i>
<a href="#displayformat" title="DisplayFormat">DisplayFormat</a>: <i>String</i>
<a href="#hidezerocounts" title="HideZeroCounts">HideZeroCounts</a>: <i>Boolean</i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="querydefinition.md">QueryDefinition</a></i>
<a href="#showlasttriggered" title="ShowLastTriggered">ShowLastTriggered</a>: <i>Boolean</i>
<a href="#sort" title="Sort">Sort</a>: <i>
      - <a href="sortdefinition.md">SortDefinition</a></i>
<a href="#summarytype" title="SummaryType">SummaryType</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
</pre>

## Properties

#### ColorPreference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideZeroCounts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: List of <a href="querydefinition.md">QueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowLastTriggered

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sort

_Required_: No

_Type_: List of <a href="sortdefinition.md">SortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SummaryType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleAlign

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

