# TF::SignalFx::AwsIntegration

SignalFx AWS CloudWatch integrations. For help with this integration see [Monitoring Amazon Web Services](https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#monitor-amazon-web-services).

~> **NOTE** When managing integrations you'll need to use an admin token to authenticate the SignalFx provider.

~> **WARNING** This resource implements a part of a workflow. You must use it with one of either `signalfx_aws_external_integration` or `signalfx_aws_token_integration`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::AwsIntegration",
    "Properties" : {
        "<a href="#customcloudwatchnamespaces" title="CustomCloudwatchNamespaces">CustomCloudwatchNamespaces</a>" : <i>[ String, ... ]</i>,
        "<a href="#enableawsusage" title="EnableAwsUsage">EnableAwsUsage</a>" : <i>Boolean</i>,
        "<a href="#enablechecklargevolume" title="EnableCheckLargeVolume">EnableCheckLargeVolume</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#externalid" title="ExternalId">ExternalId</a>" : <i>String</i>,
        "<a href="#importcloudwatch" title="ImportCloudWatch">ImportCloudWatch</a>" : <i>Boolean</i>,
        "<a href="#integrationid" title="IntegrationId">IntegrationId</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#namedtoken" title="NamedToken">NamedToken</a>" : <i>String</i>,
        "<a href="#pollrate" title="PollRate">PollRate</a>" : <i>Double</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#usegetmetricdatamethod" title="UseGetMetricDataMethod">UseGetMetricDataMethod</a>" : <i>Boolean</i>,
        "<a href="#customnamespacesyncrule" title="CustomNamespaceSyncRule">CustomNamespaceSyncRule</a>" : <i>[ <a href="customnamespacesyncruledefinition.md">CustomNamespaceSyncRuleDefinition</a>, ... ]</i>,
        "<a href="#namespacesyncrule" title="NamespaceSyncRule">NamespaceSyncRule</a>" : <i>[ <a href="namespacesyncruledefinition.md">NamespaceSyncRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::AwsIntegration
Properties:
    <a href="#customcloudwatchnamespaces" title="CustomCloudwatchNamespaces">CustomCloudwatchNamespaces</a>: <i>
      - String</i>
    <a href="#enableawsusage" title="EnableAwsUsage">EnableAwsUsage</a>: <i>Boolean</i>
    <a href="#enablechecklargevolume" title="EnableCheckLargeVolume">EnableCheckLargeVolume</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#externalid" title="ExternalId">ExternalId</a>: <i>String</i>
    <a href="#importcloudwatch" title="ImportCloudWatch">ImportCloudWatch</a>: <i>Boolean</i>
    <a href="#integrationid" title="IntegrationId">IntegrationId</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#namedtoken" title="NamedToken">NamedToken</a>: <i>String</i>
    <a href="#pollrate" title="PollRate">PollRate</a>: <i>Double</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#services" title="Services">Services</a>: <i>
      - String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#usegetmetricdatamethod" title="UseGetMetricDataMethod">UseGetMetricDataMethod</a>: <i>Boolean</i>
    <a href="#customnamespacesyncrule" title="CustomNamespaceSyncRule">CustomNamespaceSyncRule</a>: <i>
      - <a href="customnamespacesyncruledefinition.md">CustomNamespaceSyncRuleDefinition</a></i>
    <a href="#namespacesyncrule" title="NamespaceSyncRule">NamespaceSyncRule</a>: <i>
      - <a href="namespacesyncruledefinition.md">NamespaceSyncRuleDefinition</a></i>
</pre>

## Properties

#### CustomCloudwatchNamespaces

List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAwsUsage

Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCheckLargeVolume

Controls how SignalFx checks for large amounts of data for this AWS integration. If `true`, SignalFx monitors the amount of data coming in from the integration.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the integration is enabled.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalId

The `external_id` property from one of a `signalfx_aws_external_integration` or `signalfx_aws_token_integration`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportCloudWatch

Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationId

The id of one of a `signalfx_aws_external_integration` or `signalfx_aws_token_integration`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PollRate

AWS poll rate (in seconds). Value between `60` and `300`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

List of AWS regions that SignalFx should monitor.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`. See the documentation for [Creating Integrations](https://developers.signalfx.com/integrations_reference.html#operation/Create%20Integration) for valida values.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseGetMetricDataMethod

Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomNamespaceSyncRule

_Required_: No

_Type_: List of <a href="customnamespacesyncruledefinition.md">CustomNamespaceSyncRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceSyncRule

_Required_: No

_Type_: List of <a href="namespacesyncruledefinition.md">NamespaceSyncRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AuthMethod

Returns the <code>AuthMethod</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

