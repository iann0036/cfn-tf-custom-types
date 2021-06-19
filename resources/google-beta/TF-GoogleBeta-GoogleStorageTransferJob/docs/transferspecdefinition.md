# TF::GoogleBeta::GoogleStorageTransferJob TransferSpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awss3datasource" title="AwsS3DataSource">AwsS3DataSource</a>" : <i>[ <a href="awss3datasourcedefinition.md">AwsS3DataSourceDefinition</a>, ... ]</i>,
    "<a href="#azureblobstoragedatasource" title="AzureBlobStorageDataSource">AzureBlobStorageDataSource</a>" : <i>[ <a href="azureblobstoragedatasourcedefinition.md">AzureBlobStorageDataSourceDefinition</a>, ... ]</i>,
    "<a href="#gcsdatasink" title="GcsDataSink">GcsDataSink</a>" : <i>[ <a href="gcsdatasinkdefinition.md">GcsDataSinkDefinition</a>, ... ]</i>,
    "<a href="#gcsdatasource" title="GcsDataSource">GcsDataSource</a>" : <i>[ <a href="gcsdatasourcedefinition.md">GcsDataSourceDefinition</a>, ... ]</i>,
    "<a href="#httpdatasource" title="HttpDataSource">HttpDataSource</a>" : <i>[ <a href="httpdatasourcedefinition.md">HttpDataSourceDefinition</a>, ... ]</i>,
    "<a href="#objectconditions" title="ObjectConditions">ObjectConditions</a>" : <i>[ <a href="objectconditionsdefinition.md">ObjectConditionsDefinition</a>, ... ]</i>,
    "<a href="#transferoptions" title="TransferOptions">TransferOptions</a>" : <i>[ <a href="transferoptionsdefinition.md">TransferOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awss3datasource" title="AwsS3DataSource">AwsS3DataSource</a>: <i>
      - <a href="awss3datasourcedefinition.md">AwsS3DataSourceDefinition</a></i>
<a href="#azureblobstoragedatasource" title="AzureBlobStorageDataSource">AzureBlobStorageDataSource</a>: <i>
      - <a href="azureblobstoragedatasourcedefinition.md">AzureBlobStorageDataSourceDefinition</a></i>
<a href="#gcsdatasink" title="GcsDataSink">GcsDataSink</a>: <i>
      - <a href="gcsdatasinkdefinition.md">GcsDataSinkDefinition</a></i>
<a href="#gcsdatasource" title="GcsDataSource">GcsDataSource</a>: <i>
      - <a href="gcsdatasourcedefinition.md">GcsDataSourceDefinition</a></i>
<a href="#httpdatasource" title="HttpDataSource">HttpDataSource</a>: <i>
      - <a href="httpdatasourcedefinition.md">HttpDataSourceDefinition</a></i>
<a href="#objectconditions" title="ObjectConditions">ObjectConditions</a>: <i>
      - <a href="objectconditionsdefinition.md">ObjectConditionsDefinition</a></i>
<a href="#transferoptions" title="TransferOptions">TransferOptions</a>: <i>
      - <a href="transferoptionsdefinition.md">TransferOptionsDefinition</a></i>
</pre>

## Properties

#### AwsS3DataSource

_Required_: No

_Type_: List of <a href="awss3datasourcedefinition.md">AwsS3DataSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureBlobStorageDataSource

_Required_: No

_Type_: List of <a href="azureblobstoragedatasourcedefinition.md">AzureBlobStorageDataSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsDataSink

_Required_: No

_Type_: List of <a href="gcsdatasinkdefinition.md">GcsDataSinkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsDataSource

_Required_: No

_Type_: List of <a href="gcsdatasourcedefinition.md">GcsDataSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpDataSource

_Required_: No

_Type_: List of <a href="httpdatasourcedefinition.md">HttpDataSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectConditions

_Required_: No

_Type_: List of <a href="objectconditionsdefinition.md">ObjectConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransferOptions

_Required_: No

_Type_: List of <a href="transferoptionsdefinition.md">TransferOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

