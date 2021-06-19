# TF::AWS::ConfigConformancePack

Manages a Config Conformance Pack. More information about this collection of Config rules and remediation actions can be found in the
[Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) documentation.
Sample Conformance Pack templates may be found in the
[AWS Config Rules Repository](https://github.com/awslabs/aws-config-rules/tree/master/aws-config-conformance-packs).

~> **NOTE:** The account must have a Configuration Recorder with proper IAM permissions before the Conformance Pack will
successfully create or update. See also the
[`aws_config_configuration_recorder` resource](/docs/providers/aws/r/config_configuration_recorder.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ConfigConformancePack",
    "Properties" : {
        "<a href="#deliverys3bucket" title="DeliveryS3Bucket">DeliveryS3Bucket</a>" : <i>String</i>,
        "<a href="#deliverys3keyprefix" title="DeliveryS3KeyPrefix">DeliveryS3KeyPrefix</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#templatebody" title="TemplateBody">TemplateBody</a>" : <i>String</i>,
        "<a href="#templates3uri" title="TemplateS3Uri">TemplateS3Uri</a>" : <i>String</i>,
        "<a href="#inputparameter" title="InputParameter">InputParameter</a>" : <i>[ <a href="inputparameterdefinition.md">InputParameterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ConfigConformancePack
Properties:
    <a href="#deliverys3bucket" title="DeliveryS3Bucket">DeliveryS3Bucket</a>: <i>String</i>
    <a href="#deliverys3keyprefix" title="DeliveryS3KeyPrefix">DeliveryS3KeyPrefix</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#templatebody" title="TemplateBody">TemplateBody</a>: <i>String</i>
    <a href="#templates3uri" title="TemplateS3Uri">TemplateS3Uri</a>: <i>String</i>
    <a href="#inputparameter" title="InputParameter">InputParameter</a>: <i>
      - <a href="inputparameterdefinition.md">InputParameterDefinition</a></i>
</pre>

## Properties

#### DeliveryS3Bucket

Amazon S3 bucket where AWS Config stores conformance pack templates. Maximum length of 63.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryS3KeyPrefix

The prefix for the Amazon S3 bucket. Maximum length of 1024.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the conformance pack. Must begin with a letter and contain from 1 to 256 alphanumeric characters and hyphens.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateBody

A string containing full conformance pack template body. Maximum length of 51200. Drift detection is not possible with this argument.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateS3Uri

Location of file, e.g. `s3://bucketname/prefix`, containing the template body. The uri must point to the conformance pack template that is located in an Amazon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is not possible with this argument.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputParameter

_Required_: No

_Type_: List of <a href="inputparameterdefinition.md">InputParameterDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

