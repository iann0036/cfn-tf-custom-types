# TF::Volterra::Cluster

CloudFormation equivalent of volterra_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::Cluster",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>" : <i>Double</i>,
        "<a href="#defaultsubset" title="DefaultSubset">DefaultSubset</a>" : <i>[ <a href="defaultsubsetdefinition.md">DefaultSubsetDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#endpointselection" title="EndpointSelection">EndpointSelection</a>" : <i>String</i>,
        "<a href="#fallbackpolicy" title="FallbackPolicy">FallbackPolicy</a>" : <i>String</i>,
        "<a href="#httpidletimeout" title="HttpIdleTimeout">HttpIdleTimeout</a>" : <i>Double</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#loadbalanceralgorithm" title="LoadbalancerAlgorithm">LoadbalancerAlgorithm</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#nopanicthreshold" title="NoPanicThreshold">NoPanicThreshold</a>" : <i>Boolean</i>,
        "<a href="#panicthreshold" title="PanicThreshold">PanicThreshold</a>" : <i>Double</i>,
        "<a href="#circuitbreaker" title="CircuitBreaker">CircuitBreaker</a>" : <i>[ <a href="circuitbreakerdefinition.md">CircuitBreakerDefinition</a>, ... ]</i>,
        "<a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>" : <i>[ <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>, ... ]</i>,
        "<a href="#endpoints" title="Endpoints">Endpoints</a>" : <i>[ <a href="endpointsdefinition.md">EndpointsDefinition</a>, ... ]</i>,
        "<a href="#healthchecks" title="HealthChecks">HealthChecks</a>" : <i>[ <a href="healthchecksdefinition.md">HealthChecksDefinition</a>, ... ]</i>,
        "<a href="#http2options" title="Http2Options">Http2Options</a>" : <i>[ <a href="http2optionsdefinition.md">Http2OptionsDefinition</a>, ... ]</i>,
        "<a href="#outlierdetection" title="OutlierDetection">OutlierDetection</a>" : <i>[ <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a>, ... ]</i>,
        "<a href="#tlsparameters" title="TlsParameters">TlsParameters</a>" : <i>[ <a href="tlsparametersdefinition.md">TlsParametersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::Cluster
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>: <i>Double</i>
    <a href="#defaultsubset" title="DefaultSubset">DefaultSubset</a>: <i>
      - <a href="defaultsubsetdefinition.md">DefaultSubsetDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#endpointselection" title="EndpointSelection">EndpointSelection</a>: <i>String</i>
    <a href="#fallbackpolicy" title="FallbackPolicy">FallbackPolicy</a>: <i>String</i>
    <a href="#httpidletimeout" title="HttpIdleTimeout">HttpIdleTimeout</a>: <i>Double</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#loadbalanceralgorithm" title="LoadbalancerAlgorithm">LoadbalancerAlgorithm</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#nopanicthreshold" title="NoPanicThreshold">NoPanicThreshold</a>: <i>Boolean</i>
    <a href="#panicthreshold" title="PanicThreshold">PanicThreshold</a>: <i>Double</i>
    <a href="#circuitbreaker" title="CircuitBreaker">CircuitBreaker</a>: <i>
      - <a href="circuitbreakerdefinition.md">CircuitBreakerDefinition</a></i>
    <a href="#endpointsubsets" title="EndpointSubsets">EndpointSubsets</a>: <i>
      - <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a></i>
    <a href="#endpoints" title="Endpoints">Endpoints</a>: <i>
      - <a href="endpointsdefinition.md">EndpointsDefinition</a></i>
    <a href="#healthchecks" title="HealthChecks">HealthChecks</a>: <i>
      - <a href="healthchecksdefinition.md">HealthChecksDefinition</a></i>
    <a href="#http2options" title="Http2Options">Http2Options</a>: <i>
      - <a href="http2optionsdefinition.md">Http2OptionsDefinition</a></i>
    <a href="#outlierdetection" title="OutlierDetection">OutlierDetection</a>: <i>
      - <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a></i>
    <a href="#tlsparameters" title="TlsParameters">TlsParameters</a>: <i>
      - <a href="tlsparametersdefinition.md">TlsParametersDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSubset

_Required_: No

_Type_: List of <a href="defaultsubsetdefinition.md">DefaultSubsetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointSelection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpIdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadbalancerAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

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

#### EndpointSubsets

_Required_: No

_Type_: List of <a href="endpointsubsetsdefinition.md">EndpointSubsetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoints

_Required_: No

_Type_: List of <a href="endpointsdefinition.md">EndpointsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthChecks

_Required_: No

_Type_: List of <a href="healthchecksdefinition.md">HealthChecksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Options

_Required_: No

_Type_: List of <a href="http2optionsdefinition.md">Http2OptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutlierDetection

_Required_: No

_Type_: List of <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsParameters

_Required_: No

_Type_: List of <a href="tlsparametersdefinition.md">TlsParametersDefinition</a>

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

