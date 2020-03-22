# Terraform::Google::ComputeRegionHealthCheck

Health Checks determine whether instances are responsive and able to do work.
They are an important part of a comprehensive load balancing configuration,
as they enable monitoring instances behind load balancers.

Health Checks poll instances at a specified interval. Instances that
do not respond successfully to some number of probes in a row are marked
as unhealthy. No new connections are sent to unhealthy instances,
though existing connections will continue. The health check will
continue to poll unhealthy instances. If an instance later responds
successfully to some number of consecutive probes, it is marked
healthy again and can receive new connections.


To get more information about RegionHealthCheck, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/regionHealthChecks)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/load-balancing/docs/health-checks)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=region_health_check_tcp&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeRegionHealthCheck",
    "Properties" : {
        "<a href="#checkintervalsec" title="CheckIntervalSec">CheckIntervalSec</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
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
Type: Terraform::Google::ComputeRegionHealthCheck
Properties:
    <a href="#checkintervalsec" title="CheckIntervalSec">CheckIntervalSec</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
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

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

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

#### Id

Returns the <code>Id</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### Type

Returns the <code>Type</code> value.

