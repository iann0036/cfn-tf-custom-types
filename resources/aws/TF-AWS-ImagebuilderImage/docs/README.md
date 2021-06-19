# TF::AWS::ImagebuilderImage

Manages an Image Builder Image.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ImagebuilderImage",
    "Properties" : {
        "<a href="#distributionconfigurationarn" title="DistributionConfigurationArn">DistributionConfigurationArn</a>" : <i>String</i>,
        "<a href="#enhancedimagemetadataenabled" title="EnhancedImageMetadataEnabled">EnhancedImageMetadataEnabled</a>" : <i>Boolean</i>,
        "<a href="#imagerecipearn" title="ImageRecipeArn">ImageRecipeArn</a>" : <i>String</i>,
        "<a href="#infrastructureconfigurationarn" title="InfrastructureConfigurationArn">InfrastructureConfigurationArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#imagetestsconfiguration" title="ImageTestsConfiguration">ImageTestsConfiguration</a>" : <i>[ <a href="imagetestsconfigurationdefinition.md">ImageTestsConfigurationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ImagebuilderImage
Properties:
    <a href="#distributionconfigurationarn" title="DistributionConfigurationArn">DistributionConfigurationArn</a>: <i>String</i>
    <a href="#enhancedimagemetadataenabled" title="EnhancedImageMetadataEnabled">EnhancedImageMetadataEnabled</a>: <i>Boolean</i>
    <a href="#imagerecipearn" title="ImageRecipeArn">ImageRecipeArn</a>: <i>String</i>
    <a href="#infrastructureconfigurationarn" title="InfrastructureConfigurationArn">InfrastructureConfigurationArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#imagetestsconfiguration" title="ImageTestsConfiguration">ImageTestsConfiguration</a>: <i>
      - <a href="imagetestsconfigurationdefinition.md">ImageTestsConfigurationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DistributionConfigurationArn

Amazon Resource Name (ARN) of the Image Builder Distribution Configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedImageMetadataEnabled

Whether additional information about the image being created is collected. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageRecipeArn

Amazon Resource Name (ARN) of the Image Builder Infrastructure Recipe.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfrastructureConfigurationArn

Amazon Resource Name (ARN) of the Image Builder Infrastructure Configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags for the Image Builder Image. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageTestsConfiguration

_Required_: No

_Type_: List of <a href="imagetestsconfigurationdefinition.md">ImageTestsConfigurationDefinition</a>

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

#### Arn

Returns the <code>Arn</code> value.

#### DateCreated

Returns the <code>DateCreated</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### OsVersion

Returns the <code>OsVersion</code> value.

#### OutputResources

Returns the <code>OutputResources</code> value.

#### Platform

Returns the <code>Platform</code> value.

#### Version

Returns the <code>Version</code> value.

