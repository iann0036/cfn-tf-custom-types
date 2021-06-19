# TF::Thunder::Server PortListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
    "<a href="#connresume" title="ConnResume">ConnResume</a>" : <i>Double</i>,
    "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
    "<a href="#followportprotocol" title="FollowPortProtocol">FollowPortProtocol</a>" : <i>String</i>,
    "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
    "<a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>" : <i>Double</i>,
    "<a href="#healthcheckfollowport" title="HealthCheckFollowPort">HealthCheckFollowPort</a>" : <i>Double</i>,
    "<a href="#nologging" title="NoLogging">NoLogging</a>" : <i>Double</i>,
    "<a href="#nossl" title="NoSsl">NoSsl</a>" : <i>Double</i>,
    "<a href="#portnumber" title="PortNumber">PortNumber</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#range" title="Range">Range</a>" : <i>Double</i>,
    "<a href="#rporthealthcheckshared" title="RportHealthCheckShared">RportHealthCheckShared</a>" : <i>String</i>,
    "<a href="#sharedrporthealthcheck" title="SharedRportHealthCheck">SharedRportHealthCheck</a>" : <i>Double</i>,
    "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
    "<a href="#supporthttp2" title="SupportHttp2">SupportHttp2</a>" : <i>Double</i>,
    "<a href="#templateport" title="TemplatePort">TemplatePort</a>" : <i>String</i>,
    "<a href="#templateserverssl" title="TemplateServerSsl">TemplateServerSsl</a>" : <i>String</i>,
    "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
    "<a href="#alternateport" title="AlternatePort">AlternatePort</a>" : <i>[ <a href="alternateportdefinition.md">AlternatePortDefinition</a>, ... ]</i>,
    "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
<a href="#connresume" title="ConnResume">ConnResume</a>: <i>Double</i>
<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
<a href="#followportprotocol" title="FollowPortProtocol">FollowPortProtocol</a>: <i>String</i>
<a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
<a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>: <i>Double</i>
<a href="#healthcheckfollowport" title="HealthCheckFollowPort">HealthCheckFollowPort</a>: <i>Double</i>
<a href="#nologging" title="NoLogging">NoLogging</a>: <i>Double</i>
<a href="#nossl" title="NoSsl">NoSsl</a>: <i>Double</i>
<a href="#portnumber" title="PortNumber">PortNumber</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#range" title="Range">Range</a>: <i>Double</i>
<a href="#rporthealthcheckshared" title="RportHealthCheckShared">RportHealthCheckShared</a>: <i>String</i>
<a href="#sharedrporthealthcheck" title="SharedRportHealthCheck">SharedRportHealthCheck</a>: <i>Double</i>
<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
<a href="#supporthttp2" title="SupportHttp2">SupportHttp2</a>: <i>Double</i>
<a href="#templateport" title="TemplatePort">TemplatePort</a>: <i>String</i>
<a href="#templateserverssl" title="TemplateServerSsl">TemplateServerSsl</a>: <i>String</i>
<a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
<a href="#alternateport" title="AlternatePort">AlternatePort</a>: <i>
      - <a href="alternateportdefinition.md">AlternatePortDefinition</a></i>
<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnResume

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowPortProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckDisable

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckFollowPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoLogging

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoSsl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RportHealthCheckShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedRportHealthCheck

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportHttp2

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServerSsl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternatePort

_Required_: No

_Type_: List of <a href="alternateportdefinition.md">AlternatePortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

