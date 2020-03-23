# Terraform::AWS::S3BucketAnalyticsConfiguration StorageClassAnalysis DataExport

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#outputschemaversion" title="OutputSchemaVersion">OutputSchemaVersion</a>" : <i>String</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="storageclassanalysis-dataexport-destination.md">Destination</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#outputschemaversion" title="OutputSchemaVersion">OutputSchemaVersion</a>: <i>String</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="storageclassanalysis-dataexport-destination.md">Destination</a></i>
</pre>

## Properties

#### OutputSchemaVersion

The schema version of exported analytics data. Allowed values: `V_1`. Default value: `V_1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="storageclassanalysis-dataexport-destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

