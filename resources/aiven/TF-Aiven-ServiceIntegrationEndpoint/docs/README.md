# TF::Aiven::ServiceIntegrationEndpoint

CloudFormation equivalent of aiven_service_integration_endpoint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aiven::ServiceIntegrationEndpoint",
    "Properties" : {
        "<a href="#endpointname" title="EndpointName">EndpointName</a>" : <i>String</i>,
        "<a href="#endpointtype" title="EndpointType">EndpointType</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#datadoguserconfig" title="DatadogUserConfig">DatadogUserConfig</a>" : <i>[ <a href="datadoguserconfigdefinition.md">DatadogUserConfigDefinition</a>, ... ]</i>,
        "<a href="#externalawscloudwatchlogsuserconfig" title="ExternalAwsCloudwatchLogsUserConfig">ExternalAwsCloudwatchLogsUserConfig</a>" : <i>[ <a href="externalawscloudwatchlogsuserconfigdefinition.md">ExternalAwsCloudwatchLogsUserConfigDefinition</a>, ... ]</i>,
        "<a href="#externalawscloudwatchmetricsuserconfig" title="ExternalAwsCloudwatchMetricsUserConfig">ExternalAwsCloudwatchMetricsUserConfig</a>" : <i>[ <a href="externalawscloudwatchmetricsuserconfigdefinition.md">ExternalAwsCloudwatchMetricsUserConfigDefinition</a>, ... ]</i>,
        "<a href="#externalelasticsearchlogsuserconfig" title="ExternalElasticsearchLogsUserConfig">ExternalElasticsearchLogsUserConfig</a>" : <i>[ <a href="externalelasticsearchlogsuserconfigdefinition.md">ExternalElasticsearchLogsUserConfigDefinition</a>, ... ]</i>,
        "<a href="#externalgooglecloudlogginguserconfig" title="ExternalGoogleCloudLoggingUserConfig">ExternalGoogleCloudLoggingUserConfig</a>" : <i>[ <a href="externalgooglecloudlogginguserconfigdefinition.md">ExternalGoogleCloudLoggingUserConfigDefinition</a>, ... ]</i>,
        "<a href="#externalkafkauserconfig" title="ExternalKafkaUserConfig">ExternalKafkaUserConfig</a>" : <i>[ <a href="externalkafkauserconfigdefinition.md">ExternalKafkaUserConfigDefinition</a>, ... ]</i>,
        "<a href="#externalschemaregistryuserconfig" title="ExternalSchemaRegistryUserConfig">ExternalSchemaRegistryUserConfig</a>" : <i>[ <a href="externalschemaregistryuserconfigdefinition.md">ExternalSchemaRegistryUserConfigDefinition</a>, ... ]</i>,
        "<a href="#jolokiauserconfig" title="JolokiaUserConfig">JolokiaUserConfig</a>" : <i>[ <a href="jolokiauserconfigdefinition.md">JolokiaUserConfigDefinition</a>, ... ]</i>,
        "<a href="#prometheususerconfig" title="PrometheusUserConfig">PrometheusUserConfig</a>" : <i>[ <a href="prometheususerconfigdefinition.md">PrometheusUserConfigDefinition</a>, ... ]</i>,
        "<a href="#rsysloguserconfig" title="RsyslogUserConfig">RsyslogUserConfig</a>" : <i>[ <a href="rsysloguserconfigdefinition.md">RsyslogUserConfigDefinition</a>, ... ]</i>,
        "<a href="#signalfxuserconfig" title="SignalfxUserConfig">SignalfxUserConfig</a>" : <i>[ <a href="signalfxuserconfigdefinition.md">SignalfxUserConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aiven::ServiceIntegrationEndpoint
Properties:
    <a href="#endpointname" title="EndpointName">EndpointName</a>: <i>String</i>
    <a href="#endpointtype" title="EndpointType">EndpointType</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#datadoguserconfig" title="DatadogUserConfig">DatadogUserConfig</a>: <i>
      - <a href="datadoguserconfigdefinition.md">DatadogUserConfigDefinition</a></i>
    <a href="#externalawscloudwatchlogsuserconfig" title="ExternalAwsCloudwatchLogsUserConfig">ExternalAwsCloudwatchLogsUserConfig</a>: <i>
      - <a href="externalawscloudwatchlogsuserconfigdefinition.md">ExternalAwsCloudwatchLogsUserConfigDefinition</a></i>
    <a href="#externalawscloudwatchmetricsuserconfig" title="ExternalAwsCloudwatchMetricsUserConfig">ExternalAwsCloudwatchMetricsUserConfig</a>: <i>
      - <a href="externalawscloudwatchmetricsuserconfigdefinition.md">ExternalAwsCloudwatchMetricsUserConfigDefinition</a></i>
    <a href="#externalelasticsearchlogsuserconfig" title="ExternalElasticsearchLogsUserConfig">ExternalElasticsearchLogsUserConfig</a>: <i>
      - <a href="externalelasticsearchlogsuserconfigdefinition.md">ExternalElasticsearchLogsUserConfigDefinition</a></i>
    <a href="#externalgooglecloudlogginguserconfig" title="ExternalGoogleCloudLoggingUserConfig">ExternalGoogleCloudLoggingUserConfig</a>: <i>
      - <a href="externalgooglecloudlogginguserconfigdefinition.md">ExternalGoogleCloudLoggingUserConfigDefinition</a></i>
    <a href="#externalkafkauserconfig" title="ExternalKafkaUserConfig">ExternalKafkaUserConfig</a>: <i>
      - <a href="externalkafkauserconfigdefinition.md">ExternalKafkaUserConfigDefinition</a></i>
    <a href="#externalschemaregistryuserconfig" title="ExternalSchemaRegistryUserConfig">ExternalSchemaRegistryUserConfig</a>: <i>
      - <a href="externalschemaregistryuserconfigdefinition.md">ExternalSchemaRegistryUserConfigDefinition</a></i>
    <a href="#jolokiauserconfig" title="JolokiaUserConfig">JolokiaUserConfig</a>: <i>
      - <a href="jolokiauserconfigdefinition.md">JolokiaUserConfigDefinition</a></i>
    <a href="#prometheususerconfig" title="PrometheusUserConfig">PrometheusUserConfig</a>: <i>
      - <a href="prometheususerconfigdefinition.md">PrometheusUserConfigDefinition</a></i>
    <a href="#rsysloguserconfig" title="RsyslogUserConfig">RsyslogUserConfig</a>: <i>
      - <a href="rsysloguserconfigdefinition.md">RsyslogUserConfigDefinition</a></i>
    <a href="#signalfxuserconfig" title="SignalfxUserConfig">SignalfxUserConfig</a>: <i>
      - <a href="signalfxuserconfigdefinition.md">SignalfxUserConfigDefinition</a></i>
</pre>

## Properties

#### EndpointName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatadogUserConfig

_Required_: No

_Type_: List of <a href="datadoguserconfigdefinition.md">DatadogUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalAwsCloudwatchLogsUserConfig

_Required_: No

_Type_: List of <a href="externalawscloudwatchlogsuserconfigdefinition.md">ExternalAwsCloudwatchLogsUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalAwsCloudwatchMetricsUserConfig

_Required_: No

_Type_: List of <a href="externalawscloudwatchmetricsuserconfigdefinition.md">ExternalAwsCloudwatchMetricsUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalElasticsearchLogsUserConfig

_Required_: No

_Type_: List of <a href="externalelasticsearchlogsuserconfigdefinition.md">ExternalElasticsearchLogsUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalGoogleCloudLoggingUserConfig

_Required_: No

_Type_: List of <a href="externalgooglecloudlogginguserconfigdefinition.md">ExternalGoogleCloudLoggingUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalKafkaUserConfig

_Required_: No

_Type_: List of <a href="externalkafkauserconfigdefinition.md">ExternalKafkaUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalSchemaRegistryUserConfig

_Required_: No

_Type_: List of <a href="externalschemaregistryuserconfigdefinition.md">ExternalSchemaRegistryUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JolokiaUserConfig

_Required_: No

_Type_: List of <a href="jolokiauserconfigdefinition.md">JolokiaUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrometheusUserConfig

_Required_: No

_Type_: List of <a href="prometheususerconfigdefinition.md">PrometheusUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RsyslogUserConfig

_Required_: No

_Type_: List of <a href="rsysloguserconfigdefinition.md">RsyslogUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignalfxUserConfig

_Required_: No

_Type_: List of <a href="signalfxuserconfigdefinition.md">SignalfxUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EndpointConfig

Returns the <code>EndpointConfig</code> value.

#### Id

Returns the <code>Id</code> value.

