# TF::OCI::MeteringComputationQuery ReportQueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#compartmentdepth" title="CompartmentDepth">CompartmentDepth</a>" : <i>Double</i>,
    "<a href="#daterangename" title="DateRangeName">DateRangeName</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#granularity" title="Granularity">Granularity</a>" : <i>String</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ String, ... ]</i>,
    "<a href="#isaggregatebytime" title="IsAggregateByTime">IsAggregateByTime</a>" : <i>Boolean</i>,
    "<a href="#querytype" title="QueryType">QueryType</a>" : <i>String</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
    "<a href="#timeusageended" title="TimeUsageEnded">TimeUsageEnded</a>" : <i>String</i>,
    "<a href="#timeusagestarted" title="TimeUsageStarted">TimeUsageStarted</a>" : <i>String</i>,
    "<a href="#forecast" title="Forecast">Forecast</a>" : <i>[ <a href="forecastdefinition.md">ForecastDefinition</a>, ... ]</i>,
    "<a href="#groupbytag" title="GroupByTag">GroupByTag</a>" : <i>[ <a href="groupbytagdefinition.md">GroupByTagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#compartmentdepth" title="CompartmentDepth">CompartmentDepth</a>: <i>Double</i>
<a href="#daterangename" title="DateRangeName">DateRangeName</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#granularity" title="Granularity">Granularity</a>: <i>String</i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - String</i>
<a href="#isaggregatebytime" title="IsAggregateByTime">IsAggregateByTime</a>: <i>Boolean</i>
<a href="#querytype" title="QueryType">QueryType</a>: <i>String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
<a href="#timeusageended" title="TimeUsageEnded">TimeUsageEnded</a>: <i>String</i>
<a href="#timeusagestarted" title="TimeUsageStarted">TimeUsageStarted</a>: <i>String</i>
<a href="#forecast" title="Forecast">Forecast</a>: <i>
      - <a href="forecastdefinition.md">ForecastDefinition</a></i>
<a href="#groupbytag" title="GroupByTag">GroupByTag</a>: <i>
      - <a href="groupbytagdefinition.md">GroupByTagDefinition</a></i>
</pre>

## Properties

#### CompartmentDepth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateRangeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Granularity

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAggregateByTime

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUsageEnded

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUsageStarted

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forecast

_Required_: No

_Type_: List of <a href="forecastdefinition.md">ForecastDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupByTag

_Required_: No

_Type_: List of <a href="groupbytagdefinition.md">GroupByTagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

