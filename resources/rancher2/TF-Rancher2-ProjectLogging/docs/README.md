# TF::Rancher2::ProjectLogging

CloudFormation equivalent of rancher2_project_logging

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::ProjectLogging",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#enablejsonparsing" title="EnableJsonParsing">EnableJsonParsing</a>" : <i>Boolean</i>,
        "<a href="#kind" title="Kind">Kind</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespaceid" title="NamespaceId">NamespaceId</a>" : <i>String</i>,
        "<a href="#outputflushinterval" title="OutputFlushInterval">OutputFlushInterval</a>" : <i>Double</i>,
        "<a href="#outputtags" title="OutputTags">OutputTags</a>" : <i>[ <a href="outputtagsdefinition.md">OutputTagsDefinition</a>, ... ]</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#customtargetconfig" title="CustomTargetConfig">CustomTargetConfig</a>" : <i>[ <a href="customtargetconfigdefinition.md">CustomTargetConfigDefinition</a>, ... ]</i>,
        "<a href="#elasticsearchconfig" title="ElasticsearchConfig">ElasticsearchConfig</a>" : <i>[ <a href="elasticsearchconfigdefinition.md">ElasticsearchConfigDefinition</a>, ... ]</i>,
        "<a href="#fluentdconfig" title="FluentdConfig">FluentdConfig</a>" : <i>[ <a href="fluentdconfigdefinition.md">FluentdConfigDefinition</a>, ... ]</i>,
        "<a href="#kafkaconfig" title="KafkaConfig">KafkaConfig</a>" : <i>[ <a href="kafkaconfigdefinition.md">KafkaConfigDefinition</a>, ... ]</i>,
        "<a href="#splunkconfig" title="SplunkConfig">SplunkConfig</a>" : <i>[ <a href="splunkconfigdefinition.md">SplunkConfigDefinition</a>, ... ]</i>,
        "<a href="#syslogconfig" title="SyslogConfig">SyslogConfig</a>" : <i>[ <a href="syslogconfigdefinition.md">SyslogConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::ProjectLogging
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#enablejsonparsing" title="EnableJsonParsing">EnableJsonParsing</a>: <i>Boolean</i>
    <a href="#kind" title="Kind">Kind</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespaceid" title="NamespaceId">NamespaceId</a>: <i>String</i>
    <a href="#outputflushinterval" title="OutputFlushInterval">OutputFlushInterval</a>: <i>Double</i>
    <a href="#outputtags" title="OutputTags">OutputTags</a>: <i>
      - <a href="outputtagsdefinition.md">OutputTagsDefinition</a></i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#customtargetconfig" title="CustomTargetConfig">CustomTargetConfig</a>: <i>
      - <a href="customtargetconfigdefinition.md">CustomTargetConfigDefinition</a></i>
    <a href="#elasticsearchconfig" title="ElasticsearchConfig">ElasticsearchConfig</a>: <i>
      - <a href="elasticsearchconfigdefinition.md">ElasticsearchConfigDefinition</a></i>
    <a href="#fluentdconfig" title="FluentdConfig">FluentdConfig</a>: <i>
      - <a href="fluentdconfigdefinition.md">FluentdConfigDefinition</a></i>
    <a href="#kafkaconfig" title="KafkaConfig">KafkaConfig</a>: <i>
      - <a href="kafkaconfigdefinition.md">KafkaConfigDefinition</a></i>
    <a href="#splunkconfig" title="SplunkConfig">SplunkConfig</a>: <i>
      - <a href="splunkconfigdefinition.md">SplunkConfigDefinition</a></i>
    <a href="#syslogconfig" title="SyslogConfig">SyslogConfig</a>: <i>
      - <a href="syslogconfigdefinition.md">SyslogConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableJsonParsing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kind

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFlushInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputTags

_Required_: No

_Type_: List of <a href="outputtagsdefinition.md">OutputTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTargetConfig

_Required_: No

_Type_: List of <a href="customtargetconfigdefinition.md">CustomTargetConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchConfig

_Required_: No

_Type_: List of <a href="elasticsearchconfigdefinition.md">ElasticsearchConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FluentdConfig

_Required_: No

_Type_: List of <a href="fluentdconfigdefinition.md">FluentdConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaConfig

_Required_: No

_Type_: List of <a href="kafkaconfigdefinition.md">KafkaConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplunkConfig

_Required_: No

_Type_: List of <a href="splunkconfigdefinition.md">SplunkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogConfig

_Required_: No

_Type_: List of <a href="syslogconfigdefinition.md">SyslogConfigDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

