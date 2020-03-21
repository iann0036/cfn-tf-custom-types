# Terraform::Google::CloudSchedulerJob

CloudFormation equivalent of google_cloud_scheduler_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::CloudSchedulerJob",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#attemptdeadline" title="AttemptDeadline">AttemptDeadline</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#appenginehttptarget" title="AppEngineHttpTarget">AppEngineHttpTarget</a>" : <i>[ &lt;a href=&#34;appenginehttptarget.md&#34;&gt;AppEngineHttpTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#httptarget" title="HttpTarget">HttpTarget</a>" : <i>[ &lt;a href=&#34;httptarget.md&#34;&gt;HttpTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#pubsubtarget" title="PubsubTarget">PubsubTarget</a>" : <i>[ &lt;a href=&#34;pubsubtarget.md&#34;&gt;PubsubTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#retryconfig" title="RetryConfig">RetryConfig</a>" : <i>[ &lt;a href=&#34;retryconfig.md&#34;&gt;RetryConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#appenginerouting" title="AppEngineRouting">AppEngineRouting</a>" : <i>[ &lt;a href=&#34;appenginerouting.md&#34;&gt;AppEngineRouting&lt;/a&gt;, ... ]</i>,
        "<a href="#oauthtoken" title="OauthToken">OauthToken</a>" : <i>[ &lt;a href=&#34;oauthtoken.md&#34;&gt;OauthToken&lt;/a&gt;, ... ]</i>,
        "<a href="#oidctoken" title="OidcToken">OidcToken</a>" : <i>[ &lt;a href=&#34;oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::CloudSchedulerJob
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#attemptdeadline" title="AttemptDeadline">AttemptDeadline</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#appenginehttptarget" title="AppEngineHttpTarget">AppEngineHttpTarget</a>: <i>
      - &lt;a href=&#34;appenginehttptarget.md&#34;&gt;AppEngineHttpTarget&lt;/a&gt;</i>
    <a href="#httptarget" title="HttpTarget">HttpTarget</a>: <i>
      - &lt;a href=&#34;httptarget.md&#34;&gt;HttpTarget&lt;/a&gt;</i>
    <a href="#pubsubtarget" title="PubsubTarget">PubsubTarget</a>: <i>
      - &lt;a href=&#34;pubsubtarget.md&#34;&gt;PubsubTarget&lt;/a&gt;</i>
    <a href="#retryconfig" title="RetryConfig">RetryConfig</a>: <i>
      - &lt;a href=&#34;retryconfig.md&#34;&gt;RetryConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#appenginerouting" title="AppEngineRouting">AppEngineRouting</a>: <i>
      - &lt;a href=&#34;appenginerouting.md&#34;&gt;AppEngineRouting&lt;/a&gt;</i>
    <a href="#oauthtoken" title="OauthToken">OauthToken</a>: <i>
      - &lt;a href=&#34;oauthtoken.md&#34;&gt;OauthToken&lt;/a&gt;</i>
    <a href="#oidctoken" title="OidcToken">OidcToken</a>: <i>
      - &lt;a href=&#34;oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

_Type_: List of &lt;a href=&#34;appenginehttptarget.md&#34;&gt;AppEngineHttpTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpTarget

_Required_: No

_Type_: List of &lt;a href=&#34;httptarget.md&#34;&gt;HttpTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PubsubTarget

_Required_: No

_Type_: List of &lt;a href=&#34;pubsubtarget.md&#34;&gt;PubsubTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryConfig

_Required_: No

_Type_: List of &lt;a href=&#34;retryconfig.md&#34;&gt;RetryConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppEngineRouting

_Required_: No

_Type_: List of &lt;a href=&#34;appenginerouting.md&#34;&gt;AppEngineRouting&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthToken

_Required_: No

_Type_: List of &lt;a href=&#34;oauthtoken.md&#34;&gt;OauthToken&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcToken

_Required_: No

_Type_: List of &lt;a href=&#34;oidctoken.md&#34;&gt;OidcToken&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

