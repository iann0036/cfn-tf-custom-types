# TF::AWS::KinesisAnalyticsApplication

Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
allows processing and analyzing streaming data using standard SQL.

For more details, see the [Amazon Kinesis Analytics Documentation][1].

-> **Note:** To manage Amazon Kinesis Data Analytics for Apache Flink applications, use the [`aws_kinesisanalyticsv2_application`](/docs/providers/aws/r/kinesisanalyticsv2_application.html) resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::KinesisAnalyticsApplication",
    "Properties" : {
        "<a href="#code" title="Code">Code</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#startapplication" title="StartApplication">StartApplication</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>, ... ]</i>,
        "<a href="#inputs" title="Inputs">Inputs</a>" : <i>[ <a href="inputsdefinition.md">InputsDefinition</a>, ... ]</i>,
        "<a href="#outputs" title="Outputs">Outputs</a>" : <i>[ <a href="outputsdefinition.md">OutputsDefinition</a>, ... ]</i>,
        "<a href="#referencedatasources" title="ReferenceDataSources">ReferenceDataSources</a>" : <i>[ <a href="referencedatasourcesdefinition.md">ReferenceDataSourcesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::KinesisAnalyticsApplication
Properties:
    <a href="#code" title="Code">Code</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#startapplication" title="StartApplication">StartApplication</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a></i>
    <a href="#inputs" title="Inputs">Inputs</a>: <i>
      - <a href="inputsdefinition.md">InputsDefinition</a></i>
    <a href="#outputs" title="Outputs">Outputs</a>: <i>
      - <a href="outputsdefinition.md">OutputsDefinition</a></i>
    <a href="#referencedatasources" title="ReferenceDataSources">ReferenceDataSources</a>: <i>
      - <a href="referencedatasourcesdefinition.md">ReferenceDataSourcesDefinition</a></i>
</pre>

## Properties

#### Code

SQL Code to transform input data, and generate output.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Kinesis Analytics Application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartApplication

Whether to start or stop the Kinesis Analytics Application. To start an application, an input with a defined `starting_position` must be configured.
To modify an application's starting position, first stop the application by setting `start_application = false`, then update `starting_position` and set `start_application = true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of tags for the Kinesis Analytics Application. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inputs

_Required_: No

_Type_: List of <a href="inputsdefinition.md">InputsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outputs

_Required_: No

_Type_: List of <a href="outputsdefinition.md">OutputsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceDataSources

_Required_: No

_Type_: List of <a href="referencedatasourcesdefinition.md">ReferenceDataSourcesDefinition</a>

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

#### CreateTimestamp

Returns the <code>CreateTimestamp</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdateTimestamp

Returns the <code>LastUpdateTimestamp</code> value.

#### Status

Returns the <code>Status</code> value.

#### Version

Returns the <code>Version</code> value.

