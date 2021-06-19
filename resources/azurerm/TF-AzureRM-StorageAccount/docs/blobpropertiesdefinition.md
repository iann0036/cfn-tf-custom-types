# TF::AzureRM::StorageAccount BlobPropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#changefeedenabled" title="ChangeFeedEnabled">ChangeFeedEnabled</a>" : <i>Boolean</i>,
    "<a href="#defaultserviceversion" title="DefaultServiceVersion">DefaultServiceVersion</a>" : <i>String</i>,
    "<a href="#lastaccesstimeenabled" title="LastAccessTimeEnabled">LastAccessTimeEnabled</a>" : <i>Boolean</i>,
    "<a href="#versioningenabled" title="VersioningEnabled">VersioningEnabled</a>" : <i>Boolean</i>,
    "<a href="#containerdeleteretentionpolicy" title="ContainerDeleteRetentionPolicy">ContainerDeleteRetentionPolicy</a>" : <i>[ <a href="containerdeleteretentionpolicydefinition.md">ContainerDeleteRetentionPolicyDefinition</a>, ... ]</i>,
    "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="corsruledefinition.md">CorsRuleDefinition</a>, ... ]</i>,
    "<a href="#deleteretentionpolicy" title="DeleteRetentionPolicy">DeleteRetentionPolicy</a>" : <i>[ <a href="deleteretentionpolicydefinition.md">DeleteRetentionPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#changefeedenabled" title="ChangeFeedEnabled">ChangeFeedEnabled</a>: <i>Boolean</i>
<a href="#defaultserviceversion" title="DefaultServiceVersion">DefaultServiceVersion</a>: <i>String</i>
<a href="#lastaccesstimeenabled" title="LastAccessTimeEnabled">LastAccessTimeEnabled</a>: <i>Boolean</i>
<a href="#versioningenabled" title="VersioningEnabled">VersioningEnabled</a>: <i>Boolean</i>
<a href="#containerdeleteretentionpolicy" title="ContainerDeleteRetentionPolicy">ContainerDeleteRetentionPolicy</a>: <i>
      - <a href="containerdeleteretentionpolicydefinition.md">ContainerDeleteRetentionPolicyDefinition</a></i>
<a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="corsruledefinition.md">CorsRuleDefinition</a></i>
<a href="#deleteretentionpolicy" title="DeleteRetentionPolicy">DeleteRetentionPolicy</a>: <i>
      - <a href="deleteretentionpolicydefinition.md">DeleteRetentionPolicyDefinition</a></i>
</pre>

## Properties

#### ChangeFeedEnabled

Is the blob service properties for change feed events enabled? Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultServiceVersion

The API Version which should be used by default for requests to the Data Plane API if an incoming request doesn't specify an API Version. Defaults to `2020-06-12`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastAccessTimeEnabled

Is the last access time based tracking enabled? Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersioningEnabled

Is versioning enabled? Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerDeleteRetentionPolicy

_Required_: No

_Type_: List of <a href="containerdeleteretentionpolicydefinition.md">ContainerDeleteRetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of <a href="corsruledefinition.md">CorsRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRetentionPolicy

_Required_: No

_Type_: List of <a href="deleteretentionpolicydefinition.md">DeleteRetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

