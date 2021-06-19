# TF::Thunder::Server

`thunder_server` Provides details about thunder server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::Server",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#connresume" title="ConnResume">ConnResume</a>" : <i>Double</i>,
        "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
        "<a href="#externalip" title="ExternalIp">ExternalIp</a>" : <i>String</i>,
        "<a href="#fqdnname" title="FqdnName">FqdnName</a>" : <i>String</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
        "<a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>" : <i>Double</i>,
        "<a href="#healthcheckshared" title="HealthCheckShared">HealthCheckShared</a>" : <i>String</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nologging" title="NoLogging">NoLogging</a>" : <i>Double</i>,
        "<a href="#resolveas" title="ResolveAs">ResolveAs</a>" : <i>String</i>,
        "<a href="#serveripv6addr" title="ServerIpv6Addr">ServerIpv6Addr</a>" : <i>String</i>,
        "<a href="#sharedpartitionhealthcheck" title="SharedPartitionHealthCheck">SharedPartitionHealthCheck</a>" : <i>Double</i>,
        "<a href="#slowstart" title="SlowStart">SlowStart</a>" : <i>Double</i>,
        "<a href="#spoofingcache" title="SpoofingCache">SpoofingCache</a>" : <i>Double</i>,
        "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
        "<a href="#templateserver" title="TemplateServer">TemplateServer</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
        "<a href="#alternateserver" title="AlternateServer">AlternateServer</a>" : <i>[ <a href="alternateserverdefinition.md">AlternateServerDefinition</a>, ... ]</i>,
        "<a href="#portlist" title="PortList">PortList</a>" : <i>[ <a href="portlistdefinition.md">PortListDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::Server
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#connresume" title="ConnResume">ConnResume</a>: <i>Double</i>
    <a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
    <a href="#externalip" title="ExternalIp">ExternalIp</a>: <i>String</i>
    <a href="#fqdnname" title="FqdnName">FqdnName</a>: <i>String</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
    <a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>: <i>Double</i>
    <a href="#healthcheckshared" title="HealthCheckShared">HealthCheckShared</a>: <i>String</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nologging" title="NoLogging">NoLogging</a>: <i>Double</i>
    <a href="#resolveas" title="ResolveAs">ResolveAs</a>: <i>String</i>
    <a href="#serveripv6addr" title="ServerIpv6Addr">ServerIpv6Addr</a>: <i>String</i>
    <a href="#sharedpartitionhealthcheck" title="SharedPartitionHealthCheck">SharedPartitionHealthCheck</a>: <i>Double</i>
    <a href="#slowstart" title="SlowStart">SlowStart</a>: <i>Double</i>
    <a href="#spoofingcache" title="SpoofingCache">SpoofingCache</a>: <i>Double</i>
    <a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
    <a href="#templateserver" title="TemplateServer">TemplateServer</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
    <a href="#alternateserver" title="AlternateServer">AlternateServer</a>: <i>
      - <a href="alternateserverdefinition.md">AlternateServerDefinition</a></i>
    <a href="#portlist" title="PortList">PortList</a>: <i>
      - <a href="portlistdefinition.md">PortListDefinition</a></i>
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

#### ExternalIp

External IP address for NAT of GSLB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnName

Server hostname.

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

#### HealthCheckShared

Health Check Monitor (Health monitor name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

IP Address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

IPv6 address Mapping of GSLB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Server Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoLogging

Do not log connection over limit event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveAs

‘resolve-to-ipv4’: Use A Query only to resolve FQDN; ‘resolve-to-ipv6’: Use AAAA Query only to resolve FQDN; ‘resolve-to-ipv4-and-ipv6’: Use A as well as AAAA Query to resolve FQDN;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerIpv6Addr

IPV6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionHealthCheck

Reference a health-check from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlowStart

Slowly ramp up the connection number after server is up (start from 128, then double every 10 sec till 4096).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpoofingCache

This server is a spoofing cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

‘stats-data-enable’: Enable statistical data collection for real server port; ‘stats-data-disable’: Disable statistical data collection for real server port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServer

Server template (Server template name).

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

#### AlternateServer

_Required_: No

_Type_: List of <a href="alternateserverdefinition.md">AlternateServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortList

_Required_: No

_Type_: List of <a href="portlistdefinition.md">PortListDefinition</a>

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

