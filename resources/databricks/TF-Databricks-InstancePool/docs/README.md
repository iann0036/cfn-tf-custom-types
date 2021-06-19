# TF::Databricks::InstancePool

CloudFormation equivalent of databricks_instance_pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::InstancePool",
    "Properties" : {
        "<a href="#customtags" title="CustomTags">CustomTags</a>" : <i>[ <a href="customtagsdefinition.md">CustomTagsDefinition</a>, ... ]</i>,
        "<a href="#enableelasticdisk" title="EnableElasticDisk">EnableElasticDisk</a>" : <i>Boolean</i>,
        "<a href="#idleinstanceautoterminationminutes" title="IdleInstanceAutoterminationMinutes">IdleInstanceAutoterminationMinutes</a>" : <i>Double</i>,
        "<a href="#instancepoolid" title="InstancePoolId">InstancePoolId</a>" : <i>String</i>,
        "<a href="#instancepoolname" title="InstancePoolName">InstancePoolName</a>" : <i>String</i>,
        "<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>" : <i>Double</i>,
        "<a href="#minidleinstances" title="MinIdleInstances">MinIdleInstances</a>" : <i>Double</i>,
        "<a href="#nodetypeid" title="NodeTypeId">NodeTypeId</a>" : <i>String</i>,
        "<a href="#preloadedsparkversions" title="PreloadedSparkVersions">PreloadedSparkVersions</a>" : <i>[ String, ... ]</i>,
        "<a href="#awsattributes" title="AwsAttributes">AwsAttributes</a>" : <i>[ <a href="awsattributesdefinition.md">AwsAttributesDefinition</a>, ... ]</i>,
        "<a href="#azureattributes" title="AzureAttributes">AzureAttributes</a>" : <i>[ <a href="azureattributesdefinition.md">AzureAttributesDefinition</a>, ... ]</i>,
        "<a href="#diskspec" title="DiskSpec">DiskSpec</a>" : <i>[ <a href="diskspecdefinition.md">DiskSpecDefinition</a>, ... ]</i>,
        "<a href="#preloadeddockerimage" title="PreloadedDockerImage">PreloadedDockerImage</a>" : <i>[ <a href="preloadeddockerimagedefinition.md">PreloadedDockerImageDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::InstancePool
Properties:
    <a href="#customtags" title="CustomTags">CustomTags</a>: <i>
      - <a href="customtagsdefinition.md">CustomTagsDefinition</a></i>
    <a href="#enableelasticdisk" title="EnableElasticDisk">EnableElasticDisk</a>: <i>Boolean</i>
    <a href="#idleinstanceautoterminationminutes" title="IdleInstanceAutoterminationMinutes">IdleInstanceAutoterminationMinutes</a>: <i>Double</i>
    <a href="#instancepoolid" title="InstancePoolId">InstancePoolId</a>: <i>String</i>
    <a href="#instancepoolname" title="InstancePoolName">InstancePoolName</a>: <i>String</i>
    <a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>: <i>Double</i>
    <a href="#minidleinstances" title="MinIdleInstances">MinIdleInstances</a>: <i>Double</i>
    <a href="#nodetypeid" title="NodeTypeId">NodeTypeId</a>: <i>String</i>
    <a href="#preloadedsparkversions" title="PreloadedSparkVersions">PreloadedSparkVersions</a>: <i>
      - String</i>
    <a href="#awsattributes" title="AwsAttributes">AwsAttributes</a>: <i>
      - <a href="awsattributesdefinition.md">AwsAttributesDefinition</a></i>
    <a href="#azureattributes" title="AzureAttributes">AzureAttributes</a>: <i>
      - <a href="azureattributesdefinition.md">AzureAttributesDefinition</a></i>
    <a href="#diskspec" title="DiskSpec">DiskSpec</a>: <i>
      - <a href="diskspecdefinition.md">DiskSpecDefinition</a></i>
    <a href="#preloadeddockerimage" title="PreloadedDockerImage">PreloadedDockerImage</a>: <i>
      - <a href="preloadeddockerimagedefinition.md">PreloadedDockerImageDefinition</a></i>
</pre>

## Properties

#### CustomTags

_Required_: No

_Type_: List of <a href="customtagsdefinition.md">CustomTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableElasticDisk

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleInstanceAutoterminationMinutes

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePoolName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinIdleInstances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeTypeId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreloadedSparkVersions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAttributes

_Required_: No

_Type_: List of <a href="awsattributesdefinition.md">AwsAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureAttributes

_Required_: No

_Type_: List of <a href="azureattributesdefinition.md">AzureAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSpec

_Required_: No

_Type_: List of <a href="diskspecdefinition.md">DiskSpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreloadedDockerImage

_Required_: No

_Type_: List of <a href="preloadeddockerimagedefinition.md">PreloadedDockerImageDefinition</a>

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

