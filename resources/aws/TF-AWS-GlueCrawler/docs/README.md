# TF::AWS::GlueCrawler

Manages a Glue Crawler. More information can be found in the [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::GlueCrawler",
    "Properties" : {
        "<a href="#classifiers" title="Classifiers">Classifiers</a>" : <i>[ String, ... ]</i>,
        "<a href="#configuration" title="Configuration">Configuration</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>" : <i>String</i>,
        "<a href="#tableprefix" title="TablePrefix">TablePrefix</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#catalogtarget" title="CatalogTarget">CatalogTarget</a>" : <i>[ <a href="catalogtargetdefinition.md">CatalogTargetDefinition</a>, ... ]</i>,
        "<a href="#dynamodbtarget" title="DynamodbTarget">DynamodbTarget</a>" : <i>[ <a href="dynamodbtargetdefinition.md">DynamodbTargetDefinition</a>, ... ]</i>,
        "<a href="#jdbctarget" title="JdbcTarget">JdbcTarget</a>" : <i>[ <a href="jdbctargetdefinition.md">JdbcTargetDefinition</a>, ... ]</i>,
        "<a href="#lineageconfiguration" title="LineageConfiguration">LineageConfiguration</a>" : <i>[ <a href="lineageconfigurationdefinition.md">LineageConfigurationDefinition</a>, ... ]</i>,
        "<a href="#mongodbtarget" title="MongodbTarget">MongodbTarget</a>" : <i>[ <a href="mongodbtargetdefinition.md">MongodbTargetDefinition</a>, ... ]</i>,
        "<a href="#recrawlpolicy" title="RecrawlPolicy">RecrawlPolicy</a>" : <i>[ <a href="recrawlpolicydefinition.md">RecrawlPolicyDefinition</a>, ... ]</i>,
        "<a href="#s3target" title="S3Target">S3Target</a>" : <i>[ <a href="s3targetdefinition.md">S3TargetDefinition</a>, ... ]</i>,
        "<a href="#schemachangepolicy" title="SchemaChangePolicy">SchemaChangePolicy</a>" : <i>[ <a href="schemachangepolicydefinition.md">SchemaChangePolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::GlueCrawler
Properties:
    <a href="#classifiers" title="Classifiers">Classifiers</a>: <i>
      - String</i>
    <a href="#configuration" title="Configuration">Configuration</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>: <i>String</i>
    <a href="#tableprefix" title="TablePrefix">TablePrefix</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#catalogtarget" title="CatalogTarget">CatalogTarget</a>: <i>
      - <a href="catalogtargetdefinition.md">CatalogTargetDefinition</a></i>
    <a href="#dynamodbtarget" title="DynamodbTarget">DynamodbTarget</a>: <i>
      - <a href="dynamodbtargetdefinition.md">DynamodbTargetDefinition</a></i>
    <a href="#jdbctarget" title="JdbcTarget">JdbcTarget</a>: <i>
      - <a href="jdbctargetdefinition.md">JdbcTargetDefinition</a></i>
    <a href="#lineageconfiguration" title="LineageConfiguration">LineageConfiguration</a>: <i>
      - <a href="lineageconfigurationdefinition.md">LineageConfigurationDefinition</a></i>
    <a href="#mongodbtarget" title="MongodbTarget">MongodbTarget</a>: <i>
      - <a href="mongodbtargetdefinition.md">MongodbTargetDefinition</a></i>
    <a href="#recrawlpolicy" title="RecrawlPolicy">RecrawlPolicy</a>: <i>
      - <a href="recrawlpolicydefinition.md">RecrawlPolicyDefinition</a></i>
    <a href="#s3target" title="S3Target">S3Target</a>: <i>
      - <a href="s3targetdefinition.md">S3TargetDefinition</a></i>
    <a href="#schemachangepolicy" title="SchemaChangePolicy">SchemaChangePolicy</a>: <i>
      - <a href="schemachangepolicydefinition.md">SchemaChangePolicyDefinition</a></i>
</pre>

## Properties

#### Classifiers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TablePrefix

_Required_: No

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

#### CatalogTarget

_Required_: No

_Type_: List of <a href="catalogtargetdefinition.md">CatalogTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamodbTarget

_Required_: No

_Type_: List of <a href="dynamodbtargetdefinition.md">DynamodbTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JdbcTarget

_Required_: No

_Type_: List of <a href="jdbctargetdefinition.md">JdbcTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LineageConfiguration

_Required_: No

_Type_: List of <a href="lineageconfigurationdefinition.md">LineageConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongodbTarget

_Required_: No

_Type_: List of <a href="mongodbtargetdefinition.md">MongodbTargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecrawlPolicy

_Required_: No

_Type_: List of <a href="recrawlpolicydefinition.md">RecrawlPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Target

_Required_: No

_Type_: List of <a href="s3targetdefinition.md">S3TargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaChangePolicy

_Required_: No

_Type_: List of <a href="schemachangepolicydefinition.md">SchemaChangePolicyDefinition</a>

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

