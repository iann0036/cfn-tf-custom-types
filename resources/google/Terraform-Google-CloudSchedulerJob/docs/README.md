# Terraform::Google::CloudSchedulerJob

A scheduled job that can publish a pubsub message or a http request
every X interval of time, using crontab format string.

To use Cloud Scheduler your project must contain an App Engine app
that is located in one of the supported regions. If your project
does not have an App Engine app, you must create one.


To get more information about Job, see:

* [API documentation](https://cloud.google.com/scheduler/docs/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/scheduler/)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=scheduler_job_pubsub&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::CloudSchedulerJob",
    "Properties" : {
        "<a href="#attemptdeadline" title="AttemptDeadline">AttemptDeadline</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#appenginehttptarget" title="AppEngineHttpTarget">AppEngineHttpTarget</a>" : <i>[ <a href="appenginehttptarget.md">AppEngineHttpTarget</a>, ... ]</i>,
        "<a href="#httptarget" title="HttpTarget">HttpTarget</a>" : <i>[ <a href="httptarget.md">HttpTarget</a>, ... ]</i>,
        "<a href="#pubsubtarget" title="PubsubTarget">PubsubTarget</a>" : <i>[ <a href="pubsubtarget.md">PubsubTarget</a>, ... ]</i>,
        "<a href="#retryconfig" title="RetryConfig">RetryConfig</a>" : <i>[ <a href="retryconfig.md">RetryConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#appenginerouting" title="AppEngineRouting">AppEngineRouting</a>" : <i>[ <a href="appenginerouting.md">AppEngineRouting</a>, ... ]</i>,
        "<a href="#oauthtoken" title="OauthToken">OauthToken</a>" : <i>[ <a href="oauthtoken.md">OauthToken</a>, ... ]</i>,
        "<a href="#oidctoken" title="OidcToken">OidcToken</a>" : <i>[ <a href="oidctoken.md">OidcToken</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::CloudSchedulerJob
Properties:
    <a href="#attemptdeadline" title="AttemptDeadline">AttemptDeadline</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#appenginehttptarget" title="AppEngineHttpTarget">AppEngineHttpTarget</a>: <i>
      - <a href="appenginehttptarget.md">AppEngineHttpTarget</a></i>
    <a href="#httptarget" title="HttpTarget">HttpTarget</a>: <i>
      - <a href="httptarget.md">HttpTarget</a></i>
    <a href="#pubsubtarget" title="PubsubTarget">PubsubTarget</a>: <i>
      - <a href="pubsubtarget.md">PubsubTarget</a></i>
    <a href="#retryconfig" title="RetryConfig">RetryConfig</a>: <i>
      - <a href="retryconfig.md">RetryConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#appenginerouting" title="AppEngineRouting">AppEngineRouting</a>: <i>
      - <a href="appenginerouting.md">AppEngineRouting</a></i>
    <a href="#oauthtoken" title="OauthToken">OauthToken</a>: <i>
      - <a href="oauthtoken.md">OauthToken</a></i>
    <a href="#oidctoken" title="OidcToken">OidcToken</a>: <i>
      - <a href="oidctoken.md">OidcToken</a></i>
</pre>

## Properties

#### AttemptDeadline

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

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

#### Schedule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppEngineHttpTarget

_Required_: No

_Type_: List of <a href="appenginehttptarget.md">AppEngineHttpTarget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpTarget

_Required_: No

_Type_: List of <a href="httptarget.md">HttpTarget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PubsubTarget

_Required_: No

_Type_: List of <a href="pubsubtarget.md">PubsubTarget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryConfig

_Required_: No

_Type_: List of <a href="retryconfig.md">RetryConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppEngineRouting

_Required_: No

_Type_: List of <a href="appenginerouting.md">AppEngineRouting</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthToken

_Required_: No

_Type_: List of <a href="oauthtoken.md">OauthToken</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcToken

_Required_: No

_Type_: List of <a href="oidctoken.md">OidcToken</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

