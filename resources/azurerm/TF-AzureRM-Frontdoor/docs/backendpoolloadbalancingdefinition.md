# TF::AzureRM::Frontdoor BackendPoolLoadBalancingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionallatencymilliseconds" title="AdditionalLatencyMilliseconds">AdditionalLatencyMilliseconds</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#samplesize" title="SampleSize">SampleSize</a>" : <i>Double</i>,
    "<a href="#successfulsamplesrequired" title="SuccessfulSamplesRequired">SuccessfulSamplesRequired</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#additionallatencymilliseconds" title="AdditionalLatencyMilliseconds">AdditionalLatencyMilliseconds</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#samplesize" title="SampleSize">SampleSize</a>: <i>Double</i>
<a href="#successfulsamplesrequired" title="SuccessfulSamplesRequired">SuccessfulSamplesRequired</a>: <i>Double</i>
</pre>

## Properties

#### AdditionalLatencyMilliseconds

The additional latency in milliseconds for probes to fall into the lowest latency bucket. Defaults to `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Load Balancer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleSize

The number of samples to consider for load balancing decisions. Defaults to `4`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessfulSamplesRequired

The number of samples within the sample period that must succeed. Defaults to `2`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

