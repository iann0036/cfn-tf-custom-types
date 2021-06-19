# TF::GoogleBeta::GoogleComputeRegionBackendService

CloudFormation equivalent of google_compute_region_backend_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleComputeRegionBackendService",
    "Properties" : {
        "<a href="#affinitycookiettlsec" title="AffinityCookieTtlSec">AffinityCookieTtlSec</a>" : <i>Double</i>,
        "<a href="#connectiondrainingtimeoutsec" title="ConnectionDrainingTimeoutSec">ConnectionDrainingTimeoutSec</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablecdn" title="EnableCdn">EnableCdn</a>" : <i>Boolean</i>,
        "<a href="#healthchecks" title="HealthChecks">HealthChecks</a>" : <i>[ String, ... ]</i>,
        "<a href="#loadbalancingscheme" title="LoadBalancingScheme">LoadBalancingScheme</a>" : <i>String</i>,
        "<a href="#localitylbpolicy" title="LocalityLbPolicy">LocalityLbPolicy</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#portname" title="PortName">PortName</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>" : <i>String</i>,
        "<a href="#timeoutsec" title="TimeoutSec">TimeoutSec</a>" : <i>Double</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backenddefinition.md">BackendDefinition</a>, ... ]</i>,
        "<a href="#cdnpolicy" title="CdnPolicy">CdnPolicy</a>" : <i>[ <a href="cdnpolicydefinition.md">CdnPolicyDefinition</a>, ... ]</i>,
        "<a href="#circuitbreakers" title="CircuitBreakers">CircuitBreakers</a>" : <i>[ <a href="circuitbreakersdefinition.md">CircuitBreakersDefinition</a>, ... ]</i>,
        "<a href="#consistenthash" title="ConsistentHash">ConsistentHash</a>" : <i>[ <a href="consistenthashdefinition.md">ConsistentHashDefinition</a>, ... ]</i>,
        "<a href="#failoverpolicy" title="FailoverPolicy">FailoverPolicy</a>" : <i>[ <a href="failoverpolicydefinition.md">FailoverPolicyDefinition</a>, ... ]</i>,
        "<a href="#logconfig" title="LogConfig">LogConfig</a>" : <i>[ <a href="logconfigdefinition.md">LogConfigDefinition</a>, ... ]</i>,
        "<a href="#outlierdetection" title="OutlierDetection">OutlierDetection</a>" : <i>[ <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleComputeRegionBackendService
Properties:
    <a href="#affinitycookiettlsec" title="AffinityCookieTtlSec">AffinityCookieTtlSec</a>: <i>Double</i>
    <a href="#connectiondrainingtimeoutsec" title="ConnectionDrainingTimeoutSec">ConnectionDrainingTimeoutSec</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablecdn" title="EnableCdn">EnableCdn</a>: <i>Boolean</i>
    <a href="#healthchecks" title="HealthChecks">HealthChecks</a>: <i>
      - String</i>
    <a href="#loadbalancingscheme" title="LoadBalancingScheme">LoadBalancingScheme</a>: <i>String</i>
    <a href="#localitylbpolicy" title="LocalityLbPolicy">LocalityLbPolicy</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#portname" title="PortName">PortName</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>: <i>String</i>
    <a href="#timeoutsec" title="TimeoutSec">TimeoutSec</a>: <i>Double</i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backenddefinition.md">BackendDefinition</a></i>
    <a href="#cdnpolicy" title="CdnPolicy">CdnPolicy</a>: <i>
      - <a href="cdnpolicydefinition.md">CdnPolicyDefinition</a></i>
    <a href="#circuitbreakers" title="CircuitBreakers">CircuitBreakers</a>: <i>
      - <a href="circuitbreakersdefinition.md">CircuitBreakersDefinition</a></i>
    <a href="#consistenthash" title="ConsistentHash">ConsistentHash</a>: <i>
      - <a href="consistenthashdefinition.md">ConsistentHashDefinition</a></i>
    <a href="#failoverpolicy" title="FailoverPolicy">FailoverPolicy</a>: <i>
      - <a href="failoverpolicydefinition.md">FailoverPolicyDefinition</a></i>
    <a href="#logconfig" title="LogConfig">LogConfig</a>: <i>
      - <a href="logconfigdefinition.md">LogConfigDefinition</a></i>
    <a href="#outlierdetection" title="OutlierDetection">OutlierDetection</a>: <i>
      - <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AffinityCookieTtlSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDrainingTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCdn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthChecks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingScheme

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalityLbPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of <a href="backenddefinition.md">BackendDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnPolicy

_Required_: No

_Type_: List of <a href="cdnpolicydefinition.md">CdnPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CircuitBreakers

_Required_: No

_Type_: List of <a href="circuitbreakersdefinition.md">CircuitBreakersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistentHash

_Required_: No

_Type_: List of <a href="consistenthashdefinition.md">ConsistentHashDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverPolicy

_Required_: No

_Type_: List of <a href="failoverpolicydefinition.md">FailoverPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfig

_Required_: No

_Type_: List of <a href="logconfigdefinition.md">LogConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutlierDetection

_Required_: No

_Type_: List of <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a>

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

#### CreationTimestamp

Returns the <code>CreationTimestamp</code> value.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### Id

Returns the <code>Id</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

