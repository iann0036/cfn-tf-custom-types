# TF::AWS::SagemakerFeatureGroup

Provides a SageMaker Feature Group resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SagemakerFeatureGroup",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#eventtimefeaturename" title="EventTimeFeatureName">EventTimeFeatureName</a>" : <i>String</i>,
        "<a href="#featuregroupname" title="FeatureGroupName">FeatureGroupName</a>" : <i>String</i>,
        "<a href="#recordidentifierfeaturename" title="RecordIdentifierFeatureName">RecordIdentifierFeatureName</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#featuredefinition" title="FeatureDefinition">FeatureDefinition</a>" : <i>[ <a href="featuredefinitiondefinition.md">FeatureDefinitionDefinition</a>, ... ]</i>,
        "<a href="#offlinestoreconfig" title="OfflineStoreConfig">OfflineStoreConfig</a>" : <i>[ <a href="offlinestoreconfigdefinition.md">OfflineStoreConfigDefinition</a>, ... ]</i>,
        "<a href="#onlinestoreconfig" title="OnlineStoreConfig">OnlineStoreConfig</a>" : <i>[ <a href="onlinestoreconfigdefinition.md">OnlineStoreConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SagemakerFeatureGroup
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#eventtimefeaturename" title="EventTimeFeatureName">EventTimeFeatureName</a>: <i>String</i>
    <a href="#featuregroupname" title="FeatureGroupName">FeatureGroupName</a>: <i>String</i>
    <a href="#recordidentifierfeaturename" title="RecordIdentifierFeatureName">RecordIdentifierFeatureName</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#featuredefinition" title="FeatureDefinition">FeatureDefinition</a>: <i>
      - <a href="featuredefinitiondefinition.md">FeatureDefinitionDefinition</a></i>
    <a href="#offlinestoreconfig" title="OfflineStoreConfig">OfflineStoreConfig</a>: <i>
      - <a href="offlinestoreconfigdefinition.md">OfflineStoreConfigDefinition</a></i>
    <a href="#onlinestoreconfig" title="OnlineStoreConfig">OnlineStoreConfig</a>: <i>
      - <a href="onlinestoreconfigdefinition.md">OnlineStoreConfigDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTimeFeatureName

The name of the feature that stores the EventTime of a Record in a Feature Group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureGroupName

The name of the Feature Group. The name must be unique within an AWS Region in an AWS account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordIdentifierFeatureName

The name of the Feature whose value uniquely identifies a Record defined in the Feature Store. Only the latest record per identifier value will be stored in the Online Store.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of resource tags for the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureDefinition

_Required_: No

_Type_: List of <a href="featuredefinitiondefinition.md">FeatureDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OfflineStoreConfig

_Required_: No

_Type_: List of <a href="offlinestoreconfigdefinition.md">OfflineStoreConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlineStoreConfig

_Required_: No

_Type_: List of <a href="onlinestoreconfigdefinition.md">OnlineStoreConfigDefinition</a>

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

