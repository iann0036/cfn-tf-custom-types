# Terraform::Google::ComputeHealthCheck

CloudFormation equivalent of google_compute_health_check

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeHealthCheck",
    "Properties" : {
        "<a href="#checkintervalsec" title="CheckIntervalSec">CheckIntervalSec</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#timeoutsec" title="TimeoutSec">TimeoutSec</a>" : <i>Double</i>,
        "<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>" : <i>Double</i>,
        "<a href="#http2healthcheck" title="Http2HealthCheck">Http2HealthCheck</a>" : <i>[ <a href="http2healthcheck.md">Http2HealthCheck</a>, ... ]</i>,
        "<a href="#httphealthcheck" title="HttpHealthCheck">HttpHealthCheck</a>" : <i>[ <a href="httphealthcheck.md">HttpHealthCheck</a>, ... ]</i>,
        "<a href="#httpshealthcheck" title="HttpsHealthCheck">HttpsHealthCheck</a>" : <i>[ <a href="httpshealthcheck.md">HttpsHealthCheck</a>, ... ]</i>,
        "<a href="#sslhealthcheck" title="SslHealthCheck">SslHealthCheck</a>" : <i>[ <a href="sslhealthcheck.md">SslHealthCheck</a>, ... ]</i>,
        "<a href="#tcphealthcheck" title="TcpHealthCheck">TcpHealthCheck</a>" : <i>[ <a href="tcphealthcheck.md">TcpHealthCheck</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeHealthCheck
Properties:
    <a href="#checkintervalsec" title="CheckIntervalSec">CheckIntervalSec</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#timeoutsec" title="TimeoutSec">TimeoutSec</a>: <i>Double</i>
    <a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>: <i>Double</i>
    <a href="#http2healthcheck" title="Http2HealthCheck">Http2HealthCheck</a>: <i>
      - <a href="http2healthcheck.md">Http2HealthCheck</a></i>
    <a href="#httphealthcheck" title="HttpHealthCheck">HttpHealthCheck</a>: <i>
      - <a href="httphealthcheck.md">HttpHealthCheck</a></i>
    <a href="#httpshealthcheck" title="HttpsHealthCheck">HttpsHealthCheck</a>: <i>
      - <a href="httpshealthcheck.md">HttpsHealthCheck</a></i>
    <a href="#sslhealthcheck" title="SslHealthCheck">SslHealthCheck</a>: <i>
      - <a href="sslhealthcheck.md">SslHealthCheck</a></i>
    <a href="#tcphealthcheck" title="TcpHealthCheck">TcpHealthCheck</a>: <i>
      - <a href="tcphealthcheck.md">TcpHealthCheck</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### CheckIntervalSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthyThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnhealthyThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2HealthCheck

_Required_: No

_Type_: List of <a href="http2healthcheck.md">Http2HealthCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHealthCheck

_Required_: No

_Type_: List of <a href="httphealthcheck.md">HttpHealthCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsHealthCheck

_Required_: No

_Type_: List of <a href="httpshealthcheck.md">HttpsHealthCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHealthCheck

_Required_: No

_Type_: List of <a href="sslhealthcheck.md">SslHealthCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpHealthCheck

_Required_: No

_Type_: List of <a href="tcphealthcheck.md">TcpHealthCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

#### SelfLink

Returns the <code>SelfLink</code> value.

#### Type

Returns the <code>Type</code> value.

