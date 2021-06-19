# TF::OCI::MeteringComputationUsage

This resource provides the Usage resource in Oracle Cloud Infrastructure Metering Computation service.

Returns usage for the given account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::MeteringComputationUsage",
    "Properties" : {
        "<a href="#compartmentdepth" title="CompartmentDepth">CompartmentDepth</a>" : <i>Double</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
        "<a href="#granularity" title="Granularity">Granularity</a>" : <i>String</i>,
        "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ String, ... ]</i>,
        "<a href="#isaggregatebytime" title="IsAggregateByTime">IsAggregateByTime</a>" : <i>Boolean</i>,
        "<a href="#querytype" title="QueryType">QueryType</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#timeusageended" title="TimeUsageEnded">TimeUsageEnded</a>" : <i>String</i>,
        "<a href="#timeusagestarted" title="TimeUsageStarted">TimeUsageStarted</a>" : <i>String</i>,
        "<a href="#forecast" title="Forecast">Forecast</a>" : <i>[ <a href="forecastdefinition.md">ForecastDefinition</a>, ... ]</i>,
        "<a href="#groupbytag" title="GroupByTag">GroupByTag</a>" : <i>[ <a href="groupbytagdefinition.md">GroupByTagDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::MeteringComputationUsage
Properties:
    <a href="#compartmentdepth" title="CompartmentDepth">CompartmentDepth</a>: <i>Double</i>
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
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentDepth

The compartment depth level.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Granularity

The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

Aggregate the result by. example: `["tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName", "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAggregateByTime

is aggregated by time. true isAggregateByTime will add up all usage/cost over query time period.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryType

The query usage type. COST by default if it is missing Usage - Query the usage data. Cost - Query the cost/billing data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Tenant ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUsageEnded

The usage end time.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUsageStarted

The usage start time.

_Required_: Yes

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

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Items

Returns the <code>Items</code> value.

