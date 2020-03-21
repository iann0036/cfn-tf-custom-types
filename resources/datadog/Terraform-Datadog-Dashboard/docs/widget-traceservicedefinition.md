# Terraform::Datadog::Dashboard Widget TraceServiceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayformat" title="DisplayFormat">DisplayFormat</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>String</i>,
    "<a href="#service" title="Service">Service</a>" : <i>String</i>,
    "<a href="#showbreakdown" title="ShowBreakdown">ShowBreakdown</a>" : <i>Boolean</i>,
    "<a href="#showdistribution" title="ShowDistribution">ShowDistribution</a>" : <i>Boolean</i>,
    "<a href="#showerrors" title="ShowErrors">ShowErrors</a>" : <i>Boolean</i>,
    "<a href="#showhits" title="ShowHits">ShowHits</a>" : <i>Boolean</i>,
    "<a href="#showlatency" title="ShowLatency">ShowLatency</a>" : <i>Boolean</i>,
    "<a href="#showresourcelist" title="ShowResourceList">ShowResourceList</a>" : <i>Boolean</i>,
    "<a href="#sizeformat" title="SizeFormat">SizeFormat</a>" : <i>String</i>,
    "<a href="#spanname" title="SpanName">SpanName</a>" : <i>String</i>,
    "<a href="#time" title="Time">Time</a>" : <i>[ <a href="widget-traceservicedefinition-time.md">Time</a>, ... ]</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#displayformat" title="DisplayFormat">DisplayFormat</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>String</i>
<a href="#service" title="Service">Service</a>: <i>String</i>
<a href="#showbreakdown" title="ShowBreakdown">ShowBreakdown</a>: <i>Boolean</i>
<a href="#showdistribution" title="ShowDistribution">ShowDistribution</a>: <i>Boolean</i>
<a href="#showerrors" title="ShowErrors">ShowErrors</a>: <i>Boolean</i>
<a href="#showhits" title="ShowHits">ShowHits</a>: <i>Boolean</i>
<a href="#showlatency" title="ShowLatency">ShowLatency</a>: <i>Boolean</i>
<a href="#showresourcelist" title="ShowResourceList">ShowResourceList</a>: <i>Boolean</i>
<a href="#sizeformat" title="SizeFormat">SizeFormat</a>: <i>String</i>
<a href="#spanname" title="SpanName">SpanName</a>: <i>String</i>
<a href="#time" title="Time">Time</a>: <i>
      - <a href="widget-traceservicedefinition-time.md">Time</a></i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
</pre>

## Properties

#### DisplayFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowBreakdown

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowDistribution

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowErrors

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowHits

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowLatency

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowResourceList

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpanName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

_Required_: No

_Type_: List of <a href="widget-traceservicedefinition-time.md">Time</a>

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

