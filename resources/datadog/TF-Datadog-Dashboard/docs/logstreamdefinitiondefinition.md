# TF::Datadog::Dashboard LogStreamDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#columns" title="Columns">Columns</a>" : <i>[ String, ... ]</i>,
    "<a href="#indexes" title="Indexes">Indexes</a>" : <i>[ String, ... ]</i>,
    "<a href="#livespan" title="LiveSpan">LiveSpan</a>" : <i>String</i>,
    "<a href="#messagedisplay" title="MessageDisplay">MessageDisplay</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="querydefinition.md">QueryDefinition</a>, ... ]</i>,
    "<a href="#showdatecolumn" title="ShowDateColumn">ShowDateColumn</a>" : <i>Boolean</i>,
    "<a href="#showmessagecolumn" title="ShowMessageColumn">ShowMessageColumn</a>" : <i>Boolean</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>,
    "<a href="#sort" title="Sort">Sort</a>" : <i>[ <a href="sortdefinition.md">SortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#columns" title="Columns">Columns</a>: <i>
      - String</i>
<a href="#indexes" title="Indexes">Indexes</a>: <i>
      - String</i>
<a href="#livespan" title="LiveSpan">LiveSpan</a>: <i>String</i>
<a href="#messagedisplay" title="MessageDisplay">MessageDisplay</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="querydefinition.md">QueryDefinition</a></i>
<a href="#showdatecolumn" title="ShowDateColumn">ShowDateColumn</a>: <i>Boolean</i>
<a href="#showmessagecolumn" title="ShowMessageColumn">ShowMessageColumn</a>: <i>Boolean</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
<a href="#sort" title="Sort">Sort</a>: <i>
      - <a href="sortdefinition.md">SortDefinition</a></i>
</pre>

## Properties

#### Columns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Indexes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LiveSpan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageDisplay

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No

_Type_: List of <a href="querydefinition.md">QueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowDateColumn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowMessageColumn

_Required_: No

_Type_: Boolean

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

#### Sort

_Required_: No

_Type_: List of <a href="sortdefinition.md">SortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

