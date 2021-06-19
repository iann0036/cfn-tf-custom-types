# TF::AzureRM::SpringCloudService TraceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instrumentationkey" title="InstrumentationKey">InstrumentationKey</a>" : <i>String</i>,
    "<a href="#samplerate" title="SampleRate">SampleRate</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#instrumentationkey" title="InstrumentationKey">InstrumentationKey</a>: <i>String</i>
<a href="#samplerate" title="SampleRate">SampleRate</a>: <i>Double</i>
</pre>

## Properties

#### InstrumentationKey

The Instrumentation Key used for Application Insights.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleRate

The sampling rate of Application Insights Agent. Must be between `0.0` and `100.0`. Defaults to `10.0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

