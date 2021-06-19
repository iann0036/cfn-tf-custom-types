# TF::SumoLogic::Dashboard QueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metricsquerymode" title="MetricsQueryMode">MetricsQueryMode</a>" : <i>String</i>,
    "<a href="#querykey" title="QueryKey">QueryKey</a>" : <i>String</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>String</i>,
    "<a href="#querytype" title="QueryType">QueryType</a>" : <i>String</i>,
    "<a href="#metricsquerydata" title="MetricsQueryData">MetricsQueryData</a>" : <i>[ <a href="metricsquerydatadefinition.md">MetricsQueryDataDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metricsquerymode" title="MetricsQueryMode">MetricsQueryMode</a>: <i>String</i>
<a href="#querykey" title="QueryKey">QueryKey</a>: <i>String</i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>String</i>
<a href="#querytype" title="QueryType">QueryType</a>: <i>String</i>
<a href="#metricsquerydata" title="MetricsQueryData">MetricsQueryData</a>: <i>
      - <a href="metricsquerydatadefinition.md">MetricsQueryDataDefinition</a></i>
</pre>

## Properties

#### MetricsQueryMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricsQueryData

_Required_: No

_Type_: List of <a href="metricsquerydatadefinition.md">MetricsQueryDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

