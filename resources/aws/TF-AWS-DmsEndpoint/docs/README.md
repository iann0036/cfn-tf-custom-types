# TF::AWS::DmsEndpoint

Provides a DMS (Data Migration Service) endpoint resource. DMS endpoints can be created, updated, deleted, and imported.

~> **Note:** All arguments including the password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DmsEndpoint",
    "Properties" : {
        "<a href="#certificatearn" title="CertificateArn">CertificateArn</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#endpointid" title="EndpointId">EndpointId</a>" : <i>String</i>,
        "<a href="#endpointtype" title="EndpointType">EndpointType</a>" : <i>String</i>,
        "<a href="#enginename" title="EngineName">EngineName</a>" : <i>String</i>,
        "<a href="#extraconnectionattributes" title="ExtraConnectionAttributes">ExtraConnectionAttributes</a>" : <i>String</i>,
        "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#serviceaccessrole" title="ServiceAccessRole">ServiceAccessRole</a>" : <i>String</i>,
        "<a href="#sslmode" title="SslMode">SslMode</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#elasticsearchsettings" title="ElasticsearchSettings">ElasticsearchSettings</a>" : <i>[ <a href="elasticsearchsettingsdefinition.md">ElasticsearchSettingsDefinition</a>, ... ]</i>,
        "<a href="#kafkasettings" title="KafkaSettings">KafkaSettings</a>" : <i>[ <a href="kafkasettingsdefinition.md">KafkaSettingsDefinition</a>, ... ]</i>,
        "<a href="#kinesissettings" title="KinesisSettings">KinesisSettings</a>" : <i>[ <a href="kinesissettingsdefinition.md">KinesisSettingsDefinition</a>, ... ]</i>,
        "<a href="#mongodbsettings" title="MongodbSettings">MongodbSettings</a>" : <i>[ <a href="mongodbsettingsdefinition.md">MongodbSettingsDefinition</a>, ... ]</i>,
        "<a href="#s3settings" title="S3Settings">S3Settings</a>" : <i>[ <a href="s3settingsdefinition.md">S3SettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DmsEndpoint
Properties:
    <a href="#certificatearn" title="CertificateArn">CertificateArn</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#endpointid" title="EndpointId">EndpointId</a>: <i>String</i>
    <a href="#endpointtype" title="EndpointType">EndpointType</a>: <i>String</i>
    <a href="#enginename" title="EngineName">EngineName</a>: <i>String</i>
    <a href="#extraconnectionattributes" title="ExtraConnectionAttributes">ExtraConnectionAttributes</a>: <i>String</i>
    <a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#serviceaccessrole" title="ServiceAccessRole">ServiceAccessRole</a>: <i>String</i>
    <a href="#sslmode" title="SslMode">SslMode</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#elasticsearchsettings" title="ElasticsearchSettings">ElasticsearchSettings</a>: <i>
      - <a href="elasticsearchsettingsdefinition.md">ElasticsearchSettingsDefinition</a></i>
    <a href="#kafkasettings" title="KafkaSettings">KafkaSettings</a>: <i>
      - <a href="kafkasettingsdefinition.md">KafkaSettingsDefinition</a></i>
    <a href="#kinesissettings" title="KinesisSettings">KinesisSettings</a>: <i>
      - <a href="kinesissettingsdefinition.md">KinesisSettingsDefinition</a></i>
    <a href="#mongodbsettings" title="MongodbSettings">MongodbSettings</a>: <i>
      - <a href="mongodbsettingsdefinition.md">MongodbSettingsDefinition</a></i>
    <a href="#s3settings" title="S3Settings">S3Settings</a>: <i>
      - <a href="s3settingsdefinition.md">S3SettingsDefinition</a></i>
</pre>

## Properties

#### CertificateArn

The Amazon Resource Name (ARN) for the certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

The name of the endpoint database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointId

The database endpoint identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointType

The type of endpoint. Can be one of `source | target`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineName

The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraConnectionAttributes

Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password to be used to login to the endpoint database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port used by the endpoint database.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

The host name of the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccessRole

The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMode

The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The user name to be used to login to the endpoint database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchSettings

_Required_: No

_Type_: List of <a href="elasticsearchsettingsdefinition.md">ElasticsearchSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaSettings

_Required_: No

_Type_: List of <a href="kafkasettingsdefinition.md">KafkaSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisSettings

_Required_: No

_Type_: List of <a href="kinesissettingsdefinition.md">KinesisSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongodbSettings

_Required_: No

_Type_: List of <a href="mongodbsettingsdefinition.md">MongodbSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Settings

_Required_: No

_Type_: List of <a href="s3settingsdefinition.md">S3SettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EndpointArn

Returns the <code>EndpointArn</code> value.

#### Id

Returns the <code>Id</code> value.

