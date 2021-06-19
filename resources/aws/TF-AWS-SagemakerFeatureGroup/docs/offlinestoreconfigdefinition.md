# TF::AWS::SagemakerFeatureGroup OfflineStoreConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablegluetablecreation" title="DisableGlueTableCreation">DisableGlueTableCreation</a>" : <i>Boolean</i>,
    "<a href="#datacatalogconfig" title="DataCatalogConfig">DataCatalogConfig</a>" : <i>[ <a href="datacatalogconfigdefinition.md">DataCatalogConfigDefinition</a>, ... ]</i>,
    "<a href="#s3storageconfig" title="S3StorageConfig">S3StorageConfig</a>" : <i>[ <a href="s3storageconfigdefinition.md">S3StorageConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablegluetablecreation" title="DisableGlueTableCreation">DisableGlueTableCreation</a>: <i>Boolean</i>
<a href="#datacatalogconfig" title="DataCatalogConfig">DataCatalogConfig</a>: <i>
      - <a href="datacatalogconfigdefinition.md">DataCatalogConfigDefinition</a></i>
<a href="#s3storageconfig" title="S3StorageConfig">S3StorageConfig</a>: <i>
      - <a href="s3storageconfigdefinition.md">S3StorageConfigDefinition</a></i>
</pre>

## Properties

#### DisableGlueTableCreation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataCatalogConfig

_Required_: No

_Type_: List of <a href="datacatalogconfigdefinition.md">DataCatalogConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3StorageConfig

_Required_: No

_Type_: List of <a href="s3storageconfigdefinition.md">S3StorageConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

