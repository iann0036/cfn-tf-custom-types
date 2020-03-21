# Terraform::Datadog::Screenboard Widget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alertid" title="AlertId">AlertId</a>" : <i>Double</i>,
    "<a href="#autorefresh" title="AutoRefresh">AutoRefresh</a>" : <i>Boolean</i>,
    "<a href="#bgcolor" title="Bgcolor">Bgcolor</a>" : <i>String</i>,
    "<a href="#check" title="Check">Check</a>" : <i>String</i>,
    "<a href="#color" title="Color">Color</a>" : <i>String</i>,
    "<a href="#colorpreference" title="ColorPreference">ColorPreference</a>" : <i>String</i>,
    "<a href="#columns" title="Columns">Columns</a>" : <i>String</i>,
    "<a href="#displayformat" title="DisplayFormat">DisplayFormat</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>String</i>,
    "<a href="#eventsize" title="EventSize">EventSize</a>" : <i>String</i>,
    "<a href="#fontsize" title="FontSize">FontSize</a>" : <i>String</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ String, ... ]</i>,
    "<a href="#grouping" title="Grouping">Grouping</a>" : <i>String</i>,
    "<a href="#height" title="Height">Height</a>" : <i>Double</i>,
    "<a href="#hidezerocounts" title="HideZeroCounts">HideZeroCounts</a>" : <i>Boolean</i>,
    "<a href="#html" title="Html">Html</a>" : <i>String</i>,
    "<a href="#layoutversion" title="LayoutVersion">LayoutVersion</a>" : <i>String</i>,
    "<a href="#legend" title="Legend">Legend</a>" : <i>Boolean</i>,
    "<a href="#legendsize" title="LegendSize">LegendSize</a>" : <i>String</i>,
    "<a href="#logset" title="Logset">Logset</a>" : <i>String</i>,
    "<a href="#managestatusshowtitle" title="ManageStatusShowTitle">ManageStatusShowTitle</a>" : <i>Boolean</i>,
    "<a href="#managestatustitlealign" title="ManageStatusTitleAlign">ManageStatusTitleAlign</a>" : <i>String</i>,
    "<a href="#managestatustitlesize" title="ManageStatusTitleSize">ManageStatusTitleSize</a>" : <i>String</i>,
    "<a href="#managestatustitletext" title="ManageStatusTitleText">ManageStatusTitleText</a>" : <i>String</i>,
    "<a href="#margin" title="Margin">Margin</a>" : <i>String</i>,
    "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ &lt;a href=&#34;widget-monitor.md&#34;&gt;Monitor&lt;/a&gt;, ... ]</i>,
    "<a href="#mustshowbreakdown" title="MustShowBreakdown">MustShowBreakdown</a>" : <i>Boolean</i>,
    "<a href="#mustshowdistribution" title="MustShowDistribution">MustShowDistribution</a>" : <i>Boolean</i>,
    "<a href="#mustshowerrors" title="MustShowErrors">MustShowErrors</a>" : <i>Boolean</i>,
    "<a href="#mustshowhits" title="MustShowHits">MustShowHits</a>" : <i>Boolean</i>,
    "<a href="#mustshowlatency" title="MustShowLatency">MustShowLatency</a>" : <i>Boolean</i>,
    "<a href="#mustshowresourcelist" title="MustShowResourceList">MustShowResourceList</a>" : <i>Boolean</i>,
    "<a href="#params" title="Params">Params</a>" : <i>[ &lt;a href=&#34;widget-params.md&#34;&gt;Params&lt;/a&gt;, ... ]</i>,
    "<a href="#precision" title="Precision">Precision</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>String</i>,
    "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
    "<a href="#serviceservice" title="ServiceService">ServiceService</a>" : <i>String</i>,
    "<a href="#showlasttriggered" title="ShowLastTriggered">ShowLastTriggered</a>" : <i>Boolean</i>,
    "<a href="#sizeversion" title="SizeVersion">SizeVersion</a>" : <i>String</i>,
    "<a href="#sizing" title="Sizing">Sizing</a>" : <i>String</i>,
    "<a href="#summarytype" title="SummaryType">SummaryType</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#text" title="Text">Text</a>" : <i>String</i>,
    "<a href="#textalign" title="TextAlign">TextAlign</a>" : <i>String</i>,
    "<a href="#textsize" title="TextSize">TextSize</a>" : <i>String</i>,
    "<a href="#tick" title="Tick">Tick</a>" : <i>Boolean</i>,
    "<a href="#tickedge" title="TickEdge">TickEdge</a>" : <i>String</i>,
    "<a href="#tickpos" title="TickPos">TickPos</a>" : <i>String</i>,
    "<a href="#time" title="Time">Time</a>" : <i>[ &lt;a href=&#34;widget-time.md&#34;&gt;Time&lt;/a&gt;, ... ]</i>,
    "<a href="#timeframes" title="Timeframes">Timeframes</a>" : <i>[ String, ... ]</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#viztype" title="VizType">VizType</a>" : <i>String</i>,
    "<a href="#width" title="Width">Width</a>" : <i>Double</i>,
    "<a href="#x" title="X">X</a>" : <i>Double</i>,
    "<a href="#y" title="Y">Y</a>" : <i>Double</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;widget-rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>,
    "<a href="#tiledef" title="TileDef">TileDef</a>" : <i>[ &lt;a href=&#34;widget-tiledef.md&#34;&gt;TileDef&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alertid" title="AlertId">AlertId</a>: <i>Double</i>
<a href="#autorefresh" title="AutoRefresh">AutoRefresh</a>: <i>Boolean</i>
<a href="#bgcolor" title="Bgcolor">Bgcolor</a>: <i>String</i>
<a href="#check" title="Check">Check</a>: <i>String</i>
<a href="#color" title="Color">Color</a>: <i>String</i>
<a href="#colorpreference" title="ColorPreference">ColorPreference</a>: <i>String</i>
<a href="#columns" title="Columns">Columns</a>: <i>String</i>
<a href="#displayformat" title="DisplayFormat">DisplayFormat</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>String</i>
<a href="#eventsize" title="EventSize">EventSize</a>: <i>String</i>
<a href="#fontsize" title="FontSize">FontSize</a>: <i>String</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - String</i>
<a href="#grouping" title="Grouping">Grouping</a>: <i>String</i>
<a href="#height" title="Height">Height</a>: <i>Double</i>
<a href="#hidezerocounts" title="HideZeroCounts">HideZeroCounts</a>: <i>Boolean</i>
<a href="#html" title="Html">Html</a>: <i>String</i>
<a href="#layoutversion" title="LayoutVersion">LayoutVersion</a>: <i>String</i>
<a href="#legend" title="Legend">Legend</a>: <i>Boolean</i>
<a href="#legendsize" title="LegendSize">LegendSize</a>: <i>String</i>
<a href="#logset" title="Logset">Logset</a>: <i>String</i>
<a href="#managestatusshowtitle" title="ManageStatusShowTitle">ManageStatusShowTitle</a>: <i>Boolean</i>
<a href="#managestatustitlealign" title="ManageStatusTitleAlign">ManageStatusTitleAlign</a>: <i>String</i>
<a href="#managestatustitlesize" title="ManageStatusTitleSize">ManageStatusTitleSize</a>: <i>String</i>
<a href="#managestatustitletext" title="ManageStatusTitleText">ManageStatusTitleText</a>: <i>String</i>
<a href="#margin" title="Margin">Margin</a>: <i>String</i>
<a href="#monitor" title="Monitor">Monitor</a>: <i>
      - &lt;a href=&#34;widget-monitor.md&#34;&gt;Monitor&lt;/a&gt;</i>
<a href="#mustshowbreakdown" title="MustShowBreakdown">MustShowBreakdown</a>: <i>Boolean</i>
<a href="#mustshowdistribution" title="MustShowDistribution">MustShowDistribution</a>: <i>Boolean</i>
<a href="#mustshowerrors" title="MustShowErrors">MustShowErrors</a>: <i>Boolean</i>
<a href="#mustshowhits" title="MustShowHits">MustShowHits</a>: <i>Boolean</i>
<a href="#mustshowlatency" title="MustShowLatency">MustShowLatency</a>: <i>Boolean</i>
<a href="#mustshowresourcelist" title="MustShowResourceList">MustShowResourceList</a>: <i>Boolean</i>
<a href="#params" title="Params">Params</a>: <i>
      - &lt;a href=&#34;widget-params.md&#34;&gt;Params&lt;/a&gt;</i>
<a href="#precision" title="Precision">Precision</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>String</i>
<a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
<a href="#serviceservice" title="ServiceService">ServiceService</a>: <i>String</i>
<a href="#showlasttriggered" title="ShowLastTriggered">ShowLastTriggered</a>: <i>Boolean</i>
<a href="#sizeversion" title="SizeVersion">SizeVersion</a>: <i>String</i>
<a href="#sizing" title="Sizing">Sizing</a>: <i>String</i>
<a href="#summarytype" title="SummaryType">SummaryType</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#text" title="Text">Text</a>: <i>String</i>
<a href="#textalign" title="TextAlign">TextAlign</a>: <i>String</i>
<a href="#textsize" title="TextSize">TextSize</a>: <i>String</i>
<a href="#tick" title="Tick">Tick</a>: <i>Boolean</i>
<a href="#tickedge" title="TickEdge">TickEdge</a>: <i>String</i>
<a href="#tickpos" title="TickPos">TickPos</a>: <i>String</i>
<a href="#time" title="Time">Time</a>: <i>
      - &lt;a href=&#34;widget-time.md&#34;&gt;Time&lt;/a&gt;</i>
<a href="#timeframes" title="Timeframes">Timeframes</a>: <i>
      - String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#viztype" title="VizType">VizType</a>: <i>String</i>
<a href="#width" title="Width">Width</a>: <i>Double</i>
<a href="#x" title="X">X</a>: <i>Double</i>
<a href="#y" title="Y">Y</a>: <i>Double</i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;widget-rule.md&#34;&gt;Rule&lt;/a&gt;</i>
<a href="#tiledef" title="TileDef">TileDef</a>: <i>
      - &lt;a href=&#34;widget-tiledef.md&#34;&gt;TileDef&lt;/a&gt;</i>
</pre>

## Properties

#### AlertId

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRefresh

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bgcolor

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Check

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColorPreference

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Columns

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayFormat

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventSize

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FontSize

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grouping

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Height

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideZeroCounts

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Html

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LayoutVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Legend

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegendSize

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logset

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageStatusShowTitle

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageStatusTitleAlign

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageStatusTitleSize

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageStatusTitleText

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Margin

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No
_Type_: List of &lt;a href=&#34;widget-monitor.md&#34;&gt;Monitor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustShowBreakdown

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustShowDistribution

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustShowErrors

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustShowHits

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustShowLatency

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MustShowResourceList

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Params

_Required_: No
_Type_: List of &lt;a href=&#34;widget-params.md&#34;&gt;Params&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Precision

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceService

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowLastTriggered

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sizing

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SummaryType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Text

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextAlign

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextSize

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tick

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TickEdge

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TickPos

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

_Required_: No
_Type_: List of &lt;a href=&#34;widget-time.md&#34;&gt;Time&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeframes

_Required_: No
_Type_: List of String

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
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VizType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Y

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No
_Type_: List of &lt;a href=&#34;widget-rule.md&#34;&gt;Rule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TileDef

_Required_: No
_Type_: List of &lt;a href=&#34;widget-tiledef.md&#34;&gt;TileDef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

