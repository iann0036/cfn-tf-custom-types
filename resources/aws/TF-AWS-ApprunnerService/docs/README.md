# TF::AWS::ApprunnerService

Manages an App Runner Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ApprunnerService",
    "Properties" : {
        "<a href="#autoscalingconfigurationarn" title="AutoScalingConfigurationArn">AutoScalingConfigurationArn</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>" : <i>[ <a href="encryptionconfigurationdefinition.md">EncryptionConfigurationDefinition</a>, ... ]</i>,
        "<a href="#healthcheckconfiguration" title="HealthCheckConfiguration">HealthCheckConfiguration</a>" : <i>[ <a href="healthcheckconfigurationdefinition.md">HealthCheckConfigurationDefinition</a>, ... ]</i>,
        "<a href="#instanceconfiguration" title="InstanceConfiguration">InstanceConfiguration</a>" : <i>[ <a href="instanceconfigurationdefinition.md">InstanceConfigurationDefinition</a>, ... ]</i>,
        "<a href="#sourceconfiguration" title="SourceConfiguration">SourceConfiguration</a>" : <i>[ <a href="sourceconfigurationdefinition.md">SourceConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ApprunnerService
Properties:
    <a href="#autoscalingconfigurationarn" title="AutoScalingConfigurationArn">AutoScalingConfigurationArn</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>: <i>
      - <a href="encryptionconfigurationdefinition.md">EncryptionConfigurationDefinition</a></i>
    <a href="#healthcheckconfiguration" title="HealthCheckConfiguration">HealthCheckConfiguration</a>: <i>
      - <a href="healthcheckconfigurationdefinition.md">HealthCheckConfigurationDefinition</a></i>
    <a href="#instanceconfiguration" title="InstanceConfiguration">InstanceConfiguration</a>: <i>
      - <a href="instanceconfigurationdefinition.md">InstanceConfigurationDefinition</a></i>
    <a href="#sourceconfiguration" title="SourceConfiguration">SourceConfiguration</a>: <i>
      - <a href="sourceconfigurationdefinition.md">SourceConfigurationDefinition</a></i>
</pre>

## Properties

#### AutoScalingConfigurationArn

ARN of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

Name of the service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfiguration

_Required_: No

_Type_: List of <a href="encryptionconfigurationdefinition.md">EncryptionConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckConfiguration

_Required_: No

_Type_: List of <a href="healthcheckconfigurationdefinition.md">HealthCheckConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceConfiguration

_Required_: No

_Type_: List of <a href="instanceconfigurationdefinition.md">InstanceConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceConfiguration

_Required_: No

_Type_: List of <a href="sourceconfigurationdefinition.md">SourceConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### ServiceId

Returns the <code>ServiceId</code> value.

#### ServiceUrl

Returns the <code>ServiceUrl</code> value.

#### Status

Returns the <code>Status</code> value.

