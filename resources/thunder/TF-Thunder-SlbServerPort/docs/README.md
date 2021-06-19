# TF::Thunder::SlbServerPort

`thunder_slb_server_port` Provides details about thunder slb server port

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbServerPort",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#connresume" title="ConnResume">ConnResume</a>" : <i>Double</i>,
        "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
        "<a href="#followportprotocol" title="FollowPortProtocol">FollowPortProtocol</a>" : <i>String</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
        "<a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>" : <i>Double</i>,
        "<a href="#healthcheckfollowport" title="HealthCheckFollowPort">HealthCheckFollowPort</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nologging" title="NoLogging">NoLogging</a>" : <i>Double</i>,
        "<a href="#nossl" title="NoSsl">NoSsl</a>" : <i>Double</i>,
        "<a href="#portnumber" title="PortNumber">PortNumber</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#range" title="Range">Range</a>" : <i>Double</i>,
        "<a href="#rporthealthcheckshared" title="RportHealthCheckShared">RportHealthCheckShared</a>" : <i>String</i>,
        "<a href="#sharedpartitionporttemplate" title="SharedPartitionPortTemplate">SharedPartitionPortTemplate</a>" : <i>Double</i>,
        "<a href="#sharedrporthealthcheck" title="SharedRportHealthCheck">SharedRportHealthCheck</a>" : <i>Double</i>,
        "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
        "<a href="#supporthttp2" title="SupportHttp2">SupportHttp2</a>" : <i>Double</i>,
        "<a href="#templateport" title="TemplatePort">TemplatePort</a>" : <i>String</i>,
        "<a href="#templateportshared" title="TemplatePortShared">TemplatePortShared</a>" : <i>String</i>,
        "<a href="#templateserverssl" title="TemplateServerSsl">TemplateServerSsl</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
        "<a href="#alternateport" title="AlternatePort">AlternatePort</a>" : <i>[ <a href="alternateportdefinition.md">AlternatePortDefinition</a>, ... ]</i>,
        "<a href="#authcfg" title="AuthCfg">AuthCfg</a>" : <i>[ <a href="authcfgdefinition.md">AuthCfgDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbServerPort
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#connresume" title="ConnResume">ConnResume</a>: <i>Double</i>
    <a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
    <a href="#followportprotocol" title="FollowPortProtocol">FollowPortProtocol</a>: <i>String</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
    <a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>: <i>Double</i>
    <a href="#healthcheckfollowport" title="HealthCheckFollowPort">HealthCheckFollowPort</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nologging" title="NoLogging">NoLogging</a>: <i>Double</i>
    <a href="#nossl" title="NoSsl">NoSsl</a>: <i>Double</i>
    <a href="#portnumber" title="PortNumber">PortNumber</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#range" title="Range">Range</a>: <i>Double</i>
    <a href="#rporthealthcheckshared" title="RportHealthCheckShared">RportHealthCheckShared</a>: <i>String</i>
    <a href="#sharedpartitionporttemplate" title="SharedPartitionPortTemplate">SharedPartitionPortTemplate</a>: <i>Double</i>
    <a href="#sharedrporthealthcheck" title="SharedRportHealthCheck">SharedRportHealthCheck</a>: <i>Double</i>
    <a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
    <a href="#supporthttp2" title="SupportHttp2">SupportHttp2</a>: <i>Double</i>
    <a href="#templateport" title="TemplatePort">TemplatePort</a>: <i>String</i>
    <a href="#templateportshared" title="TemplatePortShared">TemplatePortShared</a>: <i>String</i>
    <a href="#templateserverssl" title="TemplateServerSsl">TemplateServerSsl</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
    <a href="#alternateport" title="AlternatePort">AlternatePort</a>: <i>
      - <a href="alternateportdefinition.md">AlternatePortDefinition</a></i>
    <a href="#authcfg" title="AuthCfg">AuthCfg</a>: <i>
      - <a href="authcfgdefinition.md">AuthCfgDefinition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### Action

‘enable’: enable; ‘disable’: disable; ‘disable-with-health-check’: disable port, but health check work;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLimit

Connection Limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnResume

Connection Resume.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

Enable extended statistics on real server port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowPortProtocol

‘tcp’: TCP Port; ‘udp’: UDP Port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

Health Check (Monitor Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckDisable

Disable health check.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckFollowPort

Specify which port to follow for health status (Port Number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoLogging

Do not log connection over limit event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoSsl

No SSL.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortNumber

Port Number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

‘tcp’: TCP Port; ‘udp’: UDP Port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

Port range (Port range value - used for vip-to-rport-mapping).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RportHealthCheckShared

Health Check (Monitor Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPortTemplate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedRportHealthCheck

Reference a health-check from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

‘stats-data-enable’: Enable statistical data collection for real server port; ‘stats-data-disable’: Disable statistical data collection for real server port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportHttp2

Starting HTTP/2 with Prior Knowledge.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePort

Port template (Port template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePortShared

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServerSsl

Server side SSL template (Server side SSL Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Port Weight (Connection Weight).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternatePort

_Required_: No

_Type_: List of <a href="alternateportdefinition.md">AlternatePortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthCfg

_Required_: No

_Type_: List of <a href="authcfgdefinition.md">AuthCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

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

