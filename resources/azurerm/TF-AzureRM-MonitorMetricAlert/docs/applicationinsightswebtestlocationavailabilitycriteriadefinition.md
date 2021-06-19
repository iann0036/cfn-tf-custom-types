# TF::AzureRM::MonitorMetricAlert ApplicationInsightsWebTestLocationAvailabilityCriteriaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#componentid" title="ComponentId">ComponentId</a>" : <i>String</i>,
    "<a href="#failedlocationcount" title="FailedLocationCount">FailedLocationCount</a>" : <i>Double</i>,
    "<a href="#webtestid" title="WebTestId">WebTestId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#componentid" title="ComponentId">ComponentId</a>: <i>String</i>
<a href="#failedlocationcount" title="FailedLocationCount">FailedLocationCount</a>: <i>Double</i>
<a href="#webtestid" title="WebTestId">WebTestId</a>: <i>String</i>
</pre>

## Properties

#### ComponentId

The ID of the Application Insights Resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedLocationCount

The number of failed locations.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebTestId

The ID of the Application Insights Web Test.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

