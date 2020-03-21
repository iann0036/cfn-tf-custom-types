# Terraform::Google::StorageTransferJob TransferSpec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awss3datasource" title="AwsS3DataSource">AwsS3DataSource</a>" : <i>[ <a href="transferspec-awss3datasource.md">AwsS3DataSource</a>, ... ]</i>,
    "<a href="#gcsdatasink" title="GcsDataSink">GcsDataSink</a>" : <i>[ <a href="transferspec-gcsdatasink.md">GcsDataSink</a>, ... ]</i>,
    "<a href="#gcsdatasource" title="GcsDataSource">GcsDataSource</a>" : <i>[ <a href="transferspec-gcsdatasource.md">GcsDataSource</a>, ... ]</i>,
    "<a href="#httpdatasource" title="HttpDataSource">HttpDataSource</a>" : <i>[ <a href="transferspec-httpdatasource.md">HttpDataSource</a>, ... ]</i>,
    "<a href="#objectconditions" title="ObjectConditions">ObjectConditions</a>" : <i>[ <a href="transferspec-objectconditions.md">ObjectConditions</a>, ... ]</i>,
    "<a href="#transferoptions" title="TransferOptions">TransferOptions</a>" : <i>[ <a href="transferspec-transferoptions.md">TransferOptions</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awss3datasource" title="AwsS3DataSource">AwsS3DataSource</a>: <i>
      - <a href="transferspec-awss3datasource.md">AwsS3DataSource</a></i>
<a href="#gcsdatasink" title="GcsDataSink">GcsDataSink</a>: <i>
      - <a href="transferspec-gcsdatasink.md">GcsDataSink</a></i>
<a href="#gcsdatasource" title="GcsDataSource">GcsDataSource</a>: <i>
      - <a href="transferspec-gcsdatasource.md">GcsDataSource</a></i>
<a href="#httpdatasource" title="HttpDataSource">HttpDataSource</a>: <i>
      - <a href="transferspec-httpdatasource.md">HttpDataSource</a></i>
<a href="#objectconditions" title="ObjectConditions">ObjectConditions</a>: <i>
      - <a href="transferspec-objectconditions.md">ObjectConditions</a></i>
<a href="#transferoptions" title="TransferOptions">TransferOptions</a>: <i>
      - <a href="transferspec-transferoptions.md">TransferOptions</a></i>
</pre>

## Properties

#### AwsS3DataSource

_Required_: No

_Type_: List of <a href="transferspec-awss3datasource.md">AwsS3DataSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsDataSink

_Required_: No

_Type_: List of <a href="transferspec-gcsdatasink.md">GcsDataSink</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsDataSource

_Required_: No

_Type_: List of <a href="transferspec-gcsdatasource.md">GcsDataSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpDataSource

_Required_: No

_Type_: List of <a href="transferspec-httpdatasource.md">HttpDataSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectConditions

_Required_: No

_Type_: List of <a href="transferspec-objectconditions.md">ObjectConditions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransferOptions

_Required_: No

_Type_: List of <a href="transferspec-transferoptions.md">TransferOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

