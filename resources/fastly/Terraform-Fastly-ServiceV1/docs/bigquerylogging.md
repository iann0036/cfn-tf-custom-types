# Terraform::Fastly::ServiceV1 Bigquerylogging

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dataset" title="Dataset">Dataset</a>" : <i>String</i>,
    "<a href="#email" title="Email">Email</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>String</i>,
    "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
    "<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>" : <i>String</i>,
    "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
    "<a href="#table" title="Table">Table</a>" : <i>String</i>,
    "<a href="#template" title="Template">Template</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dataset" title="Dataset">Dataset</a>: <i>String</i>
<a href="#email" title="Email">Email</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#placement" title="Placement">Placement</a>: <i>String</i>
<a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>: <i>String</i>
<a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
<a href="#table" title="Table">Table</a>: <i>String</i>
<a href="#template" title="Template">Template</a>: <i>String</i>
</pre>

## Properties

#### Dataset

The ID of your BigQuery dataset.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The email for the service account with write access to your BigQuery dataset. If not provided, this will be pulled from a `FASTLY_BQ_EMAIL` environment variable.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Apache style log formatting. Must produce JSON that matches the schema of your BigQuery table.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify this BigQuery logging endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

Where in the generated VCL the logging call should be placed; one of: `none` or `waf_debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The ID of your GCP project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCondition

Name of already defined `condition` to apply. This `condition` must be of type `RESPONSE`. For detailed information about Conditionals, see [Fastly's Documentation on Conditionals][fastly-conditionals].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

The secret key associated with the sservice account that has write access to your BigQuery table. If not provided, this will be pulled from the `FASTLY_BQ_SECRET_KEY` environment variable. Typical format for this is a private key in a string with newlines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Table

The ID of your BigQuery table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

Big query table name suffix template. If set will be interpreted as a strftime compatible string and used as the [Template Suffix for your table](https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

