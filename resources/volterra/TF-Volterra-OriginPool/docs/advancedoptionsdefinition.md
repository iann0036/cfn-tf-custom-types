# TF::Volterra::OriginPool AdvancedOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>" : <i>Double</i>,
    "<a href="#disablecircuitbreaker" title="DisableCircuitBreaker">DisableCircuitBreaker</a>" : <i>Boolean</i>,
    "<a href="#disableoutlierdetection" title="DisableOutlierDetection">DisableOutlierDetection</a>" : <i>Boolean</i>,
    "<a href="#disablesubsets" title="DisableSubsets">DisableSubsets</a>" : <i>Boolean</i>,
    "<a href="#httpidletimeout" title="HttpIdleTimeout">HttpIdleTimeout</a>" : <i>Double</i>,
    "<a href="#nopanicthreshold" title="NoPanicThreshold">NoPanicThreshold</a>" : <i>Boolean</i>,
    "<a href="#panicthreshold" title="PanicThreshold">PanicThreshold</a>" : <i>Double</i>,
    "<a href="#circuitbreaker" title="CircuitBreaker">CircuitBreaker</a>" : <i>[ <a href="circuitbreakerdefinition.md">CircuitBreakerDefinition</a>, ... ]</i>,
    "<a href="#enablesubsets" title="EnableSubsets">EnableSubsets</a>" : <i>[ <a href="enablesubsetsdefinition.md">EnableSubsetsDefinition</a>, ... ]</i>,
    "<a href="#http2options" title="Http2Options">Http2Options</a>" : <i>[ <a href="http2optionsdefinition.md">Http2OptionsDefinition</a>, ... ]</i>,
    "<a href="#outlierdetection" title="OutlierDetection">OutlierDetection</a>" : <i>[ <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>: <i>Double</i>
<a href="#disablecircuitbreaker" title="DisableCircuitBreaker">DisableCircuitBreaker</a>: <i>Boolean</i>
<a href="#disableoutlierdetection" title="DisableOutlierDetection">DisableOutlierDetection</a>: <i>Boolean</i>
<a href="#disablesubsets" title="DisableSubsets">DisableSubsets</a>: <i>Boolean</i>
<a href="#httpidletimeout" title="HttpIdleTimeout">HttpIdleTimeout</a>: <i>Double</i>
<a href="#nopanicthreshold" title="NoPanicThreshold">NoPanicThreshold</a>: <i>Boolean</i>
<a href="#panicthreshold" title="PanicThreshold">PanicThreshold</a>: <i>Double</i>
<a href="#circuitbreaker" title="CircuitBreaker">CircuitBreaker</a>: <i>
      - <a href="circuitbreakerdefinition.md">CircuitBreakerDefinition</a></i>
<a href="#enablesubsets" title="EnableSubsets">EnableSubsets</a>: <i>
      - <a href="enablesubsetsdefinition.md">EnableSubsetsDefinition</a></i>
<a href="#http2options" title="Http2Options">Http2Options</a>: <i>
      - <a href="http2optionsdefinition.md">Http2OptionsDefinition</a></i>
<a href="#outlierdetection" title="OutlierDetection">OutlierDetection</a>: <i>
      - <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a></i>
</pre>

## Properties

#### ConnectionTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableCircuitBreaker

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableOutlierDetection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSubsets

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpIdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoPanicThreshold

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanicThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CircuitBreaker

_Required_: No

_Type_: List of <a href="circuitbreakerdefinition.md">CircuitBreakerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSubsets

_Required_: No

_Type_: List of <a href="enablesubsetsdefinition.md">EnableSubsetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Options

_Required_: No

_Type_: List of <a href="http2optionsdefinition.md">Http2OptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutlierDetection

_Required_: No

_Type_: List of <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

