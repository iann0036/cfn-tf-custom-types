# TF::Google::MonitoringSlo

A Service-Level Objective (SLO) describes the level of desired good
service. It consists of a service-level indicator (SLI), a performance
goal, and a period over which the objective is to be evaluated against
that goal. The SLO can use SLIs defined in a number of different manners.
Typical SLOs might include "99% of requests in each rolling week have
latency below 200 milliseconds" or "99.5% of requests in each calendar
month return successfully."


To get more information about Slo, see:

* [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives)
* How-to Guides
    * [Service Monitoring](https://cloud.google.com/monitoring/service-monitoring)
    * [Monitoring API Documentation](https://cloud.google.com/monitoring/api/v3/)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_w...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::MonitoringSlo",
    "Properties" : {
        "<a href="#calendarperiod" title="CalendarPeriod">CalendarPeriod</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#goal" title="Goal">Goal</a>" : <i>Double</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#rollingperioddays" title="RollingPeriodDays">RollingPeriodDays</a>" : <i>Double</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#sloid" title="SloId">SloId</a>" : <i>String</i>,
        "<a href="#basicsli" title="BasicSli">BasicSli</a>" : <i>[ <a href="basicslidefinition.md">BasicSliDefinition</a>, ... ]</i>,
        "<a href="#requestbasedsli" title="RequestBasedSli">RequestBasedSli</a>" : <i>[ <a href="requestbasedslidefinition.md">RequestBasedSliDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#windowsbasedsli" title="WindowsBasedSli">WindowsBasedSli</a>" : <i>[ <a href="windowsbasedslidefinition.md">WindowsBasedSliDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::MonitoringSlo
Properties:
    <a href="#calendarperiod" title="CalendarPeriod">CalendarPeriod</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#goal" title="Goal">Goal</a>: <i>Double</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#rollingperioddays" title="RollingPeriodDays">RollingPeriodDays</a>: <i>Double</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#sloid" title="SloId">SloId</a>: <i>String</i>
    <a href="#basicsli" title="BasicSli">BasicSli</a>: <i>
      - <a href="basicslidefinition.md">BasicSliDefinition</a></i>
    <a href="#requestbasedsli" title="RequestBasedSli">RequestBasedSli</a>: <i>
      - <a href="requestbasedslidefinition.md">RequestBasedSliDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#windowsbasedsli" title="WindowsBasedSli">WindowsBasedSli</a>: <i>
      - <a href="windowsbasedslidefinition.md">WindowsBasedSliDefinition</a></i>
</pre>

## Properties

#### CalendarPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Goal

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollingPeriodDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SloId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicSli

_Required_: No

_Type_: List of <a href="basicslidefinition.md">BasicSliDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBasedSli

_Required_: No

_Type_: List of <a href="requestbasedslidefinition.md">RequestBasedSliDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsBasedSli

_Required_: No

_Type_: List of <a href="windowsbasedslidefinition.md">WindowsBasedSliDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

