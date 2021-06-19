# TF::AWS::KinesisFirehoseDeliveryStream

Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.

For more details, see the [Amazon Kinesis Firehose Documentation][1].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::KinesisFirehoseDeliveryStream",
    "Properties" : {
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#destinationid" title="DestinationId">DestinationId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#elasticsearchconfiguration" title="ElasticsearchConfiguration">ElasticsearchConfiguration</a>" : <i>[ <a href="elasticsearchconfigurationdefinition.md">ElasticsearchConfigurationDefinition</a>, ... ]</i>,
        "<a href="#extendeds3configuration" title="ExtendedS3Configuration">ExtendedS3Configuration</a>" : <i>[ <a href="extendeds3configurationdefinition.md">ExtendedS3ConfigurationDefinition</a>, ... ]</i>,
        "<a href="#httpendpointconfiguration" title="HttpEndpointConfiguration">HttpEndpointConfiguration</a>" : <i>[ <a href="httpendpointconfigurationdefinition.md">HttpEndpointConfigurationDefinition</a>, ... ]</i>,
        "<a href="#kinesissourceconfiguration" title="KinesisSourceConfiguration">KinesisSourceConfiguration</a>" : <i>[ <a href="kinesissourceconfigurationdefinition.md">KinesisSourceConfigurationDefinition</a>, ... ]</i>,
        "<a href="#redshiftconfiguration" title="RedshiftConfiguration">RedshiftConfiguration</a>" : <i>[ <a href="redshiftconfigurationdefinition.md">RedshiftConfigurationDefinition</a>, ... ]</i>,
        "<a href="#s3configuration" title="S3Configuration">S3Configuration</a>" : <i>[ <a href="s3configurationdefinition.md">S3ConfigurationDefinition</a>, ... ]</i>,
        "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>[ <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a>, ... ]</i>,
        "<a href="#splunkconfiguration" title="SplunkConfiguration">SplunkConfiguration</a>" : <i>[ <a href="splunkconfigurationdefinition.md">SplunkConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::KinesisFirehoseDeliveryStream
Properties:
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#destinationid" title="DestinationId">DestinationId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#elasticsearchconfiguration" title="ElasticsearchConfiguration">ElasticsearchConfiguration</a>: <i>
      - <a href="elasticsearchconfigurationdefinition.md">ElasticsearchConfigurationDefinition</a></i>
    <a href="#extendeds3configuration" title="ExtendedS3Configuration">ExtendedS3Configuration</a>: <i>
      - <a href="extendeds3configurationdefinition.md">ExtendedS3ConfigurationDefinition</a></i>
    <a href="#httpendpointconfiguration" title="HttpEndpointConfiguration">HttpEndpointConfiguration</a>: <i>
      - <a href="httpendpointconfigurationdefinition.md">HttpEndpointConfigurationDefinition</a></i>
    <a href="#kinesissourceconfiguration" title="KinesisSourceConfiguration">KinesisSourceConfiguration</a>: <i>
      - <a href="kinesissourceconfigurationdefinition.md">KinesisSourceConfigurationDefinition</a></i>
    <a href="#redshiftconfiguration" title="RedshiftConfiguration">RedshiftConfiguration</a>: <i>
      - <a href="redshiftconfigurationdefinition.md">RedshiftConfigurationDefinition</a></i>
    <a href="#s3configuration" title="S3Configuration">S3Configuration</a>: <i>
      - <a href="s3configurationdefinition.md">S3ConfigurationDefinition</a></i>
    <a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>
      - <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a></i>
    <a href="#splunkconfiguration" title="SplunkConfiguration">SplunkConfiguration</a>: <i>
      - <a href="splunkconfigurationdefinition.md">SplunkConfigurationDefinition</a></i>
</pre>

## Properties

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchConfiguration

_Required_: No

_Type_: List of <a href="elasticsearchconfigurationdefinition.md">ElasticsearchConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedS3Configuration

_Required_: No

_Type_: List of <a href="extendeds3configurationdefinition.md">ExtendedS3ConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpEndpointConfiguration

_Required_: No

_Type_: List of <a href="httpendpointconfigurationdefinition.md">HttpEndpointConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisSourceConfiguration

_Required_: No

_Type_: List of <a href="kinesissourceconfigurationdefinition.md">KinesisSourceConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedshiftConfiguration

_Required_: No

_Type_: List of <a href="redshiftconfigurationdefinition.md">RedshiftConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Configuration

_Required_: No

_Type_: List of <a href="s3configurationdefinition.md">S3ConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

_Required_: No

_Type_: List of <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplunkConfiguration

_Required_: No

_Type_: List of <a href="splunkconfigurationdefinition.md">SplunkConfigurationDefinition</a>

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

