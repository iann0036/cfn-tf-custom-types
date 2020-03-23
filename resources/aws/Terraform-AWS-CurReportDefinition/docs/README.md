# Terraform::AWS::CurReportDefinition

Manages Cost and Usage Report Definitions.

~> *NOTE:* The AWS Cost and Usage Report service is only available in `us-east-1` currently.

~> *NOTE:* If AWS Organizations is enabled, only the master account can use this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CurReportDefinition",
    "Properties" : {
        "<a href="#additionalartifacts" title="AdditionalArtifacts">AdditionalArtifacts</a>" : <i>[ String, ... ]</i>,
        "<a href="#additionalschemaelements" title="AdditionalSchemaElements">AdditionalSchemaElements</a>" : <i>[ String, ... ]</i>,
        "<a href="#compression" title="Compression">Compression</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#reportname" title="ReportName">ReportName</a>" : <i>String</i>,
        "<a href="#s3bucket" title="S3Bucket">S3Bucket</a>" : <i>String</i>,
        "<a href="#s3prefix" title="S3Prefix">S3Prefix</a>" : <i>String</i>,
        "<a href="#s3region" title="S3Region">S3Region</a>" : <i>String</i>,
        "<a href="#timeunit" title="TimeUnit">TimeUnit</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CurReportDefinition
Properties:
    <a href="#additionalartifacts" title="AdditionalArtifacts">AdditionalArtifacts</a>: <i>
      - String</i>
    <a href="#additionalschemaelements" title="AdditionalSchemaElements">AdditionalSchemaElements</a>: <i>
      - String</i>
    <a href="#compression" title="Compression">Compression</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#reportname" title="ReportName">ReportName</a>: <i>String</i>
    <a href="#s3bucket" title="S3Bucket">S3Bucket</a>: <i>String</i>
    <a href="#s3prefix" title="S3Prefix">S3Prefix</a>: <i>String</i>
    <a href="#s3region" title="S3Region">S3Region</a>: <i>String</i>
    <a href="#timeunit" title="TimeUnit">TimeUnit</a>: <i>String</i>
</pre>

## Properties

#### AdditionalArtifacts

A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalSchemaElements

A list of schema elements. Valid values are: RESOURCES.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compression

Compression format for report. Valid values are: GZIP, ZIP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Format for report. Valid values are: textORcsv.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportName

Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Bucket

Name of the existing S3 bucket to hold generated reports.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Prefix

Report path prefix. Limited to 256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Region

Region of the existing S3 bucket to hold generated reports.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUnit

The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.

_Required_: Yes

_Type_: String

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

