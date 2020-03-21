# Terraform::Google::ProjectUsageExportBucket

Sets up a usage export bucket for a particular project.  A usage export bucket
is a pre-configured GCS bucket which is set up to receive daily and monthly
reports of the GCE resources used.

For more information see the [Docs](https://cloud.google.com/compute/docs/usage-export)
and for further details, the
[API Documentation](https://cloud.google.com/compute/docs/reference/rest/beta/projects/setUsageExportBucket).

~> **Note:** You should specify only one of these per project.  If there are two or more
they will fight over which bucket the reports should be stored in.  It is
safe to have multiple resources with the same backing bucket.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ProjectUsageExportBucket",
    "Properties" : {
        "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
        "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ProjectUsageExportBucket
Properties:
    <a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
    <a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
</pre>

## Properties

#### BucketName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

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

